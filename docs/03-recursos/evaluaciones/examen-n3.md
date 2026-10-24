# 🏆 Evaluación Nivel 3 · Gestión (M8–M10) — Examen de Graduación del Negocio

> [!WARNING]
> **Contenido educativo.** Este examen evalúa comprensión del programa FIT-12. No constituye asesoría financiera ni médica.

| Campo | Detalle |
|---|---|
| 🛡️ Nivel | 3 · Gestión — evaluación 🏆 de cierre del nivel |
| 📦 Cubre | M8 (Gestión del Riesgo) · M9 (Backtesting, Journal y Validación) · M10 (Psicotrading Científico) |
| 📋 Formato | 30 preguntas cerradas + 5 preguntas socráticas + entrevista de graduación con 3 casos reales (en vivo con el agente) |
| 🎯 Aprobado | **≥ 24/30 (80 %)** en el bloque cerrado |
| 📏 Modalidad | Sin apuntes, sin lecciones abiertas, con tu journal y tu calculadora CERRADOS. Clave oculta al final |
| ⏱️ Tiempo sugerido | 100–120 min, en una sola sesión |

---

## Instrucciones

1. **Prepara la sesión:** 100–120 min sin interrupciones. El N3 mide lo que ya vive en tu conducta — la única ayuda permitida es tu propio reporte M-9/M-10 para los números que TÚ mediste (se indica en cada pregunta).
2. **Los cálculos con número:** muestra el planteo (fórmula y sustitución). El número final sin procedimiento no acredita comprensión — y en este nivel cada fórmula es un freno de tu negocio.
3. **Autocorrección honesta:** corrige con la clave, cuenta aciertos y registra en `journal/evaluaciones.md`. En 20–23: repasa los bloques fallidos y repite en 7 días (versión B, orada por el agente). Por debajo de 20: el N3 no cierra — vuelve a las lecciones señaladas; es el mapa del programa, no un juicio sobre ti.
4. **Entrega previa (criterio de apertura):** este examen solo se rinde con los entregables N3 completos — checklist abajo. La teoría se examina después de que la práctica demostró que existe: 100 operaciones de evidencia y 10 sesiones de ejecución auditada.

## ✅ Checklist de entregables previos (criterio de apertura del examen)

- [ ] **100 backtests ciegas** registrados en el journal v1 con etiquetas en caliente (M9)
- [ ] **Reporte M-9 completo:** las 13 métricas + curva de capital + decisión de 3 vías + 3 conclusiones + changelog v1.2 o abstención firmada
- [ ] **Revisión semanal simulada** con el agente auditor (acta presentada, preguntas incómodas respondidas)
- [ ] **10 sesiones forward (demo)** con temperatura pre-sesión, diario emocional completo y etiquetado en caliente (M10)
- [ ] **Reporte M-10:** correlación temperatura→errores, tasa de contención, 2 miedos + 2 avaricias dominantes, 3 mejoras de ejecución
- [ ] **Quiz M10 ≥ 8/10**

---

## Bloque A · M8 — Gestión del Riesgo (10 preguntas)

**A1.** Preservación de capital: formula el principio de inventario del programa y explica por qué el CRO del programa audita el riesgo ANTES que la técnica (qué protege cada uno y qué es irreparable).

**A2.** Asimetría del drawdown: calcula lo que cuesta recuperar (a) −10 %, (b) −25 % y (c) −50 % de cuenta. Explica por qué la relación no es lineal y qué implicación tiene sobre el objetivo del negocio.

**A3.** Regla del 1 %: demuestra con la multiplicación de probabilidades por qué 10 pérdidas seguidas al 1 % (0,99¹⁰) dejan la cuenta en −9,6 % mientras que al 5 % (0,95¹⁰) dejan −40,1 %. ¿Cuánto exige recuperar cada uno?

**A4.** Position sizing: cuenta 10 000 $, SL de 40 pips en EUR/USD, riesgo 1 %. Calcula el valor del pip y el tamaño de posición (usa la fórmula universal del programa y declara los pasos).

**A5.** Apalancamiento real: un broker ofrece 1:500. Explica qué es y qué NO es ese número, cómo se calcula el margen usado y por qué el riesgo real de la operación no cambia con el apalancamiento (si el sizing sale de la calculadora).

