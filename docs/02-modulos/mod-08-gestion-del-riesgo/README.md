# Módulo 8 · Gestión del Riesgo — el módulo que paga las cuentas

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada aquí constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 3 · Gestión — módulo de apertura |
| 📦 Módulo | 8 de 12 (FIT-12) |
| 🔬 Trazabilidad | 003 · M4.5, M6.5 · 004 · M6.1–6.5 · **Aporte propio:** riesgo de cartera y correlación de posiciones (vacío 1), protocolo de frenos en cascada con apagado firmado |
| ⏱️ Duración estimada | 5–6 h de teoría + 6–10 h de laboratorio/misión |
| 📋 Estado | 🟢 Publicado (Sprint 8) |

---

## 🎯 Objetivo del Módulo

Blindar el capital con matemática exacta. El N2 te dio una máquina que gana en esperanza ($E = +0{,}2R$); este módulo le instala el sistema inmunológico: el capital como inventario con su enfoque defensivo (8.1), la tabla de asimetría que demuestra por qué el gran daño es irreversible (8.2), la fórmula universal de position sizing que convierte "riesgo 1 %" en un lote concreto y verificable (8.3), la desmontaje del mito del apalancamiento con el valor del pip real por instrumento (8.4), el mapa de motores que evita que tres operaciones de 1 % sean una apuesta de 3 % (8.5) y la cascada de frenos con protocolo de apagado que acota el peor mes del negocio en −6 % (8.6). Al terminar sabes exactamente cuánto puedes perder HOY — y por qué es matemáticamente imposible perder más.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 8.1 | [Preservación de capital](leccion-8-1.md) | El dinero como inventario del negocio; el orden invertido de las preguntas del profesional; supervivencia al 1 % vs 10 % | 30–40 min |
| 8.2 | [Asimetría del drawdown](leccion-8-2.md) | $R = \frac{d}{1-d}$; la tabla completa (−10 % → +11,1 % ... −50 % → +100 %); por qué el gran daño es irreversible | 40–55 min |
| 8.3 | [La regla del 1 % y position sizing](leccion-8-3.md) | La fórmula universal con el caso maestro desglosado (0,06 lotes); solo la distancia al stop está en riesgo; redondeo a la baja | 50–65 min |
| 8.4 | [Apalancamiento real](leccion-8-4.md) | Margen ≠ riesgo; valor del pip por instrumento (FX, oro); micro-lotes; los 3 peligros reales del apalancamiento alto | 45–60 min |
| 8.5 | [Riesgo de cartera y correlación](leccion-8-5.md) | Motores compartidos; $R_{\text{efectiva}} = R_1 + \rho R_2$; topes escritos: 2 % por motor, 3 % global | 50–65 min |
| 8.6 | [Frenos de emergencia](leccion-8-6.md) | La cascada (−2 % día / −4 % semana / −6 % mes); protocolo de apagado firmado; la trampa de la revancha | 45–60 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo se estudia **con tu Sistema v1.0 (M7) abierto en paralelo**: cada lección formaliza una pieza del componente 9 (riesgo y tamaño) y termina escribiendo reglas nuevas en el componente 10 — al cerrar 8.6 tu sistema v1.0 habrá mutado a v1.1 con presupuesto, topes y frenos.
>
> **El caso maestro consigue su presupuesto:** las 6 lecciones usan la operación de tu [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) *(ilustrativo)* — EUR/USD H4, cuenta $C_0 = 1.920$ \$, riesgo 1 % = 19,20 \$, SL 32 pips, TP 66 pips (R:B ≈ 2,1). En M7 declaraste "riesgo 1 %" como regla del componente 9; aquí aprendes la máquina que la ejecuta: $19{,}20/(32 \times 10) = 0{,}06$ lotes — y toda la infraestructura que garantiza que ese número se respeta cuando el día se pone feo.
>
> **Puente con M7 y M9:** el M8 convierte el componente 9 en procedimiento (calculadora) y refuerza el componente 10 (topes de cartera + frenos). M9 auditará con 100 backtests si tu sizing respetó el presupuesto — la métrica "disparos ejecutados / disparos debidos = 100 %" empieza a medirse HOY.

