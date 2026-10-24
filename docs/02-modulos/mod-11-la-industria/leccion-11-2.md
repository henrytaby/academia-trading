# Lección 11.2 · Radar de estafas — las 5 que dominan el ecosistema minorista

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M11 · La Industria](README.md) |
| ⬅️ Anterior | [Lección 11.1 · Brokers de verdad](leccion-11-1.md) |
| ➡️ Siguiente | [Lección 11.3 · Prop firms: el negocio real](leccion-11-3.md) |

---

## Por qué importa

La industria del trading tiene dos economías superpuestas: la del mercado (tu negocio, con su esperanza medida) y la de la **extracción de principiantes** — un ecosistema completo diseñado para monetizar tu entusiasmo antes de que tu oficio exista. No es paranoia regulatoria: es la estructura del sector minorista, visible en las advertencias de los propios reguladores y en la aritmética de cada producto. Esta lección te arma el radar: las 5 estafas (o cuasi-estafas) que concentran la mayoría del daño — opciones binarias, bots de martingala, academias MLM, gurús con lujo alquilado e indicadores que repintan — cada una con su mecanismo exacto, su aritmética y sus señales de detección temprana. Y añade el instrumento transversal: el **protocolo de verificación regulatoria**, el mismo filtro binario del 11.1 aplicable a cualquier entidad (broker, academia, señal, fondo). La conexión con tu historia es directa: tu programa FIT-12 empezó auditando cursos reales con la misma lógica forense — si terminas con una sola idea: **en el ecosistema minorista, el producto más vendido no es el trading: es la esperanza de trading — y la esperanza se verifica con registros públicos, no con testimonios.**

## Concepto

**Estafa 1 — Opciones binarias: la esperanza negativa como producto.** Una binaria paga un % fijo si aciertas la dirección en un tiempo fijo (típicamente 70-85 %) y pierde el 100 % si fallas. La aritmética es demoledora incluso con el mejor trader del mundo:

$$E = p \times g - (1-p) \times 1 \qquad \text{con payout } g = 0{,}80 \text{ y } p = 0{,}50: \quad E = 0{,}5 \times 0{,}80 - 0{,}5 = -0{,}10$$

**−10 % por operación con acierto del 50 %** — y para empatar necesitas $p = \frac{1}{1+g} = \frac{1}{1{,}8} \approx 55{,}6$ % de acierto sostenido, sobre un instrumento de vencimientos ultracortos donde la varianza hace imposible esa medición honesta. Añade el conflicto estructural (en binarias el broker ES siempre tu contraparte: tu pérdida es literalmente su ganancia) y la historia regulatoria (prohibidas para minoristas en la Unión Europea y Reino Unido por los reguladores; múltiples acciones de fraude documentadas) — el veredicto del programa: **no es trading, es una máquina de extracción con gráfico encima.** La señal de detección: cualquier producto con payout fijo < 100 % y vencimiento fijo.

**Estafa 2 — Bots y señales de martingala.** La martingala duplica el tamaño tras cada pérdida para "recuperar todo con una ganancia": la aritmética parece infalible hasta la primera racha real. Con riesgo inicial r y duplicación, una racha de n pérdidas acumula $r(2^n - 1)$: 5 pérdidas a 0,5 % de inicio = 15,5 %; 8 pérdidas = 127,5 % — **quiebra garantizada antes de la racha esperada de tu propio WR** (con WR 40 %, la racha de 9 ya la calculaste como estructura normal). El paquete comercial: "un bot que gana todos los meses" (hasta el mes en que se quiebra: la curva del bot martingala es 11 meses de +2 % y uno de −100 % — la esperanza es negativa y la varianza asimétrica). Detección: curva de resultados sin drawdowns visibles + "señales" sin explicación + backtests sin costes ni rachas + la palabra "infalible" en cualquier variante.

