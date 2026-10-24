# Lección 9.1 · Epistemología del backtesting — cómo saber algo sobre el futuro sin mentirte

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M9 · Backtesting, Journal y Validación](README.md) |
| ⬅️ Anterior | [Lección 8.6 · Frenos de emergencia](../mod-08-gestion-del-riesgo/leccion-8-6.md) |
| ➡️ Siguiente | [Lección 9.2 · Protocolo de backtesting manual](leccion-9-2.md) |

---

## Por qué importa

El M7 aprobó tu sistema por **completitud y explicitud**, no por rentabilidad — fue una decisión deliberada: la rentabilidad no se declara, se mide. El M8 blindó el capital con presupuestos y frenos. Pero ninguna de las dos piezas produce todavía la evidencia de que tu sistema tiene esperanza positiva: esa solo la fabrica el backtest bien hecho. El backtest es la única forma ética y asequible de **comprar experiencia**: 100 operaciones de evidencia estadística que cuestan 15–25 horas de Bar Replay y cero dólares de inventario; las mismas 100 operaciones en vivo podrían costarte una racha de −9 % y meses de calendario. Pero un backtest mal hecho es **peor que ningún backtest**: produce convicción falsa, y la convicción falsa con presupuesto real es el mecanismo exacto por el que las cuentas llegan a cero — el trader no muere por no tener sistema, muere por tener fe en un sistema que nunca fue medido honestamente. Esta lección define qué puede saberse con un backtest (y qué no), cuántos datos hacen falta para decidir, y los tres sesgos que contaminan casi todos los backtests amateur. Si terminas con una sola idea incrustada, que sea esta: **un backtest no es una demostración de que ganarás — es una medición del pasado lo bastante honesta como para apostar el inventario con los ojos abiertos.**

## Concepto

**Qué es y qué NO es un backtest.** Un backtest es una **medición con protocolo del comportamiento de tu sistema sobre datos históricos**. No es una predicción: el pasado no garantiza el futuro (los regímenes cambian — 3.6), pero es la mejor evidencia disponible, y la estadística permite saltar del pasado al futuro con un margen de error declarado. La frase completa del programa: *"no sé que mi sistema ganará; sé que sobre 100 operaciones históricas midió WR 40 % ± 9,6 y decido en consecuencia"*. Esa humildad estadística no es una coletilla: es la diferencia entre operar un sistema medido y adorar un ídolo.

**La ecuación del error muestral.** El Win Rate que mides en N operaciones es una estimación con error. El error estándar de una proporción es:

$$\sigma_{WR} = \sqrt{\frac{WR(1-WR)}{N}} \qquad \text{IC 95\%} \approx \pm\, 1{,}96 \times \sigma_{WR}$$

Con WR 40 % — tu hipótesis del caso maestro — la tabla del mínimo honesto:

| N operaciones | Error estándar | IC 95 % del WR medido | Lectura |
|---|---|---|---|
| 10 | ±15,5 pp | **±30,4 pp** | Anécdota: un 40 % puede ser un 10 % o un 70 % |
| 30 *(misión M-7)* | ±8,9 pp | **±17,5 pp** | Reconocimiento: descarta desastres, no aprueba nada |
| 50 | ±6,9 pp | ±13,6 pp | Media muestra: aún cruza el equilibrio con facilidad |
| **100** *(lab de este módulo)* | ±4,9 pp | **±9,6 pp** | **Mínimo del programa para la primera decisión estructural** |
| 200 | ±3,5 pp | ±6,8 pp | Duplicar N divide el error por √2 ≈ 1,41 |
| 400 | ±2,4 pp | ±4,8 pp | Estándar de un sistema que se va a escalar |
| 1.000 | ±1,5 pp | ±3,0 pp | Territorio profesional (meses de trabajo, vale la pena después) |

Dos lecturas que la tabla fuerza. **Primera: el error cae con la raíz cuadrada** — para dividir el error por 2 necesitas CUATRO veces más datos; por eso "hagamos 10 más y ya" nunca lleva a ningún lado, y por eso el programa pide 100 y no 25. **Segunda: N=100 no compra certeza — compra la posibilidad de decidir.** Con WR medido 40 % ± 9,6, el peor caso razonable es 30,4 %: todavía por debajo del equilibrio neto (34,8 %, lo demostrará la 9.3). Por eso la decisión del backtest no es binaria ("¿gana o no gana?") sino de **tres vías**: verde (aprobar y pasar a forward), ámbar (operar provisional a 0,25–0,5 % y seguir midiendo), rojo (no operar; volver al laboratorio de M7). El intervalo de confianza no es un adorno del reporte: es la razón por la que la decisión tiene tres salidas y no dos.

