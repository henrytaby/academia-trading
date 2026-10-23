# Módulo 3 · Anatomía del Gráfico

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada en este repositorio constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 1 · Fundamentos |
| 📦 Módulo | 3 de 12 (FIT-12) |
| 🔬 Trazabilidad | 003 · M2.1–2.6 · 004 · M1.5, M3.3–3.4 · **Aporte propio:** catálogo de patrones con fiabilidad evidenciada y protocolo de confirmación unificado |
| ⏱️ Duración estimada | 4,5 h de teoría + 4–6 h de laboratorio/misión/quiz |
| 📋 Estado | 🟢 Publicado (Sprint 3) |

---

## 🎯 Objetivo del Módulo

Leer el **gráfico desnudo** — velas, ciclos, zonas, confirmaciones y régimen — sin indicadores todavía: primero el precio. Al terminar este módulo descompondrás cualquier vela en cuerpo/mechas/cierre y sabrás qué subasta la produjo (M3.1), ubicarás el mercado en su ciclo de 4 fases (M3.2), marcarás zonas — no líneas — con gradiente de fortaleza honesto (M3.3), ejecutarás el protocolo de confirmación en 3 pasos que filtra la mayoría de los falsos rompimientos (M3.4), reconocerás los patrones elementales como firmas de procesos y no como oráculos (M3.5), y clasificarás el régimen — tendencia, rango o transición — ANTES de buscar setup, entendiendo por qué la mayoría del tiempo la respuesta correcta es observar (M3.6). Este módulo existe porque el M5 te enseñará la estructura institucional sobre estas mismas bases: quien no lee el precio desnudo no puede auditar lo que encima se dibuja.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 3.1 | [Velas japonesas](leccion-3-1.md) | OHLC, cuerpo vs mechas, el cierre como veredicto; fractalidad literal (cada vela contiene un gráfico); lectura en 4 preguntas; Dojima y Homma | 40–50 min |
| 3.2 | [Los 4 ciclos del mercado](leccion-3-2.md) | Acumulación → markup → distribución → markdown; Dow (impulso+pullback, HH/HL); Weinstein Stages; clasificar el ciclo en 3 preguntas | 40–50 min |
| 3.3 | [Soportes y resistencias](leccion-3-3.md) | Zonas, no líneas; estáticos/diagonales/dinámicos; memoria de mercado y polaridad; gradiente de fortaleza (muchos toques CONSUMEN); protocolo de marcado | 45–60 min |
| 3.4 | [Confirmación en 3 pasos](leccion-3-4.md) | Ruptura → cierre fuera → retesteo que se sostiene; pullback/throwback; el falso rompimiento como mecanismo; caso con R:B 3,1 y lote calculado | 45–60 min |
| 3.5 | [Patrones elementales](leccion-3-5.md) | Vela (envolvente, martillo, estrella, doji) y figura (doble techo/suelo, triángulo, cuña, bandera) como firmas de procesos; checklist de 5 preguntas; fiabilidad honesta | 45–60 min |
| 3.6 | [Rangos vs tendencias](leccion-3-6.md) | Régimen como permiso operativo; ~70 % del tiempo en rango *(aproximación)*; el whipsaw como mecanismo de cobro; test de 3 marcas; transición = operativa cero | 40–50 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo es el más visual del N1: cada lección pide abrir TradingView (o equivalente) y VER lo que se describe — el gráfico es el libro de ejercicios.
>
> **Puente con la [Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md):** con M3 completado, el Paso 3 de la receta (análisis mínima: régimen + zonas + dirección) ya tiene todo su método. Los pasos 4–11 siguen esperando al Módulo 4.

## 🧪 Laboratorio · Ciclos y Zonas en 10 Gráficos

**Materiales:** TradingView (o plataforma equivalente) con **Bar Replay** (reproducción histórica) — el M4.1 lo formalizará; aquí solo lo usas como máquina del tiempo. 5 instrumentos: tu par principal (EUR/USD), XAU/USD, un índice (US30/US100), y 2 más a elección (otro major, otro índice).

**Procedimiento paso a paso:**

