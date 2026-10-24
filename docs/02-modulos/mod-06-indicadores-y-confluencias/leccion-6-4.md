# Lección 6.4 · Momentum y osciladores — medir la desaceleración

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M6 · Indicadores y Confluencias](README.md) |
| ⬅️ Anterior | [Lección 6.3 · Volatilidad y canales](leccion-6-3.md) |
| ➡️ Siguiente | [Lección 6.5 · Volumen y perfil](leccion-6-5.md) |

---

## Por qué importa

Los osciladores son los indicadores más vendidos y los peor entendidos. Casi todo principiante destruye su primera cuenta con la misma frase: *"el RSI está en 70, está sobrecomprado, vendo"* — y descubre que en tendencia fuerte el RSI puede dormir semanas sobre 70 mientras el precio duplica la distancia hasta su objetivo. La lección que separa al profesional: **sobrecompra y sobreventa no son señales, son lecturas de velocidad** que solo significan algo en el régimen correcto. Y dentro de esta familia vive el uso más honesto que tiene la categoría: la **divergencia**, que mide la desaceleración de un impulso con un número — la única manera de ver "el motor pierde fuerza" antes de que el gráfico diga CHoCH. Este módulo te enseña a leer velocidad con respeto por el régimen.

## Concepto

**RSI (*relative strength index*).** Compara la media de ganancias con la media de pérdidas de los últimos N cierres (clásico: 14):

$$RSI = 100 - \frac{100}{1+RS}, \qquad RS = \frac{\overline{G}}{\overline{P}}$$

donde $\overline{G}$ es la media de cierres al alza y $\overline{P}$ la de cierres a la baja en N periodos. Ejemplo numérico completo: si en los últimos 14 cierres la media de ganancias es 0,0015 y la de pérdidas 0,0010, entonces $RS = 1{,}5$ y $RSI = 100 - 100/2{,}5 = 60$. RSI 60 = las subidas recientes van 1,5 veces más rápido que las bajadas. Es un termómetro de velocidad, no un jurado de dirección.

**Sobrecompra/sobreventa dependen del régimen** — la regla central de la lección:
- **En rango** (M3): RSI > 70 / < 30 tienen contenido estadístico — el precio oscila y la reversión a la media es el hábito. Aun así, en este programa el rango solo se opera con el arquetipo de rango (M7), nunca con "RSI extremo" solo.
- **En tendencia fuerte:** RSI 70 ES el régimen. El precio hace HH sostenidos *porque* la velocidad compradora persiste; "vender sobrecompra" es operar contra la definición misma de tendencia. El RSI puede quedar >70 (o <30) durante decenas de velas.

**Estocástico.** Mide dónde cerró el precio *dentro del rango* de N periodos:

$$\%K = \frac{C - L_{14}}{H_{14} - L_{14}} \times 100$$

%K = 80 significa "cerró en el 80 % superior del rango de las últimas 14 velas". Es más rápido (y más ruidoso) que el RSI. Mismo régimen, misma advertencia: en tendencia fuerte vive pegado a 80–100 y eso es fuerza, no señal de giro. El programa lo usa como ejemplo de redundancia: mide velocidad relativa como el RSI — tener ambos es tener dos anemómetros (6.1).

**MACD (*moving average convergence divergence*).** Momentum de dos velocidades:

$$MACD = EMA_{12} - EMA_{26}, \qquad Señal = EMA_9(MACD), \qquad Histograma = MACD - Señal$$

MACD positivo = la media rápida está por encima de la lenta (tendencia reciente alcista); el histograma mide si esa diferencia se acelera o se enfría. Su lectura honesta: **pendiente del histograma = aceleración/desaceleración del régimen**, no cruce como señal.