**A6.** Riesgo de cartera: define correlación con un ejemplo de tu propio watchlist (2 pares u instrumentos), y explica los topes del programa (2 % motor / 3 % global) con la razón de cada número.

**A7.** Cascada de frenos: enuncia los 3 niveles del programa (−2 % / −4 % / −6 %), la acción de cada uno y por qué el apagado es un protocolo con pasos firmados y no una decisión del momento.

**A8.** Un trader usa 2 % de riesgo y pierde 8 seguidas (racha dentro de lo esperado para su WR). Calcula el drawdown (0,98⁸) y di qué nivel de la cascada se activa, qué actiona y por qué NO se "ajusta el riesgo" para recuperarlo.

**A9.** La calculadora y el oráculo: explica la doble verificación del programa (tu hoja vs `position_sizing.py`) — qué error tipo E4 detecta cada una y qué hace el trader cuando discrepan.

**A10.** Un día con 3 señales simultáneas correlacionadas +0,8. Con topes de cartera 2 %/3 %: ¿cuánto riesgo máximo despliegas en total y por qué la respuesta NO es "1 % cada una"? Formula la distribución concreta.

## Bloque B · M9 — Backtesting, Journal y Validación (10 preguntas)

**B1.** Epistemología: con la fórmula del IC 95 %, calcula el intervalo de un WR medido 40 % a N=30 y a N=100. ¿Qué decisión autoriza cada muestra y por qué el programa fija N=100 como mínimo estructural?

**B2.** Los 3 sesgos del backtest (supervivencia, data-mining, look-ahead): define cada uno con UNA aparición concreta en tu propio laboratorio de 100 operaciones y su antídoto operativo.

**B3.** Regla de la vela cerrada: explica qué contamina exactamente decidir con el high/low de una vela en formación, y formula la regla operativa que el programa exige (con la captura de evidencia).

**B4.** Setup válido: formula la definición operativa (componentes 1-8 verificables sí/no) y explica las 2 paradas legítimas del protocolo (N declarado, ruina simulada) — por qué existen y qué prohíben en caliente.

**B5.** Cálculo completo: 10 operaciones — 3 ganadoras de +2,2R, +1,9R, +2,5R; 7 perdedoras de −1R; coste 0,08R/op. Calcula WR, R:B medio, E bruto, E neto y PF neto. ¿En qué zona de la tabla de 3 vías cae y qué acción corresponde?

**B6.** WR de equilibrio neto: demuestra con la fórmula WR* = (1+c)/(R̄+1) por qué subir el coste de 0,05R a 0,12R con R:B 2,0 sube el requisito de WR de 35 % a 37,3 %. ¿Qué implica para los pares de spread alto?

**B7.** Rachas: con WR 40 % calcula la racha máxima esperada en 100 operaciones (fórmula ln) y el drawdown al 1 % (0,99ⁿ). Tu muestra mide racha 12: formula los 3 pasos de respuesta del programa y qué NO se hace.

**B8.** Forward testing: enumera los 4 huecos que el backtest no puede ver, con el mecanismo de medición de cada uno. ¿Qué significa "dentro de los intervalos" y qué hace el programa si el forward da WR 55 % con N=20?

**B9.** Taxonomía E0-E7: clasifica con etiqueta y justifica: (a) pérdida −1R con SL respetado y sizing correcto; (b) ganancia +2R sin setup; (c) SL movido "para darle aire"; (d) operación con la cascada en nivel 2 activa; (e) lote 0,10 en vez de 0,06. ¿Cuál es la más peligrosa y por qué (refuerzo dopaminérgico)?

**B10.** Ventana de modificación: enuncia las 4 condiciones acumulativas para tocar el sistema y la regla de UNA mejora. Tu reporte cierra con WR 36 % (IC [26,4 %, 45,6 %]), PF neto 1,19 y disparos 96/100: ¿qué decides HOY, qué entra al changelog y qué se entrena?

## Bloque C · M10 — Psicotrading Científico (10 preguntas)

