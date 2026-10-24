# Lección 6.5 · Volumen y perfil — el registro del interés real

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 40–55 min de estudio |
| 🧱 Módulo | [M6 · Indicadores y Confluencias](README.md) |
| ⬅️ Anterior | [Lección 6.4 · Momentum y osciladores](leccion-6-4.md) |
| ➡️ Siguiente | [Lección 6.6 · Fibonacci, Elliott y armónicos](leccion-6-6.md) |

---

## Por qué importa

Todas las herramientas anteriores derivan del precio. El volumen aporta la única dimensión *adicional* del panel: cuántos contratos se cruzaron — el interés ejecutado detrás de cada movimiento. Un impulso con volumen y un impulso sin volumen son eventos distintos aunque la vela sea idéntica: el primero participó gente con convicción, el segundo fue un hueco de liquidez momentáneo. Para tu caso maestro, el volumen responde la pregunta operativa más fina del pullback: *"¿la caída hacia mi zona era vendedores reales o simplemente ausencia de compradores?"* — y esa respuesta cambia la calidad asignada a la operación. Esta lección también presenta las dos herramientas de la familia: el VWAP (el promedio real de ejecución de las instituciones) y el Volume Profile (el mapa de dónde se construyó el interés), con una salvedad de honestidad que en FX spot es obligatoria.

## Concepto

**Volumen.** Número de contratos/unidades negociados en la vela. Es un registro, no una fuerza: no "empuja" el precio — documenta cuánta gente estuvo de acuerdo en transaccionar a esos precios. Usos del programa:

1. **Validar impulsos:** un BOS con volumen 1,5–2× la media de 20 velas firmó participación real; un BOS de bajo volumen es candidato a falsa ruptura (5.2).
2. **Leer pullbacks:** retroceso con volumen *decreciente* = ausencia de convicción vendedora (pullback saludable); retroceso con volumen creciente = distribución posible: exigir más al gatillo.
3. **Marcar agotamiento:** clímax de volumen en extremos (vela gigante, volumen récord, precio sin avanzar) = transferencia masiva, candidata a ser techo/suelo de episodio.

**VWAP (*volume weighted average price*).** El precio promedio de la sesión ponderado por volumen:

$$VWAP = \frac{\sum p_i \, q_i}{\sum q_i}$$

donde $p_i$ es el precio de cada transacción (o de cada tramo) y $q_i$ su volumen. Por qué importa: es el **coste promedio real de ejecución** — el precio al que "se promedió" la sesión. Las instituciones grandes se miden contra él (¿compré mejor o peor que el mercado?) y sus algoritmos de ejecución lo usan como benchmark: parte del flujo institucional está *programado* para operar cerca del VWAP. Efecto operativo: el precio tiende a re-visitar el VWAP durante la sesión (los ejecutores que se quedaron fuera completan órdenes), y el VWAP actúa como referencia dinámica intradía: por encima y sostenido, sesión compradora; por debajo, vendedora. Ejemplo numérico con 3 tramos: $(1{,}0815 \times 1\,200) + (1{,}0818 \times 800) + (1{,}0822 \times 1\,500) = 3\,786{,}54$; dividido entre $3\,500$ contratos → $VWAP \approx 1{,}0819$.

**Volume Profile horizontal.** Las velas dibujan el precio contra el tiempo; el Volume Profile dibuja el **volumen contra el precio**: un histograma horizontal que muestra dónde se negoció más y menos durante el periodo. Sus piezas: **POC** (*point of control*) = el nivel de máximo volumen — el precio más "acordado" del periodo, imán natural y zona de reacción; **HVN** (*high volume nodes*) = estaciones de interés construido (zonas donde el precio pasa, se frena y reacciona); **LVN** (*low volume nodes*) = huecos de desacuerdo (niveles que el precio atravesó sin negociar: franjas de viaje rápido). Uso del programa: HVN/POC como zonas de interés con confluencia estructural (capa 2 del top-down); LVN como tramos donde el stop viaja rápido y el TP intermedio no conviene.

**La salvedad FX (obligatoria).** El spot de divisas es descentralizado: no existe cinta central. Lo que tu plataforma llama "volumen" es el **tick volume** de TU bróker (número de cambios de precio en su propio feed): un proxy honesto del interés global, correlacionado pero no idéntico al volumen real. Regla del programa: usarlo como *tendencia relativa* (¿este impulso tiene el doble de ticks que la media?) y no como *cifra absoluta* ("se cruzaron 1 500 lotes" no lo sabes). En futuros regulados (CME) y en acciones, el volumen es real — ahí la familia opera a plena potencia.

## Analogía

La asistencia al concierto. El precio es la lista de canciones que sonaron; el volumen es cuánta gente estaba en la sala cada noche. Un "hit" con la sala vacía (impulso sin volumen) engaña menos que un hit con la sala llena. El VWAP es el precio promedio de la entrada que pagó el público esa noche — y los promotores con entradas sin vender las rematan cerca de ese promedio. El Volume Profile es el mapa de butacas: sabes qué sectores se llenaron siempre (HVN), cuál fue EL sector del año (POC) y qué pasillo casi nadie cruzó (LVN) — cuando la multitud se mueve, cruzará rápido los pasillos vacíos y se agolpará en los sectores conocidos.

## Cómo se hace: el volumen sobre el caso maestro

Los mismos tres instantes de la [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) *(ilustrativo)*, EUR/USD H4, leyendo el tick volume de la plataforma:

