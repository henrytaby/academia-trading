# Lección 8.1 · Preservación de capital — el dinero como inventario

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 30–40 min de estudio |
| 🧱 Módulo | [M8 · Gestión del Riesgo](README.md) |
| ⬅️ Anterior | [🏆 Evaluación Nivel 2 · examen-n2](../../03-recursos/evaluaciones/examen-n2.md) |
| ➡️ Siguiente | [Lección 8.2 · Asimetría del drawdown](leccion-8-2.md) |

---

## Por qué importa

Pasaste el N2 con un Sistema v1.0 escrito y medible. Antes de meterle más técnica, el N3 empieza por la única pregunta que decide si tu negocio existe el año que viene: **¿cómo se protege el capital?** Esta lección instala el cambio de marco que separa al profesional del aficionado: el dinero de la cuenta no es "puntaje" ni "saldo" — es el **inventario del negocio**. Una panadería que quema su harina no tiene problema de marketing: tiene un negocio muerto. Cada dólar de tu cuenta es la materia prima con la que tu sistema fabrica ingresos, y el módulo entero se construye sobre una convicción defensiva: primero decidir cuánto se puede perder, después cuánto se puede ganar — exactamente en el orden contrario al que el aficionado ejecuta por impulso. El SYLLABUS llama a M8 "el módulo que paga las cuentas" porque ninguna mejora de esperanza (7.4) sobrevive a una cuenta vacía.

## Concepto

**El capital como inventario.** Todo negocio tiene un activo que consume para producir: la panadería consume harina, la flota consume combustible, tu trading consume capital arriesgado. Tres consecuencias inmediatas de esta lectura, todas operativas:

1. **El inventario es finito y no se repone con promesas.** Tu caso maestro tiene 1.920 $. Ese número no es una abstracción: es la cantidad total de materia prima disponible. Cada operación consume una porción de ella (el riesgo) para intentar fabricar más. La pregunta profesional no es "¿cuánto puedo ganar con esto?" sino "**¿cuánta harina estoy quemando si sale mal?**" — y la respuesta, con la regla del 1 % (8.3), es 19,20 $ por operación.
2. **El inventario define la capacidad de producción.** Un negocio con poca harina produce poco pan. Una cuenta de 1.920 $ con riesgo 1 % puede fabricar 19,20 $ de presupuesto por operación (7.4: $E = +0{,}2R$ → +3,84 $ esperados por operación del caso). Reducir el inventario a la mitad reduce la producción a la mitad — por eso las dos primeras prioridades de todo negocio son (a) no perder inventario y (b) recuperar el que se perdió, en ese orden.
3. **El inventario tiene coste de reposición asimétrico** — el tema completo de la 8.2. Anticipo: recuperar inventario quemado cuesta más que el quemado mismo. Esa asimetría es la razón matemática por la que el profesional es defensivo por diseño y no por timidez.

**El enfoque defensivo del profesional.** La industria vende el trading como actividad de ataque: entradas valientes, capturas de movimientos, "potencial de +50 pips". El operador que sobrevive trabaja al revés, y su checklist mental por operación lo demuestra:

| Pregunta | Aficionado (ataque) | Profesional (defensa) |
|---|---|---|
| Primera | ¿Cuánto puedo ganar? | ¿Cuánto puedo perder? |
| Segunda | ¿Dónde entra? | ¿Dónde está muerta la idea? (SL) |
| Tercera | ¿Qué tamaño puedo usar? | ¿Qué tamaño **permite** el presupuesto de riesgo? |
| Cuarta | ¿Y si acierto? | ¿Y si fallan 6 seguidas (rachas, 7.5)? |

Nada de esto es pacifismo: el profesional arriesga dinero igual que el aficionado — la diferencia es el **orden de las preguntas** y la fuente del tamaño. El aficionado dimensiona por ambición ("si meto más, gano más"); el profesional dimensiona por presupuesto (8.3: el tamaño es una salida de la fórmula, no una entrada). Este reordenamiento es la regla 3 de los Principios del Programa — *preservación del capital antes que ganancia* — y el módulo entero es su implementación con matemática exacta.