**Estafa 3 — Academias MLM y "mentorías" piramidales.** El producto no es la educación: es el reclutamiento. Detección estructural: el plan de ingresos real (el que premia) paga por afiliar, no por enseñar; los "socios" te contactan con estilo de reclutamiento; la formación interna se compra con membresías recurrentes y "niveles". La prueba del programa: **un negocio educativo honesto cobra por su enseñanza y te deja ir**; un MLM disfrazado necesita que Traigas Amigos para que el modelo cierre — y su contenido (donde existe) es genérico o comprado. Señal acompañante: testimonios de ingresos por reclutamiento presentados como resultados de trading.

**Estafa 4 — El gurú con lujo alquilado.** Lamborghini alquilada, loft de lujo, screenshots de ganancias recortadas: el activo del gurú no es su trading (que probablemente no existe o pierde) — es su **audiencia**. El mecanismo: prueba social fabricada (lujo + depuración de comentarios + testimonios pagados) → audiencia → monetización (cursos, señales, "sala VIP", afiliación de brokers — donde su revenue share gana con tus pérdidas, 11.1). La verificación forense: pide UNA cuenta auditada de terceros (brokers no la tienen), contrasta la afirmación "X % de retorno" con la aritmética del WR y el R:B (si dice "gano el 90 % de las operaciones", pregunta el R:B: un 90 % con R:B 0,1 es perdedor: $E = 0{,}9 \times 0{,}1 - 0{,}1 \times 1 = -0{,}01$), y observa qué venden: si el producto es el "modo de vida", el trading es el disfraz.

**Estafa 5 — Indicadores que repintan.** Un indicador **repintante** (*repainting*) reescribe sus señales históricas a medida que llegan datos: el histograma de ayer muestra una señal perfecta que AYER nunca estuvo ahí. Es el look-ahead bias (9.1) como producto comercial: la demo muestra aciertos históricos que son ficción retroactiva. Detección operativa: (1) el test del replay — evalúa la señal EN tiempo simulado (Bar Replay) y compárala con lo que el indicador dibuja después: si cambió, repinta; (2) el test del screenshot — guarda la captura del momento de la señal y compárala 20 velas después; (3) la pregunta directa al vendedor: "¿su indicador recalcula valores pasados?" — si la respuesta no es un NO claro, es un sí.

**El protocolo de verificación regulatoria (universal, 4 pasos)** — el filtro binario que atraviesa todo el módulo:

1. **Identifica la entidad legal exacta** que cobrará tu dinero o abrirá tu cuenta (razón social + número de registro) — del contrato o el footer legal, no de la publicidad.
2. **Busca la entidad en el registro público del regulador** correspondiente a su jurisdicción — estado activo, alcance de la licencia, sanciones. El "supervisado por" ≠ "regulado por": la supervisión de registro no protege al cliente.
3. **Consulta las warn lists** (listas de alerta) del regulador y de los reguladores principales — las firmas denunciadas aparecen ahí antes de colapsar.
4. **Aplica el estándar del peor caso:** ¿qué pasa si esta entidad desaparece mañana? ¿Dónde están tus fondos (segregación), quién responde, hay fondo de compensación? Si la respuesta es "nada y nadie": la decisión es de riesgo de custodia, no de costes — y con regulación real disponible, no es una decisión que un negocio serio tome.

## Analogía

El mercado de medication falsificada. La OMS estima que una parte significativa de la medicación vendida en mercados sin control es falsificada — y la defensa de la farmacología no fue "enseñar a los pacientes a oler las pastillas": fue el **sistema de registro y trazabilidad** (laboratorios licenciados, lotes rastreables, farmacias reguladas, canales de denuncia). El trading minorista tiene el mismo mapa: la mayoría del "producto" que llega al principiante (bots milagro, gurús, binarias, MLM) es el equivalente de la pastilla falsificada — y tu defensa no es tu olfato: es el registro (verificación regulatoria), la trazabilidad (cuenta auditada, licencia, entidad legal) y el canal de denuncia (warn lists). El profesional no confía en su instinto con desconocidos en bata blanca: compra en la farmacia regulada, y con más razón cuando el vendedor grita que su producto "curo todo".

