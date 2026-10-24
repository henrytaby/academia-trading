# Lección 8.4 · Apalancamiento real — el margen no es el riesgo

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M8 · Gestión del Riesgo](README.md) |
| ⬅️ Anterior | [Lección 8.3 · La regla del 1 % y position sizing](leccion-8-3.md) |
| ➡️ Siguiente | [Lección 8.5 · Riesgo de cartera y correlación](leccion-8-5.md) |

---

## Por qué importa

"¿Qué apalancamiento te da tu broker?" es la pregunta favorita de la publicidad; "¿cuál es tu apalancamiento real?" es la que hace un profesional. Esta lección desmonta el malentendido más rentable de la industria minorista: la creencia de que el apalancamiento ofertado (1:30, 1:100, 1:500) tiene algo que ver con el riesgo de tus operaciones. Tiene que ver con el **margen inmovilizado** — una línea contable — y con un peligro técnico real pero distinto (la liquidación forzada por margen). El riesgo verdadero ya lo fijaste en 8.3: es el presupuesto dividido por la distancia al stop, y no cambia una décima según lo generoso que sea tu broker con el margen. Al terminar, sabrás calcular margen, lotaje y valor del pip de cualquier instrumento mayor, y tendrás la regla del programa sobre cuándo el apalancamiento SÍ importa — porque importa, solo que por otras razones que las que la publicidad dice.

## Concepto

**El vocabulario exacto, con el caso maestro en mano.** Tu operación de la Receta: 0,06 lotes de EUR/USD con SL de 32 pips sobre una cuenta de 1.920 $.

| Concepto | Definición | En el caso maestro |
|---|---|---|
| **Nominal** | Lo que realmente compras/vendes | $0{,}06 \times 100.000 = 6.000$ € ≈ 6.480 $ *(EUR/USD ≈ 1,08, ilustrativo)* |
| **Margen** | La garantía que el broker congela para mantener la posición abierta | A 1:30: $6.480/30 ≈ 216$ $; a 1:500: ≈ 13 $ |
| **Apalancamiento del broker** | Máximo nominal por unidad de margen (publicidad) | 1:30 / 1:100 / 1:500 — da igual, ver abajo |
| **Apalancamiento real** | Nominal ÷ capital de la cuenta | $6.480 / 1.920 ≈ 3{,}4\times$ |
| **Riesgo de la operación** | Lo que pierdes si toca el SL | $0{,}06 \times 32 \times 10 = 19{,}20$ $ — **en TODAS las columnas** |

La tabla entera tiene una sola moraleja: recorre la fila "Riesgo" — es la única constante. Cambia el broker, cambia el apalancamiento, cambia el margen congelado: **el riesgo de tu operación lo define el stop y el lote, no el margen**. El margen es un depósito de garantía (como la fianza de un alquiler): congelar más o menos dinero no cambia lo que pierdes si la operación falla.

**El valor del pip, instrumento por instrumento** *(cuenta denominada en USD, valores ilustrativos con precios típicos)*:

| Instrumento | Contrato de 1 lote | Pip | Valor del pip por lote | Nota |
|---|---|---|---|---|
| EUR/USD, GBP/USD, AUD/USD | 100.000 unidades | 0,0001 | **10 $** (fijo) | La divisa de cotización es USD |
| USD/CHF | 100.000 USD | 0,0001 | 10 CHF ÷ precio ≈ **11,4 $** (a 0,8800) | Varía con el precio |
| USD/JPY | 100.000 USD | 0,01 | 1.000 JPY ÷ precio ≈ **6,67 $** (a 150,00) | Varía con el precio |
| XAU/USD (oro) | 100 onzas | 0,01 $ de precio | 1,00 $ de movimiento = **100 $ por lote** | Convención de la ficha oro de la Receta |

