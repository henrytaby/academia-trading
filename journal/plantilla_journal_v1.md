# Journal v1 — el registro profesional del negocio (M9)

> **El instrumento de auditoría del programa.** El journal v0 (Sprint 2) registraba la mecánica de la operación; el v1 registra el **negocio**: la decisión antes (R planificado), el diagnóstico en caliente (taxonomía E0–E7), la evidencia (captura de señal) y el estado de la máquina (emocional pre/post). Todo el aparato estadístico del M9 — las 100 operaciones, las métricas del reporte, las actas de revisión — se calcula **de estas filas**.
> Definiciones completas: [Lección 9.5](../docs/02-modulos/mod-09-backtesting-journal-y-validacion/leccion-9-5.md) · Protocolo de captura de datos: [Lección 9.2](../docs/02-modulos/mod-09-backtesting-journal-y-validacion/leccion-9-2.md).

## Archivos

| Archivo | Uso |
|---|---|
| [`plantilla_journal_v1.csv`](plantilla_journal_v1.csv) | El registro: 24 columnas + 4 filas de ejemplo migradas. Cópialo a tu hoja de cálculo o úsalo directo |
| [`plantilla_journal_v0.csv`](plantilla_journal_v0.csv) | El antecesor (Sprint 2): se conserva como histórico; migra sus filas al v1 cuando sea posible |
| `reporte-m9.md` *(lo creas tú)* | El reporte de la [Misión M-9](../docs/02-modulos/mod-09-backtesting-journal-y-validacion/README.md#-misión) |
| [`../scripts/core/metricas_backtest.py`](../scripts/core/metricas_backtest.py) | El oráculo: calcula las 13 métricas desde el CSV y verifica tu hoja |

## Las 24 columnas y para qué existe cada una

| # | Columna | Definición operativa | Consumidor |
|---|---|---|---|
| 1 | `fecha` | Fecha de la operación | Acta semanal, serie temporal |
| 2-3 | `hora_inicio`, `hora_fin` | Horas de gestión de la posición (formato 24h) | Ventanas de sesión (M2) |
| 4 | `fase` | `backtest` / `forward_demo` / `real_micro` — la estación del embudo (9.4) | Reporte por fases |
| 5 | `mercado` | Instrumento (EURUSD, XAUUSD…) | Conteo por motor (M8) |
| 6-7 | `direccion`, `tipo_orden` | long/short · limit/market/stop | Auditoría de mecánica (M4) |
| 8 | `setup_valido` | `Si`/`No` — el checklist de 8 condiciones (9.2) pasó completo | Métrica de disparos (M8) |
| 9 | `disparo_debido` | `Si`/`No`/`NA` — ¿era señal del sistema y la ejecutaste? | Disparos ejecutados/debidos |
| 10 | `lote` | El lote REAL puesto (no el que debías) | Auditoría E4 vs calculadora (M8) |
| 11-13 | `entrada`, `sl`, `tp` | Precios exactos de la decisión (paso 5 de la rutina 9.2) | Auditoría de precisión |
| 14 | `r_planificada` | R:B de la operación al decidir: (TP−entrada)/(entrada−SL) | Deriva de ejecución (9.5) |
| 15 | `r_real` | Resultado en R: resultado $ ÷ riesgo real puesto | WR, E, PF, rachas, curva (9.3) |
| 16 | `resultado_usd` | Resultado en dólares | El P&L del negocio |
| 17 | `coste_r` | Spread + slippage de la operación, en R | El ladrón silencioso: audita el 0,08R |
| 18 | `sl_antes_entrada` | `Si`/`No` — la ley de M4, verificada fila por fila | Cero tolerancia (M4) |
| 19 | `captura` | Ruta de la imagen del gráfico EN el momento de la señal | La evidencia que la memoria no puede reescribir |
| 20-21 | `emocional_pre`, `emocional_post` | 1–10 (1 = pésimo, 10 = óptimo) | Semilla del diario de M10; patrones del acta |
| 22 | `etiqueta_error` | **E0–E7** (taxonomía abajo) — UNA etiqueta, en caliente | El mapa de tu ejecución |
| 23 | `regla_violada` | 1 línea: qué regla concreta, si hubo etiqueta ≠ E0 | Puente al changelog (9.6) |
| 24 | `leccion_1linea` | UNA línea de lección (opcional; si necesita más, va al acta) | Materia prima del plan (M12) |

**Columnas extra del forward** (añádelas cuando pases a la fase 2 de 9.4): `spread_real` (el spread vivo al momento de la señal) y `slippage_sl` (precio SL vs precio de ejecución, cuando el SL se ejecuta).

## La taxonomía de errores E0–E7

| Etiqueta | Nombre | Definición operativa |
|---|---|---|
| **E0** | En plan (sin error) | Setup válido + ejecución conforme + gestión conforme. **Incluye TODA pérdida con SL respetado y sizing correcto** — el coste estadístico del negocio |
| **E1** | Operar sin setup | Se ejecutó una señal que la definición de setup válido rechaza (FOMO, aburrimiento, revancha) |
| **E2** | Entrada fuera de regla | Setup válido, ejecución fuera de la regla: antes de la vela cerrada, fuera de zona, precio improvisado |
| **E3** | SL manipulado | SL movido, ampliado o eliminado — o cierre manual antes del SL sin regla de gestión que lo autorice |
| **E4** | Sizing fuera de presupuesto | El lote no es la salida de la calculadora de M8 (por exceso O por defecto no documentado) |
| **E5** | Gestión improvisada | TP movido, parcial o breakeven sin que una regla del componente 10 lo autorice |
| **E6** | Freno ignorado | Operar con la cascada de M8 activa o violar un tope de cartera |
| **E7** | Error de ejecución técnica | Orden mal puesta, fat finger, OCO olvidado, dirección invertida |

**Las 3 reglas de uso** *(lección 9.5 — sin ellas el conteo pierde valor estadístico)*:
1. **UNA etiqueta por operación** — la primera de la cadena causal; el resto va a `regla_violada`.
2. **En caliente** — al cerrar la operación, con la taxonomía a la vista; el etiquetado del domingo es reconstrucción y la reconstrucción defiende al ego.
3. **La taxonomía es cerrada** — si un error no encaja, se describe en `regla_violada` y la revisión decide si merece etiqueta nueva (con evidencia).

## La rutina de los 90 segundos (post-operación)

1. **R real + resultado $** (10 s) — la fila queda económicamente cerrada.
2. **Etiqueta E0–E7** (20 s) — con la tabla impresa junto al monitor.
3. **Emocional post 1–10** (5 s) — honestidad de 5 segundos, no ensayo.
4. **Captura verificada en la fila** (5 s) — la imagen de la señal ya existe (se tomó al disparar); falta la ruta.
5. **Lección de UNA línea** (50 s) — si no cabe en una línea, va al acta de la semana.

**Regla dura:** la plataforma no se cierra con filas pendientes. La memoria pendiente es memoria que se falsifica.

## Registro de lo que NO operaste

- **Señales válidas no ejecutadas** → van al acta semanal como no-disparos (alimentan disparos ejecutados/debidos de M8). No crean fila en el CSV.
- **Señales rechazadas por la definición** → 1 línea en el registro de la sesión (fecha, mercado, razón del rechazo). Son la diferencia entre tu sistema y tu instinto, en datos.

## Plantilla de acta semanal (9.6 — 30–45 min, día fijo)

```text
ACTA SEMANAL N.º ___ · del ___ al ___
1. La semana en datos: N ops ___ · resultado ___R · E0 __ E1 __ E2 __ E3 __ E4 __ E5 __ E6 __ E7 __
2. La etiqueta más frecuente (≠ E0) y su cadena causal: ______________________
3. Las 5 preguntas (sí/no con el dato): setups 8/8 ___ · sizing conforme ___ · SL respetados ___
   · emocional sin contaminación ___ · corrección identificada ___
4. Disparos: debidos ___ · ejecutados ___ · ratio ___ % · bloqueo del faltante: ____________
5. UNA conclusión (la regla de UNA mejora — solo ejecución, nunca reglas): __________________
6. Decisión: [entrenamiento ___] · [Sistema v1.1: sin cambios] · firma y fecha
```

## Plantilla de acta mensual (9.6 — 1–2 h, última semana del mes)

```text
ACTA MENSUAL · mes de ______
A. El mes en métricas: N __ · WR __ % (IC del backtest: [30,4; 49,6]) · PF neto ___ (backtest: 1,25)
   · racha máx __ (esperada ~9/100 ops) · Max DD __ % (línea: −15 %) · coste medio __ R (estimado: 0,08)
   · disparos __/__ · curva del mes: [adjunta o describe pendiente-valles-recuperación]
B. La comparación: ¿el mes vivido se parece al sistema medido? — sí/no por métrica, con el número delante
C. Sospechas documentadas (casos borde, cambios de régimen, dudas del diario): ____________
D. Ventana de modificación — las 4 condiciones: [ ] ventana en frío · [ ] evidencia con N
   · [ ] UNA modificación única · [ ] re-test 50-100 backtests planeado
E. Decisión de versión: v1.1 SIN CAMBIOS  /  v1.2 con la modificación única: ____________
F. Firma (en frío) y fecha
```

## El changelog del sistema (se rellena desde las actas)

| Versión | Fecha | Evidencia (actas/filas) | La modificación única | Re-test |
|---|---|---|---|---|
| v1.0 | (M7) | — | Sistema inicial con plantilla de 10 componentes | 30 repeticiones (M-7) |
| v1.1 | (M8) | Componente 9-10 | Calculadora referenciada + topes 2 %/3 % + cascada firmada | calculadora verificada (3 casos de control) |
| v1.2 | ___ | ___ | ___ | ___ |

## La calibración de la honestidad (primera semana)

Si tu primera semana cierra con 100 % E0, sospecha de ti mismo: cualquier humano que aprende produce errores E2/E7 al menos. Un 40 % de errores bien etiquetados vale más que un 0 % sospechoso — lo primero es reparable, lo segundo es ciego. El journal no califica: mide.
