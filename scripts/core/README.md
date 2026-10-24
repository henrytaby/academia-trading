# scripts/core/ — Código del Programa

> **Estado: activo desde Sprint 8.** Aquí viven las herramientas Python del programa. **Regla de arquitectura (agents.md § 2.5):** alta cohesión y bajo acoplamiento — separación estricta entre cálculo, formato y persistencia. Cada script con docstring y test mínimo si es calculable.

| Script | Módulo de origen | Qué hace | Test mínimo |
|---|---|---|---|
| [`position_sizing.py`](position_sizing.py) | M8 · Gestión del Riesgo | Calculadora de riesgo: valor del pip por instrumento, position sizing con redondeo a la baja y veto, asimetría del drawdown, riesgo efectivo de cartera con topes, cascada de frenos | `python3 position_sizing.py` — 9 asserts (3 casos de control del lab M8 + cartera + cascada) |
| [`metricas_backtest.py`](metricas_backtest.py) | M9 · Backtesting, Journal y Validación | Calculadora de métricas: validación de integridad del dataset, WR + IC 95 %, R:B medio, E bruta/neta, WR de equilibrio neto, PF bruto/neto, rachas (medida y esperada), Max DD, disparos ejecutados/debidos, decisión de 3 vías y reporte de 13 métricas desde el CSV del journal v1 | `python3 metricas_backtest.py` — 6 bloques de asserts (caso maestro de 9.3: WR 40 %, E neta +0,16R, PF neto 1,25, WR* 34,8 % + muestra sintética de 100 + CSV de ejemplo del journal v1) |