1. **Elige 10 episodios históricos** (2 por instrumento) en D1/H4: elige tramos con giro claro (una expansión tras rango, una reversión tras tendencia) — con Bar Replay retrocede hasta ANTES del giro, en un punto donde el futuro no sea visible.
2. **Por episodio, clasifica el ciclo** (M3.2, test de 3 preguntas): ¿acumulación, markup, distribución o markdown? Anótalo ANTES de avanzar el replay.
3. **Marca 2–4 zonas por episodio** (protocolo M3.3: extremos de swing, orígenes de expansión, rectángulos con cuerpo, solo H4/D1) y gradúalas (fresca/consumida, origen expansivo o no).
4. **Avanza el replay vela a vela** y anota: ¿el precio respetó, retesteó o rompió cada zona? ¿Hubo confirmación en 3 pasos en las roturas? ¿Apareció el whipsaw?
5. **Audítate:** de tus 20–40 zonas marcadas, ¿qué porcentaje respetó tu marcado? ¿Dónde fallaste: extremo vs cuerpo, marco mezclado, o zona-consumida tratada como fresca?

**Entregable:** capturas de los 10 episodios con tus anotaciones + el mini-informe de autoauditoría, guardados en `journal/laboratorio-m3.md`. La honestidad del informe vale más que el porcentaje de acierto: el error identificado es la técnica adquirida.

## 🎯 Misión

> [!IMPORTANT] Misión M-3 · Bitácora de 20 Niveles
> **Objetivo:** construir tu primera base de datos personal de zonas: 20 niveles reales anotados ANTES de conocer su desenlace, con el resultado posterior documentado — el primer contacto con la estadística visual propia.
> **Entregable:** `journal/bitacora-niveles-m3.md` con la tabla de 20 niveles (formato abajo) + un análisis final (¿qué tipo de zona respetó más: fresca o visitada? ¿con origen expansivo o sin él? ¿en qué marco?).
> **Criterio de aceptación:** 20 filas completas con: fecha de marcado, instrumento, marco, tipo (soporte/resistencia), coordenadas de la zona (borde superior e inferior), clasificación de fortaleza (gradiente M3.3), régimen del día (M3.6), y resultado posterior (respetado / retesteado y roto / barrida y revertido) verificado en el gráfico.
> **Etiqueta en journal:** `mision-3-bitacora` · **Tiempo estimado:** 20 niveles × 15–20 min de seguimiento, repartidos en 2–3 semanas de mercado real (o acelerado con Bar Replay si el calendario aprieta).
> **Regla de oro:** el nivel se anota ANTES del desenlace. Ajustar la zona después de ver dónde giró el precio es curvar la regla tras medir — invalida la fila y, si se repite, la misión entera.

**Formato de fila (copiar en la bitácora):**

```text
#N — fecha_marcado — instrumento — marco — tipo (S/R)
Zona: [borde_sup – borde_inf] — fortaleza: [fresca/consumida · origen: expansivo/ruido · confluencias]
Régimen al marcar: [tendencia/rango/transición — test de 3 marcas]
Resultado (a completar después): [respetado / retesteado y roto / barrida y revertido] — fecha_resolución
Nota (1 línea): qué aprendió este nivel sobre tu marcado
```

## ✅ Evaluación / Criterio de Graduación

- **Laboratorio entregado:** 10 episodios clasificados con zonas marcadas y autoauditoría honesta.
- **Misión M-3 completa:** 20 niveles anotados antes del desenlace + análisis final por clasificación de zona.
- **Análisis en vivo:** un gráfico actual (tu instrumento principal, H4/D1) leído con el agente siguiendo la rúbrica: ciclo (3 preguntas), 2–4 zonas con gradiente, régimen (test de 3 marcas) y — si existe — el estado de cualquier rotura según el protocolo de 3 pasos.
- **Quiz de graduación:** ≥ 8/10.
- Al aprobar todo: el módulo queda marcado ✅ en el README raíz y se abre el [Módulo 4 · Plataforma y Primera Ejecución](../mod-04-plataforma-y-primera-ejecucion/README.md) — donde la [Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) ejecuta sus pasos 3–11 y cierra el nivel con el [Examen N1](../../03-recursos/evaluaciones/examen-n1.md).

## 📝 Quiz de Graduación

