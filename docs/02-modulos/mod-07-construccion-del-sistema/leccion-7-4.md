# Lección 7.4 · Esperanza aplicada — la matriz WR × R:B

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M7 · Construcción del Sistema](README.md) |
| ⬅️ Anterior | [Lección 7.3 · Arquetipos de setup](leccion-7-3.md) |
| ➡️ Siguiente | [Lección 7.5 · Métricas y rachas](leccion-7-5.md) |

---

## Por qué importa

En M1 aprendiste la fórmula de la esperanza; en este módulo ya tienes un arquetipo elegido. Ahora falta el paso que separa a los traders que razonan su negocio de los que coleccionan setups: **mirar la matriz completa de combinaciones** WR × R:B y entender que ninguna celda es magia — que toda ventaja es un intercambio entre frecuencia de acierto y tamaño del acierto, y que el mercado te deja elegir tu punto en esa curva pero no regalarte ambos extremos. Esta lección demuestra con números tres cosas que la industria enseña al revés: que 40 % de acierto es un negocio excelente con R:B 1:2, que perseguir WR alto te empuja hacia los sistemas más frágiles ante los costes, y que la única pregunta que tu misión de 30 repeticiones debe responder es en qué fila de la matriz vive TU arquetipo — no la que te gustaría que viviera.

## Concepto

Recuperamos la ecuación del M1 con $L = 1R$ normalizado (toda pérdida cuesta lo mismo porque tu riesgo es fijo):

$$E = (P_w \times R{:}B) - (P_l \times 1) = (WR \times R{:}B) - (1 - WR)$$

Y de ahí el **WR de equilibrio (breakeven)** — el WR que hace $E = 0$ para cada R:B:

$$WR_{\text{equilibrio}} = \frac{1}{1 + R{:}B}$$

| R:B objetivo | WR de equilibrio | Lectura |
|---|---|---|
| 1:1 | 50,0 % | Necesitas acertar la mitad para no perder nada |
| 1:2 | 33,3 % | Un tercio de aciertos paga la vida entera |
| 1:3 | 25,0 % | Uno de cada cuatro basta |
| 1:4 | 20,0 % | Uno de cada cinco — pero las rachas se alargan (7.5) |

**La matriz completa de esperanza** (en R por operación; L = 1R; **negrita = E positivo**):

| WR ↓ · R:B → | 1:1 | 1:2 | 1:3 | 1:4 |
|---|---|---|---|---|
| **20 %** | −0,60 | −0,40 | −0,20 | **0,00** ⚖️ |
| **25 %** | −0,50 | −0,25 | **0,00** ⚖️ | **+0,25** |
| **30 %** | −0,40 | −0,10 | **+0,20** | **+0,50** |
| **35 %** | −0,30 | **+0,05** | **+0,40** | **+0,75** |
| **40 %** | −0,20 | **+0,20** | **+0,60** | **+1,00** |
| **45 %** | −0,10 | **+0,35** | **+0,80** | **+1,25** |
| **50 %** | **0,00** ⚖️ | **+0,50** | **+1,00** | **+1,50** |
| **55 %** | **+0,10** | **+0,65** | **+1,20** | **+1,75** |
| **60 %** | **+0,20** | **+0,80** | **+1,40** | **+2,00** |
| **65 %** | **+0,30** | **+0,95** | **+1,60** | **+2,25** |
| **70 %** | **+0,40** | **+1,10** | **+1,80** | **+2,50** |

La diagonal de celdas ⚖️ es exactamente el breakeven de la tabla anterior — la matemática es consistente consigo misma. Tres lecturas de la matriz que la industria nunca enseña juntas:

1. **La columna 1:2 es la frontera del negocio honesto.** El programa exige R:B mínimo 1:2 porque su breakeven (33,3 %) deja un colchón: un sistema realista de WR 40-45 % opera con margen estructural, no en el filo. En cambio, la columna 1:1 exige vivir permanentemente por encima de 50 % — y cualquier deterioro pequeño del WR (costes, fatiga, régimen nuevo) te cruza al rojo.
2. **El WR alto no es gratis: se compra con R:B.** Bajar de fila a fila (subir WR) es posible en cualquier arquetipo — recortando objetivos, cerrando antes, dejando menos correr. Cada recorte que sube el WR baja el R:B y te desliza a la izquierda en la misma fila: del +0,50 en (50 %, 1:2) al 0,00 en (50 %, 1:1). La matriz no premia "acertar mucho": premia el producto $WR \times R:B$, y perseguir una de las dos variables destruyendo la otra es el error clásico.
3. **Las celdas de WR bajo con R:B alto existen — y tienen precio oculto.** (25 %, 1:4) es +0,25R... pero con WR 25 % tus rachas de pérdidas son brutalmente largas (7.5 lo cuantifica: en 100 operaciones, una racha de 12-14 pérdidas es esperable) y tu máxima adversaria es psicológica antes que estadística. La matriz da la esperanza; la lección 7.5 te da el precio emocional de cada fila.

