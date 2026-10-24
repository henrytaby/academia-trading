# Módulo 7 · Construcción del Sistema de Trading

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada en este repositorio constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 2 · Técnica — módulo de cierre |
| 📦 Módulo | 7 de 12 (FIT-12) |
| 🔬 Trazabilidad | 003 · M3.1–3.2, M3.6 · **Aporte propio:** catálogo de arquetipos de setup, estadística de rachas aplicada a la misión, criterios de robustez con checklist |
| ⏱️ Duración estimada | 5–6 h de teoría + 10–14 h de laboratorio/misión/evaluación |
| 📋 Estado | 🟢 Publicado (Sprint 7) |

---

## 🎯 Objetivo del Módulo

Salir del Nivel 2 con un **Sistema v1.0 escrito** — la primera versión formal de tu negocio. El M5 te dio el mapa (estructura, liquidez, zonas) y el M6 los medidores que lo auditan; este módulo ensambla todo en una máquina operativa: el vocabulario de tres capas con su test del clon (7.1), los 10 componentes que un sistema completo debe cerrar (7.2), el catálogo de los 4 arquetipos de setup y la elección con filtros (7.3), la matriz WR × R:B que convierte la esperanza en decisiones (7.4), las métricas y la estadística de rachas que predice el dolor antes de que llegue (7.5) y los criterios de robustez que separan un sistema de un traje cosido al pasado (7.6). El entregable no es una nota: es un documento de una página — con mínimo 5 reglas explícitas — que pasa el test del clon, más la evidencia de 30 repeticiones a ciegas. Al aprobar la **Evaluación Nivel 2**, tendrás por primera vez algo que los 95 % que fracasan nunca tuvieron: un objeto medible, auditable y mejorable.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 7.1 | [Filosofía, Estrategia y Sistema](leccion-7-1.md) | Las 3 capas de abstracción; el test del clon; por qué "veo una vela en soporte" no es un sistema | 40–55 min |
| 7.2 | [Los 10 componentes](leccion-7-2.md) | La lista cerrada de preguntas que un sistema responde antes de abrir el gráfico; régimen filtra a setup | 45–60 min |
| 7.3 | [Arquetipos de setup](leccion-7-3.md) | Los 4 caminos (ruptura+retesteo, pullback, reversión en rango, barrida+giro); firma WR×R:B de cada uno; el híbrido 2+4 del programa | 50–65 min |
| 7.4 | [Esperanza aplicada](leccion-7-4.md) | La matriz WR × R:B; breakeven 1/(1+R:B); por qué 40 % con 1:2 es negocio; los costes matan primero a los de R:B corto | 45–60 min |
| 7.5 | [Métricas y rachas](leccion-7-5.md) | WR, R:B medio, Profit Factor, Max DD, curva de capital; P(racha) = (1−WR)ⁿ; con WR 40 % esperan 6-7 pérdidas seguidas en 30 operaciones | 50–65 min |
| 7.6 | [Criterios de robustez](leccion-7-6.md) | Los 4 criterios; simplicidad cuantitativa; out-of-sample; el ciclo prohibido del data-mining; la humildad del ±17,5 % | 45–60 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo se estudia **con la plantilla del Sistema v1.0 abierta en paralelo**: cada lección te regla un componente más — al terminar 7.6 tendrás la mitad del trabajo hecho si fuiste tomando notas.
>
> **El caso maestro se convierte en sistema:** las 6 lecciones usan el movimiento de tu [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) *(ilustrativo)* — EUR/USD H4: low 1,0745 → HL 1,0798 → BOS sobre 1,0860 → HH 1,0884 → pullback a la zona 1,0820–1,0824 con barrida a 1,0792, entrada 1,0820, SL 1,0788 (32 pips ≈ 1,52 ATR), TP 1,0886 (66 pips, R:B ≈ 2,1), riesgo 1 % (19,20 $). La receta era un sistema ejecutado una vez; aquí extraes de ella la máquina que produce operaciones de esa clase — y la pones a prueba 30 veces.
>
> **Puente con M6:** tu dashboard aprobado de 3 herramientas entra al sistema como componentes (régimen → componente 3, ATR → componente 6, contexto → filtro del componente 10). El M6 clasificó herramientas; el M7 les asigna un puesto con reglas escritas — un medidor sin componente asignado es decoración.

## 🧪 Laboratorio · Redactar el Sistema v1.0 en una página

**Materiales:** las 6 lecciones del módulo + tu dashboard M6 aprobado + la [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) como caso de referencia + esta plantilla.

**La plantilla oficial (cópiala a tu journal y rellénala):**

