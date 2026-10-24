# Lección 8.2 · Asimetría del drawdown — por qué el gran daño es irreversible

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 40–55 min de estudio |
| 🧱 Módulo | [M8 · Gestión del Riesgo](README.md) |
| ⬅️ Anterior | [Lección 8.1 · Preservación de capital](leccion-8-1.md) |
| ➡️ Siguiente | [Lección 8.3 · La regla del 1 % y position sizing](leccion-8-3.md) |

---

## Por qué importa

La 8.1 nombró tu capital como inventario; esta lección demuestra con aritmética exacta la propiedad más peligrosa de ese inventario: **perder y recuperar no son operaciones simétricas**. Un drawdown del 50 % no se arregla con una ganancia del 50 % — se arregla con una del 100 %. Esta asimetría es la razón matemática que sostiene todo lo demás del módulo: la regla del 1 % (8.3), el veto al oversizing (8.4), los topes de cartera (8.5) y los frenos en cascada (8.6) existen porque la curva de daño no es una recta sino una curva exponencial que, pasado cierto punto, deja de tener retorno práctico. Si terminas esta lección con una sola idea incrustada, que sea esta: **el objetivo número uno del negocio no es ganar más — es nunca entrar en la zona donde la matemática te cobra intereses compuestos por cada dólar perdido.**

## Concepto

**La fórmula de recuperación.** Si tu cuenta cae un porcentaje $d$ (drawdown), para volver exactamente al saldo inicial necesitas subir un porcentaje $R$ del capital *restante*:

$$R = \frac{d}{1 - d}$$

La deducción es una línea: si empiezas con 1 (el 100 %) y pierdes $d$, te queda $1 - d$; para volver a 1 necesitas multiplicar el resto por $\frac{1}{1-d}$, es decir ganar $R = \frac{1}{1-d} - 1 = \frac{d}{1-d}$ sobre lo que te quedó. El denominador $(1-d)$ es el traidor: cuanto más profundo el drawdown, más pequeño el capital sobre el que tienes que generar la recuperación — y la ganancia requerida crece **más rápido que el daño**.

**La tabla completa de recuperación** *(el número de la derecha es % sobre el capital restante)*:

| Drawdown $d$ | Capital restante | Recuperación necesaria $R$ | Lectura honesta |
|---|---|---|---|
| −5 % | 95 % | +5,3 % | Cosquilleo: semanas normales |
| −10 % | 90 % | +11,1 % | Herida: un mes o dos de buen sistema |
| −15 % | 85 % | +17,6 % | Dolor real — revisión obligatoria (frenos, 8.6) |
| −20 % | 80 % | +25,0 % | Un cuarto más del capital: trimestre entero |
| −25 % | 75 % | +33,3 % | Territorio del pánico y las decisiones malas |
| −30 % | 70 % | +42,9 % | Zona de no retorno práctico para un negocio v1 |
| −40 % | 60 % | +66,7 % | Necesitas dos tercios más: medio año perfecto |
| −50 % | 50 % | +100,0 % | **Duplicar el capital restante**: años enteros |
| −60 % | 40 % | +150,0 % | Multiplicar por 2,5 el restante |
| −70 % | 30 % | +233,3 % | Multiplicar por 3,3: estadísticamente inalcanzable |

Dos lecturas que la tabla fuerza, y que ningún video de la industria enseña juntas:

1. **La curva se empina hacia el final.** Del −5 % al −20 % (el cuádruple de daño) la recuperación solo pasa de +5,3 % a +25 % (el quíntuple, todavía lineal-ish). Pero del −30 % al −50 %, la recuperación pasa de +42,9 % a +100 %: en la zona profunda, **cada punto adicional de drawdown cuesta más de dos puntos de ganancia futura**. La penalización es superlineal — esa es la palabra que debes memorizar.
2. **El −10 % es el último peldaño cómodo.** Con la racha esperable de tu sistema (6-7 pérdidas al 1 %, 7.5) el drawdown normal del negocio vive entre −6 % y −8 %. La tabla muestra que hasta −10 % la recuperación sigue siendo meses, no años. Todo lo que hay entre −15 % y −30 % ya no es "el negocio funcionando": es una emergencia de inventario que exige frenos (8.6) — y más allá de −30 % la matemática misma te expulsa del negocio.

**El tiempo es la segunda dimensión del daño.** La tabla anterior mide la ganancia necesaria; ahora póngela en unidades de tu negocio. Con $E = +0{,}2R$ por operación y riesgo 1 %, cada operación fabrica ~+0,2 % de capital *(ilustrativo, caso maestro, sin contar costes)*. A 4 operaciones/mes: ~0,8 %/mes de crecimiento esperado. ¿Cuánto tarda recuperar cada herida, ejecutando PERFECTAMENTE *(cálculo compuesto, ilustrativo)*?