**La cuenta como termómetro del negocio.** Con el capital como inventario, el drawdown deja de ser "mala racha" y se convierte en el indicador de integridad del negocio: cuánta materia prima falta. El resto del módulo construye los instrumentos de ese termómetro: la tabla de asimetría (8.2), el presupuesto por operación (8.3), el apalancamiento real (8.4), los topes de cartera (8.5) y los frenos automáticos (8.6) — cuatro capas de protección que, escritas juntas, hacen matemáticamente imposible la ruina de un solo día.

## Analogía

El piloto de aviación no despega pensando en el destino: despega con el **plan de emergencia ya escrito**. Antes de mover un solo instrumento sabe cuál es la velocidad mínima, cuánta pista necesita y qué hará si falla un motor a mitad del despegue — porque a esa altura no hay tiempo para decidir bien, solo para ejecutar lo decidido. Nadie llama "miedoso" a un piloto por llevar dos veces más combustible del necesario ni por ensayar el motor fallado en simulador cien veces: se llama **profesionalismo**. El trading tiene exactamente la misma estructura: la emergencia (la racha, el día malo, el mes rojo) no se maneja con fuerza de voluntad en vivo — se maneja con los frenos escritos cuando estabas frío. Todo este módulo es tu lista de verificación previa al despegue, y la 8.6 cierra con el protocolo de apagado completo: el equivalente exacto del procedimiento de emergencia que esperas no usar jamás, pero que te mantiene vivo el día que aparezca.

## Cómo se hace: auditar tu inventario hoy

Antes de continuar a la 8.2, ejecuta esta auditoría de tres pasos — es el arranque del laboratorio del módulo:

1. **Nombra tu inventario:** anota en tu journal el saldo exacto de tu cuenta demo (o real micro) con fecha. Ese número — llámalo $C_0$ — es la materia prima del negocio y la referencia contra la que se medirá cada drawdown de aquí en adelante. Para el caso maestro: $C_0 = 1.920$ \$.
2. **Calcula tu unidad de producción:** el 1 % de $C_0$. Es el presupuesto de una operación estándar — el "costo de harina" por lote de producción. Caso maestro: $1.920 \times 0{,}01 = 19{,}20$ \$.
3. **Declara tu horizonte de supervivencia:** ¿cuántas pérdidas seguidas soporta tu cuenta con el riesgo elegido? La tabla de esta lección lo responde: al 1 %, incluso 20 pérdidas consecutivas — casi tres veces la racha esperable con WR 40 % (7.5) — solo consumen el 18,2 % del inventario. Ese margen entre "peor racha esperable" y "daño real acumulable" es el colchón que estás comprando con el sizing.

## Error común

**(1) Tratar el saldo como puntaje de videojuego.** "Todavía tengo 1.700 de los 1.920" — el número que falta no es puntaje perdido: es capacidad de producción que ya no existe, y recuperarla cuesta más de lo que costó perderla (8.2). **(2) Creer que la preservación es no operar.** El inventario sin usar no genera nada — una cuenta demo intacta en 2027 es un negocio que no existe. La preservación no es la ausencia de riesgo: es el riesgo **presupuestado** (1 %) con frenos escritos (8.6). El profesional arriesga todos los días; simplemente nunca arriesga más del presupuesto. **(3) Confundir preservación con aversión a la pérdida individual.** Tu sistema falla el 60 % de las veces (7.4) y cada fallo cuesta 1 % — eso ES el negocio funcionando. La preservación protege contra las pérdidas **no presupuestadas** (sizing a ojo, sin stop, oversizing tras una racha ganadora), no contra el coste operativo normal. **(4) Auditar el inventario solo cuando duele.** Mirar el saldo cada minuto es ansiedad, no auditoría; mirarlo una vez por semana sin protocolo es negligencia. El punto medio correcto es el journal + los frenos automáticos de 8.6: el sistema vigila el inventario por ti y solo te avisa cuando un tope se dispara.

