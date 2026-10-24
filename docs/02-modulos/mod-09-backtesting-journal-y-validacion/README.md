# Módulo 9 · Backtesting, Journal y Validación — la convicción estadística y la auditoría propia

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada aquí constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 3 · Gestión — segundo módulo del N3 |
| 📦 Módulo | 9 de 12 (FIT-12) |
| 🔬 Trazabilidad | 004 · M7.1–7.3 · 003 · M6.6 · **Aporte propio:** journal con taxonomía de errores estandarizada y protocolo de revisión semanal/mensual (vacío 3), advertencia de data-mining (D6 del informe) |
| ⏱️ Duración estimada | 6–8 h de teoría + 15–25 h de laboratorio/misión (3–4 semanas reales) |
| 📋 Estado | 🟢 Publicado (Sprint 9) |

---

## 🎯 Objetivo del Módulo

Convertir expectativas en evidencia y montar la auditoría interna que sostendrá la carrera. El M7 aprobó tu Sistema v1.0 por **completitud y explicitud** — nunca por rentabilidad — y el M8 le instaló el presupuesto (calculadora, topes, frenos). Este módulo fabrica lo único que falta: **convicción estadística**. El backtest ciego de 100 operaciones convierte tu "espero que gane el 40 %" en una medición con intervalo de confianza (±9,6 pp a N=100, la mitad del error que tenías a N=30); las métricas del reporte (9.3) convierten 100 filas en una página con zonas verdes y rojas pintadas antes de mirar; el forward testing (9.4) mide lo que el backtest no puede ver — el spread vivo, el slippage y tu propia ejecución. Y como toda esa evidencia vale lo que vale el registro que la produce, el módulo monta la infraestructura de auditoría: el **journal profesional v1** con taxonomía de errores E0–E7 y la distinción central del negocio (**pérdida ≠ error**, 9.5), más el protocolo de **revisión semanal y mensual** que decide cuándo tocar el sistema — y cuándo NO (9.6). Al terminar tienes un sistema medido, un registro que no miente y un calendario de mantenimiento: el paquete completo que la Evaluación N3 (al cierre del M10) auditará.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 9.1 | [Epistemología del backtesting](leccion-9-1.md) | Por qué N ≥ 100 (IC: ±17,5 % a 30 → ±9,6 % a 100); la ceguera como requisito; los 3 sesgos: supervivencia, data-mining, look-ahead | 45–60 min |
| 9.2 | [Protocolo de backtesting manual](leccion-9-2.md) | Definición operativa de setup válido; la rutina por operación paso a paso; cuándo parar (y cuándo NO) | 50–65 min |
| 9.3 | [Métricas del reporte](leccion-9-3.md) | Las 13 métricas con fórmulas y umbrales; los costes hunden el PF de 1,40 a 1,25; la decisión de 3 vías | 60–75 min |
| 9.4 | [Forward testing en demo](leccion-9-4.md) | El embudo de la evidencia: backtest → demo forward → real micro; los 4 huecos que el backtest no ve | 40–55 min |
| 9.5 | [El Journal profesional](leccion-9-5.md) | Del v0 al v1: campos mínimos + taxonomía E0–E7; **pérdida ≠ error** como etiqueta central; la deriva R planificado vs real | 50–65 min |
| 9.6 | [Revisión semanal y mensual](leccion-9-6.md) | Las 5 preguntas de auditoría; la regla de UNA mejora; la ventana de modificación y su lista negra | 45–60 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo se estudia **con tu Sistema v1.1 (M7+M8) y tu calculadora de sizing abiertas en paralelo**: 9.1–9.3 preparan el laboratorio, 9.4 marca la ruta del embudo, y 9.5–9.6 construyen la infraestructura que convierte cada operación futura en dato auditable.
>
> **El caso maestro entra al laboratorio:** la operación de tu [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) *(ilustrativo)* — EUR/USD H4, entrada 1,0820, SL 1,0788, TP 1,0886, 0,06 lotes, 19,20 $ de riesgo — deja de ser un ejemplo y se convierte en **una fila del journal v1** entre otras 99. Su sistema (el híbrido 2+4, pullback en tendencia con barrida) es el objeto de estudio: WR declarado 40 %, R:B 2,1 → esperanza bruta $E = +0{,}24R$, que los costes (~0,08R) llevan a **+0,16R neto** — y ese número, con su intervalo, es lo que las 100 operaciones confirmarán, corregirán o refutarán.
>
> **Puente con M8 y M10:** del M8 heredas la métrica que se audita aquí — *disparos ejecutados / disparos debidos = 100 %* — y los umbrales que el Max DD medido reemplaza (la línea de emergencia −15 % ya no se estima: se mide). Hacia M10: el estado emocional pre/post del journal v1 es la semilla del diario emocional, y las etiquetas E1/E6 son las señales tempranas de tilt que la psicología científica tratará; la **Evaluación N3** (al cierre del M10) audita los 100 backtests validados + 10 sesiones forward con journal completo.

