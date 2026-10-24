# 🏆 Evaluación Nivel 2 · Técnica (M5–M7) — Examen Estructural

> [!WARNING]
> **Contenido educativo.** Este examen evalúa comprensión del programa FIT-12. No constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 2 · Técnica — evaluación 🏆 de cierre |
| 📦 Cubre | M5 (Estructura y Liquidez) · M6 (Indicadores y Confluencias) · M7 (Construcción del Sistema) |
| 📋 Formato | 30 preguntas cerradas + 5 preguntas socráticas (en vivo con el agente) |
| 🎯 Aprobado | **≥ 24/30 (80 %)** en el bloque cerrado |
| 📏 Modalidad | Sin apuntes, sin lecciones abiertas. Clave de respuestas oculta al final |
| ⏱️ Tiempo sugerido | 90–120 min, en una sola sesión |

---

## Instrucciones

1. **Prepara la sesión:** 90–120 min sin interrupciones, sin lecciones abiertas, sin glosario. El examen mide lo que ya vive en ti, no lo que puedes consultar.
2. **Responde con tus palabras:** una línea exacta al texto puntúa igual que una explicación propia correcta — pero en la socrática lo que se defiende es TU razonamiento.
3. **Los cálculos con número:** muestra el planteo (fórmula y sustitución). El número final sin procedimiento no acredita comprensión.
4. **Autocorrección honesta:** corrige con la clave, cuenta aciertos y registra en `journal/evaluaciones.md`. En 20–23: repasa los bloques fallidos y repite en 7 días (versión B, orada por el agente). Por debajo de 20: el N2 no cierra — vuelve a las lecciones señaladas; es el mapa del programa, no un juicio sobre ti.
5. **Entrega previa:** este examen solo se rinde con los **entregables N2 completos** (checklist abajo): M-5 (15 análisis), M-6 (informe comparativo), M-7 (Sistema v1.0 aprobado + 30 repeticiones). La teoría se examina después de que la práctica demostró que existe.

## ✅ Checklist de entregables previos (criterio de apertura del examen)

- [ ] 15 análisis estructurales M-5 archivados (con ≥ 5 "no hay operación" legítimos)
- [ ] Dashboard de confluencias M6 definido por escrito y probado en 50 episodios
- [ ] Informe comparativo M-6 entregado (3 herramientas, fallos clasificados por tipo)
- [ ] **Sistema v1.0 aprobado por el agente auditor** (10 componentes + test del clon + checklist de robustez)
- [ ] 30 repeticiones M-7 con reporte de métricas (WR, R:B, PF, Max DD, rachas) y veredicto por la matriz

---

## Bloque A · M5 — Estructura de Mercado y Liquidez (10 preguntas)

**A1.** Define la secuencia de tendencia alcista (HH/HL), la frase de sesgo que produce, y qué es el test de consecuencia que la valida.

**A2.** BOS vs CHoCH: definición exacta de cada uno, el rol de la **confirmación por cierre**, y la implicación operativa de cada uno (continuación vs alerta de reversión).

**A3.** Mapa unificado PA ↔ SMC: ¿por qué el programa unificó la nomenclatura (vacío D1)? Da dos equivalencias concretas (fenómeno PA clásico ↔ término SMC).

**A4.** Pools de liquidez: describe la anatomía de una barrida en 3 pasos y explica por qué el precio "va a buscar" los niveles obvios (qué hay acumulado detrás y quién lo necesita).

**A5.** Equal highs / equal lows: qué son, qué acumulan y bajo qué condición su barrida es operable (¿contra qué sesgo es trampa?).

**A6.** FVG: define el hueco de 3 velas, sus dos usos (imán y zona de entrada), qué es la mitigación y por qué "la primera visita es la que vale".

**A7.** Order blocks con honestidad de evidencia: qué es **verificable** (y cómo se observa) y qué es **hipótesis no demostrada**. Enumera los 4 filtros que el programa exige antes de operar un OB.

**A8.** Top-down de 3 capas: qué se decide en cada capa y qué producto escrito deja. ¿Qué riesgos concretos aparecen si se salta la capa 1 (sesgo)?