**C1.** Neurobiología: narra la cascada del secuestro emocional en 4 pasos y explica por qué la defensa del programa es ambiental y anticipada (temperatura, detectores, checklist) y no volitiva ("ser fuerte").

**C2.** Los 5 miedos: enuméralos y emparéjalos con UNA etiqueta del journal que cada uno produce cuando se actúa sin protocolo (E3, deriva R, FOMO/E1, parálisis de no-disparos…). ¿Cuál es la raíz y qué la desarma?

**C3.** Mentalidad probabilística: explica los 5 axiomas con una frase cada uno, y por qué la serie (20+ operaciones) y no la operación individual es la unidad correcta de juicio. Conecta con la racha esperada (~9).

**C4.** Avaricias y geometría: entrada planeada 1,0820 (SL 1,0788, TP 1,0886). Calcula R:B y E bruta si el FOMO entra a 1,0840 (20 pips tarde) con WR 40 %. ¿A partir de cuántos pips de retraso la E bruta muere (R:B < 1,5)?

**C5.** Overtrading: tu sistema dispara ~3 señales/semana; ejecutas 8 con 5 de ruido (E ≈ −0,08R cada una). Calcula la esperanza semanal del sistema (3 × 0,16R) vs la real, y el porcentaje donado. ¿Qué dos topes escritos lo habrían cortado?

**C6.** Pérdida ≠ Error: dibuja la matriz 2×2 y explica con el refuerzo dopaminérgico por qué la ganancia fuera de plan es el error más peligroso. ¿Qué registra el journal y qué pregunta hace el acta semanal con esas filas?

**C7.** Sesgos: para cada caso, el sesgo y su antídoto estructural: (a) "el volumen bajo no importa, la estructura es clara"; (b) tras 6 ganadoras, subes el lote a ojo; (c) gestionas contra tu precio de entrada y no contra el plan; (d) entras con doble lote 4 min después de perder 1R.

**C8.** Estoicismo: con E +0,24R y σ ≈ 1,52R, calcula la σ del promedio a N=100 y compárala con la señal. ¿Qué implica para tu serenidad ante la racha de 9 y por qué la dicotomía del control es "la descripción literal de tu sistema"?

**C9.** Temperatura pre-sesión: enuncia las 3 dimensiones con su escala 0-3, los umbrales (verde/ámbar/rojo) y la consecuencia operativa de cada veredicto. ¿Por qué la regla decide y no la sensación — y qué sesión sería la más peligrosa de todas?

**C10.** Rutina: explica la ventana de ejecución (máx ~3 h en picos, ~10-12 decisiones) con sus dos razones (calidad de señal + decaencia del recurso), y el rol de la inacción estratégica en un sistema H1/H4 de 2-3 disparos/semana.

---

## Bloque Socrático · 5 preguntas + entrevista de graduación (en vivo con el agente)

> Sin apuntes. El agente evalúa TU razonamiento, no la memoria: puede pedirte derivar, invertir o aplicar tus propios números del journal.

**S1.** Defiende o refuta: *"Con mi WR medido 40 % ± 9,6 y costes reales, mi sistema podría estar perdiendo dinero y yo no lo sabría todavía."* Usa la aritmética completa (IC, WR* neto, N).

**S2.** Tu reporte M-9 queda ámbar (provisional) y tu mejor semana llega 3 semanas después con +8R. ¿Qué cambia en tu decisión de tamaño y por qué la varianza positiva tampoco es información? Trae tus números reales.

**S3.** Diseña el protocolo completo de un día rojo: temperatura ≤ 3 al despertar, pero "solo un vistazo al gráfico". ¿Qué dice cada capa del programa (temperatura, inacción estratégica, premeditatio, journal)?

**S4.** Explica a un trader amateur por qué su "sistema que nunca falla" (WR 85 % a 20 operaciones) puede ser un desastre: usa IC, R:B implicado y la trampa del sistema de martingala si la tiene.

**S5.** La regla de UNA mejora y la ventana mensual: tu acta identificó 4 problemas (deriva R, techo roto 2 veces, no-disparos por duda,spread alto en tu par). ¿Cuál eliges, por qué ese y qué pasa con los otros 3?

### 🎤 Entrevista de graduación — los 3 casos obligatorios (con tu journal en la mano)

