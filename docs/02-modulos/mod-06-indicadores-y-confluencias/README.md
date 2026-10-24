# Módulo 6 · Indicadores y Confluencias — Catálogo Crítico

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada en este repositorio constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 2 · Técnica |
| 📦 Módulo | 6 de 12 (FIT-12) |
| 🔬 Trazabilidad | 004 · M4.1–4.5 · 003 · M3.3–3.4 · **Aporte propio:** radar de fiabilidad por evidencia (incl. etiqueta pseudocientífica para lo exógeno), regla del máximo 3 indicadores |
| ⏱️ Duración estimada | 6–7 h de teoría + 8–10 h de laboratorio/misión/quiz |
| 📋 Estado | 🟢 Publicado (Sprint 6) |

---

## 🎯 Objetivo del Módulo

Usar indicadores como **medidores** (no oráculos), conocer los sistemas de canal clásicos y desarrollar el **radar** que separa herramienta de marketing. El M5 te dio el mapa (estructura, liquidez, zonas); este módulo pone instrumentos *sobre* el mapa: medias móviles como filtro de régimen (6.2), ATR como auditor del stop (6.3), osciladores como medidores de desaceleración (6.4), volumen y VWAP como registro de interés real (6.5), Fibonacci como contexto de descuento y el escepticismo entrenado ante Elliott y armónicos (6.6), el ciclo de Weinstein como vista de pájaro (6.7) — y el cierre: el radar de fiabilidad que clasifica todo el catálogo por evidencia y te obliga a un **dashboard de máximo 3 herramientas** (6.8). Al terminar, no añadirás más indicadores a tu gráfico: añadirás criterio para saber cuáles merecen estar y por qué.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 6.1 | [Filosofía del indicador](leccion-6-1.md) | El precio es primero; el indicador mide/deriva, no predice; las 4 familias; "indicador adelantado" no existe | 40–55 min |
| 6.2 | [Medias móviles](leccion-6-2.md) | SMA vs EMA; el sistema 20/50/200 (filtro macro + régimen + zona dinámica); golden/death cross y sus límites | 45–60 min |
| 6.3 | [Volatilidad y canales](leccion-6-3.md) | ATR (stops dinámicos, tamaño de rango, auditoría del SL); Bollinger ±2σ (squeeze, walking the bands); Donchian y las Tortugas | 45–60 min |
| 6.4 | [Momentum y osciladores](leccion-6-4.md) | RSI, Estocástico, MACD; sobrecompra/sobreventa dependen del régimen; divergencias: el uso más honesto | 45–60 min |
| 6.5 | [Volumen y perfil](leccion-6-5.md) | Volumen como registro de interés; VWAP ponderado; Volume Profile horizontal (POC, HVN/LVN); salvedad FX | 40–55 min |
| 6.6 | [Fibonacci, Elliott y armónicos](leccion-6-6.md) | Retrocesos como contexto (50–61,8 %), no como nivel; límites de la subjetividad de Elliott; por qué los armónicos exigen estadística extrema | 45–60 min |
| 6.7 | [Etapas de Weinstein](leccion-6-7.md) | El filtro macro de 4 etapas; prohibido comprar en Etapa 4; integración con los ciclos del M3 | 40–55 min |
| 6.8 | [Radar de fiabilidad y dashboard](leccion-6-8.md) | Clasificación final: evidencia / contextual / marketing (ciclos lunares, repintado); regla del dashboard máximo de 3 herramientas | 45–60 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo se estudia **con el gráfico abierto y cada indicador añadido de a uno**: activa la herramienta, mira qué mide sobre el caso, y desactívala — un medidor que vive fijo en el gráfico se vuelve decoración en una semana.
>
> **El mismo caso maestro, ahora con medidores:** las 8 lecciones vuelven sobre el movimiento didáctico de EUR/USD H4 *(ilustrativo)* de tu [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) y del [M5](../mod-05-estructura-de-mercado-y-liquidez/README.md): low 1,0745 → HL 1,0798 → BOS sobre 1,0860 → HH 1,0884 → pullback a la zona 1,0820–1,0824 con barrida a 1,0792, entrada 1,0820, SL 1,0788 (32 pips), TP 1,0886. Aquí descubrirás qué medían EMA, ATR, RSI, VWAP y el resto **en ese mismo instante** — y por qué ningún medidor cambió el plan que la estructura ya había dado.
>
> **Puente con M5:** la confluencia (5.6) exige factores *independientes*. Este módulo termina clasificando qué herramientas son independientes entre sí y cuáles son el mismo dato disfrazado dos veces — esa distinción es la diferencia entre confluencia y redundancia.

