# Lección 1.4 · La esperanza matemática

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio (lleva calculadora o hoja de cálculo) |
| 🧱 Módulo | [M1 · El Trading como Negocio y Ciencia](README.md) |
| ⬅️ Anterior | [Lección 1.3 · El mapa completo: 3 dimensiones](leccion-1-3.md) |
| ➡️ Siguiente | [Lección 1.5 · La curva de aprendizaje real](leccion-1-5.md) |

---

## Por qué importa

Si este programa tuviera una sola lección, sería esta. La esperanza matemática es el criterio que separa el negocio del juego: un sistema se opera si y solo si su esperanza por operación, **calculada después de costos**, es positiva. La mayoría de los principiantes evalúa su trading por el *Win Rate* — cuántas operaciones acierta — y esa métrica, sola, no distingue un negocio rentable de una ruina elegante. Aquí aprenderás la ecuación que gobierna todo el programa, a calcularla con números cerrados, y por qué la estructura del mercado (fractal y ruidosa) cobra un impuesto especial a quien opera en marcos de tiempo muy bajos.

## Concepto

La esperanza matemática (*expected value*) de un sistema es el resultado medio **esperado por operación**, ponderando cada resultado por su probabilidad:

$$E = (P_w \times W) - (P_l \times L)$$

donde $P_w$ es la probabilidad de ganar, $W$ es la ganancia media por operación ganadora, $P_l = 1 - P_w$, y $L$ es la pérdida media por operación perdedora. Si $E > 0$ (después de costos), el sistema hace dinero en promedio y la varianza decide solo el camino; si $E < 0$, el sistema pierde en promedio y ninguna racha de suerte cambia el destino, solo lo aplaza. El **Win Rate** (*P_w* en porcentaje) y el ratio **riesgo-beneficio** (*Risk:Reward*, $W/L$) son las dos ruedas del mismo carro: nunca se interpreta una sin la otra.

Tres consecuencias inmediatas que conviene memorizar:

1. **El Win Rate engaña.** Un 90 % de aciertos puede ser un sistema perdedor; un 40 % puede ser una máquina de dinero. El número que importa es el producto, no el porcentaje.
2. **Existe un umbral de equilibrio para cada ratio.** Para un Risk:Reward de 1:2, el sistema empataría con apenas 33,3 % de aciertos; todo lo superior a eso es beneficio. Fórmula general: $WR_{equilibrio} = \frac{1}{1 + R}$, donde $R = W/L$.
3. **La esperanza se cobra a largo plazo.** $E$ es un promedio: una mala semana no lo invalida y una buena no lo confirma. Se necesitan muchas operaciones (el Módulo 9 fija N ≥ 100 como mínimo estadístico) para estimarlo con confianza.

## Analogía

Piensa en cómo gana un casino con la ruleta europea. En cada apuesta a un número, el jugador gana 35 veces lo apostado con probabilidad 1/37, y pierde lo apostado con probabilidad 36/37. La esperanza del jugador: $E = \frac{1}{37} \times 35 - \frac{36}{37} \times 1 = -\frac{1}{37} \approx -0{,}027$ — pierde 2,7 céntimos por cada euro apostado, siempre, en promedio. El casino no acierta más que el jugador en ninguna tirada individual: simplemente **es la casa** — la ventaja matemática está de su lado y deja que la ley de los grandes números haga el trabajo con miles de apuestas. El trader profesional es el jugador que consiguió sentarse del otro lado de la mesa: no acierta más que el aficionado en cada operación concreta; tiene una ventaja pequeña ($E > 0$), la repite muchas veces con tamaño controlado y deja que el promedio trabaje. Y la analogía tiene una segunda lectura, incómoda pero necesaria: las **opciones binarias** son la ruleta disfrazada de plataforma de trading — con pago típico del 85 % del apostado en un resultado esencialmente binario a 50/50, la esperanza es $E = 0{,}5 \times 0{,}85 - 0{,}5 \times 1 = -0{,}075$ por unidad: pierdes 7,5 centavos por cada dólar, siempre *(ilustrativo: supuesto de pago 85 % y probabilidad 50 %; el diseño garantiza esperanza negativa para el cliente en cualquier escenario realista)*.

## Cómo se hace: calcular la esperanza con números cerrados