## 🧪 Laboratorio · Backtesting ciego de 100 operaciones

**Materiales:** las 6 lecciones + tu Sistema v1.1 impreso (1 página, M7) + la [plantilla journal v1](../../../journal/plantilla_journal_v1.md) (CSV + guía) + la calculadora de sizing (M8) + Bar Replay de tu plataforma + la [calculadora de métricas del programa](../../../scripts/core/metricas_backtest.py) como oráculo de verificación.

**El protocolo en 4 líneas:**

1. **Declara antes de medir** (9.1): hipótesis (WR esperado, R:B, E), métricas del reporte, N=100 y coste estimado por operación — por escrito, con fecha. Después ya no se toca nada.
2. **Ejecuta la rutina de 9.2** vela a vela, con ceguera estricta (nunca decisiones con el futuro visible): 8–10 sesiones de 10–15 operaciones, máximo — la fatiga contamina el registro.
3. **Registra TODO en el journal v1** (9.5): toda operación entra al dataset — incluidas las incómodas, con su etiqueta E0–E7 en caliente. Las 30 repeticiones del M7 **no cuentan**: se hicieron para aprender el oficio (observador en entrenamiento); la muestra oficial es 100 nuevas con protocolo estricto.
4. **Cierra con el reporte** (9.3): las 13 métricas + curva de capital dibujada + la decisión de 3 vías (verde / ámbar / rojo). Verifica tu hoja contra la calculadora Python del programa.

**Reglas de oro del backtest** *(los 4 candados, resumidos)*: N declarado antes y no negociable a mitad · métricas declaradas antes (anti data-mining, D6) · cero operaciones fuera del dataset · cero modificaciones al sistema durante la muestra. Las dudas se anotan en el diario del backtester con fecha — no se resuelven cambiando reglas en vuelo.

