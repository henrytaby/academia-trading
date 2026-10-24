#!/usr/bin/env python3
"""build_portal.py — Genera el portal estático multi-página del curso FIT-12.

Uso:
    python3 scripts/build_portal.py            # build limpio en <repo>/portal/
    python3 scripts/build_portal.py --out DIR  # destino alternativo

Arquitectura:
    portal/index.html          portada (hero + niveles + accesos)
    portal/<slug>.html         1 página por documento (105)
    portal/assets/             style.css · app.js (CDN: KaTeX 0.16.11 + mermaid@10)
    portal/files/              archivos enlazados no-markdown (csv, py)

Pipeline por documento:
    1) extracción de matemática fuera de bloques de código (misma lógica del visor:
       $$...$$ + $...$ con filtro isMathish) -> placeholders
    2) markdown -> HTML (extensiones tables/fenced_code/sane_lists)
    3) postproceso: callouts GitHub [!X] -> clases, mermaid -> pre.mermaid,
       <table> -> .table-wrap
    4) placeholders -> <span|div class="ktx|ktxd" data-tex="..."> (KaTeX client-side)
    5) reescritura de enlaces internos -> slugs del portal / files/
Validación en build: 0 enlaces internos rotos; cobertura 1:1 de los .md.
"""
import argparse
import html as html_mod
import json
import re
import shutil
import sys
from pathlib import Path

# rutas relativas a la ubicación del script: <repo>/scripts/portal/build_portal.py
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'portal'
ASSETS_SRC = Path(__file__).resolve().parent / 'assets_src'

import markdown as md_lib  # pip install markdown (venv)

# ---------------------------------------------------------------- orden canónico
MODULES = {
    1: 'El Trading como Negocio y Ciencia',
    2: 'El Motor del Precio',
    3: 'Anatomía del Gráfico',
    4: 'Plataforma y Primera Ejecución',
    5: 'Estructura de Mercado y Liquidez',
    6: 'Indicadores y Confluencias',
    7: 'Construcción del Sistema',
    8: 'Gestión del Riesgo',
    9: 'Backtesting, Journal y Validación',
    10: 'Psicotrading Científico',
    11: 'La Industria',
    12: 'Plan de Trading y Plan de Negocio',
}
LEVELS = {
    'N1': ('🧱 N1 · Base', range(1, 5)),
    'N2': ('📐 N2 · Técnica', range(5, 8)),
    'N3': ('🛡️ N3 · Riesgo', range(8, 11)),
    'N4': ('💼 N4 · Negocio', range(11, 13)),
}


def canonical_order():
    """Orden de lectura establecido por el visor histórico (regla, no lista fija)."""
    out = [ROOT / 'README.md', ROOT / 'agents.md',
           ROOT / 'docs/01-syllabus/SYLLABUS.md',
           ROOT / 'docs/00-analisis/analisis_cursos.md',
           ROOT / 'docs/03-recursos/laboratorio/receta-primera-operacion.md',
           ROOT / 'docs/03-recursos/laboratorio/mision-m8-escenarios.md',
           ROOT / 'journal/plantilla_journal_v1.md']
    for n in range(1, 13):
        mod_dir = next(d for d in (ROOT / 'docs/02-modulos').iterdir()
                       if d.is_dir() and re.match(rf'mod-{n:02d}-', d.name))
        out.append(mod_dir / 'README.md')
        out += sorted(mod_dir.glob('leccion-*.md'))
    out += [ROOT / f'docs/03-recursos/evaluaciones/examen-{s}.md'
            for s in ('n1', 'n2', 'n3', 'final')]
    out += [ROOT / 'docs/03-recursos/glosario.md',
            ROOT / 'docs/03-recursos/plantillas/PLANTILLA_MODULO.md',
            ROOT / 'journal/README.md',
            ROOT / 'scripts/core/README.md',
            ROOT / 'worklog.md']
    covered = {p.resolve() for p in out}
    extra = sorted(p for p in ROOT.rglob('*.md') if p.resolve() not in covered)
    if extra:
        print(f'⚠️  {len(extra)} .md fuera de la regla de orden (añadidos al final):')
        for p in extra:
            print(f'    + {p.relative_to(ROOT)}')
        out += extra
    return out


