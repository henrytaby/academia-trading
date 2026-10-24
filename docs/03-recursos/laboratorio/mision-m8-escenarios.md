# Misión M-8 · Hoja de 20 escenarios de sizing

> **Instrucciones:** resuelve cada escenario **a mano** (división completa, no aproximación a ojo) en tu cuaderno, anota presupuesto, lote bruto, lote final (con redondeo a la baja) y riesgo real. Solo DESPUÉS verifica cada respuesta contra tu calculadora (hoja de cálculo o [`scripts/core/position_sizing.py`](../../../scripts/core/position_sizing.py)). Si difieren, detente y encuentra el error antes de continuar. Puntuación de aprobación: **≥ 18/20** — este módulo exige nota alta.
>
> **Convenciones fijas de la hoja:** cuenta denominada en USD · EUR/USD, GBP/USD y AUD/USD: 10 $/pip/lote · USD/JPY a 150,00: 6,67 $/pip/lote · USD/CHF a 0,8800: 11,36 $/pip/lote · XAU/USD: 1,00 $ de movimiento = 100 $ por lote · micro-lote mínimo: 0,01.
>
> **Etiqueta en journal:** `mision-m8-sizing` · **Tiempo estimado:** 1 semana (4-5 escenarios por sesión).

## Los 20 escenarios

| # | Escenario | Pregunta |
|---|---|---|
| 1 | Capital 1.920 $, riesgo 1 %, EUR/USD, SL 32 pips | ¿Lote final y riesgo real? *(el caso maestro: debe salir exacto)* |
| 2 | Capital 5.000 $, riesgo 1 %, EUR/USD, SL 50 pips | ¿Lote final y riesgo real? |
| 3 | Capital 2.000 $, riesgo 0,5 %, GBP/USD, SL 25 pips | ¿Lote final y riesgo real? |
| 4 | Capital 1.000 $, riesgo 1 %, EUR/USD, SL 40 pips | ¿Lote final? ¿Por qué el riesgo real NO es 1,0 % exacto? |
| 5 | Capital 10.000 $, riesgo 0,25 %, AUD/USD, SL 45 pips | ¿Lote final y riesgo real? |
| 6 | Capital 3.000 $, riesgo 1 %, USD/JPY (6,67 $/pip), SL 30 pips | ¿Lote final y riesgo real? |
| 7 | Capital 1.920 $, riesgo 1 %, USD/CHF (11,36 $/pip), SL 32 pips | ¿Lote final y riesgo real? |
| 8 | Capital 500 $, riesgo 1 %, EUR/USD, SL 25 pips | ¿Lote final y riesgo real? |
| 9 | Capital 800 $, riesgo 1 %, EUR/USD, SL 80 pips | ¿Lote final y riesgo real? |
| 10 | Capital 400 $, riesgo 1 %, EUR/USD, SL 80 pips | ¿Qué decide la calculadora y por qué NO se redondea a 0,01? |
| 11 | Capital 6.000 $, riesgo 0,5 %, GBP/USD, SL 60 pips | ¿Lote final y riesgo real? |
| 12 | Capital 2.500 $, riesgo **2 %** (plan del estudiante), EUR/USD, SL 40 pips | ¿Lote final? ¿Qué alerta del programa dispara este plan además del cálculo? |
| 13 | Capital 4.000 $, riesgo 1 %, XAU/USD, SL 4,00 $ de precio | ¿Lote final y riesgo real? |
| 14 | Capital 1.500 $, riesgo 1 %, XAU/USD, SL 3,00 $ de precio | ¿Lote final y riesgo real? |
| 15 | Capital 12.000 $, riesgo 0,25 %, EUR/USD, SL 35 pips | ¿Lote final y riesgo real? |
| 16 | Capital 1.920 $, riesgo 0,5 %, EUR/USD, SL 16 pips | ¿Lote final? ¿Qué relación guarda con el caso maestro del escenario 1? |
| 17 | Cartera: EUR/USD long abierta (1 %). Llega GBP/USD long (1 %) con ρ medido 0,85 | ¿Riesgo efectivo del motor dólar y veredicto? |
| 18 | Cartera: EUR/USD long (1 %) + GBP/USD long (1 %) ya abiertas. Llega AUD/USD long (1 %) | ¿Veredicto exacto con los topes del programa? |
| 19 | Tu cuenta cae −20 % desde su máximo | ¿Recuperación necesaria? ¿Cuántas operaciones perfectas (E +0,2R, 1 %, compuesto) y cuántos meses a 4 ops/mes? |
| 20 | WR 40 %, riesgo 1 %: la racha de 6 pérdidas de 7.5 quiere ocurrir TODA en un solo día | ¿Qué dice la cascada de frenos (8.6)? ¿Cómo se reparte y cuánto daña en total? |

## Procedimiento de corrección

