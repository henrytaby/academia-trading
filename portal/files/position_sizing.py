#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
position_sizing.py — Calculadora de riesgo del programa FIT-12 (Módulo 8).

Módulo de CÁLCULO (agents.md § 2.5: alta cohesión, bajo acoplamiento —
sin lectura de archivos, sin red, sin estado global; el formato y la
persistencia viven en otra capa).

Funciones:
    valor_pip(par, precio)            -> valor del pip por lote estándar (cuenta USD)
    calc_lote(capital, pct, sl_pips, valor_pip)  -> presupuesto, lote con redondeo
                                                       a la baja, verificación inversa
    tabla_recuperacion(dd_pct)        -> recuperación necesaria R = d/(1-d)
    riesgo_efectivo(r1, r2, rho)      -> suma conservadora por bandas (M8.5)
    veredicto_cartera(...)            -> ACEPTAR/RECHAZAR contra topes 2 % motor / 3 % global
    nivel_freno(...)                  -> nivel activo de la cascada (8.6)

Test mínimo: `python3 position_sizing.py` ejecuta los 3 casos de control
del laboratorio M8 + asserts de la cascada y la cartera.
"""

# ---------- cálculo: valor del pip ----------

def valor_pip(par: str, precio: float = None) -> float:
    """Valor del pip de 1 lote estándar (100.000 unidades) en cuenta USD.

    - Pares XXX/USD (cotización USD): fijo en 10 $/pip.
    - Pares USD/XXX: (tamaño_pip * 100.000) en divisa cotizada, dividido por el precio.
    - XAU/USD (oro): convención del programa — 1,00 $ de movimiento = 100 $ por lote.
    """
    par = par.upper()
    if par == "XAU/USD":
        return 100.0  # por cada 1,00 $ de movimiento de precio
    if par.endswith("/USD"):
        return 10.0   # EUR/USD, GBP/USD, AUD/USD...
    if par.startswith("USD/"):
        if par == "USD/JPY":
            pip_size = 0.01    # el pip del JPY tiene 2 decimales
        else:
            pip_size = 0.0001
        return pip_size * 100_000 / precio
    raise ValueError(f"par no soportado en el módulo: {par}")


# ---------- cálculo: position sizing (M8.3) ----------

def calc_lote(capital: float, riesgo_pct: float, sl_pips: float,
              valor_pip_lote: float, grano: float = 0.01) -> dict:
    """La fórmula universal con las 5 micro-reglas.

    Devuelve dict con: presupuesto, lote_bruto, lote_final (redondeo SIEMPRE
    a la baja al grano — micro-lote por defecto), riesgo_real y su %,
    verificacion (lote x SL x valor_pip) y rechazada (True si el lote bruto
    no llega al grano mínimo — 'no hay espacio de riesgo').
    """
    presupuesto = capital * riesgo_pct / 100.0
    riesgo_por_lote = sl_pips * valor_pip_lote
    lote_bruto = presupuesto / riesgo_por_lote
    lote_final = int(lote_bruto / grano) * grano  # floor al grano, nunca arriba
    if lote_final < grano:
        return {"rechazada": True, "motivo": "no hay espacio de riesgo: el lote bruto "
                f"({lote_bruto:.4f}) está por debajo del grano mínimo ({grano})",
                "presupuesto": presupuesto, "lote_bruto": lote_bruto,
                "lote_final": 0.0, "riesgo_real": 0.0, "riesgo_real_pct": 0.0,
                "verificacion": 0.0}
    riesgo_real = lote_final * sl_pips * valor_pip_lote
    return {"rechazada": False, "motivo": "",
            "presupuesto": round(presupuesto, 2),
            "lote_bruto": round(lote_bruto, 4),
            "lote_final": round(lote_final, 2),
            "riesgo_real": round(riesgo_real, 2),
            "riesgo_real_pct": round(riesgo_real / capital * 100.0, 3),
            "verificacion": round(lote_final * sl_pips * valor_pip_lote, 2)}


# ---------- cálculo: asimetría del drawdown (M8.2) ----------

def tabla_recuperacion(dd_pct: float) -> float:
    """Recuperación necesaria (en % del capital restante): R = d/(1-d)."""
    d = dd_pct / 100.0
    return d / (1.0 - d) * 100.0


# ---------- cálculo: cartera y correlación (M8.5) ----------

BANDA_ALTA = 0.70      # rho >= 0.70  -> suma completa
BANDA_MEDIA = 0.30     # 0.30-0.70    -> suma de la mitad
TOPE_MOTOR = 2.0       # % máximo por motor
TOPE_GLOBAL = 3.0      # % máximo simultáneo de la cartera


def riesgo_efectivo(r1: float, r2: float, rho: float) -> float:
    """Suma conservadora por bandas: rho >= .7 -> r1+r2 ; .3-.7 -> r1+r2/2 ; <.3 -> r1+r2."""
    if rho >= BANDA_ALTA:
        return r1 + r2
    if rho >= BANDA_MEDIA:
        return r1 + r2 / 2.0
    return r1 + r2  # motores independientes: suman para el tope global


def veredicto_cartera(riesgo_motor_actual: float, riesgo_global_actual: float,
                      riesgo_nueva: float, rho_con_motor: float) -> dict:
    """Veredicto de una nueva señal contra los topes escritos del programa."""
    ef_motor = riesgo_efectivo(riesgo_motor_actual, riesgo_nueva, rho_con_motor)
    ef_global = riesgo_global_actual + riesgo_nueva
    if ef_motor > TOPE_MOTOR:
        return {"veredicto": "RECHAZAR", "motivo": "tope por motor",
                "riesgo_motor": round(ef_motor, 2)}
    if ef_global > TOPE_GLOBAL:
        return {"veredicto": "RECHAZAR", "motivo": "tope global",
                "riesgo_global": round(ef_global, 2)}
    return {"veredicto": "ACEPTAR", "motivo": "dentro de topes",
            "riesgo_motor": round(ef_motor, 2),
            "riesgo_global": round(ef_global, 2)}


# ---------- cálculo: frenos en cascada (M8.6) ----------

def nivel_freno(dd_dia_pct: float, dd_semana_pct: float, dd_mes_pct: float,
                perdidas_consecutivas: int) -> dict:
    """Nivel activo de la cascada: 0 en calma; 1-4 según el primer disparo alcanzado.

    Solo compara NÚMEROS (saldos y conteos) — nunca sentimientos.
    """
    if dd_mes_pct <= -6.0:
        return {"nivel": 4, "accion": "APAGADO TOTAL: cerrar todo, cerrar plataforma, "
                "journal, no antes de 48 h + defensa con el auditor"}
    if dd_semana_pct <= -4.0:
        return {"nivel": 3, "accion": "resto de la semana fuera + revision fria del journal"}
    if perdidas_consecutivas >= 2:
        return {"nivel": 2, "accion": "pausa obligatoria 30-60 min fuera de la plataforma"}
    if dd_dia_pct <= -2.0:
        return {"nivel": 1, "accion": "cerrar TODAS las posiciones: fin del dia"}
    return {"nivel": 0, "accion": "continuar con el sistema v1.0"}


# ---------- test mínimo: casos de control del laboratorio ----------

def _tests():
    # Caso de control (a): el caso maestro de la Receta
    r = calc_lote(1920.0, 1.0, 32.0, 10.0)
    assert r["lote_final"] == 0.06 and r["riesgo_real"] == 19.20, r
    assert r["riesgo_real_pct"] == 1.0, r
    # Caso de control (b): USD/JPY a 150
    vp = valor_pip("USD/JPY", 150.0)
    assert abs(vp - 6.6667) < 0.001, vp
    r = calc_lote(1920.0, 1.0, 30.0, round(vp, 2))
    assert r["lote_final"] == 0.09 and r["riesgo_real"] == 18.01, r
    # Caso de control (c): rechazo por grano mínimo
    r = calc_lote(350.0, 1.0, 80.0, 10.0)
    assert r["rechazada"] is True, r
    # Asimetría
    assert abs(tabla_recuperacion(50.0) - 100.0) < 1e-9
    assert abs(tabla_recuperacion(10.0) - 11.1111) < 0.001
    # Cartera: tope por motor
    v = veredicto_cartera(1.0, 1.0, 1.0, 0.85)
    assert v["veredicto"] == "ACEPTAR" and v["riesgo_motor"] == 2.0, v
    v = veredicto_cartera(2.0, 2.0, 1.0, 0.85)
    assert v["veredicto"] == "RECHAZAR" and v["motivo"] == "tope por motor", v
    # Cascada
    assert nivel_freno(-1.0, -1.0, -3.0, 1)["nivel"] == 0
    assert nivel_freno(-2.5, -2.5, -3.0, 2)["nivel"] == 2   # la pausa precede al cierre del día
    assert nivel_freno(-1.0, -4.2, -5.0, 0)["nivel"] == 3
    assert nivel_freno(-1.0, -2.0, -6.5, 0)["nivel"] == 4
    return True


if __name__ == "__main__":
    ok = _tests()
    print("TEST MINIMO:", "OK — 9 asserts superados" if ok else "FALLO")

    print("\n--- Caso maestro de la Receta ---")
    r = calc_lote(1920.0, 1.0, 32.0, 10.0)
    for k in ("presupuesto", "lote_bruto", "lote_final", "riesgo_real",
              "riesgo_real_pct", "verificacion"):
        print(f"  {k}: {r[k]}")

    print("\n--- Verificacion de la cascada (ejemplo 8.6) ---")
    print(" ", nivel_freno(-1.0, -1.0, -3.0, 2))

    print("\n--- Tabla de recuperacion (M8.2) ---")
    for dd in (5, 10, 20, 30, 50, 70):
        print(f"  -{dd}%  ->  +{tabla_recuperacion(dd):.1f}%")
