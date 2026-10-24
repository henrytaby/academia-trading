# Lección 11.4 · Reglas finas de las prop firms — el examen real está en la letra pequeña

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M11 · La Industria](README.md) |
| ⬅️ Anterior | [Lección 11.3 · Prop firms: el negocio real](leccion-11-3.md) |
| ➡️ Siguiente | [Lección 11.5 · Matriz de riesgo para evaluaciones](leccion-11-5.md) |

---

## Por qué importa

El marketing de las prop firms vende el objetivo ("+8 % en dos fases") y esconde el mecanismo: **las reglas finas** — el conjunto de restricciones donde se pierde la minoría que ya superó la varianza. El patrón documentado del sector es consistente: el aspirante estudia el objetivo y descubre el drawdown; calcula el drawdown y descubre que es *trailing*; calcula el trailing y descubre la *consistency rule*; calcula la consistencia y descubre la restricción de noticias que invalidó su mejor día. Cada regla es legítima por separado (protegen a la firma del trader de un tiro de suerte y del riesgo mal gestionado) y juntas forman el **examen real** — la 11.3 dijo que la firma vende intentos; esta lección muestra el mecanismo fino por el que los intentos se cobran. El objetivo del programa no es "jugar con las reglas": es **leerlas todas antes de pagar, simular tu propio sistema contra ellas y decidir con aritmética** — la misma matriz de due diligence del 11.1, aplicada al contrato de fondeo. Si terminas con una sola idea: **las reglas finas no son letra pequeña: son la especificación técnica del examen — y donde son ambiguas, la interpretación siempre favorece a quien las escribió.**

## Concepto

**Las 6 reglas finas que desaprueban cuentas** *(rangos típicos del sector — cada firma define las suyas y LA VERSIÓN CONTRACTUAL manda)*:

| Regla | Definición típica | Trampa estándar | Cómo se desaprueba sin darse cuenta |
|---|---|---|---|
| **Drawdown diario** (típicamente 4-5 %) | Pérdida máxima en un día — y **incluye flotantes**: el peor momento del día, no el cierre | Contarlo desde el balance del día vs desde el equity pico; algunas firmas lo miden a partir de la medianoche del servidor (TU 17h puede no ser SU 0h) | Dos operaciones de 1 % + un flotante de −2,5 % en la tarde = 4,5 % → cuenta cerrada aunque cierres en verde |
| **Drawdown total** (típicamente 8-10 %) | Límite de pérdida acumulada de la cuenta | **Estático** (desde el balance inicial) vs **trailing** (sigue el pico de equity): el trailing a tu pico +9 % pone tu suelo en −1 % — casi nada de aire | La racha esperada de 9 (M8) al 1 % = −8,65 %: al límite estático la roza, al trailing la mató tres operaciones antes |
| **Consistency rule** (20-50 %) | Ningún día puede representar más del X % del beneficio total del desafío | Se aplica AL MOMENTO de retirar/pagar, no al aprobar: aprobar con un día "grande" y descubrir en el payout que no califica | Un día de noticias genera el 70 % de tu ganancia → el payout se retiene hasta "distribuir" — o se anula el desafío |
| **Restricción de noticias** (±2-5 min) | Prohibido abrir/cerrar en ventana de datos de alto impacto | Definición de "alto impacto" cambia por firma y calendario; algunas bloquean CERRAR posiciones también | Tu TP salta en el anuncio → ganancia anulada o cuenta violada: la regla no negocia con tu plan |
| **Límites de lotaje** | Lote máximo por operación (y a veces por cuenta) proporcional al "capital" | El lote máximo real de tu sistema (0,25 lotes a 10 k) puede chocar con topes arbitrarios | Escalar a 1 lote "porque el capital lo permite" = violación técnica instantánea |
| **Políticas de copiado/grupo** | Restricciones de copiar entre cuentas (propias o de terceros) y de estrategias "idénticas" entre participantes | Las detecciones automáticas de similitud marcan falsos positivos (misma zona en H4 es común a miles) | Copiar tu propio sistema en 2 firmas con ventanas distintas → descalificación por "grupo" o por latencia |

**El detalle técnico que más cuentas cobra: el drawdown flotante.** La definición contractual de "pérdida diaria" casi siempre incluye el **equity**, no el balance: una posición flotante en −4,8 % cuenta aunque la cierres en −0,5 %. Para tu sistema con SL de 1 % y gestión de parciales, esto es estructural: el peor flotante intradía de TU historial (mídelo en el journal: es el máximo adverse excursion de la jornada) tiene que caber en el límite diario — y si tu plan abre 2 posiciones correlacionadas (M8: topes de cartera), el flotante combinado puede tocar el límite sin que ninguna operación individual esté "mal". La simulación previa (11.5) existe exactamente para esto: **tu sistema ya tiene los datos para saber si cabe.**

