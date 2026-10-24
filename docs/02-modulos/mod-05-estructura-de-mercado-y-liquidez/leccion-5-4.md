# Lección 5.4 · Imbalances y FVG — el hueco que el precio suele volver a visitar

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 40–55 min de estudio |
| 🧱 Módulo | [M5 · Estructura de Mercado y Liquidez](README.md) |
| ⬅️ Anterior | [Lección 5.3 · Liquidez operable](leccion-5-3.md) |
| ➡️ Siguiente | [Lección 5.5 · Order blocks y zonas institucionales](leccion-5-5.md) |

---

## Por qué importa

Las tres lecciones anteriores te dieron el mapa direccional (5.1), las etiquetas de actualización (5.2) y el where del dinero (5.3). Esta lección añade la pieza de **microeficiencia**: los huecos que un impulso violento deja atrás. Importa por tres razones de negocio: (1) los FVG son **objetivos** — cuando el precio deja un hueco sin llenar en la dirección de tu trade, tu TP puede anclarse ahí con lógica de mercado y no con deseo; (2) son **zonas de entrada** — un pullback que entra a un FVG solapado con tu zona (3.3) concentra confluencia; (3) son **firma de urgencia** — su mera existencia te dice que aquel impulso fue desplazamiento institucional y no meandro, lo que refina el test de "swing relevante" de 5.1. Y una razón de salud financiera: el FVG es uno de los conceptos que la industria vende como novedad exclusiva — aquí lo aprenderás como lo que es, un fenómeno de subasta desequilibrada que el PA clásico describía hace décadas como "gap de ejecución".

## Concepto

**Definición — imbalance** (*desequilibrio*, ya introducido en M2): estado en que un lado de la subasta es tan urgente que el precio avanza **dejando órdenes sin ejecutar**. El mercado, según la hipótesis de eficiencia operativa *(heurística — no hay ley física)*, tiende a volver más tarde a esos precios para "rebalancear": dar a la contraparte que faltó la oportunidad de negociar.

**Definición — FVG** (*Fair Value Gap*): la huella visual del imbalance en 3 velas consecutivas. En un **FVG alcista**: el **low de la vela 3** queda por encima del **high de la vela 1** — el hueco es esa franja vertical que ninguna de las tres velas negoció. En un **FVG bajista**: el high de la vela 3 queda por debajo del low de la vela 1. La vela central (la 2) es la explosión: su cuerpo atraviesa el hueco de un tirón.

**Los dos usos operativos:**

1. **FVG como imán (objetivo):** un FVG abierto en la dirección de la tendencia actúa como destino probable del precio *(heurística)*. En la práctica del programa: si tu TP estructural (pool de 5.3) está **más allá** de un FVG abierto a favor, el objetivo gana calidad; si tu TP está **antes** de un FVG abierto en contra, acórtalo — el hueco contrario puede consumir el recorrido de tu trade antes de tu nivel.
2. **FVG como zona (entrada):** el relleno parcial del hueco (mitigación) en la dirección de tu sesgo es una zona de vigilancia de primera clase — **siempre con confluencia**: FVG + borde de zona del gradiente [3.3](../mod-03-anatomia-del-grafico/leccion-3-3.md) + origen de desplazamiento (5.5) + confirmación [3.4](../mod-03-anatomia-del-grafico/leccion-3-4.md). Un FVG suelto en medio de la nada no es entrada: es una línea bonita.

**Definición — mitigación** (*mitigation/rebalance*): el acto de volver al hueco y negociar la franja pendiente. El FVG queda **mitigado** (consumido) cuando el precio lo recorre; la primera visita es la que interesa — un FVG ya llenado y desgastado pierde todo estatus.

**Honestidad de evidencia:** "el precio siempre llena los huecos" es **falso** — hay FVG que quedan sin mitigar durante semanas (el hueco se convierte en zona lejana de un mapa que ya no importa). Lo que la práctica y tu propio estudio (misión M-5) deben validar: *en impulsos con desplazamiento real, en marcos H1+, con tendencia vigente, la mitigación parcial ocurre con frecuencia estadísticamente útil* — y eso es lo que se usa, con SL puesto.

## Analogía

El peldaño roto de la escalera mecánica. Un impulso violento es la escalera que sube tan rápido que se salta un peldaño: los que venían detrás (las órdenes que querían negociar en esa franja de precios) se quedaron sin agarrarse — nadie pudo comprar ahí, la fila pasó de largo. El mercado detesta la fila frustrada: con frecuencia vuelve a bajar a ese peldaño (mitigación) para dejar subir a los que quedaron — y esa vuelta al peldaño es, exactamente, la segunda oportunidad que tú como operador esperas sentado con la zona marcada. Pero ojo con la honestidad: a veces la escalera ya subió un piso más y nadie vuelve (FVG sin mitigar). El peldaño roto es *probable*, no *obligatorio* — por eso tu SL vive siempre debajo.

## Cómo se hace: el FVG del caso maestro, medido y usado

Caso *(ilustrativo)*: el impulso que produjo el BOS sobre 1,0860 (5.2) — tres velas H1 de subida violenta desde ~1,0824 hasta 1,0884+.