**Sistema A** — "acierta poco, gana grande": $P_w = 40\%$, $W = 200$, $L = 100$:

$$E_A = 0{,}40 \times 200 - 0{,}60 \times 100 = 80 - 60 = +20 \text{ por operación}$$

**Sistema B** — "acierta casi siempre": $P_w = 90\%$, $W = 20$, $L = 190$:

$$E_B = 0{,}90 \times 20 - 0{,}10 \times 190 = 18 - 19 = -1 \text{ por operación}$$

El sistema B acierta 9 de cada 10 operaciones **y pierde dinero**. El sistema A falla más de la mitad de sus operaciones **y gana 20 por trade**. Si ambos operan 100 veces: A acumula +2 000; B acumula −100. La disciplina de B es irrelevante: su diseño tiene esperanza negativa.

**El mismo cálculo en unidades R.** Define $R$ = la cantidad que arriesgas en una operación (tu pérdida si toca el *Stop Loss*). Todo se simplifica: una ganancia de "2R" significa el doble de lo arriesgado. Sistema C: $P_w = 45\%$, ganancia media 1,8R, pérdida media 1R:

$$E_C = 0{,}45 \times 1{,}8 - 0{,}55 \times 1 = 0{,}81 - 0{,}55 = +0{,}26R \text{ por operación}$$

En 100 operaciones: +26R. Arriesgando el 1 % del capital por operación, el sistema C rinde ≈ +26 % en el período (aproximación lineal, antes de compuestos y drawdowns). Es el formato que usarás en TODO el programa: medir en R hace comparables sistemas de cualquier tamaño de cuenta.

**Tabla de consulta rápida** — esperanza en unidades R según Win Rate y Risk:Reward:

| Win Rate ↓ \ R:B → | 1:1 | 1:2 | 1:3 |
|---|---|---|---|
| **30 %** | −0,40R | −0,10R | **+0,20R** |
| **40 %** | −0,20R | **+0,20R** | +0,60R |
| **50 %** | 0,00R | +0,50R | +1,00R |
| **60 %** | +0,20R | +0,80R | +1,40R |

La diagonal de equilibrio: con 1:1 necesitas 50 % de aciertos; con 1:2, solo 33,3 %; con 1:3, solo 25 %. Por eso el programa exige Risk:Reward mínimo 1:2 en sus protocolos: te da margen estadístico para equivocarte con frecuencia y aun así ganar.

**Y el paso que casi todos olvidan — descontar los costos.** La esperanza real es después de spread y comisión. Si el sistema C paga en promedio 0,08R de costos por operación (ida y vuelta), su esperanza neta es $0{,}26 - 0{,}08 = +0{,}18R$ *(ilustrativo)*. Un sistema con +0,05R bruto en el mismo mercado queda en −0,03R neto: **rentable en el papel, perdedor en la cuenta**. Cuanto más pequeña la ganancia típica por operación, más devora el costo fijo — esto conecta directo con el problema del ruido que sigue.

### Fractalidad, ruido y el impuesto de los marcos de tiempo bajos

El mercado es **fractal autosimilar** (*fractal, self-similar*): las mismas formaciones cualitativas (impulsos, correcciones, rangos) aparecen en el gráfico de 1 minuto y en el mensual. Pero autosimilar **no significa idéntico**: al bajar de marco temporal, el movimiento medio de cada evento se encoge mientras que el spread se mantiene fijo, y el ruido (*noise* — fluctuación aleatoria sin información) gana peso relativo contra la señal. Ejemplo con números cerrados *(ilustrativo)*: con un spread de 1 pip, un setup típico de H1 que se mueve 40 pips paga un impuesto de $1/40 = 2{,}5\%$ de su recorrido; el mismo patrón visual en M1, moviéndose 8 pips, paga $1/8 = 12{,}5\%$ — cinco veces más. A ello se suma que más operaciones por día significan más decisiones, más riesgo de error de ejecución y más desgaste psicológico. Esta es la razón estructural por la que el programa forma en marcos H4/D1 y desaconseja el scalping hasta tener estadística propia sólida: el impuesto del ruido se paga en esperanza, y se paga siempre.

## Error común

