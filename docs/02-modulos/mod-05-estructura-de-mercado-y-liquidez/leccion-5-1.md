# Lección 5.1 · Tendencia y estructura — el esqueleto del precio

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 40–55 min de estudio |
| 🧱 Módulo | [M5 · Estructura de Mercado y Liquidez](README.md) |
| ⬅️ Anterior | — (inicio del Nivel 2; viene de la [Evaluación 🏆 N1](../../03-recursos/evaluaciones/examen-n1.md)) |
| ➡️ Siguiente | [Lección 5.2 · BOS y CHoCH](leccion-5-2.md) |

---

## Por qué importa

En el M3 aprendiste a ver *qué* hay en el gráfico (velas, ciclos, zonas); el N2 te enseña a leer *quién* mueve el mapa y *hacia dónde*. La **estructura de mercado** (*market structure*) es el esqueleto de esa lectura: la secuencia de máximos y mínimos que dice si el dinero grande está acumulando, distribuyendo o esperando. Operar sin leerla es subir a un río sin saber si fluye hacia ti o en contra: puedes nadar perfecto (mecánica del M4) y aun así avanzar al revés. Y hay una razón de negocio directa: tu esperanza $E = (P_w \times W) - (P_l \times L)$ no es la misma operando a favor de la secuencia estructural que en contra — la [Lección 3.6](../mod-03-anatomia-del-grafico/leccion-3-6.md) ya te mostró que el régimen es un multiplicador invisible; este módulo te da el instrumento para medirlo y etiquetarlo. Todo el N2 (indicadores, sistema, confluencias) se apoya en esta lección: es el vocabulario base.

## Concepto

**Definición — swing:** un **swing high** es un máximo local que supera a los highs de las velas vecinas; un **swing low**, su espejo. La unidad práctica del programa: la vela con el extremo más alto/bajo que sobrevive a *n* velas a cada lado (usamos *n* = 2 en M15/H1 y *n* = 3 en H4/D1 *(heurística)* — el valor exacto importa menos que la constancia: elige uno y no lo cambies entre análisis).

**La secuencia define la tendencia:**

| Secuencia de swings | Estructura | Nombre |
|---|---|---|
| Cada high supera el high previo **y** cada low respeta el low previo | HH + HL | Tendencia alcista |
| Cada low perfora el low previo **y** cada high cede antes del anterior | LH + LL | Tendencia bajista |
| Los swings se solapan sin definir secuencia | ni HH/HL ni LH/LL | Rango (equilibrio) |

*(HH = higher high, HL = higher low, LH = lower high, LL = lower low.)*

**La unidad de Dow: impulso + pullback.** La **pauta de Dow** (*Dow Theory*) describe una tendencia como la alternancia de una pierna de expansión (impulso) y un retroceso que respeta la estructura (pullback — término ya definido en M3). Una tendencia no avanza en línea recta: avanza en peldaños. La tendencia alcista está viva **mientras cada impulso siga rompiendo el high previo y cada pullback siga respetando el low previo**. El día que un peldaño falla, la estructura entra en alerta — eso es exactamente la Lección 5.2.

**Swing relevante vs ruido.** No todo zigzag es estructura. El criterio del programa, en orden: (1) **marco primero** — un swing se marca en el marco de decisión (H4/D1 para sesgo, esta lección); los swings del marco menor que no aparecen en el mayor son *ruido de mercado* (*noise*) por definición operativa; (2) **consecuencia** — un swing es relevante si su quiebre cambiaría la secuencia (es decir, si romperlo obligaría a reetiquetar la tendencia); si su ruptura no cambia nada del mapa, es decoración; (3) **origen de reacción** — los swings que lanzaron impulsos de verdad (con desplazamiento, [Lección 5.4](leccion-5-4.md)) pesan más que los que solo produjeron meandros.

## Analogía

La escalera de mano. Subes con seguridad mientras cada peldaño que pisas quede por debajo del siguiente (HL) y la mano alcance siempre un punto más alto (HH). La escalera no deja de ser escalera por un temblor de la mano (ruido): deja de serlo el día en que tu mano ya no supera el punto anterior (falla el HH) o tu pie no encuentra peldaño por encima del que ocupa (perfora el HL). Nadie te grita "la escalera se rompió" en el primer temblor — pero el buen escalador *sabe* qué temblor es normal y qué peldaño ausente es la alarma. Leer estructura es exactamente eso: saber qué swing es peldaño y qué swing es temblor.

## Cómo se hace: el caso maestro del módulo, marcado en 5 pasos

Este módulo entero analiza **un solo caso didáctico** (números cerrados, *(ilustrativo)* — no son precios actuales: verifica los tuyos en tu plataforma). En EUR/USD H4:

1. **Extremos mayores:** el mercado giró al alza desde el swing low estructural **1,0745** y dibujó un **HL en 1,0798**.
2. **Primer impulso:** desde 1,0798 el precio subió hasta **1,0860** (high) y retrocedió hasta 1,0812 sin tocar 1,0798 → secuencia: swing low 1,0745 → swing high 1,0860 → HL provisional.
3. **Segundo impulso:** el precio rompió 1,0860 y dibujó un nuevo high en **1,0884**, para luego corregir hacia la zona **1,0820–1,0824** — sin perder 1,0798.
4. **Etiquetado de la secuencia:** low 1,0745 → high 1,0860 → low ~1,0798 (respeta) → high 1,0884 (supera 1,0860) → **estructura alcista confirmada: HH + HL en marcha**.
5. **Declaración de sesgo:** "en H4, EUR/USD está en tendencia alcista mientras el precio respete 1,0798" — una frase, un nivel, cero ambigüedad. Esa frase es la **capa 1** del protocolo top-down ([Lección 5.6](leccion-5-6.md)).

Fíjate en lo que NO hicimos: no marcamos los 14 zigzags del marco M15, no discutimos si 1,0812 "cuenta" como swing (no cambia la secuencia: ruido), y no necesitamos ningún indicador. La estructura se lee con los ojos y se escribe con una frase.

## Error común

**(1) Coleccionar swings.** Marcar todo zigzag convierte el gráfico en un erial de líneas donde ninguna importa: si todo es estructura, nada lo es. Aplica el filtro de consecuencia: solo el swing cuya ruptura reetiquetaría la tendencia. **(2) Cambiar de marco a mitad del análisis.** Ver la estructura en H4 y "negarla" con un zoom a M5 es leer dos libros a la vez: cada marco tiene su secuencia, y la jerarquía se respeta ([Lección 5.6](leccion-5-6.md)) — el M5 es para el gatillo, no para el sesgo. **(3) Llamar "tendencia" a dos barras verdes.** La tendencia es una *secuencia*, no un color: dos impulsos verdes seguidos sin un HL respetado no son estructura, son una pierna solitaria. **(4) Anclar la tendencia al sentimiento.** "Se siente alcista" no es estructura; la secuencia se escribe en el gráfico o no existe.

## Conexión cuantitativa

La estructura es el primer filtro de calidad de tus operaciones futuras, y los filtros se pagan en WR. Razonamiento del programa *(heurística de trabajo, se auditará con tu journal en M9)*: un pullback comprado en estructura HH/HL compra en la pata estadísticamente más fiable del ciclo; la misma figura leída contra una secuencia LH/LL está comprando fuerza contracorriente — mismo riesgo nominal (1R), peor materia prima. El **sistema v1.0 del M7** exigirá que declares tu filtro de tendencia por escrito, y la misión de este módulo te obliga a etiquetar cada análisis con su secuencia: cuando llegues a M9, podrás comparar tu WR "con tendencia" vs "contra tendencia" con tus propios datos — la primera auditoría de régimen de tu negocio. Estructura no definida = análisis no auditable: si no escribió la secuencia, no sabrás jamás por qué falló el trade.

---

## 🎯 Puntos clave

1. Estructura de mercado = secuencia de swings: HH+HL alcista, LH+LL bajista, solape sin secuencia = rango.
2. Unidad de Dow: impulso + pullback; la tendencia vive mientras el impulso rompa el high previo y el pullback respete el low previo.
3. Swing relevante se define por: marco de decisión + consecuencia (su ruptura reetiqueta la tendencia) + origen de reacción.
4. El resto es ruido: no se marca, no se opera, no se discute.
5. El sesgo del marco superior se escribe en UNA frase con UN nivel de invalidación ("alcista mientras respete 1,0798").
6. La estructura es filtro de calidad: misma E nominal, distinta materia prima según el lado de la corriente.

## 🔄 Autoevaluación rápida

1. Un swing low en M15 no aparece en H4. ¿Qué es y por qué no se marca en tu análisis de sesgo?
2. ¿Cuál es el test de "consecuencia" para decidir si un swing se marca? Enuncia el caso en que un high alto NO se marca.
3. Escribe la frase de sesgo del caso maestro. ¿Qué precio la invalida y qué etiqueta recibiría ese quiebre en la próxima lección?

<details>
<summary>Ver respuestas</summary>

1. Es **ruido de mercado**: pertenece a la secuencia del marco menor, no a la del marco de decisión. Se marca en el marco que le corresponde (M15) si tu rol ahí lo exige (gatillo), pero jamás en el análisis de sesgo — mezclar marcos destruye la jerarquía del top-down (5.6).
2. Test de consecuencia: "¿su ruptura me obligaría a reetiquetar la tendencia?". Un high puede ser objetivamente alto y aun así no marcarse: si su ruptura no cambia la secuencia (sigue habiendo HH+HL con o sin él), es decoración. Ejemplo del caso: un máximo intermedio de 1,0872 dentro de la pierna hacia 1,0884 no se marca — su quiebre no reetiqueta nada.
3. "EUR/USD en H4 es tendencia alcista **mientras el precio respete 1,0798**". El precio que la invalida: un **cierre** H4 bajo 1,0798 (no una mecha). Ese quiebre, por ir EN CONTRA de la secuencia alcista, se etiqueta **CHoCH** (cambio de carácter) — el tema exacto de la [Lección 5.2](leccion-5-2.md).

</details>