**A9.** Caso numérico *(ilustrativo, el caso maestro)*: EUR/USD H4 — low 1,0745 → HL 1,0798 → quiebre sobre 1,0860 → HH 1,0884 → pullback a 1,0820–1,0824 con perforación hasta 1,0792 y recuperación. Etiqueta cada evento con el vocabulario del módulo (estructura, BOS, pool, barrida), di qué hacía operable la zona 1,0820–1,0824 y cuál era su invalidación exacta.

**A10.** Desplazamiento (*displacement*): definición, qué firma deja en el gráfico, y su relación con el FVG y el BOS (por qué los tres suelen aparecer juntos).

## Bloque B · M6 — Indicadores y Confluencias (10 preguntas)

**B1.** Con $I = f(P)$ y el argumento del arbitraje: explica por qué ningún indicador es "adelantado" y qué se vende realmente como "leading".

**B2.** SMA vs EMA: diferencia de construcción, fórmula del suavizado (α = 2/(N+1)), y el rol de cada media en el sistema 20/50/200.

**B3.** ATR: fórmula del rango verdadero (TR) y del ATR. Audita el SL del caso maestro: 32 pips con ATR(14) H4 ≈ 21 pips — ¿cuántos ATR es y por qué el rango sano es 1,0–2,0?

**B4.** Bollinger ±2σ: qué mide el squeeze y qué anticipa (sin prometer). ¿Por qué "tocó la banda inferior = compro" falla en tendencia fuerte (walking the bands)?

**B5.** RSI: fórmula completa. Si la media de ganancias es 1,5× la de pérdidas, ¿cuál es el RSI? ¿Por qué RSI 70 no es señal de venta en tendencia?

**B6.** Divergencia regular alcista: definición exacta, por qué es el uso más honesto del oscilador, y qué información operativa tiene "no hay divergencia" en el HH 1,0884 del caso.

**B7.** VWAP: fórmula, por qué les importa a las instituciones, y cálculo: (1,0815 × 1 200) + (1,0818 × 800) + (1,0822 × 1 500). ¿Qué salvedad tiene el volumen en FX spot?

**B8.** Volume Profile: qué mide, qué son el POC y las zonas HVN/LVN, y en qué se diferencia de leer el volumen de las barras.

**B9.** Fibonacci como contexto: calcula los retrocesos 50 % y 61,8 % del swing 1,0798 → 1,0884. ¿En qué porcentaje quedó la zona 1,0820–1,0824 y qué enseña ese desenlace sobre el Fib como nivel?

**B10.** Radar de fiabilidad: los 3 tiers y los 4 test. Clasifica: (a) un indicador de fases lunares con backtest "93 %"; (b) el VWAP; (c) un indicador que repinta; (d) el MACD. Cierra con la regla del máximo 3 y su requisito de independencia entre familias.

## Bloque C · M7 — Construcción del Sistema (10 preguntas)

**C1.** Filosofía, estrategia, sistema: la pregunta que responde cada capa y el test del clon. ¿Por qué "veo una vela en soporte" no es un sistema?

**C2.** Enumera los 10 componentes del sistema y marca los **tres que más suelen faltar** en los planes de los traders que fracasan — con el error concreto que produce cada hueco.

**C3.** Los 4 arquetipos: firma típica WR × R:B y modo de muerte de cada uno. ¿Cuáles son los 4 filtros de elección y por qué la invalidación estructural es la más importante?

**C4.** Esperanza: calcula E con WR 45 % y R:B 1:2, el WR de equilibrio de esa columna, y el resultado esperado de 50 operaciones al 1 % de riesgo *(planteo y números)*.

**C5.** Profit Factor: fórmula y cálculo para WR 45 % con $\overline{W}$ = 2,1R. ¿En qué franja queda y qué significa?

**C6.** Rachas: probabilidad de 5 pérdidas seguidas con WR 45 %, y racha esperable máxima en 30 operaciones con WR 40 % *(fórmulas y números)*.

**C7.** Asimetría del drawdown: con riesgo 1 %, ¿cuánto exige recuperar un valle de −6 %? ¿Y un valle de −30 % (racha de 6 al 5 %)? ¿De qué dos fórmulas sale el 1 % del programa?

**C8.** Robustez: los 4 criterios. Calcula la inflación aproximada del resultado en muestra con k = 10 reglas y N = 30 — ¿qué le pasa al número del replay y a qué se parece el ajuste excesivo de reglas?

