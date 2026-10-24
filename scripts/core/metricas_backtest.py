#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
metricas_backtest.py — Calculadora de métricas del reporte del programa FIT-12 (Módulo 9).

Módulo de CÁLCULO (agents.md § 2.5: alta cohesión, bajo acoplamiento —
sin lectura de archivos en las funciones puras, sin red, sin estado global;
la lectura del CSV vive solo en leer_csv y el test, en __main__).

Métricas del reporte de una página (lección 9.3):
    validar_filas(filas)      -> errores de integridad del dataset (9.1: todo entra, nada vacío)
    wr, ic95                  -> Win Rate medido y su intervalo de confianza 95 %
    rb_medio                  -> R:B medio de las ganadoras (R̄_g)
    esperanza                 -> E bruta y E neta (con coste medio c)
    wr_equilibrio_neto        -> WR* = (1+c)/(R̄+1) (9.3)
    profit_factor             -> PF bruto y PF neto (costes a ganadoras y perdedoras)
    rachas                    -> racha máxima medida + racha esperada ln(N)/ln(1/(1-WR))
    max_drawdown              -> Max DD de la curva de capital acumulada en R
    disparos                  -> ejecutados / debidos (métrica de M8)
    decision_3_vias           -> 🟢 aprobar / 🟡 provisional / 🔴 no operar (tabla de 9.3)
    reporte(filas)            -> dict con las 13 métricas listas para el reporte M-9

