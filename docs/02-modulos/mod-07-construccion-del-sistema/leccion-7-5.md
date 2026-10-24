# Lección 7.5 · Métricas y rachas — la estadística que sostiene el negocio

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 50–65 min de estudio |
| 🧱 Módulo | [M7 · Construcción del Sistema](README.md) |
| ⬅️ Anterior | [Lección 7.4 · Esperanza aplicada](leccion-7-4.md) |
| ➡️ Siguiente | [Lección 7.6 · Criterios de robustez](leccion-7-6.md) |

---

## Por qué importa

Cuando termines la misión de este módulo tendrás 30 filas de datos — y la pregunta que te hará el cerebro será "¿entonces mi sistema sirve o no?". Esta lección te da las cuatro métricas con las que se responde esa pregunta profesionalmente (WR, R:B medio, Profit Factor, Max DD sobre la curva de capital) y — más importante — la estadística de rachas que **predice el dolor antes de que llegue**. Porque el punto de quiebre de casi todo trader nuevo no es técnico: es la primera racha larga de pérdidas, que llega sin aviso, se lee como "el sistema se rompió" y termina en abandono o venganza (M10). Si antes de la primera racha ya sabes que con tu WR era *esperable* una de 6 pérdidas seguidas — y lo tienes calculado, en una tabla, con tu propia firma — entonces la racha deja de ser una crisis y se convierte en una confirmación del modelo. Esta es la lección más anticuada contra el pánico que existe: la vacuna matemática administrada antes del contagio.

## Concepto

**Las cuatro métricas del reporte del sistema:**

**1. Win Rate (WR)** — ya lo conoces: $\frac{\text{ganadoras}}{N}$. Es la métrica más sobrevalorada (M1.4) y aquí la usas solo como fila de la matriz de 7.4, nunca sola.

**2. R:B medio** — el tamaño medio de tus ganadoras en unidades de R: $\overline{W} = \frac{\sum R_{\text{ganadas}}}{\text{ganadoras}}$. Junto al WR forma la pareja de parámetros de tu máquina.

**3. Profit Factor (PF)** — la razón entre dinero ganado y dinero perdido, en R:

$$PF = \frac{\sum \text{ganancias}}{\sum \text{pérdidas}} = \frac{WR \times \overline{W}}{(1 - WR) \times 1}$$

| PF | Lectura del programa |
|---|---|
| < 1,0 | E negativo: la máquina pierde — no hay nada que gestionar, hay que revisar |
| 1,0 – 1,3 | E positivo débil: viable pero en el filo — los costes y la ejecución se comen el margen |
| **1,5 (objetivo)** | **Franja del negocio sano:** por cada 1 $ perdido genera 1,5 $ de ganancia |
| 2,0 – 3,0 | Excelente — pero exígelo a muestras grandes antes de creerlo |
| > 3,0 en muestra corta | 🚨 Sospecha automática de sobreoptimización o muestra contaminada (7.6, M9) |

Con la firma del curso (40 %, 1:2): $PF = \frac{0{,}40 \times 2}{0{,}60 \times 1} = 1{,}33$ — positivo pero por debajo del objetivo 1,5. Con WR 43 % y $\overline{W} = 2{,}1R$: $PF = \frac{0{,}903}{0{,}57} ≈ 1{,}58$ — el mismo arquetipo, dos semanas más de filtro afinado, ya en la franja sana. El PF traduce la matriz de 7.4 a un solo número auditable.

**4. Max Drawdown (Max DD)** — la mayor caída pico-a-valle de tu curva de capital, medida en R cuando el riesgo es fijo. No es "cuánto perdí en total": es el tamaño del peor valle sufrido — la métrica que describe lo que tu psicología y tu cuenta tuvieron que soportar.

**La curva de capital** es la serie acumulada de R (suma de resultados en orden temporal). Su forma vale más que cualquier número suelto: una curva sana sube en zigzag (sube, valle, sube más alto); una curva enferma sube en parábola (sin valles = sospecha de ajuste) o hace escalera hacia abajo. Lo que miras: pendiente global (relacionada con E), profundidad de valles (Max DD) y velocidad de recuperación.

**La estadística de rachas.** Con WR $p$, la probabilidad de que las próximas $n$ operaciones sean todas pérdidas es:

$$P(n \text{ pérdidas seguidas}) = (1 - p)^n$$

| Racha | WR 40 % | WR 50 % | WR 60 % |
|---|---|---|---|
| 3 pérdidas | 21,6 % | 12,5 % | 6,4 % |
| 5 pérdidas | 7,8 % | 3,1 % | 1,0 % |
| 8 pérdidas | 1,7 % | 0,39 % | 0,07 % |
| 10 pérdidas | 0,6 % | 0,10 % | 0,01 % |

Y la regla de estimación que convierte esa tabla en expectativa operativa: la racha máxima esperable en $N$ operaciones es aproximadamente

$$\text{racha esperable} \approx \frac{\ln N}{\ln \frac{1}{1-p}}$$

