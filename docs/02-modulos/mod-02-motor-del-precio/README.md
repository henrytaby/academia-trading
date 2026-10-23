# Módulo 2 · El Motor del Precio

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada en este repositorio constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 1 · Fundamentos |
| 📦 Módulo | 2 de 12 (FIT-12) |
| 🔬 Trazabilidad | 003 · M1.4–1.5 · 004 · M2.4 · **Aporte propio:** calendario macro aplicado (ventanas rojas en hora local) y correlación intermercados con matices de régimen (vacíos 4 y 5 del informe) |
| ⏱️ Duración estimada | 4 h de teoría + 3–4 h de laboratorio/misión/quiz |
| 📋 Estado | 🟢 Publicado (Sprint 2) |

---

## 🎯 Objetivo del Módulo

Entender **por qué se mueve el precio** — no solo dónde mirar. Al terminar este módulo sabrás cómo nace cada tick en la subasta (bid/ask, taker/maker, spread como costo), qué motor genera tendencias y rangos (oferta/demanda y desequilibrio), por qué los grandes operadores necesitan y "cazan" liquidez, cómo funcionan las sesiones del forex con TU huso horario (UTC-4), qué personalidad tiene cada mercado que vas a operar (EUR/USD, oro, índices) y qué hace el calendario macro con todos ellos a la vez. Este módulo existe porque el Módulo 3 te enseñará a leer el gráfico, pero un gráfico bien leído por quien no entiende la subasta que lo genera es un mapa de un territorio que no conoce: aquí pones el motor antes del mapa.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 2.1 | [La mecánica de subasta](leccion-2-1.md) | Bid/ask, taker vs maker, cómo nace cada tick; el spread como peaje y el viaje asimétrico del trade | 35–45 min |
| 2.2 | [Oferta y demanda](leccion-2-2.md) | Urgencia (no "número de compradores"), desequilibrio → expansión, equilibrio → rango; oferta/demanda residual como futuras zonas | 40–50 min |
| 2.3 | [Liquidez](leccion-2-3.md) | Qué es, quién la provee, por qué los stops del retail son su materia prima y qué es una barrida; defensa: SL por estructura | 40–50 min |
| 2.4 | [Forex y sus sesiones](leccion-2-4.md) | Pares, pips, lotes; las 4 sesiones convertidas a hora Bolivia; el ciclo diario y tu ventana de oro | 45–60 min |
| 2.5 | [Personalidad de cada mercado](leccion-2-5.md) | Las 5 dimensiones de auditoría; perfiles de EUR/USD, XAU/USD e índices; tamaño recalculado por mercado; concentración vs coleccionismo | 40–50 min |
| 2.6 | [Calendario macro e intermercados](leccion-2-6.md) | NFP/IPC/FOMC en tu hora; la cadena causal tasas → DXY → oro/acciones/cripto; la regla macro de formación (ventanas rojas) | 45–60 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`): repaso activo → lección → quiz rápido → misión. Intenta responder las autoevaluaciones ANTES de abrir las respuestas.
>
> **Puente con la [Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md):** los pasos 0–2 (cuenta demo, tour de plataforma, observación de sesiones) son seguros hacerlos YA — esta lección te da justo el vocabulario (sesiones, spread, lote) que esos pasos piden. Los pasos 3–11 esperan al Módulo 4.

## 🧪 Laboratorio · Tu Reloj de Sesiones y tu Mapa Macro

**Materiales:** tu auditoría personal de M1 (bloques de tiempo y energía), un calendario económico con filtro de impacto y huso configurable, hoja de papel o plantilla digital.

**Procedimiento paso a paso:**

1. **Construye tu reloj de sesiones.** Dibuja un eje horizontal de 00:00 a 24:00 **en hora Bolivia**. Marca encima las 4 sesiones (Sídney, Tokio, Londres, NY) con sus rangos aproximados, y sombrea el solapamiento Londres–NY (≈ 08:00–12:00). Recuerda: los horarios se mueven ±1 h con el horario de verano del norte — deja una nota que lo recuerde. Encima del reloj, marca tus bloques reales de energía alta de la auditoría M-1. La intersección de ambos es tu **ventana operativa candidata**: escríbela en una frase.
2. **Cruza con el calendario.** Abre el calendario económico de la semana ENTRANTE, filtra alto impacto (USD y la moneda de tu par principal) y anota los **5 primeros eventos** con: día, nombre, consenso, **hora Bolivia**. Marca cada ventana roja (15 min antes/después; FOMC 30/30).
3. **Pega el reloj y el mapa donde los veas.** Captura o fotografía ambos y déjalos junto a tu pantalla de estudio. Este es el "semáforo" de la Lección 2.6 en tu pared.
4. **Prueba de fuego (opcional, 20 min):** el día del mayor evento de la semana, a las H-20 minutos abre el gráfico de tu par y observa el spread en la ventana roja (ensánchalo visualmente con la ventana de orden). Verás en vivo el peaje ×10 de la Lección 2.6. **Sin operar.**

**Entregable:** `journal/reloj-sesiones-m2.md` con: el reloj dibujado (o su descripción), la ventana operativa candidata justificada en 3 frases, y la tabla de 5 eventos macro de la semana con horas Bolivia.

## 🎯 Misión

> [!IMPORTANT] Misión M-2 · Observación Pura de 3 Sesiones
> **Objetivo:** fabricar el reconocimiento en vivo del ciclo diario (Asia → Londres → NY) y del comportamiento del spread/volumen — sin dinero, sin órdenes, sin la tentación.
> **Entregable:** `journal/observacion-m2.md` con 3 sesiones completas del solapamiento Londres–NY (≈ 08:00–12:00 Bolivia) observadas en días distintos, cada una con la ficha de abajo.
> **Criterio de aceptación:** 3 fichas completas en 3 días distintos + una comparación final entre las tres sesiones (¿qué se repite? ¿qué fue distinto? ¿cuál fue la hora de mayor energía?).
> **Etiqueta en journal:** `mision-2-observacion` · **Tiempo estimado:** 3 × 2–4 h en vivo (puede fraccionarse por tramos de 1 h con nota de tramos).
> **Regla de oro:** **cero órdenes.** Esta misión se aprueba por la calidad de la observación, no por ningún resultado — es el entrenamiento de "estar en el mercado sin estar en él".

**Ficha por sesión (copiar por cada día):**

```text
Sesión #N — fecha — EUR/USD (o tu par principal)
1. Apertura de Londres (≈ 09:00 Bolivia): ¿qué hizo el precio en la primera hora?
   (rompió el rango asiático / lo barrió y volvió / siguió dormido)