**El trailing drawdown, diseccionado.** El drawdown estático (suelo fijo en balance inicial −10 %) es manejable con riesgo dinámico. El *trailing* (el suelo sube con tu equity) cambia la matemática del desafío: al llegar a +8 % de ganancia acumulada, tu suelo está en −2 % respecto al inicial — y tu racha esperada de 9 al 0,5 % (−4,5 %) **pasa por debajo del suelo**. La secuencia típica del aspirante: excelente primera semana (+6 %), racha normal de 7-8, cuenta cerrada por trailing — con el marketing de la firma mostrando el objetivo que alcanzó. La regla del programa: **trailing drawdown = el tamaño de riesgo se calcula contra el PEOR caso del suelo móvil, no contra el inicial** — la simulación del 11.5 lo modela.

**Las reglas finas también son señal de due diligence.** La claridad contractual es una métrica de la firma: reglas escritas con ejemplos numéricos y calculadora oficial = firma que quiere que sepas lo que firmas; reglas ambiguas ("a discreción de la firma", "uso abusivo", "consistencia razonable") = la interpretación favorable a la casa, documentada en sus propios términos. El colapso de 11.3 y las disputas públicas del sector giran casi siempre en la zona ambigua. Tu matriz del laboratorio puntuará la **precisión** de las reglas con la misma seriedad que el profit split.

## Analogía

Las reglas del maratón escritas por el organizador. Un maratón serio publica reglas claras: tiempo límite, puntos de corte con reloj, qué cuenta como abandono — y las publica ANTES de que compres la inscripción, con ejemplos ("si estás en el km 30 después de las 13:00, el bus te recoge"). Un organizador tramposo publica "tiempo razonable, a criterio del comité" y decide en el km 40. El corredor profesional no solo entrena la distancia: entrena LOS CORTES (conoce su ritmo y los horarios de cada punto) y elige eventos con reglas precisas. El aspirante ingenuo solo mira la medalla prometida y descubre los cortes en el km 30. Tu sistema con su racha esperada es tu ritmo: las reglas finas son los puntos de corte — y la simulación del 11.5 es tu entrenamiento contra el reloj real.

## Cómo se hace: la lectura forense de un contrato de desafío (20 minutos)

1. **Extrae las 6 reglas con sus números exactos** (no los "típicos": los de ESTA firma) y escríbelas en tu matriz: drawdown diario (¿equity o balance? ¿desde qué hora?), drawdown total (¿estático o trailing? ¿suelo desde qué base?), consistency (¿%? ¿cuándo se aplica?), noticias (¿ventana? ¿qué calendario? ¿aplica a cierres?), lotaje, copiado.
2. **Busca los 3 casos borde en las FAQ oficiales:** (a) flotante que toca el límite diario y se recupera — ¿cuenta?; (b) ganancia de un día de noticias que supera el % de consistencia — ¿se retiene el payout o se anula?; (c) la definición exacta del suelo del trailing en tu mejor momento (pico +8 %: ¿dónde está el suelo?). Si las FAQ no responden con números, la ambigüedad es tu respuesta.
3. **Simula tu sistema contra las 6 reglas** (el laboratorio del 11.5 tiene la plantilla): tu racha esperada, tu peor flotante intradía medido, tu concentración de beneficios por día — los tres contra los límites del contrato.
4. **Puntúa la precisión contractual** en la matriz: reglas con ejemplos numéricos y calculadora oficial (2), reglas claras sin ejemplos (1), reglas a discreción (0 — y es señal de contraparte, 11.3).
5. **Decide con la aritmética del 11.5:** el fee se compra solo si la simulación pasa con margen (el programa exige que la peor racha esperada consuma ≤ 50-60 % del drawdown total — si consume el 90 %, la aprobación depende de la suerte, no del sistema).

## Error común

**(1) "Las reglas finas son para los que operan mal."** Falso por la varianza: la racha de 9 es la estructura NORMAL de un sistema con WR 40 % — el aspirante que la ignora no es un mal trader: es un comprador que no leyó la especificación del examen. **(2) Confundir equity y balance.** El 80 % de las sorpresas de drawdown diario nacen aquí *(proporción heurística)*: flotantes que cuentan, horas de corte de servidor, equity del pico. La lectura forense es obligatoria, no opcional. **(3) "Aprobar primero, las reglas de payout después."** La consistency rule y las restricciones de payout aplican EXACTAMENTE cuando ya hiciste el trabajo: aprobar sin leer la etapa de pago es correr el maratón sin leer dónde está el bus. **(4) Optimizar el desafío en vez de operar el sistema.** "Me salto la regla de noticias con órdenes pendientes", "distribuyo las ganancias en días artificiales" — manipular las reglas es violarlas con pasos intermedios (y las firmas lo persiguen contractualmente): o tu sistema pasa las reglas, o las reglas no son para tu sistema. **(5) No documentar TU cumplimiento.** Igual que el journal v1 te protege de tu memoria, el log de tus operaciones en el desafío (hora, flotante, distancia a cada límite) es tu evidencia ante una disputa: la firma tiene sus registros; tú tienes que tener los tuyos.

## Conexión cuantitativa