# ---------------------------------------------------------------- slugs únicos
def build_urls(doc_paths):
    stems = {}
    for p in doc_paths:
        stems.setdefault(p.stem, []).append(p)
    url_of, title_src = {}, {}
    for stem, paths in stems.items():
        for p in paths:
            if len(paths) == 1:
                slug = stem
            elif p.parent.name.startswith('mod-'):
                slug = f"hub-{p.parent.name[:6]}"          # hub-mod-05
            elif p.parent == ROOT:
                slug = 'readme'                              # README raíz
            else:
                slug = f"{p.parent.name}-{stem}".lower()    # journal-readme, core-readme
            slug = re.sub(r'[^A-Za-z0-9._-]', '-', slug)
            url_of[p.resolve()] = slug + '.html'
    return url_of


# ---------------------------------------------------------------- taxonomía
def taxonomy(p):
    rel = str(p.relative_to(ROOT))
    m = re.match(r'docs/02-modulos/mod-(\d+)-', rel)
    if rel == 'README.md':
        return ('Inicio', None, None)
    if rel in ('agents.md', 'worklog.md') or rel.startswith('scripts/'):
        return ('Repo', None, None)
    if rel == 'docs/01-syllabus/SYLLABUS.md' or rel.startswith('docs/00-analisis'):
        return ('Guía', None, None)
    if m:
        n = int(m.group(1))
        for tag, (label, rng) in LEVELS.items():
            if n in rng:
                return (label, f'M{n} · {MODULES[n]}', None)
    return ('Recursos', None, None)


def doc_title(p, src):
    m = re.search(r'^#\s+(.+)$', src, re.M)
    if m:
        return re.sub(r'[#*`]', '', m.group(1)).strip()
    return p.stem.replace('-', ' ').capitalize()


# ---------------------------------------------------------------- matemática
def is_mathish(tex):
    if not tex or len(tex) > 200:
        return False
    if re.search(r'(\*\*|·|→|←|¿|¡|—)', tex):
        return False
    if re.search(r'\\[a-zA-Z]+', tex):
        return True
    if re.search(r'[\^_{}]', tex) and re.search(r'[A-Za-z0-9]', tex):
        return True
    if re.search(r'[=<>\u2264\u2265\u2260\u2248\u00b1]', tex):
        return True
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', tex):
        return True
    return False


def extract_math(src):
    store = []

    def seg_math(seg):
        # display $$...$$ y inline $...$ con matching escape-aware:
        # "\\." consume \\$ como par; \\$(?<!\\\\) en prosa nunca abre matemática
        seg = re.sub(r'(?<!\\)\$\$((?:\\.|[\s\S])+?)\$\$',
                     lambda m: _push(m.group(1).strip(), True, store), seg)
        seg = re.sub(r'(?<!\\)\$(?!\s)((?:\\.|[^$\n])+?)(?<![\s\\])\$',
                     lambda m: m.group(0) if not is_mathish(m.group(1))
                     else _push(m.group(1), False, store), seg)
        # dólares literales de la prosa ($ con barra) -> entidad HTML que sobrevive
        # al markdown y se muestra como $
        return seg.replace('\\$', '&dollar;')

    parts = re.split(r'(```[\s\S]*?```)', src)
    return ''.join(s if s.startswith('```') else seg_math(s) for s in parts), store


def _push(tex, display, store):
    store.append((tex, display))
    return f'%%MATH{len(store) - 1}%%'


def restore_math(html_body, store):
    def sub(m):
        tex, display = store[int(m.group(1))]
        cls = 'ktxd' if display else 'ktx'
        esc = html_mod.escape(tex, quote=True)
        return f'<{cls} class="{cls}" data-tex="{esc}">{esc}</{cls}>'
    return re.sub(r'%%MATH(\d+)%%', sub, html_body)


def math_sanity(store, doc_rel):
    """Avisa de TeX sospechoso: llaves desbalanceadas o terminando en barra."""
    out = []
    for tex, display in store:
        if tex.endswith('\\') or tex.count('{') != tex.count('}'):
            out.append(f'{doc_rel}: TeX sospechoso -> {tex[:60]!r}')
    return out


# ---------------------------------------------------------------- render
CALLOUTS = [
    ('WARNING', 'gfm-warn', '⚠️'), ('CAUTION', 'gfm-caution', '⛔'),
    ('NOTE', 'gfm-note', '📝'), ('TIP', 'gfm-tip', '💡'),
    ('IMPORTANT', 'gfm-important', '❗'),
]