**La ceguera como requisito, no como virtud.** Un backtest solo vale si el backtester no conoce el futuro de cada decisión. En la práctica manual eso significa: **Bar Replay estricto, vela a vela** — avanzas, pausas, decides SOLO con velas cerradas, registras, y solo entonces resuelves la operación avanzando más velas. Nunca "esta zona ya sé que aguantó". La ceguera es lo que hace que tu backtest mida el sistema y no tu conocimiento retrospectivo del gráfico; es la misma lógica del examen que estudiaste en M1 (las preguntas de `analisis_cursos.md` sobre backtests "sospechosamente perfectos": la mayoría tenía el futuro a la vista).

**Los 3 sesgos que contaminan el backtest amateur** — cada uno con su definición, cómo aparece en TU laboratorio de 100 operaciones y su antídoto:

| Sesgo | Qué es | Cómo aparece en TU backtest | Antídoto |
|---|---|---|---|
| **Supervivencia** | Quedarse solo con lo que funcionó y ocultar lo que no | Descartar del dataset las 6 operaciones "estúpidas" que hiciste por error, o borrar la sesión mala ("esa no cuenta porque estaba cansado") | **Todo entra, todo se etiqueta**: la fila incómoda con su E-tag vale más que la muestra bonita |
| **Data-mining** | Buscar la variante que mejor salió (o ajustar reglas a mitad de muestra) hasta que el backtest brilla | Probar 5 variantes del setup y reportar solo la mejor; cambiar el TP "porque con 2,5R salía más limpio" en la operación 62 | **Candados de 7.6 + D6**: hipótesis, métricas y N declarados ANTES, por escrito, con fecha; una sola hipótesis por muestra |
| **Look-ahead** | Decidir con información que no existía en la vela de decisión | Confirmar el "respeto del nivel" con el high/low de la vela EN formación; usar el volumen final de la vela; dibujar el nivel "perfecto" a ojo sabiendo dónde giró | **Regla de la vela cerrada**: toda condición se evalúa solo con velas cerradas; la captura se hace en el momento de la señal |

Los tres comparten un mecanismo: **inflan artificialmente la E medida**. Un backtest con look-ahead puede mostrar WR 55 % donde el honesto medía 40 %; uno con supervivencia, PF 2,0 donde el completo daba 1,4. La diferencia no se ve en el reporte — se ve en la cuenta real, meses después, cuando el "sistema que daba 55 %" rinde su verdadero 38 %. Por eso el programa trata estos sesgos como **errores de integridad** (como falsificar datos de laboratorio), no como "descuidos metodológicos".

## Analogía

El ensayo clínico doble ciego. Cuando la farmacología moderna decidió saber si un fármaco funciona, aprendió — a costa de desastres históricos — que la evidencia sin protocolo mata: los médicos que sabían quién tomaba el fármaco "veían" mejoras que no existían (sesgo del observador), los ensayos con 12 pacientes encontraban milagros que se desvanecían con 1.200 (tamaño muestral), y los estudios que se publicaban solo cuando salían bonitos construían una literatura de fantasmas (sesgo de supervivencia). La solución tomó décadas: N grande pre-registrado, doble ciego, y el compromiso de publicar el resultado ANTES de mirar los datos — exactamente tus candados de 7.6 y D6. Tu backtest es el ensayo clínico de tu sistema, con una dificultad añadida: **tú eres a la vez el laboratorio y el paciente** — el que mide y el que tiene intereses en el resultado. Por eso tu ceguera tiene que ser todavía más estricta que la del farmacólogo: el replay vela a vela es tu doble ciego, y el journal es tu pre-registro.

## Cómo se hace: blindar el backtest ANTES de la primera operación