**La divergencia — el uso más honesto.** Divergencia regular alcista: el precio marca un **LL** pero el oscilador marca un low menos profundo. Traducción: el precio siguió cayendo, pero la velocidad de la caída ya no acompaña — el impulso vendedor pierde fuerza *medible*. La divergencia bajista es el espejo (precio HH, oscilador LH). Dos reglas del programa: (1) la divergencia es una medición de desaceleración, no una orden de giro — el giro lo confirma la estructura (CHoCH, 5.2); (2) operar divergencias *contra* el sesgo del marco superior es otra familia de trade (reversión): solo con arquetipo y presupuesto propios (M7).

## Analogía

El velocímetro y la cuesta. Conduces subiendo una cuesta larga: el velocímetro marca 110 sostenido (sobrecompra en tendencia — el motor aguanta). Empiezas a notar que para mantener 110 el motor exige más revoluciones y el coche ya no acelera (divergencia: el precio sigue subiendo, el impulso ya no). Nada se rompió todavía: la cuesta sigue subiendo. Pero la *relación* entre pedal y velocidad cambió, y un conductor atento levanta el pie ANTES de que la cuesta termine — y el conductor estadístico espera, además, la señal de la carretera (estructura) antes de dar la vuelta.

## Cómo se hace: los osciladores sobre el caso maestro

El instante del pullback a la zona 1,0820–1,0824 *(ilustrativo)*, EUR/USD H4, sobre el movimiento de la [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md):

1. **RSI(14) en el HH 1,0884:** ≈ 68 — cerca del umbral pero sin sobrecompra estricta; y en contexto Etapa 2 ni siquiera importaría: 70+ sería fuerza. El pullback a 1,0820 lo lleva a ≈ 47: el oscilador se **reseteó al neutro** sin que la estructura (HH/HL, sesgo) cambiara — la lectura clásica de "pullback saludable en continuación".
2. **Estocástico en el mismo instante:** $\%K = \frac{1{,}0820 - 1{,}0745}{1{,}0884 - 1{,}0745} \times 100 = \frac{75}{139} \times 100 \approx 54$ — punto medio del rango de 14 velas: ni extremo ni señal. Nota la redundancia con el RSI: misma familia, casi la misma historia.
3. **MACD:** MACD ≈ 0,0011 (positivo: régimen alcista intacto) con señal ≈ 0,0014 → histograma ≈ −0,0003: leve enfriamiento durante el pullback, sin cruce bajista. Lectura: la aceleración pausa, el régimen no gira.
4. **La pregunta de divergencia (obligatoria antes de operar):** ¿el HH 1,0884 vino con el RSI marcando un high menor que en el impulso anterior? En el caso maestro: **no hay divergencia** — el oscilador acompañó el HH. Información operativa directa: el impulso sigue sano, el pullback es continuación probable y la zona de la receta cobra calidad. Si HUBIERA habido divergencia bajista en el HH, la nota en el análisis habría sido: "impulso desacelerado: exigir confirmación extra al gatillo (3.4) y considerar el TP en el primer objetivo, no en el segundo".
5. **Lo que NO se hizo:** vender en RSI 68 ("sobrecompra"), comprar por estocástico 54 ("cruce al alza"), ni convertir el histograma negativo en corto contra el sesgo. El plan seguía siendo el del mapa del M5; los osciladores firmaron el partes de salud del impulso.

## Error común

**(1) Vender sobrecompra en tendencia.** El error fundacional: RSI 70 en Etapa 2 es el motor caliente del régimen; la media de duración de esas "señales" contra tendencia destruye más cuentas que ningún gap. El extremo del oscilador solo opina en rango — y en rango el programa exige arquetipo propio. **(2) Operar toda divergencia contra estructura.** Una divergencia bajista dentro de una tendencia alcista D1 es ruido de pullback hasta que la estructura diga CHoCH (5.2): primero el sesgo, después el medidor. **(3) Elegir el oscilador ganador del histórico.** Probar Estocástico 5/3/3, luego 14/3/3, luego RSI 7… hasta que "funciona" = data-mining (D6). El programa fija parámetros clásicos por convención: la ventaja está en la constancia auditable. **(4) Apilar RSI + Estocástico + MACD como "confirmación triple".** Misma familia, mismo dato: tres anemómetros (6.1). Máximo un oscilador en el dashboard (6.8).