## 🧪 Laboratorio · Construir la calculadora de position sizing

**Materiales:** las 6 lecciones + tu hoja de cálculo preferida (Excel/Google Sheets/LibreOffice) + la [versión Python del programa](../../../scripts/core/position_sizing.py) como referencia verificada + el caso maestro como caso de control.

**Estructura de la hoja — 3 pestañas:**

**Pestaña 1 · Sizing** *(la fórmula universal con las 5 micro-reglas de 8.3)*:

```text
B1 capital actual          = [tu saldo]
B2 riesgo %                = 1 %
B3 presupuesto             = B1 * B2 / 100
B4 entrada                 = [precio de tu señal]
B5 stop                    = [precio estructural + margen]
B6 SL en pips              = ABS(B4 - B5) / 0.0001      ← pares XXX/USD de 4-5 decimales
B7 valor del pip por lote  = [10 EUR/GBP/AUD · 6,67 USD/JPY a 150 · 100 $ por 1,00 $ en oro]
B8 lote bruto              = B3 / (B6 * B7)
B9 lote final              = FLOOR(B8, 0.01)             ← redondeo a la baja, SIEMPRE
B10 verificación inversa   = B9 * B6 * B7                ← debe ser ≤ B3, si no HAY ERROR
B11 riesgo real %          = B10 / B1 * 100              ← el dato que va al journal
```

Regla de veto: si B8 < 0,01 → la celda devuelve **RECHAZADA** ("no hay espacio de riesgo") — nunca se redondea hacia arriba.

**Pestaña 2 · Cartera** *(8.5)*: filas por posición abierta (instrumento, lado, riesgo %, motor) + celda de correlación ρ medida (30-90 días) + columnas: $R_{\text{efectiva}} = R_1 + \rho R_2$ por motor, tope por motor 2 %, tope global 3 %, veredicto (ACEPTAR/RECHAZAR) para la siguiente señal.

**Pestaña 3 · Frenos** *(8.6)*: saldos de referencia (día/semana/mes) + equity actual + nivel activo de la cascada (0-4) con la acción obligatoria impresa — la calculadora compara números y devuelve el nivel, sin opinión.

**Procedimiento:**

1. **Construye las 3 pestañas** con las fórmulas exactas de arriba (30-45 min). La versión Python del repo es tu oráculo: cada función debe coincidir con la hoja al centavo.
2. **Verifica con los 3 casos de control:** (a) caso maestro → 0,06 lotes / 19,20 $ / 1,0 % exacto; (b) USD/JPY a 150, presupuesto 19,20 $, SL 30 pips → 0,09 lotes / 18,01 $ / 0,94 %; (c) capital 350 $, SL 80 pips → **RECHAZADA**. Si la hoja no reproduce los tres, la hoja está mal — no el caso.
3. **Intégrala al flujo:** añade a tu checklist pre-operación el paso "calculadora corre antes de la orden" y a tu checklist semanal "pestaña de frenos revisada".
4. **Auditoría cruzada con el agente:** muestra la hoja y responde — ¿por qué redondeo a la baja? ¿de dónde sale el valor del pip de cada instrumento? ¿qué pasa si el lote bruto es 0,005?
5. **Actualiza el Sistema v1.0 → v1.1:** el componente 9 referencia la calculadora por su nombre; el componente 10 añade topes (2 % motor / 3 % global) y la cascada de frenos firmada.

**Entregable:** la calculadora funcional (hoja + capturas de los 3 casos de control) y el Sistema v1.1 con los componentes 9-10 actualizados. La calculadora no es un accesorio: es el procedimiento que ejecuta la regla más importante del negocio.

## 🎯 Misión