**C9.** Intervalo de confianza: con N = 30 y WR medido 40 %, calcula el intervalo al 95 %. ¿Qué decisión estructural prohíbe ese intervalo y dónde se toma?

**C10.** TU Sistema v1.0: ¿qué arquetipo elegiste, cuál es su invalidación exacta, qué fila de la matriz declaraste antes de la misión, y qué harás cuando aparezca la racha esperable?

## 🗣️ Entrevista Socrática (en vivo con el agente — 5 preguntas abiertas)

**S1.** **Tu filosofía en el banquillo:** enuncia tu tesis del porqué de la ventaja y la evidencia que la refutaría. El agente jugará abogado del diablo: ¿qué pasaría con tu sistema en un mercado sin acumulación obvia de stops?

**S2.** **Top-down en vivo:** el agente abre un gráfico en Bar Replay en un punto ciego. Tienes 5 minutos: aplica tu protocolo de 3 capas en voz alta y emite veredicto — "hay setup" (con zona, gatillo y stop) o "no hay operación" (con la regla que lo veta). Se evalúa el proceso, no el desenlace.

**S3.** **Tu misión en la matriz:** el agente te da tu reporte M-7. Localiza tu celda, calcula tu E y defiende el veredicto: ¿avanza, se ajusta UN componente, o se archiva? ¿Qué NO se toca y por qué?

**S4.** **La racha:** llevas 5 pérdidas seguidas y el gráfico "claramente se está recuperando". ¿Qué dice tu tabla de rachas, qué dice tu presupuesto de DD, y qué hace tu protocolo? Se evalúa la respuesta vacunada (7.5), no el optimismo.

**S5.** **Candidato vs validado:** ¿qué diferencia hay entre tu v1.0 probado en 30 repeticiones y un sistema validado? ¿Qué secuencia exacta (M9, forward, real micro) convierte uno en otro, y qué evidencia te haría archivar todo?

## Resultado y registro

| Ítem | Resultado |
|---|---|
| Bloque A (M5) | __ / 10 |
| Bloque B (M6) | __ / 10 |
| Bloque C (M7) | __ / 10 |
| **Total cerrado** | **__ / 30** — aprobado con ≥ 24 |
| Entrevista socrática | ☐ aprobada — observaciones: ______ |
| Entregables previos | ☐ checklist completa (5/5) |

- **≥ 24 + socrática aprobada:** N2 🏆 cerrado. El Sistema v1.0 entra al N3: M8 le da presupuesto formal de riesgo, M9 lo valida con 100 backtests y forward.
- **20–23:** repite en 7 días (versión B) tras repasar los bloques fallidos.
- **< 20:** el N2 no cierra — vuelve a las lecciones que la clave te señale.

---

<details><summary>🔑 Clave de respuestas — abrir SOLO tras rendir</summary>

### Bloque A · M5