## Cómo se hace: auditar cualquier oferta en 10 minutos (la tarjeta del radar)

1. **La pregunta de la esperanza (60 s):** ¿cuál es la E matemática de este producto PARA MÍ? Payout fijo < 100 % → binaria → descartado. "Gana todo los meses sin drawdown" → martingala → descartado. Promesa de retorno % sin R:B ni WR auditables → gurú → descartado.
2. **La pregunta de la contraparte (60 s):** ¿quién gana dinero cuando yo pierdo? Si la respuesta es el vendedor (binarias, señales sin riesgo propio, revenue share de afiliados): conflicto estructural máximo — exige la evidencia doble (regulación + auditoría) o descarta.
3. **La verificación regulatoria (5 min):** los 4 pasos de arriba. Entity legal + registro público + warn lists + peor caso. Binario: pasa o no pasa.
4. **El test del replay/screenshot (3 min):** para cualquier producto con "señales históricas": ¿la señal sobrevive al tiempo simulado o se reescribe? El screenshot del momento es tu evidencia.
5. **La prueba de salida (1 min):** ¿puedo irme sin coste, sin humillación, sin "nivel bloqueado"? El negocio honesto te deja ir; el extractor necesita retenerte (membresías, niveles, "no abandones ahora que está por salir").

## Error común

**(1) "A mí no me pueden engañar, yo investigo."** El sesgo de punto ciego (10.5) aplicado a estafas: las víctimas de las estafas documentadas son desproporcionadamente gente segura de sí misma — el extractor está calibrado para venderle al que "investiga" (le da contenido técnico verosímil). La defensa es el protocolo, no la confianza en tu radar. **(2) Confundir "legal" con "bueno para ti".** Las binarias eran legales en muchas jurisdicciones cuando arruinaban minoristas; el MLM es legal; el gurú que vende humo suele estar en zona gris pero legal. La pregunta del programa no es "¿es legal?" sino "¿dónde está la esperanza y quién gana cuando yo pierdo?". **(3) Creer que los testimonios son evidencia.** Los testimonios son marketing filtrado: los perdedores no hacen video. La única evidencia de resultados es la cuenta auditada de terceros — y en el ecosistema minorista casi nadie la ofrece, que ya es un dato. **(4) Desestimar la lección "porque yo uso un broker conocido".** El radar no es solo para brokers: señales de Telegram, "gestores de cuentas" que piden tu password, academias con afiliación obligatoria, fondos que prometen 5 % mensual — la estafa 4 (gestión de terceros con promesa de retorno) es la que más dinero mueve al final: nunca entregues tu capital a un desconocido con promesa de rendimiento. **(5) No denunciar ni documentar.** Si te toca: la documentación (screenshots, contratos, pagos) alimenta las warn lists que protegen al siguiente — la misma ética de tu journal aplicada al ecosistema.

## Conexión cuantitativa

**Hacia 9.1:** las estafas 2 y 5 son sesgos de backtest empaquetados como producto: martingala = rachas ocultas; repintado = look-ahead — tu formación forense del N3 ES el antídoto. **Hacia 10.3:** la esperanza negativa de las binarias (−10 % por op) es el límite absoluto de lo que las avaricias pueden costar; el bot "infalible" es la avaricia #2 con automatización. **Hacia 11.1:** el protocolo de verificación regulatoria es el mismo filtro del pilar 1 del broker — una sola herramienta, todos los proveedores. **Hacia 11.3:** las prop firms ocupan la zona gris estructural del radar: no son estafas por definición, pero su modelo de ingresos merece el análisis completo de la siguiente lección — el embudo de fees que pocos quieren mirar.

---

## 🎯 Puntos clave