| Drawdown | Recuperación necesaria | Operaciones a +0,2R | Tiempo a 4 ops/mes |
|---|---|---|---|
| −6 % (racha esperable) | +6,4 % | ~31 | ~8 meses |
| −10 % | +11,1 % | ~53 | ~13 meses |
| −20 % | +25,0 % | ~112 | ~2,3 años |
| −30 % | +42,9 % | ~181 | ~3,8 años |
| −50 % | +100,0 % | ~347 | **~7,2 años** |

*(ilustrativo: compuesto $1{,}002^n$, sin mejoras del sistema, sin aportes externos)*. Y esta columna es la **optimista**: supone que durante esos años no aparece otra racha, que los costes no erosionan la E (7.4), que no cambias de sistema a mitad, y que la psicología de operar una cuenta herida ejecuta igual que la de una cuenta sana — los tres supuestos que M10 demostrará falsos. El drawdown grande no solo pide matemática imposible: pide **tiempo de ejecución perfecta sostenida**, que es el recurso más escaso que existe.

**Por qué el gran daño es irreversible en la práctica.** Tres mecanismos que se suman al número puro: (1) la matemática superlineal de la tabla; (2) el tiempo — la vida sigue pasando mientras recuperas, y el coste de oportunidad de operar 3 años para volver a cero es el negocio entero que podrías haber construido; (3) la psicología — el trader que perdió el 50 % ya no ejecuta el sistema original: opera la recuperación, que es un sistema distinto (y peor) del que está escrito en su journal. Por eso los profesionales hablan del "punto de no retorno" en torno al −30 %: no es que la cuenta no pueda volver — es que el humano que la maneja ya no es el mismo.

## Analogía

La cuerda floja y la altura. Un malabarista que cae de un metro se levanta, se sacude y vuelve a subir: la caída le costó un momento. El mismo malabarista que cae de diez metros no "se recupera con un poco más de esfuerzo" — la altura convirtió un accidente en un final. La distancia no escala linealmente el daño: la escala **cualitativamente**. En el trading, la "altura" es el tamaño del riesgo por operación, y el suelo es la zona de no retorno (~−30 %). La 8.1 te dio el inventario; esta lección te da la altura máxima desde la que puedes caer sin morir; y la 8.3 convierte esa altura máxima en la regla concreta del 1 %. El aficionado elige altura por emoción; el profesional la calcula a partir del suelo.

## Cómo se hace: medir y acotar tu drawdown

1. **Calcula el drawdown esperado de TU sistema ANTES de operarlo.** Con WR 40 % y riesgo 1 %: racha esperable 6-7 → $0{,}99^6 = 0{,}9415$ → drawdown ≈ −5,9 % ≈ **−6 %** (la aproximación lineal de M7 — 6 × 1 % = 6 % — sobreestima apenas: está bien, para frenos el exceso es gratis). Recuperación: $0{,}06/0{,}94 ≈ +6{,}4$ % → ~31 operaciones → ~8 meses *(ilustrativo)*. Ese es el ciclo vital NORMAL de tu negocio: una herida de −6 % y un par de trimestres de curación. Escríbelo en tu plan: cuando llegue, no será novedad ni diagnóstico de sistema roto.
2. **Fija tu línea de emergencia.** Regla del programa: **−15 % desde el máximo de la curva de capital = revisión obligatoria con el agente auditor** (freno nivel 3-4, 8.6). La tabla justifica el número: por debajo de −15 % la recuperación (+17,6 %+) empieza a exigir trimestres, y la probabilidad de decisiones contaminadas se dispara.
3. **Usa la tabla en reversa para el sizing.** La pregunta correcta no es "¿cuánto quiero ganar?" sino "**¿qué drawdown estoy dispuesto a tener que recuperar?**". Si tu tope emocional y práctico es −15 %: con rachas de 6, el riesgo máximo es ~2 % (racha 6 → −11,4 % compuesto, dentro del tope); con rachas de 10 (WR 30 %), baja a ~1 %. La 8.3 formaliza este razonamiento en la fórmula del lote.

## Error común

**(1) Restar el drawdown "en mi cabeza" linealmente.** "Perdí 30 %, gano 30 % y listo" — no: 30 % de pérdida exige +42,9 %. El error de intuición es sistemático y está en la base de cada "voy a recuperarlo operando un poco más agresivo". **(2) Los dos errores simétricos de recuperación.** Perder el 50 % y "esperar a que el mercado me devuelva el 50 %": con riesgo 1 % y E +0,2R son ~7 años, no semanas. O peor, el clásico: **doblar el riesgo para acelerar la recuperación** — al 2 % la racha que te dejó en −50 % te lleva a $0{,}98^n$... una sola racha adicional de 6 a 2 % añade −11,4 %: la aceleración de la recuperación multiplica también la aceleración del daño, en la zona donde el daño ya es superlineal. **(3) Medir el drawdown desde el saldo inicial en vez de desde el máximo.** Tu cuenta subió a +12 % y ahora está en +2 %: eso ES un drawdown de −8,9 % ($0{,}02$ vs $0{,}12$: $\frac{0{,}12-0{,}02}{1{,}12} = 8{,}9$ %), no "sigue en verde, no pasa nada". El máximo de la curva es la referencia; el journal (M9) lo registra. **(4) Celebrar draws pequeños como si no costaran.** −6 % → +6,4 % → 31 operaciones perfectas ≈ 8 meses: hasta la herida NORMAL del negocio cuesta un ciclo vital completo. Esto no es para asustar: es para dimensionar qué compras cuando decides el % de riesgo — y por qué el 1 % es la recomendación del programa y no el 5 %.