1. Resuelve los 20 a mano (2 sesiones recomendadas: 1-10 y 11-20).
2. Verifica cada uno contra tu calculadora; marca ✓ o ✗ con el valor calculado por la máquina al lado.
3. Los escenarios 17-20 piden JUSTIFICACIÓN escrita (2-3 frases), no solo la respuesta: el veredicto sin argumento no puntúa.
4. Autoevalúa: cuéntalos y anota el resultado en `journal/mision-m8.md`. Si hay errores de valor del pip, revisa 8.4 antes de repetir cualquier escenario.

<details>
<summary>Clave de verificación (ábrela SOLO después de resolver)</summary>

| # | Presupuesto | Lote bruto | Lote final | Riesgo real | Nota |
|---|---|---|---|---|---|
| 1 | 19,20 $ | 0,06 | **0,06** | 19,20 $ = 1,00 % | Caso maestro, exacto ✓ |
| 2 | 50,00 $ | 0,10 | **0,10** | 50,00 $ = 1,00 % | Exacto |
| 3 | 10,00 $ | 0,04 | **0,04** | 10,00 $ = 0,50 % | Exacto |
| 4 | 10,00 $ | 0,025 | **0,02** | 8,00 $ = 0,80 % | Redondeo a la baja: por debajo del presupuesto, NUNCA por encima |
| 5 | 25,00 $ | 0,0555… | **0,05** | 22,50 $ = 0,225 % | El grano del micro-lote deja el sobrante fuera |
| 6 | 30,00 $ | 0,1499… | **0,14** | 28,01 $ = 0,93 % | Valor pip no estándar (8.4): 30 × 6,67 = 200,10 $ por lote |
| 7 | 19,20 $ | 0,0528 | **0,05** | 18,18 $ = 0,95 % | 32 × 11,36 = 363,52 $ por lote |
| 8 | 5,00 $ | 0,02 | **0,02** | 5,00 $ = 1,00 % | Exacto |
| 9 | 8,00 $ | 0,01 | **0,01** | 8,00 $ = 1,00 % | Exacto |
| 10 | 4,00 $ | 0,005 | **RECHAZADA** | — | No hay espacio de riesgo: 0,01 daría 8 $ = 2 % del capital (doble del presupuesto). El sizing tiene veto, igual que el setup |
| 11 | 30,00 $ | 0,05 | **0,05** | 30,00 $ = 0,50 % | Exacto |
| 12 | 50,00 $ | 0,125 | **0,12** | 48,00 $ = 1,92 % | **ALERTA:** 2 % excede el estándar del programa — la racha esperable (6, 7.5) da $0{,}98^6 ≈ -11{,}4$ %, ya en zona de emergencia (8.2: recuperación +12,9 %). El plan se corrige a 1 % o menos |
| 13 | 40,00 $ | 0,10 | **0,10** | 40,00 $ = 1,00 % | Oro: $4{,}00 \times 100 = 400$ $ por lote |
| 14 | 15,00 $ | 0,05 | **0,05** | 15,00 $ = 1,00 % | Oro: $3{,}00 \times 100 = 300$ $ por lote |
| 15 | 30,00 $ | 0,0857 | **0,08** | 28,00 $ = 0,233 % | El 0,25 % es el riesgo del primer año o de WR bajos |
| 16 | 9,60 $ | 0,06 | **0,06** | 9,60 $ = 0,50 % | MISMO lote que el escenario 1: la mitad de presupuesto y la mitad de SL producen el mismo tamaño — el lote se adapta, el riesgo se respeta |
| 17 | — | — | **ACEPTAR** | Motor dólar: $1 + 0{,}85 \times 1 ≈ 1{,}85$ % | ρ ≥ 0,7 → suma completa: 2 % con la banda conservadora → tope por motor (2 %) alcanzado JUSTO, sin margen para un tercero |
| 18 | — | — | **RECHAZAR** | El motor ya está en 2 % | $2 + 1 = 3$ % > tope 2 %: "no hay espacio de riesgo" (8.5). El tope global (3 %) tampoco dejaría pasar una cuarta en otro motor sin espacio |
| 19 | — | — | **+25 %** | $0{,}20/0{,}80$ | Compuesto: $1{,}002^n = 1{,}25 → n ≈ 112$ operaciones ≈ **2,3 años** a 4 ops/mes *(ilustrativo)*. Ese es el precio de un drawdown "de solo 20 %": la tabla 8.2 en acción |
| 20 | — | — | **La cascada lo impide** | Máximo −2 % en el día | El freno 1 (Daily Max Loss −2 %) cierra el día tras la 2ª pérdida. La racha se reparte en ≥ 3 días, cada uno con su pausa obligatoria (freno 2). Daño total de la racha completa: $0{,}99^6 ≈ -5{,}9$ % — pero nunca concentrado: la fricción temporal es el antídoto del tilt |

**Puntuación:** 16 escenarios numéricos (1-16) + 4 de decisión (17-20, con justificación). **≥ 18/20 aprobado.** Los errores más comunes esperados: usar 10 $/pip en JPY y CHF (escenarios 6-7), redondear hacia arriba (4, 5, 15) y olvidar la alerta del 2 % (12).

</details>
