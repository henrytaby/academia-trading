# Lección 6.6 · Fibonacci, Elliott y armónicos — contexto con límites

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M6 · Indicadores y Confluencias](README.md) |
| ⬅️ Anterior | [Lección 6.5 · Volumen y perfil](leccion-6-5.md) |
| ➡️ Siguiente | [Lección 6.7 · Etapas de Weinstein](leccion-6-7.md) |

---

## Por qué importa

Esta lección agrupa las tres herramientas más místicas del catálogo: los retrocesos de Fibonacci, el conteo de olas de Elliott y los patrones armónicos. Las tres comparten rasgo y destino: son *matemática real* envuelta en *mitología de mercado* — y la industria las vende casi siempre por la envoltura. El programa las trata con la misma honestidad del order block (5.5): separa lo aritméticamente verificable (los ratios son números; las particiones se calculan) de lo estadísticamente no demostrado ("el mercado respeta la ratio de la reproducción de conejos"). Al terminar sabrás usar los retrocesos como lo que valen — contexto de descuento — y sabrás POR QUÉ este programa no opera Elliott ni armónicos en el nivel v1: no porque sean "malos", sino porque sus exigencias estadísticas no caben en un negocio de 12 semanas.

## Concepto

**Retrocesos de Fibonacci.** La partición clásica de un swing: 23,6 % / 38,2 % / 50 % / 61,8 % / 78,6 %. La aritmética es real: los ratios salen de la sucesión de Fibonacci (cada término es la suma de los dos anteriores; el cociente entre términos consecutivos tiende a $\varphi \approx 1{,}618$), y de ella se derivan los retrocesos: $0{,}618^2 = 0{,}382$, $1/1{,}618 = 0{,}618$, etc. El nivel de entrada se calcula:

$$Nivel = Low_{swing} + r \times (High_{swing} - Low_{swing})$$

con $r$ el retroceso elegido (para largos tras impulso al alza). La **golden zone** es el tramo 50–61,8 %: el "descuento de calidad" donde las continuaciones sanas históricamente han girado *más a menudo que en otros tramos*. Ahora, la lectura honesta del programa: eso es una **tendencia estadística débil y dependiente de contexto** — no un nivel. El precio no para en 61,8 % "porque la abeja construya su panal en hexágonos": para ahí cuando ahí había estructura, y el Fib fue coincidencia decorada.

**El uso pragmático que este programa acepta:**
1. **Contexto de descuento:** en tendencia alcista con sesgo (5.1), el pullback que llega a la golden zone *sobre zona estructural* (M5) suma contexto — nunca lo sustituye.
2. **Referencia de proporción:** "¿este retroceso es normal o excesivo?" — un pullback de 30 % es una pausa; uno de 90 % es otra historia estructural (¿CHoCH?). El Fib mide la profundidad, la estructura la interpreta.
3. **Nunca como nivel exacto de entrada ni de SL:** la diferencia entre tu zona (con gatillo 3.4) y "el 61,8 % suelto" es la diferencia entre operar un plan y operar una cifra.

**Ondas de Elliott.** El modelo describe el mercado como 5 olas de impulso + 3 de corrección, fractales en todo marco. Sus problemas operativos son estructurales: (1) **subjetividad extrema** — dos analistas competentísimos publican conteos distintos del mismo gráfico el mismo día, y ambos "cuadran"; (2) **reconteo perpetuo** — cuando el precio contradice el conteo, se "recuenta" (hipótesis in falsable en la práctica); (3) **sin producto operable** — no da zona, ni gatillo, ni invalidación concreta sin caer en juicios de artista. El programa lo enseña como *lenguaje descriptivo* (útil para narrar ciclos, hermana el impulso/corrección con la pauta de Dow del 5.1) y prohíbe operarlo como sistema.

**Patrones armónicos (Gartley, Bat, Butterfly…).** Figuras que anidan ratios de Fibonacci (p. ej., punto D en el 0,886 de XA con B en 0,618 de XA…). Lo que nadie te cuenta al venderlas: cada patrón exige 4 puntos exactos anidados; la muestra histórica limpia de cada figura es pequeña; los costos y el slippage se comen la ventaja declarada; y la disciplina estadística para validarlas (cientos de ocurrencias registradas con la misma regla, en el mismo instrumento, con costos reales) excede con creces el alcance de un negocio de 12 semanas. Veredicto del programa: **fuera del alcance v1** — no "no funcionan", sino "no tienes presupuesto estadístico para saber si funcionan", y operar lo que no puedes auditar es fe, no negocio.