## Conexión cuantitativa

La divergencia es auditable con etiquetas en tu journal: `div-si` / `div-no` en cada registro de pullback. Al llegar a M9 tendrás dos muestras: continuaciones CON divergencia previa vs SIN divergencia — tu propio dataset del efecto desaceleración. Hipótesis de trabajo del programa *(heurística, se auditará)*: la divergencia no sube el WR de la entrada (la entrada es la misma zona con el mismo gatillo); sube la *calidad del contexto* — y eso se nota en el R:B realizado: con impulso sano (sin divergencia), el primer objetivo se alcanza más a menudo y la gestión puede estirar al segundo; con divergencia, TP conservador. Números de trabajo: si "sin divergencia" realiza 1,8R de media y "con divergencia" 1,1R sobre el mismo SL, a igual WR de 45 % la esperanza diverge: $E_{sin} = 0{,}45 \times 1{,}8 - 0{,}55 \times 1 = 0{,}26R$ vs $E_{con} = 0{,}45 \times 1{,}1 - 0{,}55 \times 1 = -0{,}055R$ — el medidor no eligió la entrada: eligió el objetivo y la gestión.

---

## 🎯 Puntos clave

1. $RSI = 100 - 100/(1+RS)$ con $RS = \overline{G}/\overline{P}$: termómetro de velocidad, no jurado de dirección.
2. Sobrecompra/sobreventa solo tienen contenido en rango; en tendencia fuerte son el régimen mismo.
3. Estocástico = posición del cierre dentro del rango de N: mismo dato que el RSI (redundancia, no confirmación).
4. MACD: momentum de dos velocidades; el histograma mide aceleración/desaceleración del régimen.
5. Divergencia = desaceleración medible del impulso: el uso más honesto; el giro lo confirma la estructura.
6. "No hay divergencia" también es información: impulso sano → continuación probable y TP con margen.

## 🔄 Autoevaluación rápida

1. Calcula el RSI con $\overline{G} = 0{,}0018$ y $\overline{P} = 0{,}0012$. Interpreta el número en una frase.
2. En el caso maestro, ¿qué combinación exacta de lecturas dieron RSI, estocástico y MACD en el pullback, y qué decisión cada una respaldó?
3. Hay divergencia bajista clara en el H4 mientras tu sesgo D1 es alcista y el HH acaba de confirmarse. ¿Qué hace el programa y por qué no es "ignorar la señal"?

<details>
<summary>Ver respuestas</summary>

1. $RS = 0{,}0018/0{,}0012 = 1{,}5$; $RSI = 100 - 100/2{,}5 = 60$. Interpretación: las subidas recientes corren 1,5× más rápido que las bajadas — momentum alcista moderado, sin extremo.
2. RSI ≈ 68 en el HH → 47 en el pullback: reseteo al neutro sin romper régimen (pullback saludable). Estocástico ≈ 54: punto medio, sin extremo (y redundante con el RSI). MACD positivo (≈ 0,0011) con histograma levemente negativo (≈ −0,0003): aceleración pausada, régimen intacto. Decisión respaldada: mantener el plan de continuación de la receta — zona 1,0820–1,0824, gatillo de estructura, TP con margen.
3. El programa registra la divergencia y ajusta la GESTIÓN, no el lado: el sesgo D1 y la estructura mandan (primero jerarquía, 5.6). Concretamente: exigir gatillo de confirmación extra (3.4), acortar TP al primer objetivo y vigilar el CHoCH del marco de ejecución. No es ignorar: es operar la divergencia con el presupuesto correcto — la reversión contra sesgo es otra familia (M7), no un "short" improvisado dentro del plan de pullback.

</details>