## 🧪 Laboratorio · Tu dashboard de confluencias (máx. 3 herramientas) probado en 50 movimientos

**Materiales:** TradingView con Bar Replay ([Lección 4.1](../mod-04-plataforma-y-primera-ejecucion/leccion-4-1.md)) + la plantilla de decisión del [Lección 6.8](leccion-6-8.md) + tu journal.

**Procedimiento:**

1. **Define el dashboard por escrito ANTES de probar** (regla anti data-mining, [D6](../../00-analisis/analisis_cursos.md)): 1 filtro de régimen + 1 medidor de volatilidad + 1 gatillo/contexto, cada uno con su regla de lectura explícita ("EMA 50 creciente y precio por encima = solo largos", "SL mínimo 1,5 × ATR", "RSI: buscar divergencia alcista en zona H1"). Justifica cada pieza con una lección del módulo, no con "me gusta".
2. **Declara tu métrica antes:** qué cuenta como acierto (el medidor y el mapa coinciden en dirección/zona) y qué como fallo, para cada uno de los 50 episodios.
3. **Selecciona 50 movimientos históricos a ciegas** (Bar Replay desde fechas que no recuerdes; 10 por mercado en EUR/USD, GBP/USD, XAU/USD, US100, BTC/USD). En cada uno: aplica el dashboard SIN ver el desenlace, escribe el veredicto del medidor y tu lectura estructural (M5), y solo entonces avanza.
4. **Registra en tabla:** mercado · fecha · lectura del medidor · lectura de estructura · coincidencia (Sí/No) · desenlace a favor/en contra.
5. **Añade el indicador candidato que más te tiente** (el de YouTube, el del anuncio): clasifícalo con el radar de 6.8 y pruébalo en 10 de los episodios ya anotados — casi siempre descubrirás que mide lo mismo que una de tus 3 piezas.

**Entregable:** `journal/laboratorio-m6.md` con el dashboard justificado, la métrica declarada y la tabla de 50 filas. El objetivo NO es demostrar que el dashboard "gana": es que las 3 herramientas salgan de memoria, con su regla de lectura por escrito, y que aprendas a detectar redundancia entre medidores.

## 🎯 Misión

> [!IMPORTANT] Misión M-6 · Informe comparativo de 3 herramientas
> **Objetivo:** evaluar **3 herramientas distintas sobre el mismo mercado** (elige 1 de los 5 del laboratorio) documentando acierto/fallo en tabla — tu primer informe de auditoría de herramientas.
> **Entregable:** `journal/mision-m6.md` con: (1) las 3 herramientas elegidas y su clasificación del radar (evidencia / contextual / marketing); (2) una tabla de al menos 30 episodios (10 por herramienta o 30 cruzadas, tu diseño — decláralo antes); (3) por herramienta: aciertos, fallos, y el tipo de fallo dominante (falso positivo en rango, retardo en tendencia, señal contra estructura); (4) conclusión honesta: ¿qué herramienta sobrevive a tu dashboard y por qué?
> **Criterio de aceptación:** métrica declarada ANTES de evaluar · las 3 herramientas sobre el MISMO conjunto de episodios (comparación justa) · cada fallo clasificado por tipo · ninguna conclusión sin número que la respalde.
> **Etiqueta en journal:** `mision-m6-radar` · **Tiempo estimado:** 2 semanas (el informe se escribe al final; la recolección corre en paralelo al laboratorio).
> **Regla de oro:** si una herramienta "acierta" el 90 %, sospecha de tu métrica antes de celebrar — el sesgo de confirmación evalúa indulgente. Pide al agente auditor una revisión de la tabla.