La fórmula general para pares con la divisa de cotización distinta de USD: el pip vale (tamaño del pip × 100.000) en la divisa de cotización, y se convierte a dólares dividiendo por el precio actual. Por eso tu calculadora (8.3, celda B7) pide el valor del pip como dato — y por eso la misión del módulo incluye escenarios de USD/JPY y oro: el error clásico es meter 10 $/pip en todo.

**Los micro-lotes: la granularidad que hace viable el 1 %.** Un micro-lote = 0,01 estándar = 1.000 unidades = 0,10 $/pip en EUR/USD. Con la cuenta del caso maestro y SL 32 pips, cada micro-lote arriesga 3,20 $ — así el cálculo afina exacto: 6 micros = 19,20 $ = 1,0 %. Imagina el mismo cálculo sin micro-lotes (solo mini 0,1 / estándar 1,0): tus opciones serían 0,05 lotes (16 $ = 0,83 %) o 0,1 (32 $ = **1,67 %** — presupuesto roto). Con cuentas pequeñas, la granularidad fina no es un lujo: es la diferencia entre respetar el 1 % y romperlo sistemáticamente por redondeo.

**Cuándo el apalancamiento SÍ importa — los tres peligros reales.** (1) **Liquidación forzada por margen:** si el margen usado consume gran parte del disponible, un movimiento adverso ANTES de que el SL ejecute (gap de fin de semana, noticia, spread que se abre) puede disparar el stop-out del broker a un precio peor que tu SL — el riesgo deja de ser el presupuesto. Regla del programa: **margen usado < 20-30 % del disponible siempre**; con el caso maestro (216 $ de 1.920 $ a 1:30 ≈ 11 %) sobra margen de seguridad. (2) **La invitación psicológica:** un broker que te ofrece 1:500 te está diciendo "puedes mover 100× tu capital" — el oversizing por sugestión es más fácil cuando la plataforma hace el lote grande fácil. Tu defensa es el procedimiento de 8.3, que ignora la oferta. (3) **Costes overnight proporcionales al nominal:** el swap se cobra sobre el nominal (6.000 $), no sobre tu riesgo (19,20 $) — en operaciones largas (swing con D1) el coste de mantener un apalancamiento real alto come la E (7.4 ya contó los costes: aquí solo apunta que el swap escala con el nominal).

**La regla del programa en una línea:** el apalancamiento real es una **consecuencia** del sizing, nunca un objetivo. Con riesgo 1 % y SL estructural (~1,5 ATR de M6), el real típico del caso maestro queda en 2-4×. Si tus operaciones habituales superan ~10× real, tu SL es sospechosamente corto o tu riesgo está por encima del presupuesto — vuelve al componente 6 del sistema, no al catálogo de brokers.

## Analogía

La fianza del alquiler. Alquilas un local de 6.000 $ al mes; el casero te pide una fianza de 2 meses (12.000 $) o de medio mes (3.000 $) según la ley del país o su confianza en ti. Pregunta: ¿cuánto RIESGAS firmando el contrato? Ni 12.000 ni 3.000 — la fianza no es el riesgo: es dinero **congelado** que te devuelven si cumples. Tu riesgo real es el negocio que montas dentro del local: si quiebra, pierdes lo invertido en él, no la fianza. El apalancamiento del broker es la política de fianzas; el margen, la fianza concreta; tu riesgo es el SL × el lote. El trader que elige broker "por el apalancamiento" es el inquilino que elige local "por la fianza barata" — confunde la línea contable con el negocio. Y el stop-out por margen tiene su equivalente exacto: si gastas casi toda tu caja en fianzas, la próxima firma te deja sin liquidez y el contrato se cae en el peor momento — por eso la regla del margen usado < 20-30 %.

## Cómo se hace: el chuletero de tres cálculos

