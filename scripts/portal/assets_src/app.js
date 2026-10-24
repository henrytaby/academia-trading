/* ============================================================
   Portal FIT-12 — app.js
   KaTeX (data-tex), mermaid (una pasada), tema, copiar código,
   sidebar colapsable y drawer móvil. Sin dependencias propias.
   ============================================================ */
(function(){
  'use strict';

  /* ---------- tema (el atributo ya lo fijó el inline del <head>) ---------- */
  var themeBtn = document.getElementById('theme-toggle');
  function currentTheme(){
    return document.documentElement.getAttribute('data-theme') || 'light';
  }
  if(themeBtn){
    themeBtn.textContent = currentTheme() === 'dark' ? '☀️' : '🌙';
    themeBtn.setAttribute('title', 'Alternar modo claro/oscuro');
    themeBtn.addEventListener('click', function(){
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try{ localStorage.setItem('fit12-theme', next); }catch(e){}
      themeBtn.textContent = next === 'dark' ? '☀️' : '🌙';
    });
  }

  /* ---------- sidebar: drawer móvil ---------- */
  var menuBtn = document.getElementById('menu-toggle');
  var sidebar = document.querySelector('.sidebar');
  if(menuBtn && sidebar){
    menuBtn.addEventListener('click', function(){ sidebar.classList.toggle('open'); });
    document.addEventListener('click', function(ev){
      if(sidebar.classList.contains('open') && !sidebar.contains(ev.target) && ev.target !== menuBtn && !menuBtn.contains(ev.target)){
        sidebar.classList.remove('open');
      }
    });
  }

  /* ---------- grupos colapsables ---------- */
  document.querySelectorAll('.nav-level').forEach(function(btn){
    btn.addEventListener('click', function(){
      btn.parentElement.classList.toggle('closed');
    });
  });

  /* ---------- botón copiar en bloques de código ---------- */
  document.querySelectorAll('.doc-body pre').forEach(function(pre){
    if(pre.classList.contains('mermaid')) return;
    var wrap = document.createElement('div');
    wrap.className = 'code-block';
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);
    var btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = 'copiar';
    btn.addEventListener('click', function(){
      var text = pre.innerText;
      function done(ok){
        btn.textContent = ok ? '¡copiado!' : 'error';
        setTimeout(function(){ btn.textContent = 'copiar'; }, 1400);
      }
      if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(text).then(function(){ done(true); }, function(){ done(false); });
      }else{
        try{
          var ta = document.createElement('textarea');
          ta.value = text; document.body.appendChild(ta); ta.select();
          document.execCommand('copy'); document.body.removeChild(ta); done(true);
        }catch(e){ done(false); }
      }
    });
    wrap.appendChild(btn);
  });

  /* ---------- KaTeX: render de .ktx (inline) y .ktxd (display) ---------- */
  var nMath = 0;
  if(window.katex){
    document.querySelectorAll('.ktx, .ktxd').forEach(function(el){
      var tex = el.getAttribute('data-tex');
      if(!tex) return;
      try{
        window.katex.render(tex, el, {
          displayMode: el.classList.contains('ktxd'),
          throwOnError: false, strict: false
        });
        nMath++;
      }catch(e){ /* el contenido textual (TeX plano) queda como respaldo */ }
    });
  }

  /* ---------- mermaid: una sola pasada sobre los presentes ---------- */
  var nDiag = 0;
  if(window.mermaid){
    var blocks = document.querySelectorAll('pre.mermaid');
    if(blocks.length){
      try{
        window.mermaid.initialize({ startOnLoad:false, securityLevel:'loose', theme: currentTheme() === 'dark' ? 'dark' : 'default' });
        window.mermaid.run({ nodes: blocks }).then(function(){
          document.dispatchEvent(new CustomEvent('fit12:diagrams-done', { detail:{ count: blocks.length } }));
        });
        nDiag = blocks.length;
      }catch(e){ console.error('mermaid:', e); }
    }
  }

  /* ---------- telemetría mínima para verificación (window.__portal) ---------- */
  window.__portal = {
    math: nMath,
    mathTotal: document.querySelectorAll('.ktx, .ktxd').length,
    diagrams: nDiag,
    theme: currentTheme()
  };
})();