def render_doc(src):
    body, store = extract_math(src)
    body = md_lib.markdown(body, extensions=['tables', 'fenced_code', 'sane_lists'])
    for name, cls, icon in CALLOUTS:
        body = re.sub(
            rf'<blockquote>\s*<p>\[!{name}\]\s*',
            f'<blockquote class="{cls}"><p><strong>{icon} {name}:</strong> ',
            body)
    body = re.sub(r'<pre><code class="language-mermaid">([\s\S]*?)</code></pre>',
                  lambda m: f'<pre class="mermaid">{m.group(1)}</pre>', body)
    body = body.replace('<table>', '<div class="table-wrap"><table>') \
               .replace('</table>', '</table></div>')
    body = restore_math(body, store)
    return body


# ---------------------------------------------------------------- enlaces
def build_file_map(doc_paths):
    """Archivos no-md enlazados desde los docs -> portal/files/<basename>."""
    targets = {}
    for p in doc_paths:
        try:
            src = p.read_text(encoding='utf-8')
        except Exception:
            continue
        for t in re.findall(r'\]\(([^)\s]+)\)', src):
            t = t.split('#')[0]
            if not t or t.startswith(('http', 'mailto:')):
                continue
            f = (p.parent / t).resolve()
            if f.exists() and f.suffix != '.md' and OUT not in f.parents:
                targets.setdefault(f, f.name)
    return targets


def rewrite_links(html_body, doc_path, url_of, file_urls):
    base = doc_path.parent.resolve()

    def sub(m):
        href = m.group(1)
        if href.startswith(('#', 'http', 'mailto:')):
            return m.group(0)
        path, _, anchor = href.partition('#')
        path = path.split('?')[0]
        if not path:
            return m.group(0)
        stack = list(base.parts)
        for part in re.sub(r'^\./', '', path).split('/'):
            if part == '..':
                if len(stack) > 1:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)
        resolved = Path(*stack)
        if resolved in url_of:
            return f'href="{url_of[resolved]}"' + (f'#{anchor}' if anchor else '')
        # enlaces hacia archivos generados del propio portal (p. ej. README -> portal/index.html).
        # No se exige existencia: el build borra portal/ antes de generar, y las páginas
        # .html bajo OUT son productos de este mismo build.
        try:
            rel_out = resolved.relative_to(OUT)
            if rel_out.suffix == '.html':
                return f'href="{rel_out}"' + (f'#{anchor}' if anchor else '')
        except ValueError:
            pass
        if resolved in file_urls:
            return f'href="files/{file_urls[resolved]}"' + (f'#{anchor}' if anchor else '')
        return m.group(0)

    return re.sub(r'href="([^"]*)"', sub, html_body), None


# ---------------------------------------------------------------- plantilla
PAGE = """<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Academia FIT-12</title>
<script>try{{document.documentElement.setAttribute('data-theme',localStorage.getItem('fit12-theme')||'light')}}catch(e){{}}</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="topbar">
  <button class="icon-btn" id="menu-toggle" aria-label="Índice">☰ Índice</button>
  <span style="flex:1"></span>
  <button class="icon-btn" id="theme-toggle">🌙</button>
</div>
<div class="layout">
<nav class="sidebar">
  <div class="brand"><span class="logo">🎓</span><a href="index.html">Academia de Trading<br>FIT-12</a></div>
{nav}
</nav>
<main class="content">
  <div class="crumb">{crumb}</div>
  <article class="doc-body">
{body}
  </article>
  <nav class="pn-nav">
    {prev}
    {next}
  </nav>
</main>
</div>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script defer src="assets/app.js"></script>
</body>
</html>
"""

PN = '<a class="{cls}" href="{url}"><span class="lbl">{lbl}</span><span class="ttl">{ttl}</span></a>'


def build_nav(all_meta, active_path):
    groups = []
    seen = []
    for meta in all_meta:
        g = meta['group']
        if g not in seen:
            seen.append(g)
            groups.append((g, []))
        dict(groups)[g].append(meta)
    out = []
    for g, items in groups:
        closed = ' closed' if not any(m['path'] == active_path for m in items) else ''
        lis = []
        for m in items:
            act = ' class="active"' if m['path'] == active_path else ''
            lis.append(f'<li><a{act} href="{m["url"]}">{m["label"]}</a></li>')
        out.append(
            f'<div class="nav-group{closed}">'
            f'<button class="nav-level" type="button">{g}<span class="chev">▼</span></button>'
            f'<ul class="nav-items">{"".join(lis)}</ul></div>')
    return '\n'.join(out)