| WR | En N = 30 (tu misión) | En N = 100 (backtests de M9) |
|---|---|---|
| 40 % | **6–7 pérdidas seguidas** | ~9 pérdidas seguidas |
| 50 % | ~5 pérdidas | ~6–7 pérdidas |
| 60 % | ~4 pérdidas | ~5 pérdidas |

Lee esa tabla dos veces, porque es la oración más importante de la lección: **con un WR de 40 % — la firma de tu arquetipo candidato — una racha de 6-7 pérdidas seguidas NO es una señal de sistema roto: es el comportamiento esperado de una máquina sana en 30 repeticiones.** Con riesgo 1 %, ese valle vale −6 % a −7 % de la cuenta: desagradable, sobrevivible, y ya presupuestado antes de que ocurra.

## Analogía

La tabla de rachas es como la vacuna: se administra ANTES del contagio, con el agente debilitado del mal para que el sistema inmunológico lo reconozca cuando llegue de verdad. El trader sin esta lección vive su primera racha de 6 pérdidas como un atentado contra su identidad — "el mercado cambió", "el sistema no funciona", "yo no sirvo" — y responde con las dos reacciones del pánico: abandono del sistema justo antes de que la varianza se revierta, o doblaje de riesgo para "recuperar rápido" (la venganza que M10 cataloga como tilt). El trader vacunado vive la misma racha consultando su tabla: "con WR 40 %, esto ocurre con frecuencia esperable; mi Max DD presupuestado era −7 %; voy por −5 %; el protocolo es: no cambiar nada, mantener tamaño, registrar". Misma tormenta, dos barcos: uno tiene cartas náuticas y el otro improvisa. La estadística no elimina el dolor de la racha — le quita el significado catastrófico, que es lo que realmente hunde barcos.

## Cómo se hace: el reporte de la misión, métrica a métrica

Al cerrar tus 30 repeticiones (misión del módulo), el reporte se calcula así sobre tu tabla:

1. **WR:** cuenta ganadoras / 30 (si hiciste 25 y 5 fueron "no hay setup", el denominador son las 25 ejecutadas — el veredicto de no-operación no entra en la estadística del arquetipo).
2. **R:B medio:** promedia las R de las ganadoras. Si tu TP es fijo a 2R, esto sale directo; si hay TP estructural (liquidez opuesta), mide lo que realmente dieron.
3. **PF:** suma ganadas ÷ suma perdidas (en R). Con el formato del journal es una resta y una división.
4. **Curva y Max DD:** acumula las R en orden y dibuja la línea; mide la caída más profunda pico-a-valle. En 30 operaciones con WR 40 %, espera valles de −4R a −7R: si no hay NINGUNO, revisa que el replay fuera realmente a ciegas.
5. **Racha más larga vs tabla:** compárala con la fila de tu WR en la tabla de rachas esperables. Dentro del rango → el sistema y tú pasáis la prueba conjunta; muy por encima (p. ej. racha de 12 con WR medido 40 %) → sospecha de sesgo de registro o de muestra no a ciegas, no de mala suerte.
6. **Veredicto por la matriz (7.4):** localiza tu celda (WR medido, R:B medido) y clasifica el sistema: avanza a M9 tal cual, se ajusta en un componente, o se archiva con su registro completo. Todo veredicto sale con números delante.

Un ejemplo completo *(ilustrativo)*: 25 ejecutadas, 11 ganadoras (WR 44 %), $\overline{W} = 2{,}0R$, PF = $22R/14R = 1{,}57$, racha máxima 5, Max DD −6R. Lectura: celda (44 %, 1:2) → $E ≈ +0{,}32R$; PF en la franja objetivo; racha dentro de lo esperable para N=30; DD dentro del presupuesto de −7 %. Veredicto: sistema v1.0 avanza a M9 sin cambios. Todo el reporte cabe en una página y cada número es defendible ante el agente auditor.

## Error común

**(1) Juzgar el sistema con N pequeño.** "Llevo 8 operaciones y voy mal" — con N=8 la varianza domina por completo: cualquier WR entre 25 % y 75 % es indistinguible del azar. Las decisiones de cambio se toman con las muestras del programa (30 para diagnósticos de avance, 100 para validación en M9), nunca con el estado de ánimo de la semana. **(2) Abandonar en la racha esperable.** La racha de 6-7 pérdidas con WR 40 % está en la tabla que ya leíste: abandonar el sistema AHORA es romper el experimento en el único momento que la estadística predijo — y garantizas no ver nunca la reversión de la varianza que pagaría tu paciencia. **(3) Cambiar el sistema DENTRO de la muestra.** Ajustar el stop "un poco" en la operación 14 de 30 rompe la homogeneidad: ya no tienes 30 datos de una máquina, tienes dos muestras de 13 y 17 de dos máquinas distintas — ninguna suficientemente grande. Si tocas, empiezas de cero (regla de la misión). **(4) Medir Max DD solo en dinero.** Con riesgo variable, el DD en % mezcla el rendimiento del sistema con tus cambios de tamaño; el DD en R aísla al sistema. Por eso el journal registra R, no euros. **(5) Ignorar el tiempo de recuperación.** Un Max DD de −6R tras el cual el sistema tarda 40 operaciones en volver a máximos es información operativa (frecuencia, E) que el valle solo no cuenta.

