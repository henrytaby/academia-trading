# Módulo 5 · Estructura de Mercado y Liquidez Institucional

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada en este repositorio constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 2 · Técnica |
| 📦 Módulo | 5 de 12 (FIT-12) |
| 🔬 Trazabilidad | 004 · M2.2, M3.1, M3.5 · 003 · M3.5 (crítica SMC) · **Aporte propio:** nomenclatura unificada PA clásico ↔ SMC (vacío D1 del informe) |
| ⏱️ Duración estimada | 5 h de teoría + 6–8 h de laboratorio/misión/quiz |
| 📋 Estado | 🟢 Publicado (Sprint 5) |

---

## 🎯 Objetivo del Módulo

Leer el **mapa del dinero grande** con un solo vocabulario coherente: definir la tendencia por su secuencia de swings (5.1), etiquetar los quiebres como BOS o CHoCH con confirmación por cierre y en dos dialectos intercambiables (5.2), ubicar los pools de liquidez que el precio va a consumir (5.3), medir los desequilibrios que deja un impulso (5.4), filtrar los order blocks con evidencia y sin misticismo (5.5) — y ensamblarlo todo en el protocolo top-down de 3 capas que produce tu primer análisis profesional por escrito (5.6). Este módulo abre el Nivel 2 porque es el **sistema operativo del resto del programa**: los indicadores del M6 se usarán sobre este mapa, el Sistema v1.0 del M7 se construirá con estos arquetipos, y tu journal de M9 auditará exactamente las etiquetas que aquí aprendes a escribir. Al terminar, un gráfico deja de ser una colección de velas bonitas: es un tablero de decisiones con direcciones, zonas, objetivos y precios de entrada.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 5.1 | [Tendencia y estructura](leccion-5-1.md) | HH/HL/LH/LL; pauta de Dow (impulso + pullback) como unidad; swing relevante vs ruido (marco + consecuencia + origen); la frase de sesgo con un nivel | 40–55 min |
| 5.2 | [BOS y CHoCH](leccion-5-2.md) | Continuación vs cambio de carácter; solo el cierre etiqueta; mapa unificado PA clásico ↔ SMC (ruptura = BOS, falsa ruptura = liquidity grab); árbol de decisión | 45–60 min |
| 5.3 | [Liquidez operable](leccion-5-3.md) | Pools de stops tras niveles obvios; equal highs/lows como depósito duplicado; barrida = subasta de liquidación; SL tras la extrema; TP en el pool opuesto | 45–60 min |
| 5.4 | [Imbalances y FVG](leccion-5-4.md) | El hueco de 3 velas; mitigación como visita de rebalanceo; FVG como imán (objetivo o amenaza) y como zona con confluencia; "siempre se llena" es falso | 40–55 min |
| 5.5 | [Order blocks sin misticismo](leccion-5-5.md) | Última vela contraria + BOS; PA clásico lo llama origen del impulso; 4 filtros del programa; qué es verificable y qué es hipótesis; tabla de evidencia honesta | 45–60 min |
| 5.6 | [Top-Down Analysis](leccion-5-6.md) | Protocolo de 3 capas (sesgo D1/H4 → zonas H1/M15 → gatillo M15/M5); la plantilla oficial; "no hay operación" como veredicto válido; confluencia como filtro de calidad | 45–60 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo se estudia **con el gráfico abierto en Bar Replay**: cada lección termina pidiéndote etiquetar estructura en tu plataforma — la lectura de mapas no se aprende leyendo mapas ajenos.
>
> **Un solo caso maestro:** las 6 lecciones analizan el mismo movimiento didáctico de EUR/USD H4 *(ilustrativo)* — low 1,0745 → HL 1,0798 → BOS sobre 1,0860 → HH 1,0884 → pullback a la zona 1,0820–1,0824 con barrida a 1,0792. Es la **misma operación de tu Receta de Primera Operación**: aquí descubrirás por qué cada número de esa receta estaba donde estaba.
>
> **Puente con la [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md):** los pasos 3–5 de la receta (marcado de zonas y contexto) ahora se ejecutan con la plantilla top-down de 5.6 — tu primera operación simple se convierte en el primer top-down archivado de tu negocio.

## 🧪 Laboratorio · Análisis Top-Down de 5 mercados