**Hacia M8:** las reglas finas son topes de riesgo ajenos: el drawdown diario de 5 % es una cascada de un nivel impuesta por contrato — y tu cascada personal (−2/−4/−6 %) debe dispararse ANTES que la del contrato: la firma nunca debe ver tu peor día primero. **Hacia 9.2-9.3:** los datos de tu forward testing (peor flotante intradía, concentración diaria de ganancias) son exactamente los que la simulación de reglas necesita: tu journal ya midió lo que el contrato exige. **Hacia 11.5:** la matriz de riesgo dinámico convierte estas reglas en el plan de sizing del desafío — la próxima lección es la traducción numérica de esta. **Hacia la misión M-11:** tu informe debe incluir la lectura forense de al menos 3 contratos reales — la precisión contractual puntuada como celda de la matriz.

---

## 🎯 Puntos clave

1. Las reglas finas son **la especificación técnica del examen real**: drawdown diario (con flotantes), total (estático vs trailing), consistency, noticias, lotaje y copiado — la minoría que supera la varianza se pierde aquí.
2. El **drawdown flotante** es la trampa nº 1: el peor momento del día cuenta, no el cierre — tu peor excursión intradía medida en el journal tiene que caber en el límite.
3. El **trailing drawdown** cambia la matemática: al pico +8 % tu suelo puede estar en −2 % y la racha esperada de tu sistema pasa por debajo — el sizing se calcula contra el peor suelo móvil.
4. La **precisión contractual es una métrica de la firma**: reglas con ejemplos numéricos = transparencia; "a discreción" = interpretación favorable a la casa — puntúala en la matriz como la propia rentabilidad.
5. El protocolo: leer las 6 reglas con números exactos → 3 casos borde en las FAQ → simular tu sistema → puntuar precisión → comprar solo si la peor racha consume ≤ 50-60 % del drawdown total.

## 🔄 Autoevaluación rápida

1. Un desafío: drawdown diario 5 % (equity, medianoche servidor), total 10 % trailing, consistency 40 %, noticias ±3 min. Tu sistema: WR 40 %, racha esperada 9, peor flotante intradía medido 1,8 % (a riesgo 0,5 %). Simula: ¿cabe la racha esperada en el trailing al llegar a +6 % de ganancia acumulada? ¿Y tu peor flotante + 2 operaciones en el límite diario?
2. Un aspirante aprueba con +12 % en 40 operaciones, donde un solo día de noticias aportó +7 %. Con consistency 40 %: ¿qué pasa en el payout, cuáles eran sus opciones correctas y qué regla del programa lo habría prevenido?
3. Formula la regla del programa del margen de seguridad (peor racha ≤ 50-60 % del drawdown total) y calcula el riesgo máximo por operación que la cumple para un desafío de 10 % estático con tu racha esperada de 9. Compara con el riesgo al 1 %.

<details>
<summary>Ver respuestas</summary>

1. Trailing al pico +6 %: el suelo móvil está en −4 % respecto al inicial (10 % − 6 %); tu racha esperada de 9 a 0,5 % = −4,5 % **pasa por debajo del suelo** → descalificación estructural ANTES de terminar el desafío: el sistema no cabe a 0,5 % con trailing; a 0,25 % (−2,25 %) cabe con margen. Límite diario: peor flotante 1,8 % + 2 operaciones de 0,5 % perdidas = 2,8 % — cabe en 5 %, PERO con dos posiciones correlacionadas el flotante combinado podría llegar a ~3,8 %: todavía cabe, pero sin margen para una tercera — el plan debe limitar correlación intradía (tope motor de M8). Veredicto: el desafío solo se compra a 0,25 %, o se busca firma con drawdown estático.
2. El día de noticias (58 % del total: 7/12) supera el 40 %: en el payout, la firma retiene hasta que la distribución "califique" o anula según el contrato — el aspirante descubre que aprobó sin calificar. Opciones correctas: repartir la ganancia operando más días SIN noticias (lo que el tiempo del desafío puede no permitir), o elegir firma sin consistency (con sus propias contras), o — la del programa — **no construir el desafío sobre un día de noticias**: la restricción de noticias y la consistencia son reglas del examen que se simulan antes de pagar. La regla del programa que lo previene: la lectura forense del contrato (11.4, paso 1-2) incluye el caso borde "¿ganancia de noticias > % de consistencia?" — las FAQ responden con números o el fee no se compra.
3. Regla: la peor racha esperada de tu sistema debe consumir como máximo 50-60 % del drawdown total — el resto es margen de supervivencia para la varianza real (que no sabe que es "esperada"). Cálculo: racha de 9 al riesgo r con drawdown 10 %: $1-(1-r)^9 \le 0{,}06 \Rightarrow (1-r)^9 \ge 0{,}94 \Rightarrow r \le 1 - 0{,}94^{1/9} = 1 - 0{,}9931 = 0{,}69$ % — a 60 % de margen: $r \le 0{,}69$ %... corrigiendo a la meta estricta del 50 %: $(1-r)^9 \ge 0{,}95 \Rightarrow r \le 0{,}57$ %. El programa recomienda 0,25-0,5 % (11.5) — dentro del margen con aire adicional. Al 1 %: 0,99⁹ = 0,9135 → la racha consume 86,5 % del límite: fuera de la regla, la aprobación depende de que la varianza "no venga" — exactamente la apuesta que el 92 % pierde.

</details>