1. **Identificar las 3 velas:** vela 1 (high = 1,0840) → vela 2 (cuerpo explosivo que cruza la franja) → vela 3 (low = 1,0852). High de la 1 (1,0840) < low de la 3 (1,0852) → **FVG alcista de 12 pips: franja 1,0840–1,0852**.
2. **Clasificarlo:** nace dentro de un desplazamiento que rompió estructura (BOS 5.2) → FVG **calificado** (no cualquier hueco: el del impulso con urgencia).
3. **Uso como entrada:** el pullback posterior cae hacia la zona maestra 1,0820–1,0824 y **atraviesa la franja 1,0840–1,0852 antes de llegar** → el FVG se mitiga parcialmente en la caída; tu vigilancia se concentra en la confluencia FVG-mitigándose + borde de zona + barrida de 5.3 → entrada 1,0820 con el protocolo 3.4.
4. **Uso como objetivo (lado contrario del mismo caso):** si en vez de comprar el pullback estuvieras en tu operación larga ya montada (entrada 1,0824 de la receta), el **FVG ya mitigado** dejó de ser obstáculo; tu TP sigue en el pool 1,0886 de la lección anterior — la franja que quedó **debajo** de tu entrada ya no amenaza tu recorrido.
5. **El chequeo anti-FVG antes de cualquier trade:** "¿hay un FVG abierto EN CONTRA entre mi entrada y mi TP?" — si la respuesta es sí, el hueco puede absorber el movimiento: acorta el TP o rechaza el trade. Es un ítem más del checklist, como el spread de [4.3](../mod-04-plataforma-y-primera-ejecucion/leccion-4-3.md).

## Error común

**(1) Ver FVG en todo.** La consolidación normal produce microhuecos en todos los marcos: el programa califica FVG solo dentro de **desplazamientos** (impulsos que rompen estructura, 5.2) en marcos H1 o superiores *(heurística de marco)*. **(2) Operar el FVG contra el mapa.** Un FVG alcista no es señal de compra: es una zona que se compra solo si el sesgo (5.1/5.2) lo respalda y la confirmación (3.4) dispara. **(3) Casar la teoría del llenado.** "Siempre se llena" → operar sin SL esperando la visita: la frase más cara de este módulo. La mitigación es probabilidad, y el SL (ley 4.6) es el precio de la hipótesis. **(4) Usar huecos ya mitigados.** Un FVG recorrido dos veces es una zona gastada: su función era dar la contraparte que faltaba — ya la dio. **(5) Marco equivocado.** El FVG de M5 para el gatillo, el de H4 para la zona: usarlo al revés (sesgo con huecos de M5) invierte la jerarquía de 5.6.

## Conexión cuantitativa

El FVG entra en tu contabilidad por dos puertas. **Puerta TP:** un objetivo anclado en el pool estructural con FVG abierto a favor en el camino tiene recorrido "libre de imanes contrarios" — históricamente eso se traduce en TP que se alcanzan antes de que el trade consuma tu paciencia *(heurística; tu journal de M-5 produce tus propios datos)*. **Puerta SL/WR:** entrar en confluencia (FVG + zona + barrida) significa entrar donde ya hubo absorción real de órdenes — el punto donde la multitud ya pagó el peor precio y el tuyo es mejor; cada confluencia añadida se refleja, en tu estadística futura, como WR por arquetipo separado (la disciplina de etiquetado de la misión). Y la conexión con la ecuación del programa es directa: $E = (P_w \times W) - (P_l \times L)$ — el FVG no cambia P_w por arte de magia; **organiza tu muestra** para que P_w y W se midan en condiciones homogéneas (con confluencia) y no mezcladas: contabilidad limpia, sistema auditable, decisiones de M7 sobre datos que significan algo.

---

## 🎯 Puntos clave

1. FVG = hueco de 3 velas (high de la 1 vs low de la 3 en alcista; espejo en bajista): franja donde nadie negoció.
2. Nace de un imbalance: el impulso fue más rápido que la subasta; la mitigación es la visita que reequilibra.
3. Dos usos: imán (objetivo — o amenaza si está EN CONTRA de tu recorrido) y zona (entrada, siempre con confluencia).
4. Solo califica el FVG dentro de desplazamientos que rompen estructura, en H1+ *(heurística)*.
5. "Siempre se llena" es falso: la mitigación es probabilidad con SL de ley, no certeza sin riesgo.
6. Chequeo pre-trade: ¿hay FVG abierto en contra entre entrada y TP? → acorta o rechaza.

## 🔄 Autoevaluación rápida

1. Define las 3 velas de un FVG bajista. ¿Qué franja es el hueco y qué la diferencia de un simple retroceso?
2. Tu TP está 10 pips antes de un FVG abierto en contra. ¿Qué decide el programa y por qué?
3. Un FVG se formó hace dos semanas en D1 y el precio nunca volvió. ¿Qué estatus tiene hoy y qué NO debes hacer con él?

<details>
<summary>Ver respuestas</summary>

1. FVG bajista: vela 1 con **low** = X; vela 3 con **high** < X; la vela 2 cruza con cuerpo. El hueco es la franja (high de la 3, low de la 1) que ninguna de las tres negoció. La diferencia con un retroceso: el retroceso se negocia (hay velas dentro de la franja); el FVG es el salto — la subasta pasó de largo sin ejecutar ahí.
2. El FVG contrario puede absorber el recorrido antes de llegar a tu TP (el precio suele mitigar el hueco primero): **acortas el TP** al borde previo del hueco (protegiendo R:B ≥ 1:2 — si al acortar el R:B cae por debajo, **rechazas el trade**: la geometría no se negocia).
3. Tiene estatus de **FVG abierto pero remoto**: su marco (D1) lo hace relevante para el mapa, pero dos semanas de desgaste y distancia lo dejan fuera de tu horizonte operativo. NO debes: casarte con su llenado (operar sin SL "porque volverá"), ni usarlo como entrada fresca — la mitigación útil es la primera visita cercana en el marco de ejecución, con sesgo y confirmación.

</details>