| Caso | Lo que el agente evalúa |
|---|---|
| **Un tilt real** | Que puedas narrar una cadena E3/E4/E6 (o un casi) de tu journal con el mecanismo completo: estímulo → cascada → conducta → etiqueta → antídoto que instalaste después |
| **Un FOMO real** | El coste exacto de tu caso (geometría de la entrada tardía con TUS números) + tu tasa de contención medida + qué señal temprana te funciona |
| **Una pérdida en plan** | La narración sin drama de una E0 con su lugar en la serie: premeditatio, recibo de la varianza, y por qué esa fila NO es un error — el juicio de proceso funcionando en vivo |

**Criterio de graduación:** bloque cerrado ≥ 24/30 + socrática aprobada + los 3 casos presentados con journal real. Al aprobar: **N3 cerrado 🏆** — se abre N4 · Profesionalización con M11 · La Industria.

---

<details>
<summary>Ver clave de respuestas — Bloque A</summary>

1. El inventario es el activo irreparable: la técnica se re-aprende y el sistema se re-testea, pero la cuenta quebrada no opera. El CRO audita primero porque un error técnico cuesta esperanza y un error de riesgo cuesta EXISTENCIA — la asimetría (A2) es la razón.
2. Recuperar −10 % exige +11,1 % (1/0,90); −25 % exige +33,3 % (1/0,75); −50 % exige +100 % (1/0,50). No lineal: cada % adicional de caída exige cada vez más % de subida — la implicación: el objetivo del negocio no es maximizar ganancia, es SOBREVIVIR las rachas con inventario suficiente para que la esperanza trabaje.
3. 0,99¹⁰ = 0,904 → −9,6 %; recuperar: +10,6 %. 0,95¹⁰ = 0,599 → −40,1 %; recuperar: +67,0 %. La misma racha multiplica el daño 4× al quintuplicar el riesgo — y la recuperación exige 6× más esfuerzo. El 1 % convierte las rachas normales en mantenimiento; el 5 % las convierte en crisis.
4. Valor del pip: 0,0001 × 100 000 = 10 $/pip por lote estándar (EUR/USD cuenta en USD). Riesgo máx: 1 % × 10 000 = 100 $. Lotes = 100 / (40 × 10) = 0,25 lotes. Pasos declarados: riesgo en $ → pips de SL → valor de pip → tamaño. Verificación con el oráculo: `position_sizing.py`.
5. El apalancamiento es cuánto MARGEN exige el broker (posición/margen): 1:500 sobre 0,25 lotes (25 000 $) pide 50 $ de margen; 1:100 pide 250 $. Lo que NO cambia: el riesgo de la operación (SL 40 pips × 0,25 lote = 100 $ = 1 %) — el apalancamiento NO modifica el sizing, solo cuánto capital queda retenido (y por tanto el riesgo de liquidación si no hay margen). El error amateur: usar el apalancamiento para agrandar posiciones → es la avaricia #3 con broker cómplice.
6. Correlación +0,8 (ej.: EUR/USD y GBP/USD frente al dólar): se mueven juntos — operar los dos es casi duplicar la posición. Topes: 2 % por motor (línea temática/pares correlacionados) y 3 % global (todo el inventario expuesto a la vez) — números del programa para que ni el mejor escenario de racha quiebre la cuenta antes de que la esperanza trabaje.
7. Nivel 1 (−2 % de cartera en el día): parada del día — cerrar plataforma, no hay más entradas, journal. Nivel 2 (−4 % en la semana): revisión obligatoria con el agente + riesgo reducido la semana siguiente. Nivel 3 (−6 % en el mes): apagado total — no se opera hasta la revisión completa y la firma de reactivación. Protocolo con pasos porque en ese estado la PFC ya no decide: la regla decide por ti (el tilt de M10 es el caso de uso).
8. 0,98⁸ = 0,851 → −14,9 %. El día −2 % activó la parada diaria; la semana acumulada activa la revisión. NO se ajusta el riesgo "para recuperar" porque: (1) la racha es estructura esperada, no señal; (2) aumentar el riesgo para recuperar es martingala — sube la probabilidad del nivel 3; (3) la recuperación se produce con el MISMO 1 % y más tiempo: la aritmética de la asimetría (A2) pide proteger, no acelerar.
9. La hoja detecta el error de cálculo (aritmética, unidades); el oráculo detecta el error de procedimiento (fórmula mal memorizada, caso borde). Si discrepan: manda el oráculo (el Python del repo es la versión auditada), se anota la discrepancia y se corrige la hoja — nunca se opera con la cifra en disputa.
10. Con correlación +0,8 las tres señales son casi UNA posición: el tope motor (2 %) aplica al bloque — distribución ejemplo: 1 % la de mejor calidad + 0,5 % + 0,5 % en las otras, total 2 %, o solo la mejor con 1 %. Lo que está prohibido: 3 % (rompe el tope global) — la correlación convierte tres señales en una exposición: el programa lo mide con la suma ponderada por correlación.