Test mínimo: `python3 metricas_backtest.py` ejecuta los asserts del caso maestro
(WR 40 %, R̄ 2,1, c 0,08 -> E neta +0,16R, PF neto 1,25, racha esperada ~9,
WR* neto 34,8 %) + una muestra sintética de 100 operaciones + integración con
el CSV de ejemplo del journal v1.
"""

import csv
import math

# ---------- integridad del dataset (9.1) ----------

ETIQUETAS_VALIDAS = {"E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"}
FASES_VALIDAS = {"backtest", "forward_demo", "real_micro"}


def validar_filas(filas: list) -> list:
    """Devuelve la lista de problemas de integridad (fila vacía, etiqueta fuera
    de taxonomía, R real ausente). Un dataset con problemas NO se promedia:
    primero se audita (9.3, paso 1)."""
    problemas = []
    for i, f in enumerate(filas, start=1):
        if not f.get("etiqueta_error", "").strip():
            problemas.append(f"fila {i}: etiqueta_error vacía")
        elif f["etiqueta_error"].strip().upper() not in ETIQUETAS_VALIDAS:
            problemas.append(f"fila {i}: etiqueta {f['etiqueta_error']} fuera de la taxonomía E0-E7")
        if f.get("r_real", "") in ("", None):
            problemas.append(f"fila {i}: r_real ausente")
        if f.get("fase", "") and f["fase"].strip() not in FASES_VALIDAS:
            problemas.append(f"fila {i}: fase {f['fase']} no es del embudo")
    return problemas


def _r(filas: list) -> list:
    return [float(f["r_real"]) for f in filas]


# ---------- métricas del reporte (9.3) ----------

def wr(filas: list) -> float:
    """Win Rate medido: ganadoras (r_real > 0) sobre el total."""
    rs = _r(filas)
    return sum(1 for r in rs if r > 0) / len(rs)


def _ic95(wr_medido: float, n: int) -> tuple:
    """IC 95 % del WR: ±1,96·√(WR(1-WR)/N). Devuelve (inferior, superior)."""
    half = 1.96 * math.sqrt(wr_medido * (1 - wr_medido) / n)
    return wr_medido - half, wr_medido + half


def rb_medio(filas: list) -> float:
    """R:B medio: media de las ganadoras en R."""
    ganadoras = [float(f["r_real"]) for f in filas if float(f["r_real"]) > 0]
    if not ganadoras:
        return 0.0
    return sum(ganadoras) / len(ganadoras)


def esperanza(filas: list, coste_r: float = None) -> dict:
    """E bruta = WR·R̄ - (1-WR)·1; E neta = E bruta - c.
    Si coste_r es None usa la media de la columna coste_r."""
    w = wr(filas)
    rg = rb_medio(filas)
    if coste_r is None:
        costes = [float(f["coste_r"]) for f in filas if f.get("coste_r") not in ("", None)]
        coste_r = sum(costes) / len(costes) if costes else 0.0
    e_bruta = w * rg - (1 - w) * 1.0
    return {"wr": w, "rb_medio": rg, "coste": coste_r,
            "e_bruta": e_bruta, "e_neta": e_bruta - coste_r}


def wr_equilibrio_neto(rb: float, coste: float) -> float:
    """WR* = (1+c)/(R̄+1): el equilibrio con el coste dentro (9.3)."""
    return (1 + coste) / (rb + 1)


def profit_factor(filas: list, coste_r: float = None) -> dict:
    """PF bruto = ΣG/ΣP; PF neto = (ΣG - costes de ganadoras)/(ΣP + costes de perdedoras)."""
    if coste_r is None:
        costes = [float(f["coste_r"]) for f in filas if f.get("coste_r") not in ("", None)]
        coste_r = sum(costes) / len(costes) if costes else 0.0
    g = sum(r for r in _r(filas) if r > 0)
    p = -sum(r for r in _r(filas) if r < 0)
    n = len(filas)
    pf_bruto = g / p if p > 0 else float("inf")
    # el coste se reparte: ganadoras c a cada ganadora, perdedoras c a cada perdedora
    n_w = sum(1 for r in _r(filas) if r > 0)
    n_l = n - n_w
    g_neto = max(g - n_w * coste_r, 1e-9)
    p_neto = max(p + n_l * coste_r, 1e-9)
    return {"bruto": pf_bruto, "neto": g_neto / p_neto}


def rachas(filas: list) -> dict:
    """Racha máxima medida + racha esperada ln(N)/ln(1/(1-WR)) + P de una racha n puntual."""
    mejor = actual = 0
    for r in _r(filas):
        if r < 0:
            actual += 1
            mejor = max(mejor, actual)
        else:
            actual = 0
    n = len(filas)
    w = wr(filas)
    esperada = math.log(n) / math.log(1 / (1 - w)) if w < 1 else 0.0
    return {"max_medida": mejor, "esperada": esperada,
            "p_puntual": (1 - w) ** mejor if mejor else 0.0}


def max_drawdown(filas: list) -> float:
    """Max DD de la curva acumulada en R (valor negativo, pico a valle)."""
    curva, maximo, dd = 0.0, 0.0, 0.0
    for r in _r(filas):
        curva += r
        maximo = max(maximo, curva)
        dd = min(dd, curva - maximo)
    return dd


def disparos(filas: list) -> dict:
    """Ejecutados/debidos (M8): señales del sistema ejecutadas sobre las debidas.
    filas con disparo_debido=Si cuentan como debidas; ejecutadas son las mismas filas
    (una señal debida no ejecutada no crea fila — vive en el acta semanal)."""
    debidos = sum(1 for f in filas if f.get("disparo_debido", "").lower() == "si")
    return {"ejecutados": len(filas), "debidos": debidos,
            "ratio": len(filas) / debidos if debidos else 1.0}


def decision_3_vias(reporte: dict) -> str:
    """La tabla de 9.3 leída completa: el veto más restrictivo manda.
    🟢 WR ≥ 0,40 y PF neto ≥ 1,25 y racha ≤ 12 y disparos = 1,0
    🔴 WR < WR* neto o PF neto < 1,1 o racha ≥ 15
    🟡 lo demás (provisional)."""
    w = reporte["wr"]
    pf_n = reporte["pf"]["neto"]
    racha = reporte["rachas"]["max_medida"]
    disp = reporte["disparos"]["ratio"]
    wr_star = reporte["wr_equilibrio_neto"]
    if w < wr_star or pf_n < 1.1 or racha >= 15:
        return "🔴 ROJO — no operar: volver al laboratorio de M7 con los datos"
    if w >= 0.40 and pf_n >= 1.25 and racha <= 12 and disp >= 0.9999:
        return "🟢 VERDE — aprobar al 1 % y pasar a forward (9.4)"
    return "🟡 ÁMBAR — provisional: 0,25-0,5 % en demo forward y seguir sumando muestra"


def reporte(filas: list, coste_r: float = None) -> dict:
    """Las 13 métricas del reporte de una página, listas para el reporte M-9."""
    n = len(filas)
    w = wr(filas)
    esp = esperanza(filas, coste_r)
    pf = profit_factor(filas, esp["coste"])
    rac = rachas(filas)
    dd = max_drawdown(filas)
    return {
        "n": n,
        "wr": w,
        "ic95": _ic95(w, n),
        "rb_medio": esp["rb_medio"],
        "e_bruta": esp["e_bruta"],
        "coste_medio": esp["coste"],
        "e_neta": esp["e_neta"],
        "wr_equilibrio_neto": wr_equilibrio_neto(esp["rb_medio"], esp["coste"]),
        "pf": pf,
        "rachas": rac,
        "max_dd_r": dd,
        "disparos": disparos(filas),
        "decision": None,
    }


# ---------- lectura del CSV del journal v1 ----------

def leer_csv(ruta: str) -> list:
    """Lee el CSV del journal v1 (o el de ejemplo). Devuelve listas de dicts."""
    with open(ruta, encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------- test mínimo ----------

if __name__ == "__main__":
    print("=== Test 1 · caso maestro analítico (10 ops: WR 40 %, R̄ 2,1, c 0,08) ===")
    filas_caso = (
        [{"r_real": r, "coste_r": 0.08, "disparo_debido": "Si", "etiqueta_error": "E0", "fase": "backtest"} for r in (2.0, 1.8, 2.4, 2.2)]
        + [{"r_real": -1.0, "coste_r": 0.08, "disparo_debido": "Si", "etiqueta_error": "E0", "fase": "backtest"}] * 6
    )
    rep = reporte(filas_caso)
    assert abs(rep["wr"] - 0.40) < 1e-9
    assert abs(rep["rb_medio"] - 2.10) < 1e-9
    assert abs(rep["e_bruta"] - 0.24) < 1e-9
    assert abs(rep["e_neta"] - 0.16) < 1e-9
    assert abs(rep["pf"]["bruto"] - 1.40) < 1e-9
    assert abs(rep["pf"]["neto"] - 1.2469135802) < 1e-9   # 0,808/0,648
    assert abs(rep["wr_equilibrio_neto"] - 0.3483870968) < 1e-9  # 1,08/3,10
    print(f"WR {rep['wr']:.0%} · E bruta +{rep['e_bruta']:.2f}R · E neta +{rep['e_neta']:.2f}R · "
          f"PF bruto {rep['pf']['bruto']:.2f} · PF neto {rep['pf']['neto']:.2f} · "
          f"WR* neto {rep['wr_equilibrio_neto']:.1%} ✓")
    print("  El coste se come 0,08/0,24 = 33 % de la E bruta ✓")

    print("=== Test 2 · IC y rachas esperadas ===")
    lo30, hi30 = _ic95(0.40, 30)
    assert abs(lo30 - 0.2250) < 0.001 and abs(hi30 - 0.5750) < 0.001
    lo, hi = _ic95(0.40, 100)
    assert abs(lo - 0.3039) < 0.001 and abs(hi - 0.4961) < 0.001
    assert abs(math.log(100) / math.log(1 / 0.6) - 9.01) < 0.02
    assert abs(0.99 ** 9 - 0.9135) < 1e-4
    print(f"N=30 -> IC [{lo30:.1%}, {hi30:.1%}] ±17,5 pp ✓ · N=100 -> [{lo:.1%}, {hi:.1%}] ±9,6 pp ✓")
    print(f"racha esperada a N=100: ~9 · DD al 1 %: -8,6 % ✓")

    print("=== Test 3 · muestra sintética de 100 operaciones (WR 40 %, R̄ 2,1) ===")
    sintetica = (
        [{"r_real": 2.1, "coste_r": 0.08, "disparo_debido": "Si", "etiqueta_error": "E0", "fase": "backtest"}] * 40
        + [{"r_real": -1.0, "coste_r": 0.08, "disparo_debido": "Si", "etiqueta_error": "E0", "fase": "backtest"}] * 60
    )
    rep2 = reporte(sintetica)
    assert rep2["n"] == 100
    assert abs(rep2["wr"] - 0.40) < 1e-9
    assert abs(rep2["e_neta"] - 0.16) < 1e-9
    assert abs(rep2["pf"]["neto"] - 1.2469135802) < 1e-9
    assert rep2["max_dd_r"] == -60.0  # el orden del bloque concentra 60 pérdidas al final: pico +84R -> valle +24R
    assert rep2["rachas"]["max_medida"] == 60
    print(f"N=100 · WR {rep2['wr']:.0%} · E neta +{rep2['e_neta']:.2f}R · PF neto {rep2['pf']['neto']:.2f} · "
          f"Max DD {rep2['max_dd_r']:.1f}R y racha {rep2['rachas']['max_medida']} "
          f"(artefacto del orden del bloque: 40 victorias y luego 60 pérdidas seguidas) — fórmulas ✓")
    print("  (en una muestra real vela a vela el orden es aleatorio: la racha medida la da el dataset)")

    print("=== Test 4 · integridad del dataset (9.1) ===")
    sucias = [{"etiqueta_error": "E0", "r_real": 1.0, "fase": "backtest"},
              {"etiqueta_error": "", "r_real": -1.0, "fase": "backtest"},
              {"etiqueta_error": "E9", "r_real": 2.0, "fase": "forward_demo"},
              {"etiqueta_error": "E1", "r_real": "", "fase": "backtest"},
              {"etiqueta_error": "E0", "r_real": 1.0, "fase": "hoy"}]
    problemas = validar_filas(sucias)
    assert len(problemas) == 4
    assert all("fila" in p for p in problemas)
    print(f"{len(problemas)} problemas detectados (etiqueta vacía, E9 fuera de taxonomía, R ausente, fase inválida) ✓")
    assert validar_filas(filas_caso) == []
    print("dataset limpio -> 0 problemas ✓")

    print("=== Test 5 · integración con el CSV de ejemplo del journal v1 ===")
    filas_csv = leer_csv("/home/z/my-project/download/academia-trading/journal/plantilla_journal_v1.csv")
    assert len(filas_csv) == 4
    assert validar_filas(filas_csv) == [], validar_filas(filas_csv)
    rep3 = reporte(filas_csv)
    # WR 50 % (2 de 4), R̄ (2,0+2,0)/2 = 2,0 -> E bruta 0,5·2 - 0,5 = +0,5R
    assert abs(rep3["wr"] - 0.50) < 1e-9
    assert abs(rep3["rb_medio"] - 2.0) < 1e-9
    assert abs(rep3["e_neta"] - 0.4175) < 1e-9  # c medio = (0,08+0,09+0,08+0,08)/4 = 0,0825 -> 0,5 - 0,0825
    etiquetas = sorted(f["etiqueta_error"] for f in filas_csv)
    assert etiquetas == ["E0", "E0", "E2", "E4"]
    assert abs(max_drawdown(filas_csv) - (-2.0)) < 1e-9  # orden CSV: +2,-1,-1,+2 -> pico +2R, valle 0R: DD -2R
    print(f"4 filas migradas · etiquetas {etiquetas} · WR {rep3['wr']:.0%} · "
          f"E bruta +{rep3['e_bruta']:.2f}R · E neta +{rep3['e_neta']:.2f}R ✓")

    print("=== Test 6 · decisión de 3 vías (los umbrales de 9.3) ===")
    # rojo: WR bajo el equilibrio neto
    rep_rojo = reporte(filas_caso)
    rep_rojo["wr"] = 0.30
    rep_rojo["wr_equilibrio_neto"] = 0.348
    rep_rojo["pf"] = {"bruto": 1.0, "neto": 0.95}
    rep_rojo["rachas"] = {"max_medida": 10}
    rep_rojo["disparos"] = {"ratio": 1.0}
    assert decision_3_vias(rep_rojo).startswith("🔴")
    # verde: todo en umbral
    rep_verde = dict(reporte(filas_caso))
    rep_verde.update({"pf": {"bruto": 1.40, "neto": 1.30}, "rachas": {"max_medida": 9},
                      "disparos": {"ratio": 1.0}})
    assert decision_3_vias(rep_verde).startswith("🟢")
    # ámbar: WR 37 % en zona [34,8; 40)
    rep_amb = dict(reporte(filas_caso))
    rep_amb.update({"wr": 0.37, "pf": {"bruto": 1.35, "neto": 1.22},
                    "rachas": {"max_medida": 11}, "disparos": {"ratio": 0.98}})
    assert decision_3_vias(rep_amb).startswith("🟡")
    print("rojo / verde / ámbar según la tabla de 9.3 ✓")

    print("\nTodos los asserts superados — la calculadora coincide con el caso maestro de 9.3.")