El error clásico es **rendir culto al Win Rate**: mover el *Stop Loss* para "no perder" esta operación convierte pérdidas pequeñas y frecuentes en pérdidas catastróficas y raras — eleva el WR aparente mientras hunde $L$ hacia valores que aniquilan $E$ (es el ADN de la martingala, la gestión que dobla la apuesta tras cada pérdida: ganador casi siempre hasta el día que existe). El segundo error es juzgar sistemas con pocas operaciones: con 10 trades, la varianza domina — un sistema de $E = +0{,}3R$ puede mostrar rachas de 6 pérdidas seguidas sin haberse "estropeado" (la Lección 1.6 lo cuantifica). El antídoto operativo: toda evaluación de sistema se hace con N ≥ 100 operaciones registradas, sobre el journal, después de costos — no sobre la memoria de las últimas dos semanas.

## Conexión cuantitativa

Esta lección **es** la conexión cuantitativa: la ecuación del encabezado es el norte del programa entero. Cada decisión técnica que aprenderás después (dónde colocar el stop, cuándo cerrar, qué mercado operar) y cada decisión de gestión (qué tamaño por operación, cuántas posiciones simultáneas) no son más que formas de mover $P_w$, $W$, $L$ o la frecuencia $N$ — y solo tienen sentido en la medida en que mejoren $E_{negocio} = N \times E_{por\ operación}$ después de costos. Cuando en el Módulo 7 diseñes tu Sistema v1.0, no se te preguntará "¿te gusta el setup?": se te preguntará por su esperanza estimada y por la evidencia que la respalda.

---

## 🎯 Puntos clave

1. $E = (P_w \times W) - (P_l \times L)$: el resultado medio esperado por operación; único criterio de operatividad de un sistema.
2. El Win Rate aislado no dice nada: 90 % de aciertos puede perder dinero; 40 % puede enriquecer.
3. Umbral de equilibrio: $WR_{equilibrio} = \frac{1}{1+R}$ — con R:B 1:2 basta acertar 33,3 %; por eso el programa exige mínimo 1:2.
4. La esperanza válida es **después de costos**: spread y comisión son el alquiler del negocio y se pagan en cada operación.
5. El mercado es fractal autosimilar pero no idéntico: en marcos bajos el ruido y los costos relativos crecen — el scalping paga el impuesto más alto.
6. Se estima con N ≥ 100 operaciones: con menos datos, hablas con la varianza, no con el sistema.

## 🔄 Autoevaluación rápida

1. Sistema D: WR 55 %, ganancia media 80, pérdida media 100. Calcula $E$ e interpreta el resultado en una frase.
2. ¿Qué Win Rate mínimo necesita un sistema con R:B 1:3 para no perder dinero? Muéstralo con la fórmula.
3. Tu amigo presume: "nuevo bot, 30 operaciones seguidas ganadoras, cero pérdidas". Da dos explicaciones estadísticamente razonables que no requieren magia.

<details>
<summary>Ver respuestas</summary>

1. $E_D = 0{,}55 \times 80 - 0{,}45 \times 100 = 44 - 45 = -1$ por operación. Un sistema que acierta la mayoría de las veces y pierde dinero en promedio: la pérdida media supera la ganancia media — el caso clásico del WR alto mal diseñado (o de stops muy lejanos y objetivos muy cortos).
2. $WR_{equilibrio} = \frac{1}{1+3} = 25\%$. Aciertos por encima de 25 % con pérdidas de 1R y ganancias de 3R producen esperanza positiva.
3. (a) Objetivo cercano y stop lejísimos o inexistente: la probabilidad de cada acierto es altísima (p. ej. ≈ 95 % si el objetivo está a pocos pips y la pérdida latente a cientos), y con 95 % por operación, 30 aciertos seguidos tiene ≈ 21 % de probabilidad (cálculo propio) — perfectamente esperable antes del día catastrófico. (b) Varianza pura en muestra pequeña: con un WR real del 85 %, la probabilidad de 30 ganancias seguidas es $0{,}85^{30} \approx 0{,}8\%$ — raro, pero con miles de bots vendidos, a alguno le ocurre y ese es el que se fotografía; además 30 operaciones están muy por debajo del N mínimo para concluir algo. En ambos casos: pide las 200 operaciones siguientes con drawdown incluido.

</details>