2. Spread: ¿cómo era a las 08:55 vs a las 10:30? (ventana de orden, sin enviar nada)
3. Eventos macro del día: ¿cuál salió y qué hizo el precio en los 15 min siguientes?
4. Volumen/energía: ¿en qué hora hubo velas más grandes y más rápidas?
5. Si tuvieras que operar HOY: ¿en qué tramo habrías tenido la mejor relación
   señal/ruido? (observación, no recomendación)
6. Estado del régimen (pre-M3, en palabras): ¿día de tendencia clara, de rango, o mixto?
```

## ✅ Evaluación / Criterio de Graduación

- **Misión M-2 completa:** 3 fichas + comparación, con la regla de cero órdenes respetada (si enviaste alguna orden "solo para probar", reinicia la misión: la tentación es parte del material de estudio).
- **Quiz de graduación:** 10 preguntas (subasta, liquidez, sesiones, macro) con ≥ 8/10.
- **Laboratorio entregado:** reloj de sesiones + 5 eventos con hora Bolivia en `journal/`.
- Al aprobar todo: el módulo queda marcado ✅ en el README raíz y se abre el [Módulo 3 · Anatomía del Gráfico](../mod-01-negocio-trading/README.md) (se publica en el Sprint 3).

## 📝 Quiz de Graduación

1. Completa: compras al ______, vendes al ______, y la diferencia entre ambos es el ______.
2. ¿Quién "paga" el spread y quién lo "cobra"? Nómbralos con sus dos roles (urgencia vs paciencia).
3. ¿Por qué la frase "el precio sube porque hay más compradores que vendedores" es imposible? ¿Cuál es la explicación correcta?
4. Compras EUR/USD con SL de 30 pips y TP de 30 pips, con un spread de 2 pips. ¿Cuántos pips debe recorrer el mercado hacia arriba para darte el TP y hacia abajo para darte el SL? ¿Qué se llama este efecto?
5. Define liquidez en una frase y explica por qué el conjunto de stops del retail bajo un mínimo obvio ES liquidez para un institucional.
6. Son las 13:00 UTC de un martes. ¿Qué hora es en Bolivia y qué sesión(es) están activas? ¿Cómo se llama ese tramo y por qué importa?
7. Operas 0,05 lotes de EUR/USD y el precio recorre 40 pips a tu favor. ¿Cuántos dólares ganaste? (1 lote = 10 $/pip)
8. ¿Cuándo sale el NFP (día y hora del Este) y qué le pasa al spread dentro de la ventana roja del evento?
9. El IPC de EE. UU. sorprende al alza. Recorre la cadena: ¿qué hacen típicamente los rendimientos de los bonos, el DXY y el oro? ¿Con qué palabra se califica todo el pronóstico?
10. Enuncia la regla macro de formación (ventanas rojas) completa: cuánto antes/después de un evento de alto impacto, y qué se hace con una posición abierta si el evento es inminente.

<details>
<summary>Ver clave de respuestas</summary>

1. Ask · bid · spread. (Compras al ask, vendes al bid: el peaje de entrada/salida.)
2. Paga el **taker** (urgencia, orden market, consume el libro); lo cobra el **maker** (paciencia, orden limit, provee liquidez). Toda transacción tiene al menos un taker y al menos un maker.
3. En toda transacción hay exactamente un comprador y un vendedor — nunca puede haber "más" de unos que de otros. Lo correcto: el precio sube cuando los compradores son **más urgentes** (dispuestos a pagar asks más altos, Lección 2.1) y los vendedores suben precios o retiran órdenes.
4. Arriba: 32 pips (30 + spread); abajo: 28 pips (30 − spread). Se llama el **viaje asimétrico** — el spread acorta el camino a la pérdida y alarga el camino a la ganancia (asimetría total = 2 × spread).
5. Liquidez = capacidad de ejecutar tamaño inmediato sin mover el precio. Los stops son órdenes reales esperando: cuando el precio los alcanza se convierten en ventas/compras a mercado — un depósito concentrado de contrapartida que un institucional puede usar para llenar una orden grande (la barrida, Lección 2.3).
6. 13:00 UTC = **09:00 Bolivia** (UTC−4). Están activas Londres (07:00–16:00 UTC) y Nueva York (12:00–21:00 UTC): es el **solapamiento Londres–NY** — el tramo de mayor volumen y menores spreads del día; ahí está la mejor relación señal/costo del forex.
7. 0,05 lotes × 40 pips × 10 $/pip/lote = **20 $**. (El orden de la multiplicación no importa; importa no confundir pip con pipette.)
8. **Primer viernes del mes, 08:30 ET** (≈ 08:30 Bolivia en horario de verano del norte; +1 h en invierno). Dentro de la ventana roja el spread se multiplica (de ~1,5 pips a 10–20, ilustrativo) y el slippage puede ejecutar tu SL peor que su nivel exacto.
9. Típicamente: **rendimientos suben** (se descuentan tasas más altas por más tiempo), **DXY sube** (dólar más atractivo), **oro cae** (no paga interés, más caro en dólares). Todo se califica con **"típicamente"**: las correlaciones cambian de signo por régimen (en pánicos todo se vende junto) — contexto, no ley.
10. Sin posiciones abiertas desde **15 minutos antes hasta 15 minutos después** de cada evento de alto impacto (FOMC: 30/30 incluyendo la rueda de prensa). Posición inminente: **cerrarla** o — solo si el plan lo contempla — asegurar el SL y reducir tamaño, nunca tamaño completo con SL apretado. Nunca se "opera el dato".

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| Bid | *bid* | Precio al que el mercado te compra (tu salida de un long) |
| Ask | *ask/offer* | Precio al que el mercado te vende (tu entrada en un long) |
| Spread | *spread* | Diferencia bid-ask; el costo fijo por operación que cobran los proveedores de liquidez |
| Libro de órdenes | *order book / DOM* | Fila de órdenes de compra y venta por nivel de precio con sus cantidades |
| Taker | *taker* | Participante agresivo con orden market: consume el libro y paga el spread |
| Maker | *maker* | Participante pasivo con orden limit: provee liquidez y cobra el spread |
| Liquidez | *liquidity* | Capacidad de ejecutar tamaño inmediato sin mover el precio (spread + profundidad) |
| Impacto de mercado | *market impact* | Desplazamiento de precio que produce tu propia orden al consumir el libro |
| Slippage | *slippage* | Diferencia entre el precio de tu orden/stop y el de ejecución real; crece en ventanas de baja liquidez |
| Pip | *pip* | Unidad mínima convencional de movimiento: 0,0001 (pares con yen: 0,01) |
| Pipette | *pipette* | Décima de pip (quinta decimal); fuente clásica de errores ×10 en SL/TP |
| Lote | *lot* | Tamaño de posición: estándar 100 000 u. (10 $/pip en EUR/USD), mini 0,1, micro 0,01 |
| Oferta/demanda residual | *unfilled orders* | Interés que no se llenó en un movimiento previo y espera al retorno del precio (futuras zonas) |
| Desequilibrio | *imbalance* | Estado en que un lado del mercado es más urgente; produce expansión |
| Expansión | *expansion* | Salida rápida del precio de un nivel/rango hasta la próxima zona con órdenes |
| Barrida de stops | *liquidity sweep / stop hunt* | Rotura breve de un nivel obvio para detonar stops y llenar órdenes grandes antes de revertir |
| ADR | *average daily range* | Recorrido medio diario de un instrumento; calibra SL/TP realistas |
| Sesiones | *sessions* | Turnos del día forex: Sídney, Tokio, Londres, Nueva York (horarios ±1 h por DST) |
| Solapamiento | *London–NY overlap* | Tramo Londres+NY (≈ 12:00–16:00 UTC ≈ 08:00–12:00 Bolivia): máximo volumen, mínimo spread |
| Gap | *gap* | Salto de precio sin negociación entre un cierre y la apertura siguiente (fines de semana, índices) |
| NFP | *non-farm payrolls* | Dato de empleo de EE. UU.; primer viernes del mes, 08:30 ET |
| IPC | *CPI* | Inflación al consumidor de EE. UU.; ~mediados de mes, 08:30 ET |
| FOMC | *FOMC* | Comité de la Fed: decisión de tasas 14:00 ET + rueda de prensa 14:30 ET, 8 veces/año |
| DXY | *dollar index* | Índice del dólar frente a una cesta (EUR ~58 %); termómetro del apetito por USD |
| Ventana roja | *high-impact window* | Perímetro sin posición alrededor de un evento macro: 15/15 min (FOMC 30/30) |
| Correlación | *correlation* | Co-movimiento típico entre activos; válida por régimen, no como ley |

## 🔗 Referencias

- [SYLLABUS.md § 5 — N1, Módulo 2](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — vacíos curriculares 4 y 5 (calendario aplicado e intermercados)
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — pasos 0–2 activos con este módulo
- [Módulo 1 · El Trading como Negocio y Ciencia](../mod-01-negocio-trading/README.md) — anterior
- Módulo 3 · Anatomía del Gráfico — siguiente (se publica en el Sprint 3)