def nav_label(p, title, meta):
    rel = str(p.relative_to(ROOT))
    if re.match(r'docs/02-modulos/mod-\d+-.*/README\.md$', rel):
        n = int(re.search(r'mod-(\d+)-', rel).group(1))
        return f'Hub · M{n}'
    m = re.match(r'docs/02-modulos/mod-(\d+)-.*/leccion-(\d+)-(\d+)\.md$', rel)
    if m:
        t = title.split('—', 1)[-1].split('·', 1)[-1].strip()
        return f'{m.group(2)}.{m.group(3)} {t[:44]}'
    short = {'README.md': 'README raíz', 'agents.md': 'agents.md',
             'worklog.md': 'Worklog'}.get(p.name)
    if short:
        return short
    return title[:52]


def pn_link(meta, cls):
    if meta is None:
        return '<span></span>'
    lbl = '← Anterior' if cls == 'prev' else 'Siguiente →'
    return PN.format(cls=cls, url=meta['url'], lbl=lbl, ttl=html_mod.escape(meta['title'])[:70])


def render_page(meta, body_html, nav_html, crumb, prev_m, next_m):
    return PAGE.format(title=html_mod.escape(meta['title'][:70]), nav=nav_html,
                       crumb=crumb, body=body_html,
                       prev=pn_link(prev_m, 'prev'), next=pn_link(next_m, 'next'))


def breadcrumb(meta):
    parts = [f'<a href="index.html">Inicio</a>', f'<span class="sep">/</span>',
             html_mod.escape(meta['group'])]
    if meta['module']:
        parts += [f'<span class="sep">/</span>', html_mod.escape(meta['module'])]
    parts += [f'<span class="sep">/</span>', html_mod.escape(meta['title'][:60])]
    return ''.join(parts)