**Materiales:** TradingView con Bar Replay ([Lección 4.1](../mod-04-plataforma-y-primera-ejecucion/leccion-4-1.md)) + la plantilla top-down de la [Lección 5.6](leccion-5-6.md) (cópiala 15 veces: 5 mercados × 3 sesiones de análisis) + tu journal.

**Procedimiento (por cada mercado: EUR/USD, GBP/USD, XAU/USD, US100, BTC/USD):**

1. **Capa 1 en Bar Replay:** abre un histórico "a ciegas" (replay desde una fecha que no recuerdes), avanza el D1/H4 hasta poder escribir la frase de sesgo con su nivel de invalidación. Anota la fecha del replay.
2. **Capa 2:** avanza a H1/M15 y marca máximo 3 zonas a favor del sesgo, cada una con su tipo (gradiente 3.3 / OB 5.5 / FVG 5.4 / pool 5.3) y sus confluencias.
3. **Capa 3:** avanza vela a vela y registra qué pasó con tus zonas: ¿gatillo válido? ¿barrida antes del rebote? ¿BOS que cambió el mapa? ¿"no hay operación"?
4. **Veredicto y resultado:** completa el formulario con el desenlace *(sin operar: es análisis, no trading)* — qué haría el protocolo y qué hizo el precio.
5. **Autocrítica de 2 líneas:** qué capa te costó más y qué etiqueta confundiste.

**Entregable:** los 5 formularios completos en `journal/laboratorio-m5.md` (o un archivo por mercado). El objetivo NO es acertar direcciones: es que el embudo de 3 capas salga de memoria, en orden y por escrito — la disciplina del formulario antes que la velocidad del veredicto.

## 🎯 Misión

> [!IMPORTANT] Misión M-5 · 15 Análisis Estructurales Documentados
> **Objetivo:** certificar tu lectura de mapa: **15 análisis top-down completos** (los 5 del laboratorio cuentan) donde cada uno etiquete explícitamente BOS/CHoCH, pools de liquidez, FVG y zonas filtradas — con el resultado posterior anotado.
> **Entregable:** `journal/mision-m5.md` con las 15 plantillas archivadas + resumen final: cuántos veredictos "operación planificada" vs "no hay operación", y qué etiqueta confundiste más.
> **Criterio de aceptación (por análisis):** frase de sesgo con nivel de invalidación · máximo 3 zonas con tipo y porqué · gatillo e invalidación definidos ANTES de avanzar el replay · veredicto binario con porqué · etiquetas BOS/CHoCH/liquidez/FVG presentes donde corresponda. **Un análisis sin capa 1 escrita no cuenta.**
> **Etiqueta en journal:** `mision-m5-topdown` · **Tiempo estimado:** 15 análisis en 2–3 semanas (2–3 por semana; la profundidad no se corre).
> **Regla de oro:** al menos 5 de los 15 deben terminar en "no hay operación" justificada — si todos "encuentran operaciones", tu filtro está roto y el agente lo auditara en la revisión.

**Formato de fila resumen (una línea por análisis, al final del archivo):**

```text
#N — fecha — mercado — sesión — secuencia capa 1 — zonas usadas (tipos) — veredicto — resultado posterior (A favor/Barrida primero/Invalidado/Rango)
```

## ✅ Evaluación / Criterio de Graduación

Criterio del SYLLABUS para cerrar M5 y abrir M6:

- **Misión M-5 completa:** 15/15 análisis con la plantilla íntegra — incluyendo mínimo 5 "no hay operación" bien justificados.
- **Quiz de estructura:** [10 preguntas del hub](#-quiz-de-graduación) — **≥ 8/10** para aprobar (umbral estándar del N2).
- **Revisión con el agente:** 3 formularios elegidos al azar se defienden en vivo: ¿por qué esa frase de sesgo? ¿por qué ese SL? ¿qué etiqueta recibió el quiebre y por qué?

Al aprobar todo: M5 🟢 y se abre M6 · Indicadores y Confluencias — donde las herramientas del mercado se evaluarán **sobre el mapa que ya sabes leer** (un indicador sin estructura es un oráculo de feria; con estructura, es un medidor).

## 📝 Quiz de Graduación

1. Define la secuencia de las tres estructuras posibles (alcista, bajista, rango) con sus siglas. ¿Por qué "dos velas verdes" no es una tendencia?
2. ¿Cuál es el test de consecuencia para marcar un swing? Da un ejemplo de high alto que NO se marca.
3. BOS vs CHoCH: definición, dirección respecto a la secuencia y qué hace el programa con cada una. ¿Por qué solo el cierre etiqueta?
4. Traduce al otro dialecto: (a) "ruptura de resistencia confirmada" en SMC; (b) "liquidity grab" en PA clásico; (c) "origin of the move" en SMC.
5. ¿Por qué el precio "va a buscar" los niveles obvios? Responde con el mecanismo de contraparte, no con metáforas.
6. Equal lows en 1,0800 y 1,0802. Un compañero dice: "aguantó dos veces, es un suelo fuerte". ¿Qué dice la lección 5.3 y qué implica para su SL?
7. Describe las 3 velas de un FVG alcista y sus dos usos operativos. ¿Qué chequeo pre-trade impone el FVG?
8. Enumera los 4 filtros del order block. ¿Cuál elimina más candidatos y por qué?
9. ¿Qué es verificable y qué es hipótesis no demostrada en la teoría del OB? ¿Cómo opera el programa la parte verificable?
10. Enumera las 3 capas del top-down con su marco, su pregunta y su producto. ¿Por qué "gatillo perfecto contra el sesgo" no se opera en este programa?

<details>
<summary>Ver clave de respuestas</summary>

1. Alcista = HH+HL (cada high supera el previo, cada low respeta); bajista = LH+LL; rango = swings solapados sin secuencia. Dos velas verdes son una pierna solitaria, no una secuencia: la tendencia es una estructura de peldaños, no un color — sin un HL respetado no hay "peldaño" que sostenga.
2. "¿Su ruptura me obligaría a reetiquetar la tendencia?" — solo se marca el swing que pasa el test. Ejemplo: un máximo intermedio dentro de una pierna (1,0872 camino a 1,0884) no se marca: su quiebre no cambia la secuencia, es decoración.
3. **BOS:** cierre a favor de la secuencia → continuación; el programa busca pullback a favor. **CHoCH:** primer cierre en contra → alerta; el programa pausa el arquetipo de pullback. Solo el cierre etiqueta porque la mecha es ruido o barrida (5.3): el cierre demuestra que el lado dominante sostuvo el nivel tras la prueba.
4. (a) **BOS** (break of structure); (b) **falsa ruptura / bull-bear trap**; (c) **order block / zona de demanda desplazada**. Mismo fenómeno, dos vocabularios — y desconfianza por defecto de quien vende el segundo como "secreto".
5. Las órdenes grandes necesitan contraparte de tamaño sin mover el precio contra sí mismas; los stops agrupados tras los niveles obvios son las únicas bolsas de órdenes market conocidas y concentradas: el precio visita el depósito porque ahí está la comida (liquidez), por logística de ejecución, no por magnetismo técnico.
6. La lección 5.3 dice lo contrario: dos toques casi iguales = **depósito duplicado** (cada toque añadió stops), no suelo fuerte. Implicación: su SL en el borde exacto está en el pool — la barrida siguiente lo ejecuta estadísticamente antes de girar; el SL correcto va tras la estructura con respiración (ley 4.6).
7. Vela 1 con low = X, vela 2 con cuerpo explosivo que cruza la franja, vela 3 con **low > high de la 1**; el hueco es la franja (high de la 1, low de la 3) que ninguna negoció. Usos: imán/objetivo (o amenaza si está en contra del recorrido) y zona de entrada con confluencia. Chequeo pre-trade: ¿hay FVG abierto EN CONTRA entre entrada y TP? → acortar o rechazar.
8. (1) Desplazamiento con BOS por cierre posterior; (2) frescura (primer retesteo); (3) confluencia con gradiente/FVG; (4) confirmación 3.4 antes de entrar. El filtro 1 elimina más: sin BOS no hay OB, hay una vela — y el gráfico sin ese filtro parece sembrado de "zonas sagradas".
9. Verificable: el desplazamiento, el BOS por cierre, la coincidencia con el gradiente, la reacción en el retesteo. Hipótesis no demostrada: las órdenes institucionales pendientes detrás (el book no es público). El programa opera la reacción observada: zona vigilada + confirmación 3.4 + SL por estructura (4.6) — nunca la fe en el nivel exacto.
10. Capa 1 sesgo (D1/H4): "¿quién controla la estructura?" → frase de sesgo + invalidación. Capa 2 zonas (H1/M15): "¿dónde actuar a favor?" → máximo 3 zonas con tipo y porqué. Capa 3 gatillo (M15/M5): "¿qué evento me hace entrar?" → gatillo + SL + lote. El gatillo contra el sesgo es otra familia de trade (reversión): este programa la opera solo con arquetipo y presupuesto propios (M7) — seguirla con el presupuesto del pullback es mezclar muestras y destruir la audibilidad de la estadística.

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| Estructura de mercado | *market structure* | Secuencia de swings (HH/HL/LH/LL) que define la dirección dominante del marco |
| Swing high / swing low | *swing high / swing low* | Máximo/mínimo local que separa piernas; unidad de la estructura |
| Máximo/mínimo creciente | *HH / HL (higher high / higher low)* | Secuencia alcista: cada high supera el previo y cada low respeta el previo |
| Máximo/mínimo decreciente | *LH / LL (lower high / lower low)* | Secuencia bajista: cada low perfora el previo y cada high cede antes |
| Pauta de Dow | *Dow Theory* | La tendencia como alternancia impulso + pullback; unidad de análisis del programa |
| Rango | *range / consolidation* | Swings solapados sin secuencia definida: equilibrio, sin sesgo operativo |
| Ruido de mercado | *market noise* | Movimiento sub-estructural que no cambia la secuencia del marco de decisión |
| BOS | *break of structure* | Cierre más allá del swing a favor de la secuencia: continuación confirmada |
| CHoCH | *change of character* | Primer cierre en contra de la secuencia: alerta de reversión, pausa de pullbacks |
| Confirmación por cierre | *close confirmation* | Solo el cierre del marco de decisión etiqueta quiebres; la mecha no |
| Mecha | *wick* | Rechazo intra-vela fuera del cuerpo; puede ser barrida de liquidez |
| Pool de liquidez | *liquidity pool* | Acumulación de stops tras un nivel obvio: la contraparte que buscan las órdenes grandes |
| Equal highs/lows | *equal highs / equal lows (EQH/EQL)* | Máximos/mínimos casi idénticos: depósito de stops duplicado, no "soporte fuerte" |
| Nivel obvio | *obvious level* | El que ve cualquier principiante; por definición, cargado de stops |
| FVG | *fair value gap* | Hueco de 3 velas donde nadie negoció (high de la 1 vs low de la 3): imán y zona |
| Mitigación | *mitigation / rebalance* | Visita del precio al hueco para ejecutar la franja pendiente; la primera visita es la que vale |
| Desplazamiento | *displacement* | Impulso violento que rompe estructura y deja FVG: firma de urgencia en la subasta |
| Order block | *order block (OB)* | Última vela contraria antes del desplazamiento con BOS; se opera con 4 filtros |
| Origen del impulso | *origin of the move* | El mismo fenómeno del OB en dialecto PA clásico: punto de partida de la pierna |
| Sesgo | *bias* | Dirección probabilística definida por escrito en el marco superior antes de bajar de capa |
| Confluencia | *confluence* | Coincidencia de factores independientes (zona + sesgo + gatillo) que sube la calidad del setup |
| Gatillo | *trigger* | Evento concreto y definido antes de tiempo que autoriza la entrada en el marco de ejecución |
| Análisis top-down | *top-down analysis* | Protocolo de 3 capas (sesgo → zonas → gatillo) con producto escrito por capa |
| Marco temporal | *timeframe* | El rol del marco en cada capa: decisión (D1/H4), zonas (H1/M15), ejecución (M15/M5) |

## 🔗 Referencias

- [SYLLABUS.md § 6 — N2, Módulo 5](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — crítica SMC (003 § M3.5) y vacío D1 de nomenclatura, resueltos por el mapa unificado de la Lección 5.2
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — su zona maestra 1,0820–1,0824 es el caso maestro de todo el módulo
- [Módulo 4 · Plataforma y Primera Ejecución](../mod-04-plataforma-y-primera-ejecucion/README.md) — anterior
- [Módulo 6 · Indicadores y Confluencias](../mod-06-indicadores-y-confluencias/README.md) — siguiente: los medidores se colocan sobre este mapa y se clasifican por evidencia