1. Las binarias tienen **esperanza negativa construida en el producto** (payout 80 % → necesitas 55,6 % de acierto solo para empatar) y el broker como contraparte fija — no es trading, es extracción con gráfico.
2. La martingala acumula $r(2^n-1)$: **el quiebra llega antes que la racha esperada de tu WR** — la curva "todo verde" es la firma visual del bot que un día pierde el 100 %.
3. MLM de trading, gurús con lujo alquilado e indicadores repintantes comparten mecanismo: **monetizar la audiencia, no el oficio** — la prueba de salida y el test del replay los delatan.
4. El **protocolo de verificación regulatoria** (entidad exacta → registro público → warn lists → peor caso) es binario y universal: aplica a brokers, academias, señales y fondos.
5. La evidencia de resultados es la **cuenta auditada de terceros** — testimonios, screenshots y lujo son marketing; tu pregunta forense es siempre: ¿dónde está la esperanza y quién gana cuando yo pierdo?

## 🔄 Autoevaluación rápida

1. Calcula el payout mínimo (g) para que una binaria con acierto 50 % no sea perdedora, y el acierto mínimo necesario con payout 0,75. ¿Por qué la segunda cifra es inalcanzable como medición honesta en vencimientos de 1 minuto?
2. Un bot con "12 meses de +2 % mensual sin drawdown" te ofrece su backtest. Identifica el mecanismo probable (con la fórmula de martingala), calcula qué racha quiebra el bot si arranca al 0,5 %, y formula las 2 preguntas del test de detección.
3. Un "mentor" afirma ganar el 88 % de sus operaciones. Con esa tasa, ¿qué R:B máximo puede tener sin ser perdedor? Usa WR* y demuestra con un R:B razonable (0,15) qué E obtiene. ¿Qué pides como única evidencia válida?

<details>
<summary>Ver respuestas</summary>

1. Empatar: $0{,}5 \times g = 0{,}5 \Rightarrow g = 1{,}0$ (payout 100 %, que ninguna binaria ofrece — su margen vive en el gap). Con payout 0,75: $p^* = 1/1{,}75 = 57{,}1$ %. Inalcanzable como medición honesta: a vencimientos de 1 minuto el ruido domina completamente la señal (tu σ individual es 6× la señal a escala H4 — a 60 s es órdenes de magnitud peor) y N medible sería de miles para un IC útil: nadie opera eso con journal honesto — y el broker B-Book puro garantiza el conflicto máximo.
2. Mecanismo: martingala — la curva sin drawdowns es la firma (cada "mes verde" financia la ilusión; el mes rojo no existe en el backtest porque está truncado). Quiebra del bot a 0,5 % de inicio: $0{,}5\%(2^n-1) \ge 100\% \Rightarrow 2^n \ge 201 \Rightarrow n = 8$ pérdidas seguidas quiebra la cuenta (127,5 % de exposición acumulada). Preguntas del test: (1) "¿cuál es la racha máxima de pérdidas simulada y qué tamaño tenía la posición 8?" (2) "¿puedo ver el equity curve con drawdowns reales y el log de posiciones?" — la ausencia de ambas respuestas es el veredicto.
3. Con WR 88 %: empate en $WR^* = 1/(\bar{R}+1) \Rightarrow \bar{R} = (1-WR^*)/WR^* = 0{,}12/0{,}88 = 0{,}136R$ — un R:B de solo 0,14 ya lo pone en equilibrio; cualquier R:B menor y es perdedor. Con R:B 0,15: $E = 0{,}88 \times 0{,}15 - 0{,}12 \times 1 = 0{,}132 - 0{,}12 = +0{,}012R$ — técnicamente positivo pero con costes (0,08R típico) es $0{,}88 \times 0{,}07 - 0{,}12 \times 1{,}08 = 0{,}0616 - 0{,}1296 = -0{,}068R$: perdedor neto. Evidencia única válida: cuenta auditada por un tercero independiente (verificación del broker/auditor con N y periodos completos) — si la ofrece "por privacidad", ya tienes el veredicto.

</details>