# ---------------------------------------------------------------- home
def render_home(all_meta, n_math, n_diag, url_of):
    mods = {}
    for meta in all_meta:
        if meta['module']:
            mnum = int(re.search(r'M(\d+)', meta['module']).group(1))
            mods.setdefault(mnum, {'title': meta['module'], 'hub': None,
                                   'lecciones': 0})
            if 'Hub ·' in meta['label']:
                mods[mnum]['hub'] = meta['url']
            else:
                mods[mnum]['lecciones'] += 1
    n_docs = len(all_meta)
    cards = []
    for tag, (label, rng) in LEVELS.items():
        rows = []
        for n in rng:
            info = mods.get(n, {'title': f'M{n} · {MODULES[n]}', 'hub': '#', 'lecciones': 0})
            rows.append(
                f'<li><a href="{info["hub"]}"><span class="m-t">M{n} · {MODULES[n]}</span>'
                f'<span class="m-d">{info["lecciones"]} lecciones</span></a></li>')
        cards.append(
            f'<div class="level-card"><h2>{label}</h2>'
            f'<div class="sub">3 módulos · lecciones + laboratorio + misión + quiz</div>'
            f'<ul class="mod-list">{"".join(rows)}</ul></div>')
    quick = [('SYLLABUS', url_of[(ROOT / 'docs/01-syllabus/SYLLABUS.md').resolve()]),
             ('Glosario (302)', url_of[(ROOT / 'docs/03-recursos/glosario.md').resolve()]),
             ('Examen N1', url_of[(ROOT / 'docs/03-recursos/evaluaciones/examen-n1.md').resolve()]),
             ('Examen N2', url_of[(ROOT / 'docs/03-recursos/evaluaciones/examen-n2.md').resolve()]),
             ('Examen N3', url_of[(ROOT / 'docs/03-recursos/evaluaciones/examen-n3.md').resolve()]),
             ('Examen final', url_of[(ROOT / 'docs/03-recursos/evaluaciones/examen-final.md').resolve()]),
             ('Receta 1ª operación', url_of[(ROOT / 'docs/03-recursos/laboratorio/receta-primera-operacion.md').resolve()]),
             ('Journal v1', url_of[(ROOT / 'journal/plantilla_journal_v1.md').resolve()])]
    quick_html = ''.join(f'<a href="{u}">{t}</a>' for t, u in quick)
    body = (
        f'<div class="hero"><h1>🎓 Academia de Trading — Programa FIT-12</h1>'
        f'<p>Formación Integral en Trading · 12 módulos · 4 niveles · del primer gráfico al plan de negocio</p>'
        f'<div class="stats"><span class="stat">📚 {n_docs} documentos</span>'
        f'<span class="stat">🧮 {n_math} fórmulas</span><span class="stat">📐 {n_diag} diagramas</span>'
        f'<span class="stat">🏆 Programa completo</span></div></div>'
        + ''.join(cards)
        + f'<div class="quick">{quick_html}</div>')
    meta = {'title': 'Inicio', 'url': 'index.html', 'group': 'Inicio',
            'module': None, 'path': None, 'label': 'Inicio'}
    return render_page(meta, body, build_nav(all_meta, None), '', None, None)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(OUT))
    args = ap.parse_args()
    out_dir = Path(args.out)

    doc_paths = canonical_order()
    url_of = build_urls(doc_paths)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / 'assets').mkdir(parents=True)
    (out_dir / 'files').mkdir(parents=True)

    # assets
    shutil.copy(ASSETS_SRC / 'style.css', out_dir / 'assets/style.css')
    shutil.copy(ASSETS_SRC / 'app.js', out_dir / 'assets/app.js')

    file_urls = build_file_map(doc_paths)
    for f, name in sorted(file_urls.items()):
        shutil.copy(f, out_dir / 'files' / name)
    if file_urls:
        print(f'✓ {len(file_urls)} archivos no-md copiados a portal/files/')

    all_meta, bodies, n_math, n_diag, broken = [], [], 0, 0, []
    suspect = []
    for p in doc_paths:
        src = p.read_text(encoding='utf-8')
        title = doc_title(p, src)
        group, module, _ = taxonomy(p)
        meta = {'path': p.resolve(), 'url': url_of[p.resolve()], 'title': title,
                'group': group, 'module': module}
        meta['label'] = nav_label(p, title, meta)
        body, store = extract_math(src)
        suspect += math_sanity(store, p.relative_to(ROOT))
        body = md_lib.markdown(body, extensions=['tables', 'fenced_code', 'sane_lists'])
        for name, cls, icon in CALLOUTS:
            body = re.sub(
                rf'<blockquote>\s*<p>\[!{name}\]\s*',
                f'<blockquote class="{cls}"><p><strong>{icon} {name}:</strong> ',
                body)
        body = re.sub(r'<pre><code class="language-mermaid">([\s\S]*?)</code></pre>',
                      lambda m: f'<pre class="mermaid">{m.group(1)}</pre>', body)
        body = body.replace('<table>', '<div class="table-wrap"><table>') \
                   .replace('</table>', '</table></div>')
        body = restore_math(body, store)
        body, warn = rewrite_links(body, p, url_of, file_urls)
        if warn:
            broken += warn
        n_math += body.count('class="ktx"') + body.count('class="ktxd"')
        n_diag += body.count('<pre class="mermaid">')
        all_meta.append(meta)
        bodies.append(body)

    for i, (meta, body) in enumerate(zip(all_meta, bodies)):
        prev_m = all_meta[i - 1] if i > 0 else None
        next_m = all_meta[i + 1] if i + 1 < len(all_meta) else None
        page = render_page(meta, body, build_nav(all_meta, meta['path']),
                           breadcrumb(meta), prev_m, next_m)
        (out_dir / meta['url']).write_text(page, encoding='utf-8')

    home = render_home(all_meta, n_math, n_diag, url_of)
    (out_dir / 'index.html').write_text(home, encoding='utf-8')

    # ---------------- validación en build ----------------
    pages = {m['url'] for m in all_meta} | {'index.html'}
    errors = []
    for m in all_meta:
        html_txt = (out_dir / m['url']).read_text(encoding='utf-8')
        for href in re.findall(r'href="([^"]+)"', html_txt):
            if href.startswith(('http', 'mailto:', '#', 'assets/')):
                continue
            target = href.split('#')[0]
            if not target:
                continue
            if target not in pages and not (out_dir / target).exists():
                errors.append(f'{m["url"]} -> {href}')
    for href in re.findall(r'href="(files/[^"#]+)"', (out_dir / 'index.html').read_text(encoding='utf-8')):
        if not (out_dir / href).exists():
            errors.append(f'index.html -> {href}')

    print('=' * 60)
    print('PORTAL FIT-12 — resumen del build')
    print('=' * 60)
    print(f'  páginas: {len(all_meta) + 1} ({len(all_meta)} docs + portada)')
    print(f'  fórmulas KaTeX: {n_math} · diagramas mermaid: {n_diag}')
    print(f'  archivos en portal/files/: {len(file_urls)}')
    if suspect:
        print(f'  ⚠️  TeX sospechoso ({len(suspect)}):')
        for s in suspect[:10]:
            print(f'     {s}')
    if errors:
        print(f'  ❌ ENLACES ROTOS ({len(errors)}):')
        for e in errors[:15]:
            print(f'     {e}')
        sys.exit(1)
    print('  ✅ validación: 0 enlaces internos rotos')
    print(f'  destino: {out_dir}')


if __name__ == '__main__':
    main()