1. Descompón una vela en sus dos componentes y di qué mide cada uno. ¿Cuál de los cuatro precios (OHLC) es el veredicto del período y por qué el programa evalúa confirmaciones sobre él?
2. Nombra los 4 ciclos en orden y describe en una frase cada uno. ¿En qué fase compra en fragmentos el institucional sin mover el precio?
3. ¿Qué secuencia de máximos/mínimos define una tendencia alcista sana según Dow, y qué evento marca su muerte?
4. ¿Por qué el programa marca ZONAS y no líneas? Da las dos razones (macroestructura de las órdenes + qué implica en la práctica del marcado).
5. Una zona acumula 7 toques recientes. ¿Más fuerte o más débil? ¿Por qué, con la lógica de órdenes pendientes (M2.2)?
6. Enuncia el protocolo de confirmación en 3 pasos completo. ¿Qué fenómeno de la Lección 2.3 es el que el paso 2 (cierre fuera) filtra?
7. ¿Qué es la polaridad y por qué el retesteo de un nivel confirmado es la entrada con mejor estadística del protocolo?
8. ¿Qué es un falso rompimiento, qué proceso del mercado lo genera (no es mala suerte), y cuál es la única conducta permitida ante él durante la formación?
9. Aplica el test de 3 marcas al caso: "US30 lleva 9 sesiones solapadas entre dos bordes; las roturas intra-vela vuelven siempre; cuerpos pequeños alternados". ¿Clasificación y qué se prohíbe en ese régimen?
10. ¿Qué es el whipsaw, a quién cobra y qué dos reglas del programa lo neutralizan?

<details>
<summary>Ver clave de respuestas</summary>