## Conexión cuantitativa

La estadística de rachas es la razón aritmética del riesgo del 1 % que el programa fijó antes de conocer tu WR. La cadena: tu racha esperable en la misión es 6-7 pérdidas (WR 40 %, N=30); con riesgo $r$ por operación, el valle vale $6{,}5 \times r$; para que ese valle —**esperable por diseño, no por mala suerte**— quede dentro de un drawdown sobrevivible (la asimetría del drawdown que M8 formaliza: −10 % necesita +11 % para recuperar, −25 % necesita +33 %, −50 % necesita +100 %), el programa elige $r = 1$ % → valle esperable −6,5 %, recuperable con +6,9 %. Con $r = 5$ %, la MISMA racha esperable valdría −32,5 %, que exige +48 % para volver — el punto donde las cuentas mueren de verdad. Nótese la estructura lógica: el 1 % no deriva de ser conservador, deriva de la tabla de rachas multiplicada por la asimetría de recuperación — dos fórmulas, ninguna emoción. Esta misma cadena se reutilizará en M8 (sizing formal), M11 (matriz de riesgo para evaluaciones de prop firms) y M12 (presupuesto de DD del plan de negocio): es la columna vertebral cuantitativa de todo el programa.

---

## 🎯 Puntos clave

1. Las 4 métricas del reporte: WR, R:B medio, PF y Max DD sobre la curva de capital — nunca una sola de ellas sola.
2. PF = $\frac{WR \times \overline{W}}{(1-WR)}$: objetivo del programa ≥ 1,5; > 3 en muestra corta es sospecha, no éxito.
3. $P(n \text{ pérdidas}) = (1-WR)^n$ y racha esperable en $N$ operaciones $\approx \frac{\ln N}{\ln \frac{1}{1-WR}}$: con WR 40 %, en 30 operaciones esperan 6-7 pérdidas seguidas.
4. La racha esperable no es fracaso: es el comportamiento normal de una máquina sana — la vacuna es leer la tabla antes de la tormenta.
5. Con riesgo 1 %, el valle esperable (−6,5 %) es sobrevivible por la asimetría del drawdown; con 5 %, la misma racha es terminal. El 1 % sale de dos fórmulas, no del miedo.
6. El reporte de la misión cabe en una página y termina siempre en un veredicto de la matriz: avanzar, ajustar UN componente, o archivar con registro.

## 🔄 Autoevaluación rápida

1. Calcula la probabilidad de 5 pérdidas seguidas con WR 45 %, y la racha esperable máxima en 100 operaciones con ese WR. ¿Qué valle en % de cuenta implica con riesgo 1 %?
2. Tu misión: 30 filas, 3 "no hay setup", 10 ganadoras que dieron 21R en total, 17 perdedoras. Calcula WR, R:B medio, PF y di si el sistema avanza.
3. ¿Por qué un PF de 3,4 en 12 operaciones es una mala noticia y no un motivo de celebración? Argumenta con 7.6 y con lo que M9 exigirá.

<details>
<summary>Ver respuestas</summary>

1. $P = 0{,}55^5 = 0{,}0503 ≈ 5{,}0$ %. Racha esperable en N=100: $\ln 100 / \ln(1/0{,}55) = 4{,}605/0{,}598 ≈ 7{,}7$ → **7-8 pérdidas seguidas** son esperables. Con riesgo 1 %: valle de −7 % a −8 %, recuperable con ≈ +8 % (asimetría leve a ese tamaño). Conclusión operativa: incluso un WR de 45 % — bueno — exige presupuestar un valle de −8 % en el primer año; quien planificó su vida financiera (M1.6) para tolerar −8 % está bien construido; quien no, ya sabe por qué el módulo de expectativas venía primero.
2. Ganadoras 10 de 27 ejecutadas → **WR ≈ 37 %**. R:B medio = 21/10 = **2,1**. PF = 21/17 = **1,24**. Matriz: celda (37 %, 2,1) → $E = 0{,}37 \times 2{,}1 - 0{,}63 = 0{,}777 - 0{,}63 ≈ +0{,}15R$ — positivo pero débil (PF 1,24 < 1,5). Veredicto del programa: avanza a M9 como candidato, PERO con nota de mejora en el filtro o el gatillo (el R:B de 2,1 es sano; el WR 37 % está en el borde del breakeven 32,4 % para ese R:B — poco colchón). Se documenta la celda y la mejora UNA variable para v1.1, después de los 100 backtests.
3. Porque es improbable por construcción: un sistema honesto con 12 operaciones no tiene evidencia para PF 3,4 — con N tan pequeño, la varianza del PF es enorme y los valores extremos casi siempre delatan (a) muestra contaminada (operaciones elegidas a favor), (b) reglas ajustadas al pasado (el ajuste por el que 7.6 prohíbe iterar mirando resultados) o (c) riesgo no acotado (ganadoras grandes con L no normalizado). M9 exigirá N ≥ 100 con protocolo a ciegas justamente para que el PF signifique algo: celebrar un 3,4 con N=12 es celebrar ruido con formato de estadística.

</details>