> [!IMPORTANT] Misión M-8 · 20 escenarios de sizing resueltos a mano
> **Objetivo:** convertir la fórmula de 8.3 en reflejo. Los 20 escenarios ([hoja de escenarios con clave oculta](../../03-recursos/laboratorio/mision-m8-escenarios.md)) cubren FX mayor, cruces USD/JPY, oro, redondeos, un rechazo por grano mínimo, una cartera con correlación y una recuperación de drawdown — cada uno resuelto **a mano, sin calculadora primero**, y verificado DESPUÉS contra tu hoja (o el script del repo).
> **Procedimiento por escenario:** (1) lee el dato; (2) resuelve a mano en tu cuaderno (la división completa, no "aproximado a ojo"); (3) verifica contra la calculadora; (4) si difieren, encuentra el error ANTES de seguir — un error de valor del pip contaminaría los 20.
> **Entregable:** `journal/mision-m8.md` con los 20 resultados a mano + la verificación de la calculadora + las 3-4 líneas de error corregido (si las hubo). Puntuación: **≥ 18/20 correctos** para aprobar — este módulo exige nota alta porque es el que paga las cuentas.
> **Criterio de aceptación:** 20/20 intentados · ≥ 18 correctos · los escenarios de decisión (17-20) con la JUSTIFICACIÓN escrita, no solo la respuesta · calculadora usada como verificador, no como oráculo previo.
> **Etiqueta en journal:** `mision-m8-sizing` · **Tiempo estimado:** 1 semana (4-5 escenarios por sesión).

## ✅ Evaluación / Criterio de Graduación

Criterio del SYLLABUS para este módulo — **el único con umbral elevado (≥ 90 %)**, porque sus errores no se pagan en notas sino en inventario:

- **Calculadora funcional:** 3 pestañas construidas + los 3 casos de control verificados + integrada en el checklist pre-operación.
- **Misión M-8 completa:** 20 escenarios resueltos a mano, ≥ 18/20 correctos, con justificación escrita en los de decisión.
- **Quiz de graduación de este módulo: ≥ 9/10 (90 %)** — el umbral de los demás módulos (80 %) no aplica aquí: un 60 % de acierto en conceptos de riesgo equivale a operar sin entender el freno de emergencia.
- **Sistema v1.1 entregado:** componentes 9-10 con calculadora, topes y cascada referenciados por nombre.

Al aprobar todo: se abre [M9 · Backtesting, Journal y Validación](../mod-09-backtesting-journal-y-validacion/README.md) — donde tu Sistema v1.1 consigue su evidencia estadística (100 operaciones ciegas) y el journal v1 (taxonomía E0-E7 + actas) se convierte en tu auditoría interna.

## 📝 Quiz de Graduación — umbral ≥ 9/10 (90 %)

1. Preservación de capital: define el capital como inventario y enumera el orden de las 4 preguntas del profesional. ¿Por qué "el tamaño es una salida de la fórmula" es la diferencia estructural con el aficionado?
2. Con la fórmula $R = \frac{d}{1-d}$: calcula la recuperación necesaria para −15 % y −40 %, explica por qué la curva es superlineal, y por qué la referencia del drawdown es el máximo de la curva de capital (ejemplo: cuenta que subió a +12 % y está en +2 %).
3. Deriva la regla del 1 % desde la estadística: con WR 40 % (rachas esperables de 6-7, 7.5) y la tabla de 8.2, muestra por qué al 1 % la peor racha esperable es una herida (−6 %) y al 5 % es no retorno práctico (−26,5 %). ¿Cuándo bajaría a 0,25-0,5 %?
4. Fórmula universal completa: capital 3.600 $, riesgo 1 %, SL 45 pips, EUR/USD. Calcula presupuesto, lote bruto, lote final y la verificación inversa. ¿Qué haces si el lote bruto sale 0,004?
5. USD/JPY cotiza a 160,00: calcula el valor del pip por lote. Con presupuesto 25 $ y SL de 25 pips, ¿qué lote operas? Muestra el redondeo a la baja y el riesgo real resultante.
6. Oro (XAU/USD): capital 2.000 $, riesgo 1 %, SL 2,50 $ de precio. Con la convención "1,00 $ de movimiento = 100 $ por lote", calcula el lote exacto.
7. Apalancamiento: con 0,06 lotes de EUR/USD (nominal ≈ 6.480 $) sobre capital 1.920 $, calcula el margen a 1:30 y a 1:500, el apalancamiento real, y explica por qué el riesgo es el mismo en ambos. ¿Cuáles son los 3 peligros reales del apalancamiento alto?
8. Correlación: cartera con EUR/USD long (1 %). Llega AUD/USD long (1 %) con ρ medido 0,70. Calcula el riesgo efectivo del motor dólar y el veredicto. ¿Y si después llega GBP/USD long? ¿Por qué ρ ≤ −0,70 no da "crédito de cobertura"?
9. Cascada de frenos: reproduce la tabla completa (disparador → acción) de los 5 niveles. ¿Cuál es el peor mes posible con la cascada activa y por qué todos los disparadores son números y no sentimientos? ¿Cómo trocea el freno diario una racha de 6?
10. Integración (el día del dato): es mediodía; tu día ya marca −1 % (una pérdida al 1 % sobre capital inicial 1.920 $) y la cartera está vacía. Llegan dos señales simultáneas: GBP/USD long y AUD/USD long (ρ entre ambas ≈ 0,85, ambas cortan el dólar). Decide con el orden completo del módulo: freno (espacio diario) → cartera (topes) → sizing (calculadora con el capital ACTUAL). Muestra todos los números.