1. **Declara el experimento por escrito (la declaración PRE).** Antes de la operación 1, un documento corto con fecha: hipótesis (WR esperado 40 %, R:B 2,1, E bruta +0,24R), N=100 (no se negocia), coste estimado por op (0,08R), mercados y timeframe del sistema, y las métricas del reporte con sus umbrales (la tabla de 9.3). Este documento es tu pre-registro: su función es que sea **imposible** confundir "lo que salió" con "lo que quería que saliera". Guárdalo junto al journal; la misión M-9 lo pedirá.
2. **Prepara el entorno de ceguera.** TradingView → Bar Replay → rango de fechas que NO conozcas (evita la historia que "ya estudiaste" en M3/M5: tu memoria de esos episodios contaminaría); velocidad lenta al avanzar; sin indicadores que no estén en tu sistema (cada medidor extra es una tentación de look-ahead).
3. **Aplica la regla de la vela cerrada como religión.** Toda condición de los componentes 1–8 se verifica solo con velas cerradas. Si tu sistema dice "pullback a la zona + vela de reacción": la vela de reacción se evalúa cuando CIERRA, con su close final visible — nunca "parece que va a cerrar bien". La captura se toma en ese instante: es la evidencia de que no hubo look-ahead.
4. **Comprométete con la integridad del dataset.** Toda operación entra — las buenas, las malas y las estúpidas (con su etiqueta de error, 9.5). Un backtest con 100 filas elegantes y 8 borradas mide tu ego, no tu sistema. La regla práctica: **nada se borra del CSV, nunca**; lo que se corrige se corrige con nota al pie, no con reemplazo.
5. **Lleva el diario del backtester.** Cada duda que surja midiendo ("¿esta barrida cuenta como válida?", "¿este pullback es demasiado profundo?") se anota con fecha en un apartado del journal — y NO se resuelve modificando reglas en vuelo. Al final de la muestra, esas dudas son materia prima: o son casos borde que tu definición de setup válido ya cubría, o alimentan (con evidencia) la ventana de modificación de 9.6. Lo que está prohibido es resolverlas a mitad de muestra: eso es data-mining con buena intención.

## Error común

**(1) "Con 30 me basta, la esperanza se ve clara."** A N=30 el IC es ±17,5 pp: tu 40 % puede ser un 22,5 % (por debajo del equilibrio neto) o un 57,5 % (sistema de oro) — la muestra NO distingue entre ambos. Las 30 del M-7 fueron para aprender el oficio y declarar métricas; su valor fue epistémico, no estadístico. **(2) Backtestear la historia que "ya conozco".** "Llevo meses mirando ese gráfico, no necesito replay" — sí lo necesitas: tu memoria retrospectiva ES look-ahead. El replay en fechas vírgenes no es burocracia: es la única forma de que la medición sea honesta. **(3) El rastreo de parámetros disfrazado de ajuste fino.** "Solo probé si el SL a 1,5×ATR salía mejor que a 1,4×" — eso es data-mining: cada variante que pruebes y descartes es una apuesta encubierta contra la muestra; con 10 variantes probadas, la "mejor" debe su corona al azar (7.6: la inflación ≈ √(k/N)). La única variante que se mide es la que declaraste antes. **(4) Confundir el intervalo con un detalle técnico.** "Mi WR medido es 40 %, punto" — no: tu WR medido es 40 % ± 9,6 y tu decisión debe sobrevivir al peor caso razonable (30,4 %). El trader que lee el número puntual y no el intervalo es el que "no entiende cómo perdió" cuando la varianza cobra. **(5) Creer que el backtest aprueba para dinero real.** La muestra histórica autoriza la decisión de backtest (verde/ámbar/rojo); el paso a real micro exige el forward (9.4) — y en este programa, además, esperar a la Fase 4 tras M12: el embudo completo se recorre en orden, sin atajos.

## Conexión cuantitativa

**Hacia 7.5 y 7.6:** la estadística de rachas te dijo QUÉ esperar (P(n)=(1−WR)ⁿ, rachas de 6-7 a 30 ops); el IC de esta lección te dice con QUÉ error lo esperarás — y juntos fijan la muestra: 100 operaciones es el punto donde "racha esperada ~9" y "±9,6 pp" hacen que la decisión de 3 vías sea posible. **Hacia 8.2:** el Max DD que la regla del 1 % estimó (−6 % esperable, −15 % emergencia) dejará de ser una estimación compuesta: tus 100 operaciones medirán el drawdown REAL de tu sistema al 1 % — la métrica que la misión M-9 compara contra la línea de emergencia. **Hacia 9.3:** esta lección definió la integridad de la muestra; la siguiente define cómo leerla — sin las 13 métricas y sus umbrales, 100 filas honestas son solo un CSV grande. **Hacia M10:** la ceguera del backtest tiene un límite estructural: al no haber dinero en juego, mide el sistema pero **no puede medir tu ejecución bajo presión** — por eso existe el forward (9.4) y por eso la Evaluación N3 exige ambas cosas. El backtest responde "¿funciona el sistema?"; la pregunta "¿puedo yo ejecutarlo?" todavía está abierta.