1. **Margen:** $\text{margen} = \frac{\text{nominal}}{\text{apalancamiento}}$, con $\text{nominal} = \text{lote} \times 100.000$ (o × 100 onzas en oro) convertido a la divisa de la cuenta. Caso maestro a 1:100: $6.480/100 ≈ 65$ $ — el 3,4 % de la cuenta congelado: tranquilidad total.
2. **Apalancamiento real:** $\text{real} = \text{nominal}/\text{capital}$. Caso maestro: $3{,}4\times$. Tu checklist semanal puede apuntar el promedio: si la media de tus operaciones v1.0 vive entre 2× y 4×, el sistema está ejecutándose como fue diseñado.
3. **Valor del pip cuando la cotización no es USD:** $\text{valor pip} = \frac{\text{tamaño pip} \times 100.000}{\text{precio}}$ (en pares USD/XXX). USD/JPY a 150,00: $\frac{0{,}01 \times 100.000}{150} = 6{,}67$ $. Con SL de 30 pips y presupuesto 19,20 $: $\text{lote} = 19{,}20/(30 \times 6{,}67) = 19{,}20/200{,}1 = 0{,}096$ → redondeo a la baja → **0,09 lotes** (riesgo real $0{,}09 \times 200{,}1 = 18{,}01$ $ = 0{,}94$ % — dentro del presupuesto ✓). *(El escenario 6 de la misión lo pide con otros números.)*

## Error común

**(1) "Tengo 1:500, puedo ganar más."** El apalancamiento multiplica la velocidad del dinero en AMBAS direcciones; lo que defines tú es el tamaño — y con el sizing de 8.3, dos brokers con 1:30 y 1:500 ejecutan tu sistema con resultados idénticos (solo cambia el margen congelado). **(2) "El margen es lo que puedo perder."** No: el margen es la fianza. Lo que pierdes es SL × valor pip × lote. Confundirlos lleva a creer que "con 1:500 riesgo todo el margen" — falso — o peor, que "con margen pequeño no hay riesgo" — doblemente falso. **(3) Usar el apalancamiento disponible como capacidad.** "Me ofrece 1:500 sobre 1.920 $ → puedo abrir 960.000 $ de nominal": exacto, y con SL 32 pips eso son 3.072 $ de riesgo = **160 % de la cuenta** en una operación. La plataforma te lo permite; la aritmética te lo prohíbe. **(4) Ignorar el stop-out.** Con margen usado al 80 % del disponible, una noticia mueve el precio 40 pips y el broker liquida ANTES de tu SL a un precio peor: el riesgo ya no es 19,20 $ sino lo que el mercado decida. La regla del 20-30 % no es burocracia. **(5) Meter 10 $/pip en todo.** En USD/JPY (≈ 6,67 $ a 150) te deja fuera un tercio del tamaño; en USD/CHF (≈ 11,36 $ a 0,8800) te pasa del presupuesto (0,06 lotes × 11,36 × 32 = 21,81 $ = 1,14 %): dos errores opuestos del mismo descuido. La celda B7 de la calculadora es un dato por instrumento, no una constante universal.

## Conexión cuantitativa

El apalancamiento real es la variable que conecta el sizing (8.3) con la estructura de costes (7.4). Su efecto sobre la E llega por tres canales, todos medibles: (1) el swap sobre nominal — en swing con R:B 1:2 y 3 días de mantenimiento, un swap típico puede añadir 0,01-0,03R de coste por operación: no decide nada en un sistema sano, pero escala LINEALMENTE con el apalancamiento real; (2) el spread en proporción — con nominal alto y cuenta pequeña, el spread pagado (2-3 pips del M4) es idéntico en pips pero su peso en R no cambia... el que cambia es tu capacidad de sostener varias posiciones simultáneas (8.5) sin tocar el stop-out; (3) la granularidad del sizing — con micro-lotes, la desviación entre presupuesto y riesgo real queda en ±0,05 % (el caso 0,06 exacto); sin ella, el redondeo añade sistemáticamente 0,5-0,7 % por operación, que en 100 operaciones es un impuesto silencioso de ~50 % de E... en cuentas donde la granularidad no existe, la solución no es redondear arriba: es reducir el % (0,5 %) hasta que el grano permita respeto exacto. Hacia delante: 8.5 toma el sizing por operación y lo convierte en presupuesto por cartera; la 8.6 asume el 1 % como base de su cascada de frenos. Y hacia M9: el apalancamiento real promedio será una de las métricas de tu reporte de 100 backtests — el dato que confirma que el sistema v1.0 se ejecuta con la misma palanca con la que fue diseñado.