- **A1.** Tendencia alcista = progresión de **máximos cada vez más altos (HH) y mínimos cada vez más altos (HL)**, con impulsos y pullbacks que respetan la estructura. Frase de sesgo: *"solo buscar largos mientras la secuencia HH/HL viva"*. Test de consecuencia: la tendencia está viva **mientras el último HL resista** — el primer cierre decidido bajo el HL no es "pullback profundo": es la advertencia estructural que exige reevaluar todo el sesgo.
- **A2.** **BOS** (break of structure): quiebre del último swing relevante **a favor** de la tendencia activa — confirma continuación (en el caso, el quiebre sobre 1,0860). **CHoCH** (change of character): primer quiebre **contra** la secuencia — alerta de posible reversión, aún no reversión. Confirmación por cierre: la vela debe **cerrar** fuera del nivel en el marco de análisis — el cierre implica que la urgencia sobrevivió al período; la mecha que perfora y vuelve es barrida (5.3), no quiebre. Implicación: BOS = buscar continuación con el sesgo; CHoCH = suspender el sesgo, esperar confirmación del nuevo régimen antes de operar contra la tendencia vieja.
- **A3.** Porque el mercado enseña el mismo fenómeno con dos vocabularios en guerra, y el estudiante que lee ambas escuelas cree que son conceptos distintos (vacío D1 de coherencia). Equivalencias: la "ruptura de nivel" del PA clásico = el **BOS/CHoCH** del SMC (mismo quiebre de estructura); el "origen del impulso" clásico = el **order block** SMC (misma vela de partida del desplazamiento); el "falso quiebre" clásico = la **barrida de liquidez** (liquidity grab) SMC. Un vocabulario, dos dialectos: el programa elige uno y traduce el otro.
- **A4.** (1) El precio se aproxima a un nivel obvio (mínimo/maximo visible, EQH/EQL) con una fila de stops/órdenes pendientes acumuladas detrás; (2) lo atraviesa detonando esa fila — los stops son órdenes market que generan el "combustible"; (3) el participante grande llena tamaño con esa liquidez y el precio revierte o continúa con desplazamiento. El precio "va a buscar" los obvios porque ahí es donde la contraparte está concentrada: es el único lugar donde una orden grande puede llenarse sin mover el precio por sí sola. El retail pone los stops en el lugar visible → el lugar visible es el inventario.
- **A5.** Dos o más máximos/mínimos **casi idénticos**: el mercado "falla" el nivel dos veces y el retail añade sus stops justo detrás del segundo. Acumulan liquidez doble. Operables cuando la barrida va **a favor del sesgo del marco superior** (barrida de EQH en tendencia bajista = llenado para continuar bajando; barrida de EQH en tendencia alcista = trampa para cortos tardíos que luego alimenta el HH). Sin sesgo, la barrida de EQH es moneda al aire: por eso el M5 exige sesgo ANTES de etiquetar.
- **A6.** FVG = hueco donde nadie negoció: **high de la vela 1 < low de la vela 3** (alcista) — el desplazamiento fue tan violento que saltó una franja de precios. Usos: **imán** (el precio tiende a volver a "rebalancear" la franja incompleta) y **zona** (la visita del hueco es el punto de entrada con estructura alrededor). Mitigación = la visita que ejecuta las órdenes pendientes de la franja. La primera visita es la que vale: la zona se construyó con órdenes sin ejecutar; tras la primera visita el almacén está servido — la segunda visita encuentra la fama, no la munición (misma lógica del gradiente de M3.3).
- **A7.** Verificable: que el OB sea la **última vela contraria antes de un desplazamiento con BOS**, que deje FVG, que el volumen de la pierna sea anómalo, que la zona coincida con liquidez — todo se observa. Hipótesis no demostrada: que detrás haya "órdenes institucionales sin ejecutar" concretas — es la narrativa explicativa, plausible pero no auditable desde un gráfico retail. Los 4 filtros del programa: (1) origen de desplazamiento con BOS, (2) FVG asociado, (3) contexto de sesgo a favor, (4) confluencia con liquidez — sin los cuatro, la vela contraria es solo una vela.
- **A8.** Capa 1 (D1/H4): **sesgo** — dirección probabilística por escrito (frase de tendencia/rango + régimen). Capa 2 (H1/M15): **zonas** — dónde estaría interesado el negocio (OB, FVG, pools, niveles). Capa 3 (M15/M5): **gatillo** — el evento exacto de entrada. Productos escritos: frase de sesgo, mapa de zonas con invalidación, checklist de gatillo. Saltar la capa 1: operar zonas sin dirección = moneda al aire con comisiones; el sesgo es lo que convierte una zona en setup y no en dibujo bonito — y es lo que dice "no hay operación" cuando falta.
- **A9.** Etiquetas: low 1,0745 = origen del impulso; HL 1,0798 = swing relevante validado; quiebre sobre 1,0860 = **BOS** alcista (continuación confirmada); mínimo visible bajo 1,0798 = **pool** de stops del retail; perforación a 1,0792 = **barrida** del pool (llenado institucional); recuperación del nivel = confirmación de que la barrida sirvió a la continuación. La zona 1,0820–1,0824 era operable porque confluían: OB/origen del impulso + FVG + sesgo alcista activo + pool cercano como gatillo de barrida. Invalidación exacta: **cierre M15/H1 bajo el HL 1,0798** (o bajo el extremo de la barrida con margen ATR): CHoCH — la idea de continuación muere ahí, no "cuando se vea mal".
- **A10.** Desplazamiento = impulso violento, con cuerpos grandes y mínima superposición, que **rompe estructura y deja FVG**. Firma: velas consecutivas direccionales sin retroceso interno. Relación: es el síntoma de urgencia en la subasta (alguien necesita llenar YA); el BOS es su consecuencia medible y el FVG su cicatriz — por eso el OB se define con desplazamiento + BOS + FVG: los tres son el mismo evento visto desde la vela, la estructura y el hueco.