</details>

<details>
<summary>Ver clave de respuestas — Bloque B</summary>

1. IC 95 % = ±1,96√(WR(1−WR)/N): a N=30, √(0,4×0,6/30) = 0,0894 → ±17,5 pp → [22,5 %, 57,5 %]: inútil para decidir (cruza el equilibrio por completo). A N=100: 0,049 → ±9,6 pp → [30,4 %, 49,6 %]: el peor caso razonable ya permite la decisión de 3 vías. N=100 es el punto donde el intervalo deja de cruzar ampliamente el equilibrio neto en sistemas razonables.
2. Supervivencia: borrar las filas incómodas del CSV ("esas no cuentan") → antídoto: todo entra, todo se etiqueta. Data-mining: probar variantes del TP y reportar la mejor (o ajustar a mitad de muestra) → antídoto: hipótesis, métricas y N declarados antes. Look-ahead: confirmar el nivel con el high/low de la vela en formación → antídoto: replay estricto + vela cerrada.
3. El high/low de la vela en formación no existe en vivo — usarlo para decidir infla las señales del backtest (cada "respeto del nivel" que en vivo era incierto aparece confirmado). Regla: toda condición se evalúa SOLO con velas cerradas; la vela de decisión se procesa al cierre y la captura se toma en ese instante — es la evidencia de que no hubo look-ahead.
4. Setup válido: TODAS las condiciones de los componentes 1-8 verificables sí/no en la vela de decisión; la duda es un no. Paradas: (1) N declarado alcanzado (la muestra termina, no se estira); (2) ruina simulada −15 % (la muestra se detiene antes si el drawdown toca la línea de emergencia de M8 — el daño máximo declarado). Ambas prohíben "una más para arreglar el resultado": eso es data-mining en vivo.
5. WR = 3/10 = 30 %. R̄ = (2,2+1,9+2,5)/3 = 2,2R. E bruto = 0,3 × 2,2 − 0,7 × 1 = 0,66 − 0,70 = **−0,04R**. E neto = 0,3 × 2,12 − 0,7 × 1,08 = 0,636 − 0,756 = **−0,12R**. PF neto = 0,636/0,756 = 0,84. Zona: **roja** (PF < 1,0 y E negativa) → no operar; volver al laboratorio del M7 — con N=10 solo es señal de sospecha, pero en la muestra real de 100 la decisión es la misma si los números se sostienen.
6. WR* = (1+c)/(R̄+1): c = 0,05 → 1,05/3,0 = 35,0 %; c = 0,12 → 1,12/3,0 = 37,3 %. Implicación: el coste sube el listón SIN cambiar tu sistema — en pares de spread alto (o sesiones líquidas mal elegidas), el mismo WR que "servía" queda por debajo del equilibrio: el coste medio por operación se audita SIEMPRE (9.3) y la elección de par/sesión es parte del sistema.
7. Racha esperada: ln(100)/ln(1/0,6) = 4,605/0,511 ≈ **9**; DD al 1 %: 0,99⁹ = 0,9135 → −8,6 %. Ante racha 12 (P puntual 0,6¹² ≈ 0,2 %): (1) verificar integridad del dato (registro, costes, régimen); (2) comparar con la distribución — con ~90 ventanas en 100 ops no es imposible: sospecha documentada, no pánico; (3) decidir en la ventana mensual con evidencia. NO: cambiar reglas en caliente (data-mining en vivo), subir tamaño "para recuperar" (martingala) ni abandonar el sistema por la racha que ya sabías que venía.
8. Los 4 huecos: spread vivo (medido op por op vs el 0,08R estimado), slippage del SL (diferencia precio SL vs ejecución), tu ejecución (disparos debidos vs ejecutados + deriva R), infraestructura (incidentes contados). "Dentro de los intervalos": el WR forward cae dentro del IC del backtest y el PF neto cerca del medido. WR 55 % con N=20 (IC ±22 pp): NO se celebra ni se escala — la muestra no autoriza nada; se sigue midiendo y se revisa si cambió la selección de señales.
9. (a) **E0** — coste estadístico, no error. (b) **E1** — sin setup (y la más peligrosa: el premio refuerza el atajo). (c) **E3** — SL manipulado. (d) **E6** — freno ignorado. (e) **E4** — sizing fuera de presupuesto. La más peligrosa: la (b) — la ganancia fuera de plan premia el circuito equivocado (10.4): el dolor corrige, el premio instala.
10. Condiciones acumulativas: fin de mes (ventana) + evidencia con N suficiente + UNA modificación por vez + re-test planificado (50-100 backtests). Con WR 36 %, IC [26,4 %, 45,6 %] (cruza el equilibrio 34,8 %), PF 1,19 y disparos 96/100: la decisión HOY es seguir provisional (0,25-0,5 %), sin modificación estructural (el IC cruza el equilibrio: la evidencia no autoriza) — se entrena la UNA mejora de ejecución (los 4 disparos debidos no ejecutados: revisar el bloqueo), y al changelog entra solo la decisión documentada de continuar midiendo. Los "problemas" restantes van al diario de dudas con fecha, no al sistema.