---

## 🎯 Puntos clave

1. Margen = fianza congelada; riesgo = SL × valor pip × lote. Son líneas distintas: el apalancamiento del broker solo afecta a la primera.
2. Apalancamiento real = nominal/capital (caso maestro: 3,4×) — es consecuencia del sizing, nunca objetivo.
3. Valor del pip: 10 $ fijo en EUR/USD/GBP/AUD (cuenta USD); USD/JPY ≈ 6,67 $ a 150; oro: 100 $ por cada 1,00 $ de movimiento por lote.
4. Los micro-lotes (0,01) dan la granularidad que permite respetar el 1 % en cuentas pequeñas.
5. El apalancamiento alto SÍ importa por tres peligros: stop-out por margen (regla: margen usado < 20-30 %), invitación al oversizing y swap sobre nominal.
6. ~10× real habitual = alarma: SL demasiado corto o riesgo fuera de presupuesto — revisar el componente 6, no el broker.

## 🔄 Autoevaluación rápida

1. Cuenta 2.500 $, operación GBP/USD 0,04 lotes con SL 40 pips. Calcula nominal (GBP/USD ≈ 1,26), margen a 1:30, apalancamiento real y riesgo. ¿Qué pasaría con el riesgo a 1:500?
2. USD/JPY cotiza a 155,00. ¿Valor del pip por lote? Con presupuesto 20 $ y SL 30 pips, ¿qué lote operas (con redondeo a la baja)?
3. Oro: cuenta 4.000 $, riesgo 1 %, SL 4,00 $ de precio. Calcula el lote con la convención de la tabla (1,00 $ = 100 $/lote).
4. Tu media de apalancamiento real del último mes es 12×. Diagnóstico completo: ¿qué dos causas lo explican, qué riesgo oculto añade la primera y qué lección del módulo te toca revisar?

<details>
<summary>Ver respuestas</summary>

1. Nominal: $0{,}04 \times 100.000 = 4.000$ GBP ≈ 5.040 $. Margen a 1:30: ≈ 168 $. Real: $5.040/2.500 ≈ 2{,}0\times$. Riesgo: $0{,}04 \times 40 \times 10 = 16$ $ = 0,64 %. A 1:500 el margen baja a ≈ 10 $ y el riesgo queda EXACTAMENTE igual: 16 $ — la demostración de que el apalancamiento del broker no toca el riesgo.
2. $\frac{0{,}01 \times 100.000}{155} = 6{,}45$ $/pip. Lote: $20/(30 \times 6{,}45) = 20/193{,}5 = 0{,}103$ → redondeo a la baja → **0,10 lotes** (riesgo real 19,35 $ ≈ 0,97 % — dentro del presupuesto ✓).
3. Presupuesto: 40 $. Riesgo por lote: $4{,}00 \times 100 = 400$ $. Lote: $40/400 = 0{,}10$ lotes — 10 onzas, que se mueven 4 $ en tu contra = 40 $ exactos ✓.
4. (a) SL estructural demasiado corto (stops de 10-15 pips obligan a lotes grandes para el mismo presupuesto) → revisar el componente 6 con la auditoría ATR de M6 (SL ≈ 1,5 ATR): stops cortos = más whipsaw (M3) + más lotes = doble daño. (b) Riesgo por encima del presupuesto (el % se subió "a mano") → volver a 8.3. El riesgo oculto de (a): además del whipsaw, el stop-out — con lotes grandes el margen usado sube y un gap puede liquidar antes del SL. Ambas causas se curan con el procedimiento de 8.3, no con un broker "más flexible".

</details>
