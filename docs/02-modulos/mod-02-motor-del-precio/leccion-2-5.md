# Lección 2.5 · Personalidad de cada mercado

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 40–50 min de estudio |
| 🧱 Módulo | [M2 · El Motor del Precio](README.md) |
| ⬅️ Anterior | [Lección 2.4 · Forex y sus sesiones](leccion-2-4.md) |
| ➡️ Siguiente | [Lección 2.6 · Calendario macro e intermercados](leccion-2-6.md) |

---

## Por qué importa

Un sistema no se opera "en el mercado" en abstracto: se opera en UN mercado concreto, con su horario, su volatilidad, sus costos y sus drivers. El EUR/USD de la madrugada y el NAS100 a la apertura de Nueva York son dos deportes distintos con la misma pelota. El principiante que cambia de instrumento cada día no está "diversificando": está estrenando un mercado nuevo sin conocer sus reglas locales, y pagando la matrícula de cada uno. Esta lección te da el perfil operativo de los tres mercados que el programa usa como coordenada principal (forex, oro, índices, según tu mapa del Módulo 1), con la lógica para auditar cualquier otro que te tiente más adelante. Y cierra con la regla de concentración del programa: **un mercado dominado vale más que seis medianamente conocidos** — en formación, la profundidad bate a la amplitud.

## Concepto

Cada mercado tiene una **microestructura** — el conjunto de reglas y comportamientos que lo distinguen — organizada en cinco dimensiones. Las dos primeras ya las tienes (Lecciones 2.1–2.4); aquí añadimos las tres restantes:

| Dimensión | Qué pregunta | Dónde se vio |
|---|---|---|
| Costo | ¿Cuánto spread/comisión pago por operar? | 2.1 |
| Energía | ¿Cuánto se mueve y en qué horas? (volatilidad, ADR) | 2.2, 2.4 |
| Liquidez | ¿Puede ejecutarse tamaño sin impacto? | 2.3 |
| **Estructura de horario** | ¿Abre/cierra? ¿Hay gaps? ¿24/7 o sesiones? | esta lección |
| **Drivers** | ¿Qué mueve el precio aquí? ¿Quién decide? | esta lección |

**Perfil de los tres mercados de la coordenada del programa** *(rangos ilustrativos — se verifican en vivo en el laboratorio)*:

**FX majors (EUR/USD como representante).** Horario: 24/5, sin gaps salvo fin de semana. Volatilidad: moderada; ADR (recorrido medio diario) típicamente 50–90 pips. Costo: el más bajo de todos. Drivers: diferencial de tasas entre las dos economías del par, flujos comerciales, riesgo sistémico. Personalidad: el buey de labranza — lento, fuerte, predecible en su cansancio; las tendencias grandes tardan semanas.

**Oro (XAU/USD).** Horario: 24/5 como forex, pero su energía se concentra en el horario de EE. UU. (datos, FOMC). Volatilidad: alta — ADR típicamente de decenas de dólares (un 1 %–1,5 % del precio por día *(ilustrativo)*). Costo: spread notablemente mayor que EUR/USD y tamaño de lote distinto (1 lote = 100 oz). Drivers: tasas reales de EE. UU. (relación inversa típica), DXY (inversa), aversión al riesgo (directa en pánicos). Personalidad: el gallo de pelea — reacciona a todo, amplifica lo que toca; premia mucho y castiga mucho más.

**Índices (US30/US100/US500 como CFD).** Horario: sesión de *cash* centrada en NY + sesiones extendidas; **gaps** de apertura frecuentes y de tamaño variable. Volatilidad: alta en apertura (primeros 30–60 min) y cierre; ADR de cientos de puntos según el período y el VIX *(ilustrativo)*. Costo: spread en puntos + valor del tick que **varía por bróker** (obligación: leer la especificación del contrato antes de calcular nada). Drivers: tasas, ganancias corporativas (*earnings*), apetito de riesgo, flujo pasivo indexado. Personalidad: caballo de carreras con salida en caja — arrastra fuerte desde el portalazo y odia el estancamiento.