</details>

<details>
<summary>Ver clave de respuestas — Bloque C</summary>

1. Cascada: estímulo → amígdala (ms, pre-consciente) → descarga hormonal (adrenalina/cortisol: visión de túnel) → PFC degradada (memoria, riesgo, horizonte colapsados). Volitiva no funciona porque el secuestro ocurre ANTES del análisis consciente — el conocimiento no alcanza a intervenir. Ambiental y anticipada: la temperatura impide la sesión imposible, los detectores cortan en los primeros segundos (etiquetación verbal recluta PFC), el checklist bloquea en la fase final.
2. Equivocarse → parálisis/no-disparos (miedo raíz; lo desarma la etiqueta E0: pérdida en plan = coste). Perder dinero → E3 (cerrar antes del SL). Quedarse fuera → E1/E2 (FOMO, chasing). Devolver ganancias → deriva R (cerrar el ganador temprano). Lo desconocido → sobre-preparación/congelación ante noticias.
3. Axiomas: cualquier cosa puede pasar · no necesitas adivinar para ganar (la E es de la serie) · dentro de la ventaja el orden es aleatorio · la ventaja es probabilidad mayor, no predicción · cada momento es único. Serie como unidad: una operación es ruido (σ 1,52R vs señal 0,24R); la racha de 9 es estructura esperada — juzgar la serie libera de leer el azar como retrato propio.
4. Entrada 1,0840: SL = 52 pips, TP = 46 pips → R:B = 0,88; E = 0,4 × 0,88 − 0,6 = **−0,25R bruto**. Muerte de la E bruta: (66−d)/(32+d) < 1,5 → d > 7,2 → **~8 pips**. La degradación es en curva, no lineal.
5. Sistema: 3 × 0,16R = **+0,48R**/semana. Real: 3 × 0,16 + 5 × (−0,08) = 0,48 − 0,40 = **+0,08R** — donado: el 83 % de la esperanza. Topes que lo cortan: el techo de operaciones declarado (pre-compromiso de 10.3) y el techo de decisiones de la ventana (10.7: ~10-12 activas → cierre).
6. Matriz: en plan/gana (construye) · en plan/pierde (E0, coste) · fuera de plan/pierde (dolor que corrige) · **fuera de plan/gana (premio al atajo: el refuerzo dopaminérgico instala la conducta que quiebra)**. El journal la destaca (E1/E2/E4/E5 con marca) y el acta pregunta: *"¿cuánto me costará a largo plazo este premio?"*
7. (a) Confirmación → checklist sí/no + caso contrario escrito. (b) Exceso de confianza → calculadora (tamaño fijo) + WR histórico a la vista. (c) Anclaje → gestión por estructura, SL inmodificable. (d) Revancha → timer de 90 s + cascada de M8.
8. σ promedio = 1,52/√100 = 0,152R vs señal 0,24R: a N=100 el ruido aún es comparable a la señal — la muestra ACOTA, no certifica (es el IC de 9.1 en otra ropa). Serenidad: la racha de 9 ya estaba en el guion (P(n) = 0,6ⁿ); ni ella ni la racha buena hablan de ti. Dicotomía: tu columna izquierda (checklist, sizing, SL, registro, revisión) ES literalmente tu sistema; la derecha (precio, rachas, resultados) es clima.
9. Dimensiones: sueño (<5h=0 … ≥7h regular=3), estrés (crisis=0 … bajo=3), apego (recuperar=0 … proceso puro=3). Umbrales: 7-9 verde → plan completo (1 %); 4-6 ámbar → mitad de riesgo (0,5 %) y máx 2 disparos; 0-3 rojo → no se opera. La regla decide porque la sensación mintió siempre que la PFC estaba degradada (10.1). La sesión más peligrosa: la que "se siente genial" con sueño rojo — entusiasmo + PFC cansada = el cóctel del overtrading (la temperatura la captura: sueño 0-1 la manda a ámbar/rojo pese a las ganas).
10. Ventana: máx ~3 h en los picos (solapamiento de sesiones de tu tabla 2.5) y ~10-12 decisiones activas. Razones: (1) calidad — fuera de picos el ruido crece y tu sistema no dispara mejor por mirar más; (2) recurso — la fatiga decisional degrada la calidad sin sentirse (se mide con el contador). Inacción estratégica: con 2-3 disparos/semana, estar fuera es la recomendación del sistema el resto del tiempo — protege la esperanza ya fabricada y se registra igual que una operación.