**La demostración del curso: 40 % con 1:2 es negocio.** Con la celda (40 %, 1:2): $E = 0{,}40 \times 2 - 0{,}60 \times 1 = +0{,}20R$ por operación. En 100 operaciones con riesgo 1 %: **+20R = +20 % del capital** *(ilustrativo, sin componer)*. Ese número — uno de cada cinco por encima del capital al año con un sistema que FALLA el 60 % de las veces — es la mejor vacuna contra la obsesión del acierto: el negocio no vive de tener razón, vive de que el producto frecuencia×tamaño sea positivo con pérdidas acotadas.

## Analogía

El casino a la inversa. La ruleta europea paga 35 a 1 al pleno pero la probabilidad real es 1/37: la casa tiene $E = -0{,}027$ por ficha apostada — una ventaja microscópica. Y sin embargo esa ventaja de 2,7 centavos por euro construye los hoteles de Las Vegas, porque el casino no apuesta una vez: apuesta **millones de veces** y la ley de los grandes números convierte el 2,7 % en certeza. Tu matriz es exactamente eso del otro lado del mostrador: una ventaja de +0,2R por operación parece trivial — 20 centavos por euro arriesgado — pero es la misma clase de máquina. La diferencia entre tú y el casino no está en la magnitud de la ventaja sino en la disciplina de frecuencia: el casino nunca deja de girar su rueda con sus reglas; el trader minorista cambia de rueda cada semana. Tu +0,2R solo se convierte en +20 % si respetas las 100 repeticiones del mismo juego.

## Cómo se hace: leer tu propia fila después de la misión

La matriz tiene un uso operativo exacto en este módulo:

1. **Antes de la misión:** declara la fila que tu arquetipo *debería* ocupar. El híbrido 2+4 (7.3) apunta a WR 35-50 % con R:B ≥ 1:2 — es decir, entre las celdas +0,05R y +0,50R. Ese es tu rango de expectativa honesta, escrito antes de mirar datos.
2. **Durante la misión:** no recalculas nada — solo registras cada operación con su R (ganado o perdido). Las 30 filas del registro son la materia prima.
3. **Después de la misión:** calculas tu WR real y tu R:B medio real, y localizas la celda. Tres veredictos posibles: (a) tu celda es E+ y el sistema avanza a M9 tal como está; (b) tu celda es E− pero tu R:B real es sano (≥ 1:2) — el problema es el gatillo o el filtro, se revisa el componente 5; (c) tu R:B real es < 1,5 — el problema está en las salidas o en stops demasiado anchos, se revisan los componentes 6-7. En todos los casos el diagnóstico sale de la matriz, no del ánimo.
4. **Con los costes por delante:** resta el coste de ejecución en R. Con SL de 32 pips y coste total típico de 2-3 pips (spread + slippage, M4.3), el coste es ≈ 0,06-0,09R: la celda (40 %, 1:2) pasa de +0,20R bruto a ≈ +0,13R neto. Ahora mira la columna 1:1: la celda (55 %, 1:1) era +0,10R bruto — **el coste la mata**. Esta es la razón cuantitativa por la que el programa no diseña sistemas de R:B corto: son los únicos que la fricción puede convertir en pérdidas.

## Error común

**(1) Optimizar WR recortando ganadores.** Cerrar a +1R "para asegurar" con SL de 1R: te mueves a la columna 1:1, donde necesitas > 50 % neto de costes para sobrevivir — acabas de fabricar el sistema más frágil del catálogo convencido de que "aseguras más". **(2) El WR 95 % sin preguntar la L.** El clásico de las martingalas: gana 0,2R casi siempre, pierde 20R de vez en cuando. Cuenta: $E = 0{,}95 \times 0{,}2 - 0{,}05 \times 20 = 0{,}19 - 1{,}00 = -0{,}81R$ — una máquina de perder disfrazada de máquina de ganar. En la matriz, el WR alto con L > 1R rompe la normalización: pregunta SIEMPRE cuánto cuesta la pérdida. **(3) Confundir E por operación con E por mes.** +0,2R con 4 operaciones/mes es +0,8R/mes; la frecuencia es una variable del negocio (M12) pero solo cuenta DESPUÉS de que E > 0 — acelerar un sistema negativo solo acelera la ruina. **(4) Leer la matriz como menú.** Elegir la celda (60 %, 1:4) "porque es la más verde" sin preguntarse qué arquetipo podría sostener esa combinación: la matriz describe resultados, no los fabrica; primero el arquetipo y su régimen, después la celda que emerge. **(5) Ignorar los costes.** Comparar sistemas en bruto: con 0,1R de coste, la columna 1:1 pierde sus tres primeras celdas verdes — la fricción no es un detalle, es un filtro de diseño.