## Conexión cuantitativa

La asimetría es el motor cuantitativo de todo el módulo. **Hacia 8.3:** la regla del 1 % no es una superstición — es la respuesta a "¿qué % hace que la PEOR racha esperable del sistema (7.5) produzca una herida de la tabla superior con recuperación de meses y no de años?". Con WR 40 % y rachas de 6-7: al 1 % → −6 % (recuperable); al 3 % → −17 % (emergencia); al 5 % → −27 % (zona de no retorno). La fórmula del lote de la 8.3 es esta tabla escrita al revés. **Hacia 7.5:** la estadística de rachas te da la FRECUENCIA del daño (P(racha) = (1−WR)ⁿ, esperable, no excepcional); esta lección te da el PRECIO de cada unidad de daño (d/(1−d), superlineal). El producto de ambas — frecuencia × precio — es lo que eliges cada vez que fijas el % de riesgo. **Hacia M9:** el drawdown máximo medido en tus 100 backtests será el dato real que reemplace las estimaciones de esta lección — y el criterio objetivo para el sizing de la fase forward. La curva de capital no es decoración del reporte: es el ECG del negocio, y esta tabla es la escala con la que se lee.

---

## 🎯 Puntos clave

1. $R = \frac{d}{1-d}$: la recuperación necesaria crece **más rápido que el daño** (superlineal).
2. La tabla: −10 % → +11,1 %; −25 % → +33,3 %; −50 % → +100 %; −70 % → +233,3 %.
3. El tiempo de recuperación (a E +0,2R, 1 %): racha normal de −6 % ≈ 8 meses perfectos; −30 % ≈ 3,8 años; −50 % ≈ 7,2 años *(ilustrativo)*.
4. La referencia del drawdown es el **máximo de la curva de capital**, no el saldo inicial.
5. Línea de emergencia del programa: −15 % desde el máximo = revisión obligatoria; el objetivo del sizing es que la peor racha esperable produzca heridas, nunca amputaciones.

## 🔄 Autoevaluación rápida

1. Calcula la recuperación necesaria para −12 %, −35 % y −55 % (fórmula + números). ¿Qué pasa con el incremento entre cada par?
2. Tu misión M-7 midió una racha máxima de 8 pérdidas con riesgo 1 %. Calcula el drawdown compuesto exacto, la recuperación necesaria y cuántas operaciones perfectas la curan.
3. Un trader con WR 30 % (rachas esperables de 10-12, 7.5) quiere arriesgar 3 % por operación "porque su R:B es 1:3 y le sobra margen". Usando esta lección, calcula el drawdown de su racha esperable y juzga el plan.

<details>
<summary>Ver respuestas</summary>

1. $R(12) = 0{,}12/0{,}88 = +13{,}6$ %. $R(35) = 0{,}35/0{,}65 = +53{,}8$ %. $R(55) = 0{,}55/0{,}45 = +122{,}2$ %. De 12 a 35 (el daño casi se triplica) la recuperación casi se CUADRUPLICA; de 35 a 55, pasa de +53,8 % a +122,2 % — cada punto extra de drawdown cuesta cada vez más puntos de ganancia: la superlinealidad en acción.
2. $0{,}99^8 = 0{,}9227$ → drawdown **−7,7 %** (la lineal daría −8 %: sobreestima, bien). Recuperación: $0{,}077/0{,}923 = +8{,}4$ %. Operaciones: $1{,}002^n = 1{,}084$ → $n = \ln 1{,}084/\ln 1{,}002 ≈ 0{,}0807/0{,}002 ≈ 40$ → **~40 operaciones perfectas ≈ 10 meses a 4 ops/mes** *(ilustrativo)*. Lectura: una racha peor que la esperable (8 vs 6-7) sigue siendo una herida administrable — exactamente el diseño que el 1 % compra.
3. Rachas de 10-12 esperables (7.5: $\ln 100/\ln(1/0{,}7) ≈ 9{,}7$). Al 3 %: $0{,}97^{10} = 0{,}7374$ → **−26,3 %**; con 12: $0{,}97^{12} = 0{,}6938$ → **−30,6 %**. Recuperación: +36-44 %. A 4 ops/mes y +0,2R... con WR 30 % y 1:3, $E = 0{,}3 \times 3 - 0{,}7 = +0{,}2R$ igual, pero la frecuencia de las rachas es mucho mayor → 3-4 años por cada ciclo de racha esperable. El margen "sobrante" del R:B no está en la curva de daño: la racha de su WR es la que fija el daño, no el R:B. Veredicto: su sizing está diseñado sobre el parámetro equivocado — el 1 % (o menos) es su tamaño correcto, no el 3 %.

</details>