</details>

<details>
<summary>Ver clave orientativa — Bloque Socrático</summary>

1. SÍ — defensa correcta: [30,4 %, 49,6 %] contiene el WR de equilibrio neto 34,8 %: el peor caso razonable sigue siendo perdedor neto. Por eso la decisión de 3 vías permite rojo/ámbar y el tamaño provisional (0,25-0,5 %) acota el daño mientras la muestra crece: la honestidad estadística ES la gestión del riesgo.
2. La varianza positiva tampoco es información (misma σ): el tamaño no cambia por una semana buena — solo por la evidencia con N y la ventana de modificación. El tamaño sigue en provisional (0,25-0,5 %) hasta el re-test o el cierre del IC; el acta registra la semana sin adjetivos.
3. Protocolo: temperatura ≤ 3 → rojo → no se opera (la decisión YA está tomada por la regla); el "vistazo" se sustituye por observación sin plataforma o repaso; la premeditatio ya anticipó la frustración del día rojo; el journal registra el día igualmente (los días rojos también son datos: la correlación del reporte M-10 los necesita). Inacción estratégica: la posición correcta hoy es no estar.
4. WR 85 % a N=20 tiene IC ±15,7 pp: el WR real podría ser 69 % — o 100 %, o 70 %… y el R:B implicado de los sistemas de WR alto suele ser pésimo (E = 0,85×0,3 − 0,15×3 = −0,20R si pierde 3R cada vez que pierde): una sola pérdida devora diez ganancias. Con martingala, peor: la esperanza se disfraza de ruina garantizada por la asimetría del drawdown (A2) — el IC pequeño y la colita de pérdidas enormes.
5. Se elige la UNA con mayor impacto medible y menor riesgo de regression (típicamente la deriva R o los no-disparos por duda — las de ejecución); las otras 3 van al diario de dudas con fecha y entran a la SIGUIENTE ventana si la primera se estabiliza. La regla existe porque 4 cambios simultáneos destruyen la atribución: nunca sabrás cuál funcionó.

</details>