**Entregable:** `journal/plantilla_journal_v1.csv` (o su hoja de cálculo) con 100 filas completas + capturas de las señales + curva de capital + el reporte de la [Misión M-9](#-misión).

## 🎯 Misión

> [!IMPORTANT] Misión M-9 · Reporte estadístico + 3 conclusiones documentadas
> **Objetivo:** convertir tu journal de 100 filas en el reporte de una página que decide, y en las 3 conclusiones que alimentarán la versión v1.2 del sistema.
> **El reporte mínimo** *(plantilla — cópiala en `journal/reporte-m9.md`)*: N operado · WR medido + IC 95 % · R:B medio · E bruto · coste medio por op · E neto · WR de equilibrio neto · PF bruto · PF neto · racha máxima medida (vs la esperada ~9) · Max DD medido (vs la línea −15 % de M8) · disparos ejecutados/debidos · curva de capital. Cada métrica con su **umbral declarado antes** (tabla de 9.3) y su veredicto verde/ámbar/rojo.
> **Las 3 conclusiones** (mínimo, en el mismo documento): (1) qué dice el dato MÁS débil del reporte; (2) qué UNA cosa de ejecución corriges la próxima semana (9.6: la regla de UNA mejora); (3) la decisión de versión: v1.2 con UNA modificación (ventana mensual + re-test de 50–100 backtests) **o** la decisión escrita de NO tocar nada — ambas son resultados válidos; la ausencia de decisión, no.
> **Revisión semanal simulada con el agente:** agenda una sesión socrática (30 min) con tu agente auditor usando tu primera semana del backtest como material: tú presentas el acta semanal (6 pasos de 9.6), el agente hace las preguntas incómodas (etiquetas evitadas, métricas "olvidadas", decisiones no documentadas).
> **Entregable:** `journal/reporte-m9.md` con las 13 métricas + veredictos + 3 conclusiones + el acta de la revisión simulada + changelog v1.2 (o la abstención firmada). **Tiempo estimado:** 2–3 h tras cerrar las 100 operaciones.

## ✅ Evaluación / Criterio de Graduación

Criterio del SYLLABUS para este módulo — la evidencia antes de la psicología, porque M10 se estudia sobre datos, no sobre esperanzas:

- **100 operaciones registradas** con el journal v1 completo (sin campos vacíos, etiqueta en caliente, capturas de señal).
- **Reporte estadístico completo** (las 13 métricas con umbrales + curva + decisión de 3 vías) y las 3 conclusiones documentadas con su changelog v1.2 o abstención firmada.
- **Revisión semanal simulada con el agente:** acta presentada, preguntas incómodas respondidas con datos del journal.
- **Quiz de graduación de este módulo: ≥ 8/10 (80 %)**.

Al aprobar todo: se abre [M10 · Psicotrading Científico](../mod-10-psicotrading-cientifico/README.md) — donde el journal que montaste aquí entrega su cosecha: tus etiquetas E1/E6 y tus emocionales pre/post son la materia prima del diagnóstico. La **Evaluación N3** (cierre del M10) exigirá: 100 backtests validados + 10 sesiones forward con journal completo + entrevista socrática de graduación (casos de tilt, FOMO y pérdida en plan).

## 📝 Quiz de Graduación — umbral ≥ 8/10 (80 %)

1. Epistemología: explica por qué N ≥ 100 usando el intervalo de confianza (compara ±17,5 % a N=30 con ±9,6 % a N=100) y por qué el backtest es "comprar experiencia" sin quemar inventario. ¿Qué decisión estructural autoriza la muestra y cuál sigue pendiente hasta el forward?
2. Define con tus palabras los 3 sesgos (supervivencia, data-mining, look-ahead) y da un ejemplo concreto de CÓMO aparecería cada uno en TU backtest de 100 operaciones, con el antídoto correspondiente.
3. Look-ahead aplicado: un backtester decide comprar cuando "el precio respeta el nivel" usando el high/low de la vela en formación y confirma con el volumen final de esa misma vela. Identifica los 2 errores, explica qué contamina y formula la regla de la vela cerrada que los elimina.
4. Setup válido: formula la definición operativa con los componentes 1–8 de tu v1.1, explica por qué "la duda es un no" protege la muestra, y describe qué pasa con una señal válida que NO ejecutaste (¿entra al journal? ¿como qué?).
5. Cálculo completo: 10 operaciones — 4 ganadoras de +2,0R, +1,8R, +2,4R, +2,2R; 6 perdedoras de −1R; coste 0,08R por op. Calcula WR, R:B medio, E bruto, E neto, PF bruto y PF neto. ¿Qué porcentaje de la E bruta se comen los costes?
6. Umbrales: con R:B 2,1 y coste 0,08R, demuestra que el WR de equilibrio sube de 32,3 % (bruto) a 34,8 % (neto). ¿Qué consecuencia tiene eso sobre la zona ámbar de la tabla de decisión de 3 vías?
7. Rachas: con WR 40 %, calcula la racha máxima esperada en 100 operaciones (fórmula ln) y su drawdown al 1 %. Tu muestra mide una racha de 14: ¿cuál es la respuesta del programa (3 pasos), y por qué NO es "cambiar el sistema"?
8. Forward: enumera los 4 huecos que el backtest no puede ver y explica cómo mide cada uno el demo forward. ¿Qué significa que las métricas forward estén "dentro de los intervalos" del backtest, y qué haces si el forward da WR 55 % vs 40 % del backtest?
9. Journal: clasifica con etiqueta (E0–E7) estas 5 operaciones y justifica: (a) pérdida −1R con SL respetado y sizing correcto; (b) ganancia +2R tomada "a ojo" fuera de zona, sin setup; (c) pérdida −1R tras mover el SL "para darle espacio"; (d) pérdida −1R operada con la cascada de frenos en nivel 2 activo; (e) ganancia +1R donde la orden se envió con el lote equivocado (0,10 en vez de 0,06). ¿Cuál de las 5 es la MÁS peligrosa para tu carrera y por qué?
10. Integración: tu reporte M-9 cierra con WR 37 % (IC ±9,6 → [27,4 %, 46,6 %]), PF neto 1,22, racha máxima 11 (−10,4 %), disparos 98/100. Con la tabla de 3 vías y el protocolo de 9.6: ¿qué decisión tomas HOY, qué entra en el changelog, qué se entrena en la semana y qué NO se toca? Justifica cada pieza con la lección que la respalda.

<details>
<summary>Ver clave de respuestas</summary>

1. El IC 95 % del WR es $1{,}96\sqrt{WR(1-WR)/N}$: a N=30 → ±17,5 pp (un WR medido 40 % puede ser 22,5–57,5 %: inútil para decidir); a N=100 → ±9,6 pp (30,4–49,6 %: la decisión empieza a ser posible). N=100 es el mínimo del programa para la primera decisión estructural porque es el punto donde el intervalo deja de cruzar ampliamente el equilibrio en sistemas razonables. El backtest es "comprar experiencia" porque 100 operaciones en Bar Replay cuestan 15–25 h y cero inventario; las mismas 100 en vivo al 1 % podrían costar una racha de −9 % y meses de calendario. La muestra autoriza la decisión de 3 vías del backtest (aprobar al 1 % / provisional a 0,25–0,5 % / no operar); la aprobación para real micro sigue pendiente del forward (9.4), que mide ejecución y costes vivos.
2. Supervivencia: descartar del dataset las operaciones "estúpidas" o los intentos incómodos — la muestra queda hecha de sobrevivientes y la E se infla; antídoto: todo entra, todo se etiqueta. Data-mining: probar 10 variantes del sistema y reportar la mejor (o ajustar reglas a mitad de muestra); antídoto: métricas, N e hipótesis declarados antes (candados de 7.6 y D6). Look-ahead: decidir usando información que no existía en la vela de decisión (el close final, el volumen final, niveles dibujados con el futuro); antídoto: replay estricto vela a vela y regla de la vela cerrada.
3. Error 1: el high/low de la vela en formación NO existe todavía en vivo — usarlo para "respeto del nivel" es leer el futuro; en replay además el nivel "perfecto" suele dibujarse a ojo sabiendo dónde fue el giro. Error 2: el volumen final de la vela no se conoce hasta el cierre. Contaminación: las señales parecen mejores que en vivo — la E del backtest se infla y el forward castiga. Regla: toda condición del setup se evalúa SOLO con velas cerradas; la vela de decisión se procesa cuando cierra (captura en ese momento).
4. Setup válido = TODAS las condiciones de los componentes 1–8 del v1.1 verificables sí/no en la vela de decisión (con la captura como evidencia). La duda es un no porque un criterio interpretativo en caliente no es una regla (test del clon): si cada duda la resuelves a favor de operar, tu WR medido mide tu optimismo, no el sistema. La señal válida no ejecutada SÍ entra: se registra como no-disparo en el acta semanal (disparos debidos vs ejecutados — la métrica de M8); no genera fila de operación en el CSV, pero sí línea en el registro de señales rechazadas con la razón.
5. WR = 4/10 = 40 %. R:B medio = (2,0+1,8+2,4+2,2)/4 = 2,1R. E bruto = 0,4×2,1 − 0,6×1 = +0,24R. E neto = 0,4×2,02 − 0,6×1,08 = 0,808 − 0,648 = +0,16R. PF bruto = 8,4/6 = 1,40. PF neto = 8,08/6,48 = 1,25. Los costes se comen 0,08/0,24 = **33 % de la esperanza bruta** — por eso 7.4 dijo que el coste "mata primero" y el reporte lo audita siempre.
6. Con coste c en R: WR×(R̄−c) = (1−WR)×(1+c) → WR* = (1+c)/(R̄+1) = 1,08/3,10 = 34,8 % (bruto: 1/3,1 = 32,3 %). Consecuencia: la zona ámbar se ENGARGOLA por arriba (el equilibrio real está más alto de lo que dice el R:B nominal) — un WR medido 34 % parece "sobre equilibrio" bruto pero está BAJO el neto: es rojo, no ámbar. Los umbrales siempre netos de coste.
7. Racha esperada: ln(100)/ln(1/0,6) = 4,605/0,511 ≈ 9; drawdown al 1 %: 0,99⁹ = 0,9135 → −8,6 % (dentro de la herida normal de M8). Respuesta ante 14: (1) verificar integridad del dato (¿coste, registro, régimen del período?) — no impulsividad; (2) comparar con la distribución: P(racha puntual de 14) = 0,6¹⁴ ≈ 0,08 % — con ~90 ventanas en 100 ops sigue siendo raro (≈ 5-7 %): es señal de sospecha documentada, no de acción inmediata; (3) decidir en la ventana mensual con el protocolo de 9.6 — si el régimen cambió, la evidencia lo mostrará con más datos; cambiar reglas en caliente es data-mining en vivo.
8. Los 4 huecos: spread vivo en el momento de la señal (el forward lo mide op por op vs el 0,08R estimado), slippage del SL (gaps/noticias — se registra la diferencia precio SL vs precio de ejecución), tu ejecución (disparos debidos vs ejecutados + deriva R planificado vs real), infraestructura (fallos de plataforma/conexión — se cuentan los incidentes). "Dentro de los intervalos": el WR forward no tiene que salir mejor — tiene que caer dentro del IC del backtest (ej. 30,4–49,6 %) y el PF neto cerca del medido. WR forward 55 % con N=20 (IC ±22 pp): no se celebra ni se escala — la muestra no autoriza nada; se sigue midiendo y se revisa si el régimen o la selección de señales cambió (¿filtraste sin darte cuenta?).
9. (a) **E0** — pérdida en plan: coste estadístico del negocio, no error. (b) **E1** — operar sin setup. (c) **E3** — SL manipulado. (d) **E6** — freno ignorado. (e) **E4** — sizing fuera de presupuesto. La más peligrosa: la (b) — la ganancia fuera de plan: refuerza y premia el circuito equivocado (el cerebro aprende "así se gana"), mientras las pérdidas erróneas dejan dolor que invita a corregir; una ganancia E1 repetida construye un trader sin sistema que cree tener uno. (La lección 10.4 lo formalizará: una ganancia fuera de plan es más peligrosa que una pérdida en plan.)
10. Decisión de 3 vías: WR 37 % está en [34,8, 40) neto → zona ámbar (no rojo: 37 > 34,8 equilibrio neto; no verde: < 40) → **provisional**: sigue en demo/0,25–0,5 %, sin escalar. Changelog: NO entra modificación estructural (el IC cruza el equilibrio: la evidencia no autoriza cambios — y menos desde el ámbar); el acta mensual documenta la decisión de seguir midiendo (v1.1 permanece). Se entrena en la semana (regla de UNA mejora, de ejecución): los 2 disparos debidos no ejecutados — revisar el bloqueo (¿freno mal calibrado, miedo, checklist?). NO se toca: el sistema (reglas 1–8), el sizing estructural, y nada "inspirado" en la racha de 11 (dentro de lo esperable a N=100 con WR 40 %). Respaldos: 9.3 (tabla de 3 vías), 9.6 (ventana + regla de UNA), 9.1 (el IC prohíbe decisiones estructurales), M8 (la métrica de disparos).

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| Backtesting | *backtesting* | Medición con protocolo del comportamiento de un sistema sobre datos históricos: la única forma ética de comprar experiencia sin quemar inventario |
| Backtest ciego | *blind backtesting* | Replay vela a vela sin ver el futuro; toda condición se evalúa solo con velas cerradas |
| Sesgo de supervivencia | *survivorship bias* | Quedarse solo con lo que funcionó (operaciones, variantes, mercados) y falsificar la muestra; antídoto: todo entra y se etiqueta |
| Data-mining | *data mining / curve fitting* | Buscar la variante que mejor salió en el pasado (o ajustar a mitad de muestra) hasta que el backtest brilla y el futuro castiga; candado: métricas y N declarados antes |
| Look-ahead bias | *look-ahead bias* | Decidir con información que no existía en la vela (close/volumen final, niveles dibujados a futuro); antídoto: vela cerrada |
| Tamaño muestral | *sample size (N)* | Número de operaciones de la muestra; el error del WR escala con 1/√N: 100 es el mínimo del programa para decisiones estructurales |
| Intervalo de confianza | *confidence interval (CI)* | Rango donde vive el parámetro real con 95 % de confianza: ±1,96√(WR(1−WR)/N); a N=100, ±9,6 pp |
| Setup válido | *valid setup* | Todas las condiciones de los componentes 1–8 del sistema verificables sí/no en la vela de decisión; la duda es un no |
| Protocolo de backtesting | *backtesting protocol* | La rutina fija por operación (9 pasos) + las listas PRE/POST que hacen las 100 filas comparables entre sí |
| R:B medio | *average R:B* | Media de las ganadoras en R; junto al WR define la E bruta |
| Coste medio por operación | *average cost per trade* | Spread + slippage en R (típico 0,06–0,1R); el ladrón silencioso que se come ~1/3 de la E bruta |
| Esperanza neta | *net expectancy* | E bruto − coste medio: el motor real del negocio; en el caso maestro +0,24R → +0,16R |
| WR de equilibrio neto | *net breakeven win rate* | WR* = (1+c)/(R̄+1) con coste c: con R:B 2,1 y c 0,08 → 34,8 % (el bruto decía 32,3 %) |
| Distribución de rachas | *streak distribution* | Conteo de rachas de la muestra vs lo esperado P(n)=(1−WR)ⁿ; en 100 ops con WR 40 %, racha esperada ~9 |
| Racha máxima medida | *measured max streak* | La peor secuencia de pérdidas de la muestra; > 14 con WR 40 % es sospecha de régimen (ventana mensual, no pánico) |
| Forward testing | *forward testing* | Prueba del sistema con datos vivos en tiempo real: mide lo que el backtest no puede (spread vivo, slippage, ejecución) |
| Demo forward | *demo forward* | Fase 2 del embudo: mismo sistema, datos vivos, cuenta demo, N mínimo 20–30; el puente honesto antes del dinero |
| Real micro | *micro real account* | Fase 3 del embudo: dinero real con riesgo 0,25–0,5 %; en este programa abre tras M12 (Fase 4) |
| Journal profesional | *trading journal (v1)* | La caja negra del negocio: campos mínimos + captura de señal + etiqueta de error en caliente + emocional pre/post |
| Taxonomía de errores | *error taxonomy* | E0 en plan · E1 sin setup · E2 entrada fuera de regla · E3 SL manipulado · E4 sizing fuera · E5 gestión improvisada · E6 freno ignorado · E7 ejecución técnica |
| Pérdida ≠ error | *loss ≠ mistake* | La pérdida en plan (E0) es el coste estadístico del negocio; el error es la desviación del proceso; una ganancia fuera de plan ES un error — y es el más peligroso |
| Deriva de ejecución | *execution drift* | Diferencia sistemática entre R planificado y R real (o entre disparos debidos y ejecutados): diagnóstico de ejecución, no del sistema |
| Revisión semanal | *weekly review* | Protocolo de 6 pasos (30–45 min): leer la semana, contar etiquetas, 5 preguntas, disparos, UNA conclusión, decisión documentada o abstención |
| Ventana de modificación | *modification window* | El único momento legítimo donde el sistema cambia: fin de mes + evidencia con N + UNA modificación por vez + re-test |
| Changelog del sistema | *system changelog* | Registro firmado de versiones v1.x: fecha, evidencia, la modificación única y el plan de re-test |

## 🔗 Referencias

- [SYLLABUS.md § 6 — N3, Módulo 9](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — trazabilidad 004 · M7.1-7.3 y 003 · M6.6; aportes propios: taxonomía de errores + revisión semanal/mensual (vacío 3), advertencia de data-mining (D6)
- [Módulo 8 · Gestión del Riesgo](../mod-08-gestion-del-riesgo/README.md) — anterior: el presupuesto y los frenos que este módulo audita con datos
- [Sistema v1.0 → v1.1 (M7)](../mod-07-construccion-del-sistema/README.md) — el objeto de estudio: los componentes 1–8 definen el setup válido
- [Plantilla journal v1](../../../journal/plantilla_journal_v1.md) — el CSV + la guía de la taxonomía E0–E7 y las actas
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — el caso maestro: hoy entra al laboratorio como fila 1
- [scripts/core/metricas_backtest.py](../../../scripts/core/metricas_backtest.py) — la calculadora de métricas del programa: oráculo de verificación del reporte
- [Módulo 10 · Psicotrading Científico](../mod-10-psicotrading-cientifico/README.md) — el siguiente: sobre tus datos, no sobre tus esperanzas; cierra el N3 con la [Evaluación N3](../../03-recursos/evaluaciones/examen-n3.md)