<details>
<summary>Ver clave de respuestas</summary>

1. El capital es la materia prima finita del negocio (8.1): cada dólar quemado reduce la capacidad de producir. Orden del profesional: (1) ¿cuánto puedo perder? (2) ¿dónde muere la idea (SL)? (3) ¿qué tamaño PERMITE el presupuesto? (4) ¿y si fallan 6 seguidas? El aficionado recorre el orden inverso y dimensiona por ambición. "El tamaño es una salida" significa que NO es una decisión libre: sale del presupuesto dividido por la distancia al stop — dos traders con los mismos datos calculan el mismo lote (test del clon cuantitativo).
2. $R(15) = 0{,}15/0{,}85 = +17{,}6$ %; $R(40) = 0{,}40/0{,}60 = +66{,}7$ %. Superlineal: el denominador $(1-d)$ encoge el capital sobre el que se recupera, así cada punto extra de drawdown cuesta MÁS de un punto de ganancia futura (de −30 % a −50 %, pasa de +42,9 % a +100 %). La referencia es el máximo: $0{,}12 \to 0{,}02$ es $\frac{0{,}10}{1{,}12} ≈ -8{,}9$ % de drawdown, no "sigue en verde" — el máximo es el punto desde el que el negocio debe reconstruirse.
3. Rachas de 6-7 esperables (7.5). Al 1 %: $0{,}99^6 ≈ 0{,}9415$ → −5,9 % ≈ −6 % → recuperación +6,4 % ≈ 31 operaciones: herida. Al 5 %: $0{,}95^6 ≈ 0{,}735$ → −26,5 % → recuperación +36 % con 3-4 años de ejecución perfecta: no retorno práctico (8.2). El 1 % es el cruce: mantiene el peor escenario normal del sistema por debajo de la línea de emergencia (−15 %) incluso con la estadística más fea. Se baja a 0,25-0,5 % con WR medido bajo (rachas de 10-12), instrumentos con gap, o primer año de ejecución.
4. Presupuesto: $3.600 \times 0{,}01 = 36$ $. Lote bruto: $36/(45 \times 10) = 0{,}08$ exacto. Lote final: 0,08. Verificación: $0{,}08 \times 45 \times 10 = 36$ $ ✓. Si el lote bruto sale 0,004: **RECHAZADA** — no cabe ni un micro-lote sin exceder el presupuesto (0,01 daría 0,45 $ de riesgo... al revés: 0,01 × SL × 10 sería el riesgo real; el principio es riesgo real ≤ presupuesto — el sizing tiene veto igual que el setup).
5. $\frac{0{,}01 \times 100.000}{160} = 6{,}25$ $/pip. Lote bruto: $25/(25 \times 6{,}25) = 25/156{,}25 = 0{,}16$ exacto → **0,16 lotes**; verificación: $0{,}16 \times 156{,}25 = 25{,}00$ $ ✓ exacto.
6. Presupuesto: 20 $. Riesgo por lote: $2{,}50 \times 100 = 250$ $. Lote: $20/250 = 0{,}08$ lotes (8 onzas: 8 × 2,50 = 20 $ exactos ✓).
7. Margen 1:30: $6.480/30 = 216$ $; 1:500: ≈ 13 $. Apalancamiento real: $6.480/1.920 ≈ 3{,}4\times$. El riesgo NO cambia porque lo define el SL × valor pip × lote ($0{,}06 \times 32 \times 10 = 19{,}20$ $): el margen es solo la fianza congelada. Los 3 peligros reales: stop-out (liquidación forzada antes del SL si el margen usado es alto — regla: < 20-30 %), la invitación psicológica al oversizing, y el swap/costes que escalan con el nominal.
8. $R_{\text{efectiva}} = 1 + 0{,}70 \times 1 = 1{,}70$ % — banda $\rho \geq 0{,}7$ → suma completa conservadora: 2 % → **tope por motor alcanzado JUSTO: ACEPTAR** (sin margen). GBP/USD long después: $2 + 1 = 3$ % > tope 2 % → **RECHAZAR** ("no hay espacio de riesgo"). La correlación negativa no da crédito porque las coberturas rompen en pánico (las correlaciones convergen a +1 en crisis): el día que necesitas la anulación, no llega — y pagar dos spreads y dos swaps por una "protección" condicional es coste sin beneficio garantizado.
9. Nivel 0: 1 % por operación (sizing). Nivel 1: día ≤ −2 % → cerrar todo, fin del día. Nivel 2: 2 pérdidas consecutivas → pausa 30-60 min. Nivel 3: semana ≤ −4 % → fuera hasta la próxima semana + revisión. Nivel 4: mes ≤ −6 % → APAGADO TOTAL + protocolo (cerrar todo, cerrar plataforma, journal, no antes de 48 h + defensa, firma). Peor mes posible: ≈ −6 % (vs −26,5 % al 5 % sin frenos). Disparadores = números porque el cerebro estresado falsifica las evaluaciones cualitativas ("se ve raro", "me siento bien") — el dato no negocia. El freno diario trocea la racha: máximo 2 pérdidas por día → la racha de 6 necesita ≥ 3 días, cada uno con su pausa: la fricción temporal que el tilt no puede atravesar.
10. **Paso 1 — Freno (espacio diario):** el día marca −1 % → el margen hasta el disparo del freno 1 (−2 %) es exactamente UN 1 % (38,40 $ de presupuesto diario; ya gastados 19,20 $): solo cabe UNA operación estándar más, no dos. **Paso 2 — Cartera:** ambas señales comparten motor (ambas cortan USD, ρ 0,85 ≥ 0,7 → suma completa): tomar las dos valdría 2 % de motor (tope justo) — pero el freno ya limitó el día a 1 %: el freno manda sobre la cartera, es la capa superior. **Paso 3 — Sizing con capital ACTUAL:** $1.920 - 19{,}20 = 1.900{,}80$ $ → presupuesto $1.900{,}80\times 0{,}01 = 19{,}01$ $; con SL 32 pips y valor pip 10: $19{,}01/320 = 0{,}059$ → redondeo a la baja → **0,05 lotes** (riesgo real $0{,}05\times 320 = 16$ $ = 0{,}84$ %). **Veredicto:** UNA señal (la que tu checklist priorice), la otra **RECHAZADA** ("no hay espacio de riesgo" — diario y de motor). Si la elegida pierde: día ≈ −1,84 % — el freno 1 NO dispara (no llegó al −2 %) pero el presupuesto diario quedó agotado: la sesión termina. Si gana: el día queda ≈ −0,16 % y la segunda señal SÍ podría evaluarse (motor pasaría a 2 %, justo en tope). El orden freno → cartera → sizing no es negociable: cada capa limita a las que están debajo.

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| Preservación de capital | *capital preservation* | Prioridad nº 1 del negocio: proteger el inventario antes que buscar ganancia — el orden de preguntas invertido del profesional |
| Inventario del negocio | *trading capital as inventory* | El saldo de la cuenta como materia prima finita que se consume para producir: sin inventario no hay negocio |
| Drawdown | *drawdown* | Caída desde el máximo de la curva de capital; se mide desde el máximo, nunca desde el saldo inicial |
| Asimetría del drawdown | *drawdown asymmetry* | $R = \frac{d}{1-d}$: la recuperación necesaria crece más rápido que el daño (−50 % → +100 %); superlineal |
| Riesgo por operación | *risk per trade* | La única cantidad que el trader controla directamente: capital actual × %, ejecutada por la calculadora |
| Regla del 1 % | *1 % rule* | El estándar del programa: mantiene la peor racha esperable (−6 %) muy por debajo de la línea de emergencia (−15 %) |
| Position sizing | *position sizing* | $\text{lote} = \frac{\text{riesgo en \$}}{\text{SL pips} \times \text{valor pip}}$: el tamaño es una salida de la fórmula, no una decisión libre |
| Redondeo a la baja | *rounding down* | El lote final SIEMPRE hacia abajo al grano disponible: el riesgo real queda ≤ presupuesto, sin excepciones |
| Verificación inversa | *inverse verification* | Recalcular el riesgo con el lote final (lote × SL × valor pip) antes de enviar: la última línea defensiva |
| Valor del pip | *pip value* | Cuánto vale 1 pip por lote estándar: 10 $ en EUR/GBP/AUD (cuenta USD); USD/JPY ≈ 6,67 $ a 150; oro: 100 $ por 1,00 $ |
| Micro-lote | *micro lot* | 0,01 estándar = 0,10 $/pip en EUR/USD: la granularidad que permite respetar el 1 % en cuentas pequeñas |
| Margen | *margin* | La fianza congelada por el broker para mantener la posición: una línea contable, NO el riesgo |
| Apalancamiento del broker | *broker leverage* | Máximo nominal por unidad de margen (1:30...1:500): publicidad, no parámetro de riesgo |
| Apalancamiento real | *effective leverage* | Nominal ÷ capital: consecuencia del sizing (típico 2-4× con el 1 %); > 10× habitual = alarma |
| Stop-out | *stop out* | Liquidación forzada por margen antes del SL (gap, noticia, spread): el riesgo deja de ser el presupuesto |
| Correlación | *correlation* | ρ entre −1 y +1: cuánto se mueven juntas dos posiciones; se mide (30-90 días) o no existe |
| Riesgo efectivo de cartera | *effective portfolio risk* | $R_1 + \rho R_2$: dos operaciones de 1 % con ρ 0,85 son ~1,85 % — casi una sola apuesta |
| Tope por motor | *per-motor exposure cap* | Máx 2 % de riesgo efectivo sobre el mismo motor (divisa/activo): EUR/USD + GBP/USD largos = tope alcanzado |
| Daily Max Loss | *daily max loss* | Freno nivel 1: día ≤ −2 % → cerrar todo y terminar; el techo que trocea las rachas |
| Frenos en cascada | *cascading circuit breakers* | 1 % → −2 % día → 2 pérdidas → −4 % semana → −6 % mes: el techo que acota el peor mes en ≈ −6 % |
| Protocolo de apagado | *shutdown protocol* | Cerrar TODO → cerrar plataforma → journal + temperatura → no antes de 48 h + defensa → firma en frío |
| Tilt | *tilt / revenge trading* | "Una más para recuperar": el mecanismo de ruina que la cascada hace imposible por construcción |

## 🔗 Referencias

- [SYLLABUS.md § 6 — N3, Módulo 8](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — trazabilidad 003 · M4.5/M6.5 y 004 · M6.1-6.5; aportes propios: cartera y correlación (vacío 1), frenos en cascada
- [Módulo 7 · Construcción del Sistema](../mod-07-construccion-del-sistema/README.md) — anterior: el componente 9 se convierte aquí en procedimiento ejecutable
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — el caso maestro: el paso 9 (riesgo 1 %) hoy se convierte en calculadora
- [Hoja de 20 escenarios de la misión M-8](../../03-recursos/laboratorio/mision-m8-escenarios.md) — con clave de verificación oculta
- [scripts/core/position_sizing.py](../../../scripts/core/position_sizing.py) — la versión Python del programa: oráculo de verificación del lab
- [Módulo 9 · Backtesting, Journal y Validación](../mod-09-backtesting-journal-y-validacion/README.md) — el siguiente: la evidencia estadística que decide si tu sizing sobrevivió a 100 operaciones