```text
SISTEMA v1.0 — [tu nombre] — fecha — versión 1.0
Filosofía (una frase, falsable): [¿por qué existe tu ventaja?]

| # | Componente | Regla escrita |
|---|------------|---------------|
| 1 | Mercado y vehículo    | [mercado, instrumento, y por qué] |
| 2 | Marcos temporales     | [marco de decisión / zonas / ejecución] |
| 3 | Régimen               | [qué estados permiten operar y cuáles no] |
| 4 | Setup (arquetipo)     | [el fenómeno que buscas, con su nombre] |
| 5 | Gatillo de entrada    | [evento exacto + tipo de orden] |
| 6 | Stop inicial          | [ubicación estructural + margen + auditoría ATR] |
| 7 | Salidas               | [TP único / parciales / criterio de fin] |
| 8 | Gestión post-entrada  | [qué se hace — incluida la abstención] |
| 9 | Riesgo y tamaño       | [% fijo por operación + cálculo del lote] |
| 10 | Filtros, horario y registro | [cuándo NO opero + journal] |

Fila esperada en la matriz (7.4): WR esperado [__ %] · R:B mínimo [__] · E esperada [+__ R]
Coste estimado por operación: [__ R] — E neta esperada: [+__ R]
```

**Procedimiento:**

1. **Filosofía primero (7.1):** una frase falsable sobre el mecanismo de tu ventaja. Si no puedes imaginar la evidencia que la refutaría, aún no tienes filosofía — vuelve a 5.3 y 5.5.
2. **Elige UN arquetipo con los 4 filtros (7.3):** compatibilidad de filosofía, de mercado, de invalidación y de costes — por escrito. Si aún no tienes criterio propio, adopta el híbrido 2+4 del programa (pullback en tendencia con barrida de liquidez): es operable, está documentado en el M5 y su invalidación es estructural.
3. **Rellena los 10 componentes (7.2)** con reglas que pasen el test del clon. Mínimo del SYLLABUS: **5 reglas explícitas numeradas** — pero recuerda que el sistema completo cierra las 10 preguntas. Simple y cumplible antes que sofisticado y roto.
4. **Declara tu fila de la matriz (7.4) ANTES de la misión:** WR esperado y R:B mínimo del arquetipo — es tu hipótesis, y la misión la pondrá a prueba sin que la muevas.
5. **Corre la checklist de robustez (7.6):** 10 ítems, del test del clon al out-of-sample. Cada "no" vuelve a la mesa.
6. **Defensa con el agente auditor:** presenta el documento y responde — ¿por qué este arquetipo? ¿qué hace cada componente? ¿dónde muere la idea? ¿qué evidencia te haría cambiarla?

**Entregable:** `journal/sistema-v1.md` — una página (la plantilla cabe exactamente ahí; los anexos — checklists, capturas — van por fuera). El objetivo NO es tener el sistema perfecto: es tener **el primer objeto completo y auditable** — la v1.0 existe para ser medida y mejorada, no para ser adorada.

## 🎯 Misión

> [!IMPORTANT] Misión M-7 · 30 repeticiones del setup a ciegas
> **Objetivo:** estimar los parámetros reales de TU arquetipo — el WR verdadero, el R:B real, el Profit Factor, el Max DD y las rachas — en 30 repeticiones Bar Replay **desde fechas que no recuerdes** (out-of-sample por construcción, 7.6).
> **Procedimiento por repetición:** (1) avanza el replay hasta un punto ciego; (2) aplica el sistema COMPLETO — régimen, zona, gatillo — sin ver el desenlace; (3) si no hay setup válido, la fila es "no hay setup" y avanzas: ese veredicto también es dato; (4) si lo hay, marca entrada, SL y TP en el gráfico, captura, y solo entonces avanza el replay hasta el desenlace; (5) registra la fila.
> **Entregable:** `journal/mision-m7.md` con la tabla de 30 filas (`nº · mercado · fecha replay · régimen previo · gatillo · SL/TP en pips · resultado en R · nota`) y el **reporte de una página** (7.5): WR, R:B medio, PF, curva de capital, Max DD en R, racha más larga vs tabla de rachas esperables, y la celda real (WR × R:B) de la matriz de 7.4 con su veredicto.
> **Criterio de aceptación:** 30/30 filas con desenlace real anotado tras avanzar el replay · mínimo 5 filas "no hay setup" (el no-operar es veredicto del sistema, no fracaso tuyo) · **ninguna regla modificada a mitad de la muestra** — si tocas una regla, la cuenta arranca de nuevo (el experimento se rompe y se documenta) · cada veredicto respaldado por un número.
> **Etiqueta en journal:** `mision-m7-sistema-v1` · **Tiempo estimado:** 2 semanas (5-8 repeticiones por sesión, nunca más: la fatiga contamina el registro).
> **Regla de oro:** tu distribución de rachas debe parecerse a la tabla de 7.5 — con WR ~40 %, una racha de 6-7 pérdidas en 30 repeticiones es el comportamiento ESPERADO de una máquina sana. Si tu muestra no tiene ninguna racha de 4+, sospecha del registro (¿fue realmente a ciegas?) antes de celebrar.