## Conexión cuantitativa

La preservación cuantifica con una sola tabla. Con riesgo 1 % por operación (y pérdidas consecutivas compuestas, $0{,}99^n$), el inventario sobrevive a la estadística completa de rachas del sistema:

| Pérdidas seguidas | Cuenta al 1 % | Cuenta al 5 % | Cuenta al 10 % |
|---|---|---|---|
| 5 | −4,9 % | −22,6 % | −41,0 % |
| 10 | −9,6 % | −40,1 % | −65,1 % |
| 20 | −18,2 % | −64,2 % | −87,8 % |

*(ilustrativo, interés compuesto sobre el saldo)*. Con WR 40 % (7.4-7.5), la racha esperable máxima en 30 operaciones es de 6-7 pérdidas: al 1 % eso consume ~6 % del inventario — una herida; al 10 %, ~47 % — una amputación que la 8.2 demostrará que casi no se recupera. El enfoque defensivo no es una filosofía: es la única respuesta aritméticamente consistente con esa tabla. Y conecta directo con el principio 85/15 del programa: la técnica que ya tienes (Sistema v1.0) es la mitad menor — la mitad mayor del negocio es exactamente este módulo.

---

## 🎯 Puntos clave

1. El capital es el **inventario del negocio**: materia prima finita cuya quema reduce la capacidad de producción.
2. El profesional invierte el orden de preguntas: primero cuánto se puede perder (y dónde muere la idea), después cuánto se puede ganar.
3. El tamaño no lo decide la ambición: es una **salida** de la fórmula de presupuesto — el 1 % de la cuenta dividido por la distancia al stop (8.3).
4. Al 1 %, incluso 20 pérdidas seguidas (muy por encima de la racha esperable) solo consumen −18,2 %: el sizing compra supervivencia estadística.
5. Preservar no es no operar: es operar con riesgo presupuestado y frenos escritos — la cuenta intacta es un negocio que no existe.

## 🔄 Autoevaluación rápida

1. Tu caso maestro: ¿cuál es el inventario, cuál es la unidad de producción por operación y qué consume la racha esperable máxima (7.5) con WR 40 %?
2. Un conocido dice: "con 500 $ no se puede operar, el riesgo de perderlo todo es enorme". Refuta el argumento con la tabla de esta lección.
3. ¿Por qué "no operar hasta recuperar" NO es preservación de capital? Explica la diferencia entre riesgo presupuestado y ausencia de riesgo.

<details>
<summary>Ver respuestas</summary>

1. Inventario $C_0 = 1.920$ \$; unidad de producción $= 19{,}20$ \$ (1 %). La racha esperable máxima con WR 40 % en 30 operaciones es 6-7 pérdidas → $0{,}99^6 = 0{,}9415$ → consume ~5,9 % ≈ **6 % del inventario (≈ 113 $)** *(la 8.2 calcula su recuperación exacta)*.
2. Con riesgo 1 %, 500 $ arriesgan 5 $ por operación. Veinte pérdidas seguidas — casi tres veces la racha esperable — dejan $500 \times 0{,}99^{20} = 409$ \$ (−18,2 %): imposible "perderlo todo" por rachas con sizing correcto. Lo que destruye cuentas de 500 $ no es el tamaño de la cuenta sino el **sizing a ojo** (10 % por operación, sin stop): ahí 20 pérdidas son −87,8 %. El problema nunca fue el inventario; es la falta de presupuesto.
3. El inventario sin usar no produce: $E = +0{,}2R$ × 0 operaciones = 0. "No operar hasta recuperar" congela el negocio y, peor, suele significar operar LUEGO con más miedo (M10: miedo a perder). Preservación = riesgo presupuestado (1 %, calculado, con redondeo a la baja y stop obligatorio) + frenos que acotan el daño por día/semana/mes (8.6). La ausencia de riesgo no es un estado del negocio: es la suspensión del negocio.

</details>