## Analogía

Los cortes de una receta. El pastelero sabe que la mousse se corta mejor si el chocolate entra en el rango 45–55 °C — un tramo de temperatura con historial. Eso es la golden zone: un tramo de descuento con historial, útil *dentro de la receta completa* (estructura, gatillo, SL). El mistificador te vende el termómetro como el pastel: "compra exactamente a 50,0 °C y el pastel se hace solo". El conteo de Elliott es el crítico gastronómico que explica tu negocio con 5 actos y 3 interludios: narrativa elegante, receta ninguna — y cuando la mesa sale mal, "reinterpreta el menú". Los armónicos son pastelería molecular de alta cocina: requiere laboratorio, muestras y años; en tu cocina de 12 semanas, intentarlos es invitar el desastre con estilo.

## Cómo se hace: los retrocesos sobre el caso maestro

El swing del caso [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) *(ilustrativo)*, EUR/USD H4 — low 1,0798 → high 1,0884 (86 pips):

1. **Calculas la partición** con $Nivel = Low + r \times (High - Low)$: 38,2 % → $1{,}0798 + 32{,}9$ pips ≈ 1,0831; 50 % → $1{,}0798 + 43$ = **1,0841**; 61,8 % → $1{,}0798 + 53{,}1$ ≈ **1,0831** (la golden zone completa: 1,0831–1,0841).
2. **Comparas con la zona estructural de la receta:** 1,0820–1,0824. El precio de entrada (1,0820) quedó en el $\frac{1{,}0884 - 1{,}0820}{1{,}0884 - 1{,}0798} = \frac{64}{86} \approx 74\,\%$ del retroceso (el tope de zona, 1,0824, en el 70 %) — **más profundo que la golden zone**.
3. **La enseñanza del desenlace:** el Fib clásico no habría dado la zona de la receta — habría señalado comprar 7–11 pips más arriba, donde la estructura no confirmaba y donde la barrida posterior a 1,0792 habría dejado un stop expuesto. La zona la marcó el order block + el pool (5.3, 5.5); el Fib la *aproximó* como contexto de descuento profundo ("el pullback está comprando caro — espera más profundidad"). Contexto: sí. Nivel: no.
4. **La barrida bajo el 100 %:** el precio perforó 1,0798 (el 100 % del retroceso) 6 pips antes de girar. Lección doble: ningún porcentaje del Fib protege de las barridas de liquidez (5.3 explica la visita al pool; el Fib no); y el SL por estructura (tras la extrema + respiración) ya lo contemplaba.
5. **Nota Elliott sobre el mismo gráfico:** el impulso 1,0798→1,0884 se narra cómodamente como 3 olas al alza en H1 — y esa narrativa no cambió ninguna decisión: ni zona, ni gatillo, ni SL. En el programa, la narrativa Elliott es como la banda sonora de la película: acompaña, no dirige.

## Error común

**(1) Dibujar el Fib desde el swing equivocado.** La partición depende del swing elegido; sin la disciplina del test de consecuencia (5.1) para marcar swings, cada analista dibuja un Fib distinto y el nivel "exacto" deja de existir. **(2) Tratar 61,8 % como ley física.** El mercado no conoce la sucesión; conoce órdenes. La coincidencia estadística en la golden zone es débil, dependiente de contexto, y solo sirve acompañada de estructura. **(3) Recountear Elliott hasta que cuadre.** Cada reconteo es un sesgo de confirmación con formato de análisis: si el conteo necesita revisión tras cada vela, no es un sistema, es un horóscopo con números. **(4) Vender armónicos sin muestra.** Quien te enseña "el Bat funciona el 80 %" casi nunca tiene 300 Bat registrados con costos reales; pedírselos no es descortés — es due diligence (M11).

## Conexión cuantitativa