## ✅ Evaluación / Criterio de Graduación — 🏆 Evaluación Nivel 2

Criterio del SYLLABUS para cerrar el N2 y abrir el N3:

- **Sistema v1.0 aprobado por el agente auditor:** completitud de los 10 componentes + test del clon superado + checklist de robustez (7.6) sin "no" sin resolver. La aprobación es de **completitud y explicitud**, no de rentabilidad — la rentabilidad la medirán los 100 backtests de M9.
- **Misión M-7 completa:** 30 repeticiones documentadas con reporte de métricas y veredicto por la matriz.
- **Examen estructural N2:** [`examen-n2.md`](../../03-recursos/evaluaciones/examen-n2.md) — 30 preguntas (M5-M7) + 5 socráticas, **≥ 24/30 (80 %)**.
- **Defensa en vivo del sistema** ante el agente: ¿por qué este arquetipo y no otro? ¿cuál es tu invalidación? ¿qué racha esperas y qué harás cuando ocurra? ¿qué evidencia haría archivar el sistema?

Al aprobar todo: **N2 🏆 completo** y se abre el N3 con [M8 · Gestión del Riesgo](../mod-08-gestion-del-riesgo/README.md) — el módulo que paga las cuentas, donde tu sistema consigue su presupuesto formal de riesgo.

## 📝 Quiz de Graduación

1. Define filosofía, estrategia y sistema con la pregunta que cada capa responde. Aplica el test del clon: ¿por qué "veo una vela en soporte" falla las tres?
2. Enumera los 10 componentes del sistema con la pregunta que cierra cada uno. ¿Cuáles faltan en el plan "compro pullbacks en EUR/USD"?
3. Los 4 arquetipos: lógica de captura, régimen óptimo y firma típica WR × R:B de cada uno. ¿Por qué el híbrido 2+4 es el candidato del programa?
4. Calcula la esperanza de WR 40 % con R:B 1:2, el WR de equilibrio de esa columna, y el resultado esperado de 100 operaciones al 1 % de riesgo *(planteo y números)*.
5. Profit Factor: fórmula, valor del caso (40 %, 1:2), y por qué un PF > 3 en una muestra corta es una mala noticia disfrazada de éxito.
6. Rachas: probabilidad de 5 pérdidas seguidas con WR 40 %, y racha esperable máxima en 30 operaciones con ese WR *(fórmulas y números)*. ¿Qué significa para tu misión?
7. Max DD: definición exacta. Con riesgo 1 %, ¿cuánto vale el valle de una racha de 6, y cuánto necesita subir la cuenta para recuperarlo? ¿Por qué con 5 % ese valle es terminal?
8. Robustez: los 4 criterios del programa. ¿Por qué la simplicidad es un criterio cuantitativo (k/N) y no una preferencia estética?
9. Data-mining: describe el ciclo prohibido y los dos candados del protocolo honesto. ¿Qué es out-of-sample y por qué el replay "a ciegas" lo garantiza?
10. Con N=30 y WR medido 40 %, calcula el intervalo de confianza al 95 % del WR verdadero. ¿Qué decisión estructural prohíbe ese intervalo y dónde se toma esa decisión?

<details>
<summary>Ver clave de respuestas</summary>