**Cripto (por contraste, mercado de referencia):** 24/7 sin sesiones — sin "turno de oro" horario pero con fines de semana de liquidez fina y spreads engordados, donde los movimientos repentinos (*flash moves*) son más violentos. Drivers: ciclo propio, flujos de ETF, financiamiento de futuros perpetuos. El programa lo deja fuera de la coordenada de formación por costo relativo y régimen de volatilidad; el criterio de auditoría que aprendiste aquí sirve si algún día lo incorporas.

## Analogía

Piensa en climas, no en animales. EUR/USD es clima templado: puedes planificar la semana con sombrilla pequeña; rara vez hay tormenta, pero casi nunca hay cosecha rápida. El oro es clima de montaña: amanece helado y a mediodía asa — el que se viste como en el valle (SL de forex sobre precios de oro) termina tiritando. Los índices son clima tropical de tarde: mañanas de portalazo eléctrico y tardes donde todo se calma de golpe; el que sale a las 11:00 buscando la tormenta de las 09:30 llega tarde. La cripto es el monzón: llueve cuando quiere, incluidos domingos. El punto pedagógico: **tu sistema es tu vestimenta**. El mismo outfit (SL fijo, tamaño fijo, expectativas fijas) no funciona en los cuatro climas — y por eso el programa te pide dominar UNO antes de coleccionar los otros.

## Cómo se hace: comparar mercados con la misma vara, números cerrados

La comparación honesta se hace con **el mismo riesgo y el mismo tipo de idea** en cada mercado. Riesgo fijo: 1 % de 2 000 $ = 20 $ por operación (como siempre):

| Variable | EUR/USD | XAU/USD | US30 (CFD) |
|---|---|---|---|
| ADR típico *(ilustrativo)* | ~70 pips | ~30 $ | ~350 puntos |
| SL estructural típico | 25 pips | 4,00 $ | 80 puntos |
| Valor por unidad de movimiento | 10 $/pip por lote | 100 $/1 $ por lote (100 oz) | según bróker — p. ej. 1 $/punto por contrato *(ilustrativo)* |
| Lote para arriesgar 20 $ | $20/(25 \times 10) = 0{,}08$ | $20/4 = 5$ oz = 0,05 lotes | $20/80 = 0{,}25$ contratos *(según especificación)* |
| Spread típico *(ilustrativo)* | ~1–2 pips | ~0,20–0,40 $ | ~2–5 puntos |
| Costo como % del SL | ~6–8 % | ~5–10 % | ~3–6 % |
| Ventana de energía | Solapamiento Londres–NY | Horario de NY + datos | Apertura y cierre de NY |

Tres lecturas del cuadro:

1. **El riesgo es el mismo; el transporte cambia.** 20 $ de riesgo se implementan con tamaños completamente distintos — por eso el Paso 5 de la receta es una fórmula, no una cifra memorizada. Si mañana cambias de mercado, el riesgo no cambia: cambia el cálculo.
2. **El costo relativo se compara contra el SL, no contra el precio del activo.** Un spread de 0,30 $ en oro no es "barato" ni "caro" en abstracto: es ~7 % de un SL de 4 $ — comparable al 6-8 % de EUR/USD. La pregunta siempre es: *¿qué porcentaje de mi recorrido típico se lleva el peaje?*
3. **La ventana de energía dicta tu horario.** Tres mercados, tres ventanas distintas — y tu agenda (laboratorio de M1) solo puede estar en una a la vez con calidad. Otra razón para la concentración: **tu reloj ya elige tu mercado** aunque no lo sepas.

## Error común

El primero: **transplantar parámetros entre mercados** — SL de 25 pips "funcionará" en oro (allí 25 pips = 0,0025 $: el ruido del spread te saca), TP de índice "adaptado" a EUR/USD (objetivo imposible para el ADR del par). Cada mercado se recalcula desde cero: ADR observado, SL por estructura, lote por fórmula. El segundo: **coleccionar instrumentos en formación** — operar lunes EUR/USD, martes oro, miércoles NAS100 "para ver qué gusta". Cada cambio reinicia tu curva de aprendizaje de ese instrumento (sesiones, personalidad, niveles relevantes) y fragmenta tus N operaciones: 30 trades repartidos en 3 mercados no son estadística de NINGUNO (N ≥ 100 por sistema, Lección 1.4). El programa fija la regla: un mercado principal durante toda la formación; los otros existen para observar y para la ficha de variación de tu receta, no para alternar por aburrimiento.