### Bloque B · M6

- **B1.** $I = f(P)$: el indicador es función del precio ya ocurrido — no puede contener información que el precio no tenga, porque la deriva de él. Si existiera un predictor verificable, su uso con capital movería el precio hasta neutralizar la ventaja (arbitraje): las ventajas públicas y persistentes se autodestruyen. Lo que se vende como "leading" es mayor **sensibilidad**: reacciona antes Y falla antes — más captaciones en el backtest del vendedor, más falsos disparos en vivo.
- **B2.** SMA promedia N cierres por igual; EMA pondera más lo reciente con $$EMA_t = \alpha P_t + (1-\alpha)EMA_{t-1}, \quad \alpha = \frac{2}{N+1}$$. Roles: **EMA 200** = filtro macro de régimen (el caso: ≈ 1,0712 creciente → solo largos); **EMA 50** = régimen intermedio (≈ 1,0771 — la tendencia de swing sigue viva); **EMA 20** = zona dinámica de referencia en pullbacks (≈ 1,0806). El precio de la operación (1,0820) estaba sobre las tres: el filtro no vetaba.
- **B3.** $$TR = \max(H-L,\ |H-C_{prev}|,\ |L-C_{prev}|)$$ y ATR = media móvil del TR. $32/21 ≈ 1{,}52$ ATR — dentro del rango sano 1,0–2,0: bajo 1,0 la respiración normal del marco caza el stop (estructural pero demasiado justo); sobre 2,0 el TP se aleja sin mejorar el motivo. La estructura fija el SL; el ATR **audita** que sea habitable.
- **B4.** Squeeze = contracción simultánea de ambas bandas = σ mínima = volatilidad comprimida; anticipa **expansión** (fase del ciclo M3), nunca dirección. En tendencia fuerte el precio "camina" sobre la banda (walking the bands): tocarla es la **medición de la fuerza** del régimen, no una señal de giro — vender ahí es operar contra el régimen usando el medidor del régimen como oráculo.
- **B5.** $$RSI = 100 - \frac{100}{1+RS}, \quad RS = \overline{G}/\overline{P}$$. Con RS = 1,5: $RSI = 100 - 100/2{,}5 = \mathbf{60}$. RSI 70 no es venta en tendencia porque en régimen alcista fuerte el momentum **es** el régimen: el RSI puede vivir > 70 muchas velas (el HH 1,0884 del caso se marcó con RSI ≈ 68). La venta la autoriza la estructura (CHoCH), nunca el nivel del oscilador.
- **B6.** Divergencia regular alcista: el precio marca un **LL** pero el oscilador marca un low menos profundo — la pierna bajista pierde velocidad de forma medible. Es el uso más honesto porque mide **desaceleración** (dato) sin predecir el giro (interpretación), y obliga a la confirmación de estructura. "No hay divergencia" en el HH 1,0884 = el impulso sigue acelerando → información operativa: el pullback es continuación probable, no trampa — sesgo intacto.
- **B7.** $$VWAP = \frac{\sum p_i q_i}{\sum q_i}$$ — el precio promedio **real de ejecución** de la sesión: es donde se promediaron las instituciones, y por eso funciona como benchmark (quien compró muy por encima del VWAP sabe que pagó caro). Cálculo: $(1{,}0815 \times 1200) + (1{,}0818 \times 800) + (1{,}0822 \times 1500) = 3{,}786{,}54$ → $3{,}786{,}54/3{,}500 ≈ \mathbf{1{,}0819}$ — la zona de la receta volvió exactamente al benchmark del día. Salvedad FX: el spot es descentralizado — el volumen visible es el feed del bróker (proxy del tick volume), no el global: se usa con humildad.
- **B8.** El Volume Profile apila el volumen **por nivel de precio** (horizontal): muestra dónde se construyó el interés en el periodo. POC = el nivel con más volumen (el precio más "acordado"); HVN = zonas de alto volumen (aceptación — zonas de interés institucional); LVN = bajo volumen (rechazo — el precio las atraviesa rápido). Diferencia: el volumen de barras dice "cuánto se movió en esa vela" (temporal); el perfil dice "a QUÉ precios se acordó" (espacial) — conecta directamente con las zonas del M5.
- **B9.** Swing = $1{,}0884 - 1{,}0798 = 86$ pips. 50 % → $1{,}0798 + 43 = \mathbf{1{,}0841}$; 61,8 % → $1{,}0798 + 53{,}1 ≈ \mathbf{1{,}0831}$. La zona de la receta (1,0820–1,0824) quedó en el **70–74 %** del retroceso — más profunda que la golden zone: el Fib solo no la habría marcado; la estructura (OB + FVG + pool) sí. Enseñanza: el Fib es **contexto de descuento** (a qué profundidad es razonable esperar interés), no nivel de entrada — y la barrida a 1,0792 perforó el 100 %, algo que el Fib no explica pero la liquidez del M5 sí.
- **B10.** Tiers: **A** defendibles con mecanismo claro; **B** contextuales (miden algo real, uso condicionado); **C** marketing/pseudociencia. Test: ¿qué propiedad mide? ¿de qué deriva? ¿es auditable? ¿aporta lo que tus 3 no miden? (a) fases lunares → **C** (exógeno, sin mecanismo en la subasta; el "93 %" sin muestra ni regla es marketing con número); (b) VWAP → **A** con salvedad FX (benchmark de ejecución real, mecanismo claro); (c) repintado → **descalificado por construcción** (inauditable); (d) MACD → **B** (mide velocidad; redundante si ya hay RSI). Máximo 3 con UNA pieza por familia (tendencia/volatilidad/momentum/volumen): dos medidores de la misma familia son el mismo dato dicho dos veces — redundancia, no confluencia.