---

## 🎯 Puntos clave

1. Un backtest es una **medición con protocolo del pasado**, no una predicción: se decide con el intervalo, no con el número puntual.
2. El error del WR escala con 1/√N: N=30 → ±17,5 pp; **N=100 → ±9,6 pp** (mínimo del programa); duplicar la precisión exige cuadruplicar la muestra.
3. La decisión del backtest es de **tres vías** (verde al 1 % / ámbar a 0,25–0,5 % / rojo: no operar) — nunca binaria, porque el intervalo a N=100 todavía puede cruzar el equilibrio.
4. La ceguera es un requisito: replay vela a vela, fechas vírgenes, regla de la vela cerrada, captura en el momento de la señal.
5. Los 3 sesgos (supervivencia, data-mining, look-ahead) inflan la E medida y se combaten con los candados: **todo entra, todo se declara antes, nada se decide con el futuro visible.**

## 🔄 Autoevaluación rápida

1. Calcula el IC 95 % del WR para N=50 y N=200 con WR medido 40 % (fórmula + números). ¿Cuánto gana exactamente en precisión quien pasa de 100 a 200 operaciones?
2. Clasifica estas 4 prácticas como sesgo (supervivencia / data-mining / look-ahead / ninguna): (a) "borré las 3 operaciones del viernes porque estaba fatigado"; (b) "decidí la entrada cuando la vela aún no cerraba pero ya se veía fuerte"; (c) "probé 6 variantes del TP y reporté la que mejor salió"; (d) "registré el coste real de cada operación con el spread de la plataforma".
3. Tu backtest de 100 ops mide WR 37 %, R:B 2,1, coste 0,08R (equilibrio neto 34,8 %). Con el IC ±9,6: clasifica la decisión de 3 vías y justifica por qué NO es ni verde ni rojo.

<details>
<summary>Ver respuestas</summary>

1. N=50: $\sigma = \sqrt{0{,}4 \times 0{,}6/50} = \sqrt{0{,}0048} = 0{,}0693$ → IC **±13,6 pp** ([26,4 %, 53,6 %]). N=200: $\sigma = \sqrt{0{,}24/200} = \sqrt{0{,}0012} = 0{,}0346$ → IC **±6,8 pp** ([33,2 %, 46,8 %]). De 100 a 200: de ±9,6 a ±6,8 — la ganancia es un factor $1/\sqrt{2} ≈ 0{,}707$: **solo un 29 % de reducción del error por duplicar el esfuerzo**. Por eso la economía del backtest manda: primero 100 honestas (decisión posible), luego el forward (que añade información de otro TIPO), y solo si el sistema se escala, 200-400 (precisión).
2. (a) **Supervivencia** — las fatigadas también cuentan (mejor: se etiquetan, y si la fatiga es patrón, el horario de sesión se corrige en la ventana); (b) **Look-ahead** — "ya se veía fuerte" es información que no existía al cierre anterior; la vela se evalúa cerrada; (c) **Data-mining** — 6 variantes probadas y una reportada: la "mejor" debe su corona al azar (√(6/100) de inflación ≈ 24 %); (d) **Ninguno** — registrar el coste real es exactamente lo correcto (alimentará el coste medio de 9.3).
3. WR 37 % ± 9,6 → intervalo [27,4 %, 46,6 %]. El equilibrio neto (34,8 %) queda DENTRO del intervalo: el sistema puede ser ligeramente negativo o razonablemente bueno — la muestra no distingue. Veredicto: **ámbar** — operar provisional a 0,25–0,5 % (el daño máximo se acota mientras el dato madura), pasar a forward igual (mide ejecución), y seguir sumando muestra hacia 200. No es verde: 27,4 % < 34,8 % significa que el peor caso razonable es un sistema perdedor. No es rojo: el mejor caso (46,6 %) es un sistema sólido con E +0,48R. La decisión correcta frente a la incertidumbre es **acotar el daño y comprar más evidencia**, no adivinar.

</details>