1. **Filosofía:** por qué existe la ventaja (tesis falsable sobre el mecanismo). **Estrategia:** cómo se captura (fenómeno + régimen + arquetipo). **Sistema:** cuándo exactamente y cuánto (10 componentes con reglas cerradas). "Veo una vela en soporte" falla: no hay filosofía (¿qué mecanismo?), la "estrategia" no define fenómeno ni régimen, y no pasa el clon — dos desconocidos discrepan sobre marco, definición de soporte, vela válida, riesgo y salida: es subjetividad con vocabulario técnico.
2. (1) Mercado y vehículo, (2) marcos temporales, (3) régimen, (4) setup/arquetipo, (5) gatillo de entrada, (6) stop inicial, (7) salidas, (8) gestión post-entrada, (9) riesgo y tamaño, (10) filtros, horario y registro. "Compro pullbacks en EUR/USD" solo cierra el 1 (a medias) y enuncia el 4: faltan marcos (mezclarás señales de escalas distintas), régimen (comprarás pullbacks en tendencia rota), gatillo (entrarás "cuando se sienta"), stop (o ausente o arbitrario), salidas (cierre por miedo), gestión (moverás el stop), riesgo (tamaño a ojo) y horario/registro (operativa nocturna inauditable).
3. **Ruptura+retesteo:** la ruptura agota el lado contrario, se entra en la revalida — expansión post-squeeze; ~35-45 % × ≥ 1:2,5; muere en falsa ruptura. **Pullback en tendencia:** el retroceso a zona es el punto de añadir a favor del régimen — tendencia establecida; ~40-55 % × 1:2; muere en CHoCH real. **Reversión en rango:** el extremo está caro/barato vs media — rango definido; ~55-70 % × ~1:0,8; muere en la ruptura del rango. **Barrida+giro:** el barrido del pool completa el llenado institucional — con sesgo claro en zona; ~35-50 % × ≥ 1:2,5; muere cuando el barrido era la primera pierna de la aceleración. El 2+4 integra TODAS las herramientas del N2 (régimen, estructura, liquidez, zona, top-down), es frecuente en EUR/USD, tiene invalidación estructural (CHoCH bajo el HL) y R:B ≥ 1:2 con margen para costes — por eso es el candidato.
4. $E = 0{,}40 \times 2 - 0{,}60 \times 1 = +0{,}20R$. Breakeven: $1/(1+2) = 33{,}3$ % — el sistema opera 6,7 puntos por encima del filo. 100 operaciones al 1 %: $+0{,}20 \times 100 = +20R$ → **+20 % del capital** *(ilustrativo, sin componer)* — el negocio que falla el 60 % de las veces y gana por el producto frecuencia×tamaño con pérdidas acotadas.
5. $PF = \frac{\sum \text{ganancias}}{\sum \text{pérdidas}} = \frac{WR \times \overline{W}}{(1-WR) \times L}$. Caso (40 %, 1:2): $PF = 0{,}8/0{,}6 = 1{,}33$ — por cada $ perdido genera 1,33 $: positivo pero bajo el objetivo 1,5. PF > 3 en muestra corta: con N pequeño la varianza del PF es enorme y los valores extremos casi siempre delatan reglas ajustadas al pasado, muestra contaminada o riesgo no acotado — celebrar eso es celebrar ruido con formato de estadística (M9 exige N ≥ 100 para que el número signifique).
6. $P(5) = 0{,}6^5 = 7{,}8$ %. Racha esperable: $\ln 30 / \ln(1/0{,}6) = 3{,}401/0{,}511 ≈ 6{,}7$ → **6-7 pérdidas seguidas son esperables en tu misión**. Significa: si aparece, es confirmación del modelo (la tabla lo predijo), no señal de sistema roto — el protocolo es no cambiar nada, mantener tamaño y registrar; abandonar ahí es romper el experimento justo donde la estadística lo anticipó.
7. Max DD = la mayor caída pico-a-valle de la curva de capital. Racha de 6 al 1 % = **−6 %**; recuperar −6 % exige $1/0{,}94 - 1 ≈ +6{,}4$ % (asimetría leve). Al 5 %: la MISMA racha vale **−30 %**, que exige $+43$ % para volver — el territorio donde la cuenta y el trader mueren. El 1 % no es timidez: es la tabla de rachas (6-7 esperables) multiplicada por la asimetría de recuperación — dos fórmulas, ninguna emoción.
8. (1) Escrito y clonable, (2) componentes completos, (3) E plausible con margen para costes, (4) simple y probado fuera de muestra. La simplicidad es cuantitativa porque el rendimiento ajustado se infla aproximadamente como $\sqrt{k/N}$: con k=10 reglas sobre N=30, ≈ 58 % de inflación esperable del resultado en muestra — cada regla extra agranda el espejismo. Menos reglas = menos parámetros ajustados al pasado = el número de la prueba se parece más al número del futuro.
9. Ciclo prohibido: probar → ajustar mirando el resultado → repetir → celebrar el mejor de N intentos (entre suficientes loterías, el azar siempre fabrica un histórico brillante sin significado). Candados: la métrica se **declara antes** de probar y cada iteración se **archiva con su registro**. Out-of-sample: la prueba en datos que el sistema no vio al construirse; el replay arrancando en fechas no recordadas garantiza que ninguna información de esos movimientos pudo entrar en las reglas — mide predicción, no explicación.
10. $\pm 1{,}96\sqrt{0{,}4 \times 0{,}6/30} = \pm 1{,}96 \times 0{,}0894 ≈ \pm 17{,}5$ % → el WR verdadero está entre ~22 % y ~58 %. Prohíbe decisiones estructurales con esta muestra: cambiar de arquetipo, abandonar el sistema o "validarlo" — ninguna es defendible con una horquilla que cubre desde ruina hasta excelencia. La decisión de validación se toma en M9 con N ≥ 100 (intervalo ≈ ±9,8 %) más el forward de demo: primero el candidato, después la evidencia.

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| Sistema de trading | *trading system* | Formalización escrita y clonable de tu ventaja: 10 componentes con reglas explícitas que dos desconocidos ejecutarían igual |
| Filosofía de mercado | *market philosophy* | Tesis falsable sobre por qué el mercado deja dinero en la mesa; el mecanismo de tu ventaja |
| Estrategia | *strategy* | Narrativa coherente que convierte la filosofía en forma de captura: fenómeno + régimen + arquetipo |
| Regla explícita | *explicit rule* | Condición verificable por un tercero sin interpretación; no admite "se veía" |
| Test del clon | *clone test* | Dos desconocidos con tu documento ante el mismo gráfico deben ejecutar la misma operación |
| Componente del sistema | *system component* | Cada una de las 10 preguntas que un sistema completo cierra antes de operar |
| Régimen | *market regime* | Estado dominante del mercado (tendencia, rango, expansión) que condiciona qué arquetipos son viables |
| Arquetipo de setup | *setup archetype* | Familia de setups con la misma lógica de captura: dónde entra, contra qué apuesta, cómo muere |
| Ruptura y retesteo | *break and retest* | Entrada en la vuelta al nivel roto: el retesteo filtra la falsa ruptura |
| Pullback en tendencia | *trend pullback* | Entrada a favor del régimen en el retroceso hacia zona de interés; el caballo de batalla estadístico |
| Reversión en rango | *range fade / mean reversion* | Operar el rechazo del extremo hacia el centro del rango: WR alto, R:B corto, muere en rupturas |
| Barrida y giro | *sweep and reversal* | Entrada tras la barrida del pool, a favor del sesgo, con confirmación estructural |
| Gestión post-entrada | *trade management* | Reglas escritas de qué hacer con la posición abierta — incluida la abstención |
| Profit Factor | *profit factor* | Ganancia bruta ÷ pérdida bruta = WR×W̄ / ((1−WR)×L); objetivo ≥ 1,5; > 3 en muestra corta es sospecha |
| Curva de capital | *equity curve* | Serie acumulada de R en orden temporal; su forma (pendiente, valles, recuperación) vale más que un número suelto |
| Drawdown máximo | *maximum drawdown (max DD)* | Mayor caída pico-a-valle de la curva de capital; en R con riesgo fijo: la métrica de lo que soportaste |
| Racha de pérdidas | *losing streak* | Serie consecutiva de pérdidas; P = (1−WR)ⁿ y es esperable, no excepcional |
| WR de equilibrio | *breakeven win rate* | WR que hace E = 0 para un R:B dado: 1/(1+R:B); 1:2 → 33,3 % |
| Robustez | *robustness* | Capacidad de mantener E fuera de la muestra donde las reglas surgieron; el único test que importa |
| Sobreoptimización | *overfitting / curve fitting* | Ajustar reglas a las particularidades del pasado hasta que el backtest brilla y el futuro castiga; se infla ≈ √(k/N) |

## 🔗 Referencias

- [SYLLABUS.md § 6 — N2, Módulo 7](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — catálogo de estrategias (003 · M3) reordenado en arquetipos, y vacío D6 (data-mining) convertido en criterio de robustez
- [Módulo 6 · Indicadores y Confluencias](../mod-06-indicadores-y-confluencias/README.md) — anterior: tu dashboard entra al sistema como componente
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — el caso maestro: un sistema de una sola operación que este módulo generaliza
- [🏆 Evaluación Nivel 2 · examen-n2](../../03-recursos/evaluaciones/examen-n2.md) — siguiente: la evaluación de cierre del N2 (30 preguntas + socráticas)
- [Módulo 8 · Gestión del Riesgo](../mod-08-gestion-del-riesgo/README.md) — el siguiente nivel: donde el componente 9 de tu sistema se formaliza con matemática exacta (calculadora, topes de cartera y frenos en cascada)