1. **Cuerpo** (apertura→cierre): quién ganó la subasta del período y con cuánta determinación. **Mechas** (cuerpo→extremos): dónde fue rechazada la urgencia. El **Close** es el veredicto: es el último acuerdo con toda la información del período; un toque intra-vela puede ser una barrida que se revierte, mientras el cierre implica que la urgencia sobrevivió al período entero — evaluar en cierres filtra falsos rompimientos.
2. **Acumulación** (los grandes compran en fragmentos en un rango post-caída, sin mover el precio) → **markup** (la oferta local se consumió y el precio expande con cuerpo pleno) → **distribución** (los grandes venden su inventario al retail eufórico en un rango alto) → **markdown** (inventario vendido, urgencia de miedo, caída rápida). Compran sin mover el precio en la **acumulación**.
3. Tendencia alcista sana: **máximos y mínimos ascendentes sucesivos (HH/HL)** con impulsos y pullbacks que respetan la estructura. Muere cuando la secuencia se rompe — el precio falla en hacer HH y hace un LL (mínimo más bajo) con cierre decidido: ruptura de estructura.
4. (a) Macroestructura: los grandes fragmentan y ningún nivel reacciona en un precio exacto — el interés vive en un área con cuerpo; una línea de píxel es falsa precisión. (b) Práctica: marcar rectángulos define dónde entra, dónde muere la idea (SL tras el cuerpo) y dónde está el objetivo (borde de la zona opuesta) — la línea no permite ninguno de los tres cálculos.
5. **Más débil.** Cada reacción consume órdenes pendientes: los que querían comprar/vender en la zona ya lo hicieron. A la séptima visita el almacén está casi vacío — la zona tiene fama pero poca munición real, y es hábitat clásico de barrida final.
6. **Ruptura** (el precio atraviesa el nivel) → **cierre fuera** (la vela del marco cierra decididamente más allá) → **confirmación** (retesteo del nivel roto que se sostiene, con reacción del lado nuevo). El paso 2 filtra la **barrida de stops/liquidez** (Lección 2.3): la rotura momentánea que detona órdenes y vuelve — el cierre fuera implica que la urgencia sobrevivió al período.
7. Polaridad: el nivel roto y confirmado **cambia de bando** (resistencia rota → soporte; soporte roto → resistencia). El retesteo es la entrada con mejor estadística porque (a) el filtro del cierre ya está descontado, (b) hay documentación del nuevo bando (compradores que esperaban el retesteo + cubrimiento de atrapados), y (c) el SL va tras la estructura del retesteo, no en el depósito obvio de stops.
8. Falso rompimiento: rotura que no logra cierre decidido fuera (o vuelve con fuerza tras lograrlo) y gira. Lo genera el **mecanismo de recolección de liquidez**: detrás de todo nivel obvio hay stops y entradas del retail, y atravesarlo unas velas los detona (M2.3). Conducta en formación: dejar que el protocolo te filtre a TI (no operar roturas sin los 3 pasos) — operar el falso como setup del lado contrario llega después, con criterio y estadística propia.
9. Test: estructura sin progresión (solapamiento) ✓ · recorridos que vuelven al corredor ✓ · cuerpos pequeños alternados ✓ → **rango confirmado** (3/3). Prohibido: anticipar roturas de los bordes; el centro del rango es tierra de nadie; lo operable es solo el rechazo confirmado en bordes (y suspender la lógica si un borde rompe con cierre H4 fuera: el régimen puede estar cambiando).
10. Whipsaw: el vaivén de roturas falsas de rango que cobra 1R a cada comprador de rompimiento (atracción de tardíos + barrida + retorno, repetido). Lo neutralizan: (1) clasificar el régimen ANTES de buscar setups — en rango, las roturas anticipadas no existen como setup; (2) operar roturas solo con el protocolo de 3 pasos (cierre fuera + retesteo sostenido), dejando que el filtro rechace las primeras roturas.

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| OHLC | *open/high/low/close* | Los cuatro precios de una vela: apertura, máximo, mínimo, cierre |
| Cuerpo | *candle body* | Distancia apertura-cierre; mide la determinación del bando ganador |
| Mecha | *wick/shadow* | Extensión del cuerpo al máximo/mínimo; mide el viaje rechazado |
| Doji | *doji* | Vela con apertura ≈ cierre; empate de la subasta, pausa — nunca señal de dirección |
| Martillo | *hammer* | Mecha inferior ≥ 2× cuerpo; venta absorbida abajo — señal solo EN contexto de zona |
| Envolvente | *engulfing* | Vela que envuelve el cuerpo de la anterior en sentido contrario; reemplazo de bando |
| Ciclo | *market cycle* | Acumulación → markup → distribución → markdown; el mapa de fases de todo mercado |
| Impulso | *impulse* | Pierna de expansión en la dirección dominante con energía |
| Pullback | *pullback* | Retroceso de una tendencia que respeta la estructura; andén de continuación |
| Throwback | *throwback* | Retorno al origen de una rotura para retestear antes de continuar |
| HH/HL | *higher high / higher low* | Secuencia de máximos y mínimos ascendentes: firma de tendencia alcista sana |
| LL/LH | *lower low / lower high* | Secuencia descendente: firma de tendencia bajista |
| Soporte/Resistencia | *support/resistance* | Zona con interés comprador/vendedor pendiente capaz de detener o invertir |
| Zona | *zone* | Área (rectángulo con cuerpo) donde el precio reaccionó — la forma correcta de marcar niveles |
| Polaridad | *polarity* | El nivel roto y confirmado cambia de bando: soporte↔resistencia |
| Retesteo | *retest* | Vuelta del precio a un nivel roto para probarlo antes de continuar; paso 3 del protocolo |
| Falso rompimiento | *false breakout* | Rotura sin cierre decidido fuera (o revertida tras lograrlo); mecanismo de recolección de liquidez |
| Cuello | *neckline* | Línea de decisión de una figura (valle del doble techo); su rotura confirmada activa el patrón |
| Régimen | *market regime* | Estado estructural: tendencia, rango o transición; el permiso operativo de cada sistema |
| Transición | *transition* | Régimen mezclado (señales de dos estados); protocolo: operativa reducida o cero |
| Whipsaw | *whipsaw* | Vaivén de roturas falsas de rango que cobra 1R por intento a los impacientes |
| Bar Replay | *bar replay* | Reproducción vela a vela del histórico para practicar sin ver el futuro |

## 🔗 Referencias

- [SYLLABUS.md § 5 — N1, Módulo 3](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — aporte propio del módulo: catálogo de patrones con fiabilidad evidenciada
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — su Paso 3 (análisis mínima) se completa con este módulo
- [Módulo 2 · El Motor del Precio](../mod-02-motor-del-precio/README.md) — anterior
- [Módulo 4 · Plataforma y Primera Ejecución](../mod-04-plataforma-y-primera-ejecucion/README.md) — siguiente (cierra el N1 con el [Examen N1](../../03-recursos/evaluaciones/examen-n1.md); el N2 arranca con M5 en el Sprint 5)