1. **Vela del BOS (ruptura de 1,0860):** volumen ≈ 1,8× la media de 20 velas → participación real detrás del quiebre: el BOS suma una evidencia (no se rompe estructura con la sala vacía — la etiqueta 5.2 queda reforzada).
2. **Pullback a la zona 1,0820–1,0824:** volumen ≈ 0,6× la media y decreciente vela a vela → la caída fue *ausencia de compradores*, no ataque vendedor organizado. La zona de la receta cobra calidad: el precio volvió al descuento y nadie quiso venderlo en serio.
3. **Barrida a 1,0792:** pico breve de volumen (la subasta de liquidación del pool, 5.3) seguido del giro: el patrón volumen-pico + reversión que la lección 5.3 ya describía por estructura — ahora con el registro de interés delante.
4. **VWAP del día:** ≈ 1,0819. El precio del pullback (1,0820–1,0824) volvió EXACTAMENTE al VWAP de la sesión y reaccionó: confluencia zona-estructural + benchmark institucional. En la ejecución real intradía (M15/M5), ese era un gatillo de calidad superior al simple toque de zona.
5. **Volume Profile del último tramo H4:** el POC del periodo ≈ 1,0812, justo bajo la zona de entrada; la franja 1,0840–1,0860 como HVN (estación del impulso) y el hueco 1,0760–1,0740 como LVN. Lectura: el TP 1,0886 requería atravesar el HVN — objetivo realista porque el impulso ya demostró capacidad; y el SL 1,0788 se ejecutaba antes del LVN 1,0760–1,0740 (el hueco de viaje rápido quedaba más allá del stop, no encima) — coherente con la auditoría ATR de 6.3.

## Error común

**(1) Creer que el volumen empuja.** El volumen documenta; no fuerza. "Subió con mucho volumen, tiene que seguir" es una correlación débil, no un mecanismo. **(2) Tomar el tick volume de FX como volumen real.** Es el feed de tu bróker: usar cifras absolutas ("millones de lotes") en spot es contaminar el análisis con un dato que no existe. Tendencia relativa sí, contabilidad no. **(3) Usar el VWAP del marco equivocado.** El VWAP es una métrica de SESIÓN (se reinicia cada día); el "VWAP semanal" es otra herramienta con otra lectura — el programa usa el diario, y solo en ejecución intradía. **(4) Operar el POC como nivel mágico.** El POC es el nivel más "acordado" del pasado: imán probable, no pared. Sin confluencia estructural (M5), es solo estadística bonita.

## Conexión cuantitativa

El volumen es la única pieza del dashboard que puede auditar la *participación* detrás de cada etiqueta del M5 — y por eso es el candidato natural al tercer asiento del panel (6.8) cuando el gatillo del estudiante es intradía. Registro auditable desde hoy: en cada trade del journal, columna `vol-mult` = volumen de la vela del gatillo ÷ media 20. Hipótesis de trabajo *(heurística, se auditará en M9)*: los BOS de tu muestra con `vol-mult ≥ 1,5` rinden mejor R:B realizado que los de `vol-mult < 1,0` — si TU dataset lo confirma, el volumen entra al dashboard con tu evidencia propia, que vale más que cualquier curso; si TU dataset lo desmiente, lo sacas y también ganas: un medidor menos, un panel más limpio, una regla menos que discutir.

---

## 🎯 Puntos clave

1. El volumen es registro de interés ejecutado, no fuerza: valida impulsos, lee pullbacks, marca clímax.
2. $VWAP = \sum(p_i q_i)/\sum q_i$: el promedio real de ejecución de la sesión; benchmark institucional y referencia intradía.
3. Volume Profile: volumen contra precio — POC como imán, HVN como estaciones, LVN como pasillos rápidos.
4. Salvedad FX: el "volumen" de spot es tick volume de tu bróker — tendencia relativa sí, cifra absoluta no.
5. El patrón operativo de calidad: impulso con volumen alto + pullback con volumen decreciente + regreso al VWAP.
6. En el dashboard, el volumen audita participación: su métrica (`vol-mult`) es registrable desde hoy.

## 🔄 Autoevaluación rápida

1. Calcula el VWAP de: (1,0820 × 900) + (1,0823 × 600) + (1,0817 × 1 500). ¿Qué precio promedió la sesión?
2. Un BOS rompe 1,0860 con volumen 0,9× la media. ¿Qué etiqueta pondría el programa al quiebre y cómo cambia la calidad de la zona 1,0820–1,0824?
3. ¿Por qué el programa no acepta "se negociaron 2 400 lotes" como dato en EUR/USD spot, pero sí "el impulso tenía 1,8× los ticks de la media"?

<details>
<summary>Ver respuestas</summary>

1. $900 + 600 + 1\,500 = 3\,000$ contratos; $1{,}0820 \times 900 = 973{,}8$; $1{,}0823 \times 600 = 649{,}38$; $1{,}0817 \times 1\,500 = 1\,622{,}55$; suma $= 3\,245{,}73$; $3\,245{,}73 / 3\,000 \approx 1{,}0819$. La sesión se promedió a ≈ 1,0819 — esa es la referencia institucional del día.
2. BOS de bajo volumen: candidato a falsa ruptura (liquidity grab, 5.2) hasta confirmación posterior — la etiqueta sería "BOS débil / en observación". La zona 1,0820–1,0824 pierde una confluencia (participación en el impulso) y el gatillo exige confirmación extra; con volumen 1,8× la zona cobraba calidad directamente.
3. Porque en spot descentralizado no existe cinta central: esos 2 400 lotes son solo lo que vio TU bróker — cifra absoluta no verificable. En cambio, el múltiplo 1,8× compara el feed del mismo bróker consigo mismo: como tendencia relativa es reproducible y auditable en tu journal — mide conducta, no contabilidad.

</details>