## Conexión cuantitativa

La matriz explica con aritmética por qué el programa ordena sus módulos como los ordena. El R:B ≥ 1:2 no es una preferencia estética: es la condición que hace viable un WR realista (33 % de breakeven contra 35-50 % esperable) **con margen para los tres asesinos silenciosos** — costes (−0,06 a −0,1R), deterioro de ejecución (tu WR en vivo será menor que en replay) y régimen cambiante (el WR no es constante en el tiempo). Ese colchón estructural es lo que la lección 7.5 convierte en supervivencia: con WR 40 % y R:B 1:2, las rachas de pérdidas son largas y frecuentes — y solo un E con margen (no un breakeven en el filo) paga emocionalmente esas rachas mientras la ley de los grandes números hace su trabajo. La matriz también prefigura el position sizing de M8: como E se expresa en R, todo el negocio escala linealmente con el riesgo por operación — y elegir ese riesgo (1 %) es la decisión que convierte una máquina de +0,2R en un sueldo o en una cuenta muerta, según sea 1 % o 20 %.

---

## 🎯 Puntos clave

1. $E = WR \times R{:}B - (1 - WR)$ y el breakeven $WR = \frac{1}{1+R{:}B}$: 1:1 → 50 %, 1:2 → 33,3 %, 1:3 → 25 %, 1:4 → 20 %.
2. La matriz premia el producto $WR \times R{:}B$, no cada variable: subir WR recortando R:B te desliza al filo del breakeven.
3. 40 % de acierto con 1:2 es +0,2R por operación → +20R por cada 100 operaciones al 1 %: el negocio que falla el 60 % de las veces.
4. Los costes (≈ 0,06-0,1R en FX mayor) matan primero a los sistemas de R:B corto — razón cuantitativa del mínimo 1:2 del programa.
5. WR alto sin preguntar por L es la trampa de la martingala: $0{,}95 \times 0{,}2R - 0{,}05 \times 20R = -0{,}81R$.
6. La misión sirve para localizar TU celda real: WR y R:B medidos, no deseados — y el diagnóstico de un E− sale de la matriz, no del ánimo.

## 🔄 Autoevaluación rápida

1. Un sistema anuncia "WR 55 %, R:B 1:1,5". Calcula su E, su distancia al breakeven de su columna, y qué le pasa si el coste es 0,1R.
2. Tu misión da WR 38 % con R:B medio 2,3. Localiza la celda aproximada, calcula E y el resultado esperado en 50 operaciones a 1 % de riesgo. ¿Qué componente revisarías para mejorar, sin tocar el arquetipo?
3. La receta: con TP de 66 pips y SL de 32 pips, ¿cuál era el breakeven WR exacto del trade? Si la misión posterior mide WR 40 % con ese R:B, ¿cuántas R esperas por cada 20 operaciones?

<details>
<summary>Ver respuestas</summary>

1. $E = 0{,}55 \times 1{,}5 - 0{,}45 = 0{,}825 - 0{,}45 = +0{,}375R$. Breakeven de la columna 1:1,5 = $1/2{,}5 = 40$ %: vive 15 puntos por encima del filo. Con coste 0,1R: $E_{neto} = +0{,}275R$ — sigue positivo (el margen de 15 puntos absorbe el golpe), pero fíjate que el coste se comió un 27 % de la esperanza bruta: en sistemas de R:B corto la fricción es el segundo competidor más fuerte, después de tu propia ejecución.
2. Celda ≈ (38 %, 1:2,3): $E = 0{,}38 \times 2{,}3 - 0{,}62 = 0{,}874 - 0{,}62 = +0{,}25R$ → en 50 operaciones a 1 %: **+12,5R ≈ +12,5 %** *(ilustrativo)*. Diagnóstico: el R:B es sano (≥ 2) y el WR está en la franja baja del rango del arquetipo (35-50 %) — el cuello de botella está en la frecuencia de acierto, es decir, en el gatillo (componente 5) o en el filtro de régimen (componente 3): se revisan esos dos, nunca las salidas (que están dando 2,3R de media — recortarlas empeoraría la celda).
3. Breakeven exacto: $1/(1 + 66/32) = 32/98 ≈ 32{,}7$ % — con R:B ≈ 2,06, bastaba acertar uno de cada tres para no perder. Con WR 40 %: $E = 0{,}40 \times 2{,}06 - 0{,}60 = 0{,}824 - 0{,}60 = +0{,}22R$ → en 20 operaciones: **+4,4R esperados** *(≈ +4,4 % al 1 % de riesgo — ilustrativo)*. La receta no era una apuesta: era una celda de la matriz ejecutada una vez.

</details>