## ✅ Evaluación / Criterio de Graduación

Criterio del SYLLABUS para cerrar M6 y abrir M7:

- **Dashboard definido con justificación:** máximo 3 herramientas, cada una con regla de lectura explícita y anclaje a lección — sin justificación, el dashboard no existe.
- **Laboratorio completo:** 50 episodios registrados con la métrica declarada por adelantado.
- **Informe de misión:** las 3 herramientas comparadas sobre el mismo conjunto, fallos clasificados por tipo, conclusión con números.
- **Quiz de catálogo:** [10 preguntas del hub](#-quiz-de-graduación) — **≥ 8/10** (umbral estándar del N2).
- **Revisión con el agente:** defensa en vivo del dashboard: ¿por qué estas 3 y no otras? ¿qué mide cada una que las otras no? ¿dónde clasificaste la herramienta de moda y con qué evidencia?

Al aprobar todo: M6 🟢 y se abre [M7 · Construcción del Sistema](../mod-07-construccion-del-sistema/README.md) — donde tu dashboard aprobado entra como componente del **Sistema v1.0**, el primer entregable formal de tu negocio.

## 📝 Quiz de Graduación

1. Explica por qué ningún indicador es "adelantado". Usa la cadena precio → indicador y el argumento del arbitraje.
2. SMA vs EMA: diferencia de construcción, fórmula del suavizado exponencial (α), y por qué el EMA "miente" más en rango.
3. Enumera el rol de cada media del sistema 20/50/200 aplicado al caso maestro (valores del módulo: 1,0712 / 1,0771 / 1,0806).
4. Fórmula del rango verdadero (TR) y del ATR. Audita el SL de la receta: 32 pips con ATR(14) H4 de 21 pips — ¿cuántos ATR es, y en qué rango está "sano"?
5. ¿Qué mide el squeeze de Bollinger y qué anticipa (sin prometer)? ¿Por qué "tocó la banda inferior = compro" es falso en tendencia fuerte?
6. RSI: fórmula completa. Si la media de ganancias es 1,5× la media de pérdidas, ¿cuál es el RSI? ¿Por qué RSI 70 no es señal de venta en tendencia?
7. Divergencia regular alcista: definición exacta, por qué es el uso más honesto del oscilador, y qué información da "no hay divergencia" en el HH 1,0884 del caso.
8. VWAP: fórmula y por qué a las instituciones les importa. Calcula el VWAP de 3 tramos: (1,0815 × 1 200) + (1,0818 × 800) + (1,0822 × 1 500). ¿Qué salvedad tiene el volumen en FX spot?
9. Fibonacci: calcula los retrocesos 50 % y 61,8 % del swing 1,0798 → 1,0884. ¿En qué porcentaje del retroceso quedó la zona de la receta (1,0820–1,0824) y qué enseña ese desenlace sobre el Fib como nivel?
10. Las 4 etapas de Weinstein: nombre, carácter y qué se prohíbe en cada una. ¿Por qué "está barato" no justifica comprar en Etapa 4? Enumera las 3 piezas del dashboard máximo y justifica su independencia mutua.

<details>
<summary>Ver clave de respuestas</summary>

1. Todo indicador es una función del precio/volumen ya ocurrido: $I = f(P)$. No puede contener información que el precio no tenga, porque la deriva de él. Si existiera un preditor verificable, el arbitraje lo consumiría en segundos: quien lo usara movería el precio hasta neutralizarlo. Los "leading" son solo más sensibles (más ruido), no anticipadores.
2. SMA promedia N cierres por igual; EMA pondera más los recientes con $$EMA_t = \alpha P_t + (1-\alpha)EMA_{t-1}, \alpha = \frac{2}{N+1}$$. El EMA reacciona antes (menos retardo en tendencia) pero también gira antes sin motivo: en rango produce más cruces falsos que el SMA — más señal, más ruido, mismo dato.
3. EMA 200 ≈ 1,0712 creciente: filtro macro (solo largos). EMA 50 ≈ 1,0771: régimen intermedio (la tendencia de swimg semanal está viva). EMA 20 ≈ 1,0806: zona dinámica de referencia en pullbacks. La entrada 1,0820 estaba por encima de las tres, las tres con pendiente positiva: el filtro no bloqueó la operación.
4. $$TR = \max(H-L,\ |H-C_{prev}|,\ |L-C_{prev}|)$$ y ATR = media móvil del TR. 32 pips ÷ 21 pips ≈ 1,52 ATR — dentro del rango sano del programa (1,0–2,0 ATR): la estructura fijó el SL y el ATR lo auditó. Menos de 1 ATR: la respiración normal caza el stop; más de 2: el TP se aleja sin mejorar el motivo.
5. El squeeze es la contracción simultánea de ambas bandas = caída de σ = volatilidad comprimida; anticipa expansión (fase del ciclo M3), no dirección. En tendencia fuerte el precio "camina" sobre la banda (walking the bands): tocarla es medición de fuerza, no señal de giro — vender ahí es operar contra el régimen con un medidor de régimen.
6. $$RSI = 100 - \frac{100}{1+RS},\ RS = \overline{G}/\overline{P}$$ Con RS = 1,5: RSI = 100 − 100/2,5 = **60**. RSI 70 no es venta en tendencia porque el sobreexcitado momentum ES el régimen: en HH/HL sostenido el RSI puede vivir >70 muchas velas; la señal de venta la da la estructura (CHoCH), no el oscilador.
7. Divergencia regular alcista: precio marca LL pero el oscilador marca un low menos profundo — la pierna bajista pierde velocidad medible. Es honesta porque mide desaceleración (dato), no predice giro (interpretación), y porque obliga a esperar confirmación de estructura. En el HH 1,0884 "no hay divergencia" = el impulso sigue acelerando: información operativa — el pullback es continuación probable, no trampa.
8. $$VWAP = \frac{\sum p_i q_i}{\sum q_i}$$ Es el precio promedio REAL de ejecución de la sesión: es donde se promediaron las instituciones. (1,0815×1200 + 1,0818×800 + 1,0822×1500) / 3 500 = 3 786,54/3 500 ≈ **1,0819**. Salvedad FX: el spot es descentralizado — el volumen que ves es el feed de tu bróker (proxy), no el volumen global; se usa con humildad, no como verdad.
9. Swing 86 pips: 50 % → 1,0798 + 43 = **1,0841**; 61,8 % → 1,0798 + 53,1 ≈ **1,0831**. La zona de la receta (1,0820–1,0824) quedó en el **70–74 %** del retroceso — más profunda que la golden zone: el Fib solo no la habría marcado; la estructura (OB + pool) sí. Enseñanza: el Fib es contexto de descuento, no nivel de entrada — y la barrida a 1,0792 perforó el 100 %, lo que el Fib no explica pero la liquidez (5.3) sí.
10. Etapa 1 acumulación (rango tras caída: no operar rupturas falsas); Etapa 2 avance (tendencia: operar a favor); Etapa 3 distribución (techo: recoger, no abrir); Etapa 4 declive (prohibido comprar). "Barato" en Etapa 4 es la trampa del promedio descendente: la estadística del régimen (3.6) muestra que comprar contra markdown paga peor materia prima con el mismo riesgo. Dashboard máximo: (1) filtro de régimen (EMA 50/200 o Weinstein), (2) medidor de volatilidad (ATR → SL y tamaño), (3) gatillo/contexto (RSI-divergencias o volumen). Son independientes porque miden cosas distintas (dirección, amplitud, velocidad/interés): dos derivados del mismo dato no suman confluencia, suman redundancia.

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| Indicador | *indicator* | Transformación matemática del precio/volumen que mide una propiedad (dirección, amplitud, velocidad); nunca predice |
| Derivado del precio | *price-derived* | Dato calculado a partir del precio: comparte con él toda su información y ninguna adicional |
| Media simple | *simple moving average (SMA)* | Promedio aritmético de los últimos N cierres; retardo uniforme |
| Media exponencial | *exponential moving average (EMA)* | Media con ponderación α = 2/(N+1) a favor de los datos recientes; menos retardo, más nerviosa |
| Cruce dorado / de la muerte | *golden cross / death cross* | EMA 50 cruza arriba/abajo a la 200: confirmación tardía de régimen, no señal de entrada |
| Soporte dinámico | *dynamic support* | Media móvil que el precio respeta en tendencia como zona de pullback; se desplaza con ella |
| ATR | *average true range* | Media móvil del rango verdadero (TR): mide la amplitud típica del marco; audita SL y TP |
| Bandas de Bollinger | *Bollinger Bands* | SMA 20 ± 2σ: canal estadístico que mide desviación de la media; en tendencia se camina sobre ellas |
| Squeeze | *squeeze / band squeeze* | Contracción simultánea de las bandas (σ mínima): volatilidad comprimida antes de expansión |
| Canal de Donchian | *Donchian channel* | Máximo/mínimo de N periodos: canal de ruptura base del sistema de las Tortugas |
| RSI | *relative strength index* | Oscilador 0–100 del ratio de medias de ganancia/pérdida en N periodos; 70/30 solo significan en rango |
| Divergencia | *divergence* | Desacuerdo entre el extremo del precio y el del oscilador: medición de desaceleración del impulso |
| Estocástico | *stochastic oscillator* | Posición porcentual del cierre dentro del rango de N periodos (%K/%D); más rápido y ruidoso que el RSI |
| MACD | *moving average convergence divergence* | Diferencia EMA12 − EMA26 con línea de señal EMA9: momentum de dos velocidades |
| VWAP | *volume weighted average price* | Precio promedio ponderado por volumen de la sesión: el promedio real de ejecución institucional |
| Volume Profile | *volume profile* | Histograma horizontal de volumen por nivel de precio: dónde se construyó el interés |
| POC | *point of control* | El nivel con más volumen del perfil: el precio más "acordado" del periodo |
| Retroceso de Fibonacci | *Fibonacci retracement* | Partición porcentual del swing (38,2/50/61,8 %): contexto de descuento, no nivel exacto |
| Onda de Elliott | *Elliott wave* | Modelo de 5 impulsos + 3 correcciones; conteo subjetivo, baja falsabilidad práctica |
| Armónicos | *harmonic patterns* | Figuras de ratios anidados (Gartley, Bat); exigen muestras estadísticas fuera del alcance del negocio v1 |
| Repintado | *repainting* | Indicador que reescribe sus valores pasados: imposible de auditar — descalificado por construcción |
| Etapas de Weinstein | *Weinstein stages* | Ciclo de 4 fases (acumulación → avance → distribución → declive); filtro macro del marco D1 |
| Radar de fiabilidad | *reliability radar* | Clasificación del catálogo por evidencia: herramientas defendibles / contextuales / marketing |
| Dashboard de confluencias | *confluence dashboard* | Tu máximo de 3 herramientas con reglas de lectura explícitas: 1 régimen + 1 volatilidad + 1 gatillo |

## 🔗 Referencias

- [SYLLABUS.md § 6 — N2, Módulo 6](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — crítica a la sobreventa de indicadores (004 · M4) y vacíos D6 (data-mining) resueltos por el radar y la regla del máximo 3
- [Módulo 5 · Estructura de Mercado y Liquidez](../mod-05-estructura-de-mercado-y-liquidez/README.md) — anterior: el mapa sobre el que se colocan estos medidores
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — su SL de 32 pips es el caso de auditoría ATR de la Lección 6.3
- [Módulo 7 · Construcción del Sistema](../mod-07-construccion-del-sistema/README.md) — siguiente: el dashboard entra como componente del Sistema v1.0 (el asiento de régimen, el ATR del stop y el filtro de contexto ya tienen puesto asignado)