### Bloque C · M7

- **C1.** Filosofía = por qué existe la ventaja (tesis falsable). Estrategia = cómo se captura (fenómeno + régimen + arquetipo). Sistema = cuándo exactamente y cuánto (reglas cerradas, 10 componentes). Test del clon: dos desconocidos con tu documento ante el mismo gráfico ejecutan la misma operación. "Vela en soporte" falla las tres: sin mecanismo (¿por qué ese soporte?), sin fenómeno definido (¿qué vela? ¿qué marco?), y sin clonabilidad (cada lector vería algo distinto) — es subjetividad con formato.
- **C2.** (1) Mercado y vehículo, (2) marcos temporales, (3) régimen, (4) setup/arquetipo, (5) gatillo de entrada, (6) stop inicial, (7) salidas, (8) gestión post-entrada, (9) riesgo y tamaño, (10) filtros, horario y registro. Los tres que más faltan: **régimen** (→ pullbacks comprados en tendencia rota), **gestión post-entrada** (→ stop movido "porque se estaba recuperando"), **horario** (→ operativa nocturna con spreads y fatiga) — cada hueco es una puerta de la improvisación.
- **C3.** Ruptura+retesteo (~35-45 % × ≥ 1:2,5; muere en falsa ruptura) · Pullback en tendencia (~40-55 % × 1:2; muere en CHoCH real) · Reversión en rango (~55-70 % × ~1:0,8; muere en la ruptura del rango) · Barrida+giro (~35-50 % × ≥ 1:2,5; muere cuando el barrido era la primera pierna de la aceleración). Filtros: filosofía, mercado, invalidación, costes. La invalidación es la más importante porque sin evento estructural objetivo no hay stop defendible — y sin stop defendible no hay R definible ni esperanza calculable: toda la arquitectura del negocio cuelga de que "la idea muere" sea un hecho verificable.
- **C4.** $E = 0{,}45 \times 2 - 0{,}55 \times 1 = 0{,}90 - 0{,}55 = +0{,}35R$. Breakeven de la columna 1:2: $1/(1+2) = 33{,}3$ % — vive 11,7 puntos por encima del filo. 50 operaciones al 1 %: $0{,}35 \times 50 = +17{,}5R$ → **≈ +17,5 % del capital** *(ilustrativo, sin componer)*.
- **C5.** $PF = \frac{WR \times \overline{W}}{(1-WR) \times L} = \frac{0{,}45 \times 2{,}1}{0{,}55 \times 1} = \frac{0{,}945}{0{,}55} ≈ \mathbf{1{,}72}$ — franja del negocio sano (objetivo ≥ 1,5): por cada $ perdido genera 1,72 $ de ganancia; margen suficiente para absorber costes (−0,06/0,1R) y deterioro de ejecución sin caer al breakeven.
- **C6.** $P(5) = 0{,}55^5 = 0{,}0503 ≈ \mathbf{5{,}0}$ %. Racha esperable en N=30 con WR 40 %: $\ln 30 / \ln(1/0{,}6) = 3{,}401/0{,}511 ≈ 6{,}7$ → **6-7 pérdidas seguidas** son el comportamiento esperado de una máquina sana en la misión — la racha no invalida el sistema: la tabla lo predijo.
- **C7.** −6 % exige $1/0{,}94 - 1 ≈ \mathbf{+6{,}4}$ %. −30 % exige $1/0{,}70 - 1 ≈ \mathbf{+43}$ % — el valle que ya no se recupera en la práctica. El 1 % sale de multiplicar dos fórmulas: la racha esperable ($\ln N / \ln\frac{1}{1-WR}$ ≈ 6-7 con WR 40 %) por la asimetría de recuperación — el riesgo por operación se elige para que el valle ESPERABLE sea sobrevivible, no para "sentirse conservador".
- **C8.** (1) escrito y clonable, (2) componentes completos, (3) E plausible con margen para costes, (4) simple y probado fuera de muestra. Inflación ≈ $\sqrt{k/N} = \sqrt{10/30} ≈ 0{,}58$ → **~58 %** de inflación esperable del resultado en muestra: un replay que "mide" +0,3R puede deber +0,19R o menos fuera. Ajustar más reglas al pasado es memorizar las respuestas del examen anterior: perfecto en el histórico, suspendido en el futuro.
- **C9.** $\pm 1{,}96\sqrt{0{,}4 \times 0{,}6/30} = \pm 1{,}96 \times 0{,}0894 ≈ \pm \mathbf{17{,}5}$ % → el WR verdadero está entre ~22 % y ~58 %. Prohíbe decisiones estructurales con N=30: cambiar de arquetipo, abandonar o "validar" el sistema — ninguna es defendible con una horquilla que cubre de la ruina a la excelencia. La decisión se toma en M9 con N ≥ 100 (intervalo ≈ ±9,8 %) más el forward de demo.
- **C10.** *(Respuesta personal — el auditor la verifica contra tu `journal/sistema-v1.md` y `journal/mision-m7.md`.)* Debe contener: arquetipo declarado (el candidato del programa es el híbrido 2+4), invalidación estructural exacta (p. ej. cierre bajo el HL/bajo el extremo de barrida), fila declarada ANTES de la misión (WR esperado y R:B mínimo), y el protocolo de racha: consultar la tabla, no cambiar nada, mantener tamaño, registrar — la respuesta vacunada de 7.5.

### Socráticas — criterio del evaluador

- **S1:** se aprueba si la tesis tiene mecanismo, es falsable y el estudiante nombra la evidencia refutadora sin parpadear (p. ej. "si el precio dejara de barrer pools sistemáticamente en 200 episodios, la filosofía de llenado muere y el sistema con ella").
- **S2:** se evalúa el PROCESO — capas en orden, producto escrito de cada una, veredicto con regla citada. Un "hay setup" sin gatillo y stop exactos vale menos que un "no hay operación" bien argumentado.
- **S3:** el veredicto debe salir de la matriz (celda localizada, E calculada) y respetar la regla de congelamiento: ajustes solo tras M9, UN componente, hipótesis nueva con muestra nueva.
- **S4:** se aprueba la respuesta que cita tabla de rachas + presupuesto de DD + protocolo por escrito; se suspende la que cita "intuición", "el mercado avisa" o promete cambiar algo a mitad de muestra.
- **S5:** candidato ≠ validado: faltan los 100 backtests a ciegas (M9), el forward en demo con datos vivos y, solo después, real micro. Se archiva todo si la evidencia acumulada contradice la fila declarada — y se archiva CON su registro, nunca en silencio.

</details>