La lección cuantitativa de fondo: los ratios de Fibonacci son una *hipótesis estadística*, y las hipótesis se validan con muestras, no con anécdotas. El protocolo de validación correcto (que practicarás en M9 con tus arquetipos): define la regla ANTES (p. ej., "pullback a 50–61,8 % sobre zona estructural H1"), fija el universo de casos, registra acierto/fallo con costos, y compara contra el mismo arquetipo sin el filtro Fib. Si tu muestra no distingue las dos poblaciones, el Fib no aportó nada y fuera del dashboard. El mismo estándar se aplica, en escala mayor, a Elliott y armónicos — y por eso su etiqueta definitiva en el radar (6.8): *contextual descriptivo* y *fuera de alcance v1*, respectivamente. La aritmética de los ratios ($0{,}618^2 = 0{,}382$; $1/1{,}618 = 0{,}618$) es verdadera y hermosa; que el mercado la respete es, hasta que TÚ lo demuestres con tu journal, una frase de marketing con números bonitos.

---

## 🎯 Puntos clave

1. Retrocesos = partición aritmética real de un swing ($Nivel = Low + r \times (High - Low)$); la golden zone 50–61,8 % es contexto de descuento con historial débil, no nivel.
2. El Fib aproxima; la estructura marca. La zona de la receta quedó en el 70–74 % — el Fib clásico no la habría dado.
3. Ningún porcentaje protege de las barridas: la perforación del 100 % (1,0792 vs 1,0798) la explica la liquidez (5.3), no el Fib.
4. Elliott: lenguaje descriptivo del ciclo, subjetivo e infalsable en la práctica — se narra, no se opera.
5. Armónicos: ratios anidados con exigencia estadística fuera del alcance v1 — fe auditable ninguna.
6. Todo porcentaje de este catálogo se somete al estándar del programa: regla antes, muestra después, comparación contra el arquetipo base.

## 🔄 Autoevaluación rápida

1. Calcula los retrocesos 38,2 %, 50 % y 61,8 % del swing 1,0745 → 1,0884 (el swing mayor del caso). ¿Dónde cae la golden zone?
2. Tu compañero compra "exactamente en el 61,8 %" con SL 3 pips por debajo. Dos errores del programa y qué alternativa propone.
3. ¿Por qué el programa clasifica Elliott como "lenguaje descriptivo" y los armónicos como "fuera de alcance v1"? ¿Qué distingue ambas etiquetas de "marketing" (6.8)?

<details>
<summary>Ver respuestas</summary>

1. Swing de 139 pips (1,0884 − 1,0745). 38,2 % → $1{,}0745 + 53{,}1$ ≈ 1,0798 (¡el propio HL! coincidencia estructural del caso); 50 % → $1{,}0745 + 69{,}5$ ≈ 1,0815; 61,8 % → $1{,}0745 + 85{,}9$ ≈ 1,0831. Golden zone del swing mayor: ≈ 1,0815–1,0831 — que CONTIENE la zona de la receta 1,0820–1,0824: en el swing mayor el Fib sí la enmarca (contexto), aunque en el swing menor la quedara corta. El Fib suma contexto; la zona sigue siendo de la estructura.
2. Error 1: nivel exacto como entrada — el 61,8 % suelto no tiene gatillo (3.4) ni confluencia estructural verificada. Error 2: SL de 3 pips — cualquier respiración (6.3: 0,15 ATR) lo ejecuta por ruido, y la barrida del pool (5.3) lo caza con prioridad estadística. Alternativa del programa: esperar la zona estructural con confluencia Fib como contexto, gatillo de confirmación en el marco de ejecución y SL tras la estructura con respiración (1,0–2,0 ATR).
3. Elliott se narra pero no se opera: sin producto operable (zona/gatillo/invalidación), nunca entra al plan — es decoración cultural, no herramienta. Armónicos podrían ser operables en principio, pero su validación exige muestras y disciplina que el negocio v1 no puede pagar: etiqueta "fuera de alcance" = "podría ser real, no puedes saberlo todavía". Ninguna de las dos es "marketing": el marketing es vender certeza (80 % de acierto) sin muestra auditable — el programa no dice que no funcionen; dice que TÚ no puedes sostener aún que funcionan.

</details>