## Conexión cuantitativa

El mercado elegido modifica los tres términos de tu ecuación. **$W$ y $L$:** el ADR determina cuánto recorrido estructural cabe en tu timeframe — un SL estructural de 25 pips en EUR/USD y otro de 80 puntos en US30 son proporcionalmente similares; un TP diseñado fuera del ADR típico es un deseo, no un objetivo. **$P_w$:** la personalidad del mercado interactúa con tu sistema — un sistema de ruptura gana $P_w$ donde hay expansión real (aperturas de NY) y la pierde en rangos finos de madrugada. **Costos:** ya visto — el spread relativo al SL es un impuesto por mercado. La suma cuantitativa: el "mejor mercado" no existe en abstracto; existe el mercado cuya **energía, costo y horario** encajan con tu sistema y tu vida — y eso se audita con el cuadro de esta lección, no con la impresión de un fin de semana. En la Lección 2.6 añadirás la última capa: los eventos macro que sacuden a los tres a la vez.

---

## 🎯 Puntos clave

1. Todo mercado se audita en 5 dimensiones: costo, energía, liquidez, estructura de horario y drivers.
2. FX majors: buey de labranza — 24/5, bajo costo, volatilidad moderada, driver = diferencial de tasas.
3. Oro: gallo de pelea — energía en horario de EE. UU., volatilidad alta, drivers = tasas reales (inversa), DXY (inversa), pánico (directa).
4. Índices: caballo con salida en caja — gaps, apertura violenta, valor del tick variable por bróker, drivers = tasas + earnings + apetito de riesgo.
5. El mismo riesgo (1 %) se implementa con tamaños totalmente distintos por mercado: la fórmula manda, no la cifra.
6. Un mercado principal en formación: los N ≥ 100 se necesitan POR sistema Y mercado; repartir trades fragmenta tu estadística.

## 🔄 Autoevaluación rápida

1. Tu colega usa su SL "estándar" de 25 pips en oro porque "le funcionó en EUR/USD". Calcula cuánto arriesga en realidad si 25 pips de oro = 0,0025 $ de movimiento y el spread es de 0,30 $.
2. Con riesgo 20 $, SL de 80 puntos en US30 y especificación de 1 $/punto por contrato: ¿qué tamaño operas? ¿Y qué debes verificar ANTES de confiar en ese 1 $/punto?
3. ¿Por qué el programa prohíbe alternar de mercado cada día durante la formación, si "diversificar es bueno"?

<details>
<summary>Ver respuestas</summary>

1. Los "25 pips" de oro son 25 × 0,01 $ = 0,25 $ por onza de recorrido... en el mejor caso: el spread solo (0,30 $) ya supera ese SL — el stop quedaría DENTRO del costo de entrada/salida normal. En la práctica: el stop se ejecuta con el primer respiro del spread (slippage incluido), y como el lote se calculó con un SL ficticio de 25 "pips de forex", el tamaño real queda multiplicado por 40 respecto al correcto (4 $ vs 0,10 $ de unidad). Resultado: riesgo real ≈ 40× el previsto o pérdida inmediata por spread. Moraleja: cada mercado recalcula SL por estructura ADR + lote por fórmula.
2. Tamaño = 20 $ / 80 puntos = 0,25 contratos. Antes de confiar: verificar en la **especificación del contrato** de tu bróker el valor real del tick/punto, el tamaño del contrato, el margen exigido y los horarios — el valor "1 $/punto" era ilustrativo y en CFD de índices varía entre brókeres; calcular con el valor equivocado multiplica tu riesgo por el factor de error.
3. Porque "diversificar" con 30 trades en 3 mercados no es estadística de ninguno (N ≥ 100 por sistema-mercado, Lección 1.4), y porque cada mercado exige su curva de aprendizaje local (sesiones, ADR, niveles). En formación, la profundidad en UN mercado produce la validación que la amplitud fragmentada nunca alcanza. La diversificación real de cartera llega en M8 — con correlaciones medidas, no con aburrimiento.

</details>
