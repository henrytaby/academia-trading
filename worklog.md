# worklog.md — Bitácora de Construcción (append-only)

---
Task ID: sprint-0
Agent: Z.ai (Mentor Trading + Knowledge Architect)
Task: Análisis forense de los 2 cursos base + estructura del repo + agents.md + SYLLABUS.md

Work Log:
- Recibidos y analizados `003_trading_completo_2026_guia_completa.html` (TradingLab, 7 módulos, 7h39m) y `004_la_industria_del_trading_guia_completa.html` (Sáenz & Ruiz, 10 módulos, 11h55m)
- Verificación de datos clave en los HTML fuente (estadísticas de prop firms 92%/0.072%, sesiones por "Día", catálogo de estrategias)
- Emitido informe ATR-001 con: fortalezas/debilidades por curso, comparativa por áreas, insumos adoptados, 9 vacíos curriculares y correcciones técnicas
- Diseñado el programa FIT-12: 4 niveles × 12 módulos con laboratorios, misiones y evaluaciones por nivel
- Escrito agents.md v1.0: 5 roles expertos, protocolo pedagógico socrático, workflow de sprints, formatos estándar, checklist de calidad, límites éticos y comandos rápidos
- Creada la estructura completa del repo con placeholders (mod-01, glosario, journal/, scripts/core/)

Stage Summary:
- Decisiones: enfoque universal (fiscalidad por principios), ES + EN técnico, un sprint por módulo, riesgo con veto del rol Chief Risk Officer, nomenclatura PA/SMC unificada
- Artefactos: agents.md, README.md, worklog.md, docs/00-analisis/analisis_cursos.md, docs/01-syllabus/SYLLABUS.md, docs/03-recursos/plantillas/PLANTILLA_MODULO.md, docs/03-recursos/glosario.md, docs/02-modulos/mod-01-negocio-trading/README.md, journal/README.md, scripts/core/README.md
- Siguiente paso: Sprint 1 — construir Módulo 1 completo (6 lecciones + laboratorio + misión + evaluación)

---
Task ID: sprint-1
Agent: Z.ai (Mentor Trading + Pedagogical Coach + Knowledge Architect)
Task: Construcción completa del Módulo 1 · El Trading como Negocio y Ciencia

Work Log:
- Leídos SYLLABUS.md §5 (definición del M1), PLANTILLA_MODULO.md y el protocolo de sprint §5.2 de agents.md
- Redactadas las 6 lecciones (`leccion-1-1.md` … `leccion-1-6.md`) con el formato §6.2 completo: por qué importa → concepto → analogía → cómo se hace → error común → conexión cuantitativa, más puntos clave y autoevaluación con respuestas ocultas (`<details>`)
- Construido el README del módulo como hub: índice de lecciones, laboratorio de auditoría personal (5 pasos), misión M-1 (Carta de Expectativas de 4 secciones + contrato anti-ludopatía de 10 cláusulas), quiz de graduación de 10 preguntas con clave de respuestas, glosario de 38 términos y referencias
- Actualizado el glosario maestro (`docs/03-recursos/glosario.md`) con los 38 términos de M1
- Actualizada la tabla de estado del README raíz (M1 → 🟢 Publicado; M2 marcado como Sprint 2 siguiente)
- Auto-auditoría con checklist §7 de agents.md: corregidos un link roto a mod-02 (aún no existe), un ancla de GitHub imprecisa, la errata "sensaciación" y una inconsistencia numérica en la pregunta 2 del quiz (la opción B ahora es rentable con E=+6)
- Verificación numérica de todos los ejemplos cerrados: E de los sistemas A/B/C/D, breakeven WR=1/(1+R), tabla WR×R:B, 0,6⁹≈1 %, 0,95³⁰≈21 %, 0,85³⁰≈0,8 %, racha de 8 pérdidas ≈80 % en 100 operaciones (aproximación por ventanas)

Stage Summary:
- Artefactos: 6 archivos de lección + README del módulo completo + glosario maestro poblado (38 términos) + README raíz actualizado
- Decisiones: lecciones como archivos separados (permitido por §6.2 "archivo o sección") para sesiones de estudio manejables y navegación con enlaces anterior/siguiente; quiz con clave de respuestas oculta para autoestudio honesto; contrato anti-ludopatía como texto copiable con firma y fecha; lema "de ~720 combinaciones, 719 son incorrectas para ti" como heurística que conecta con la regla anti-719 de M12
- Estado: M1 🟢 Publicado. Siguiente paso: sesión de estudio de la Lección 1.1 con el estudiante; Sprint 2 (M2 · El Motor del Precio) solo tras aprobar M1 (quiz ≥ 8/10 + misión M-1 entregada en journal/)

---
Task ID: revision-0
Agent: Z.ai (Mentor Trading + Chief Risk Officer)
Task: Revisión de Sprint 0 con el estudiante + evaluación de propuesta práctica ("mi primera operación")

Work Log:
- Presentado el paquete Sprint 0 al estudiante (SYLLABUS.md, agents.md, analisis_cursos.md, README, worklog, PLANTILLA_MODULO)
- Decisión del estudiante: temario FIT-12 v1.0 APROBADO
- Propuesta del estudiante: tutorial tipo "receta" — tu primera operación paso a paso, por mercado, muy tangible ("ganar el primer dólar")
- Evaluación del panel: idea validada pedagógicamente; el hueco natural ya existe en el temario (M4 · Plataforma y Primera Ejecución, §4.5 cuenta demo + misión de 10 operaciones demo)
- Veto parcial del CRO: el marco "ganar el primer dólar" como objetivo queda reemplazado por "primera operación PROCESADA de principio a fin (en demo)"; el primer dólar real se mantiene en F4 (tras M9-M12) con riesgo micro 0,25-0,5 %
- Propuesta presentada: recurso transversal "La Receta de tu Primera Operación" en docs/03-recursos/laboratorio/receta-primera-operacion.md — receta maestra EUR/USD + fichas de variación (XAU/USD, índices), 12 pasos numerados de apertura de demo a revisión en journal, referenciado desde M4 en el SYLLABUS

Stage Summary:
- Estado: temario v1.0 aprobado por el estudiante; propuesta de receta presentada, pendiente de visto bueno (construcción sugerida: Sprint 4, junto con M4)
- Siguiente paso: si el estudiante aprueba, añadir el recurso al SYLLABUS (referencia en §M4 y §recursos) y construirlo en Sprint 4

---
Task ID: sprint-1.5
Agent: Z.ai (Mentor Trading + Chief Risk Officer + Knowledge Architect)
Task: Integración del recurso "La Receta de tu Primera Operación" en el temario + construcción del recurso

Work Log:
- Recibida la aprobación del temario v1.0 por el estudiante ("temario aprobado") y su propuesta de un tutorial tipo receta ("mi primera operación paso a paso, por mercado, ganar el primer dólar")
- Evaluación del panel: idea validada; hueco natural = M4; veto parcial del CRO al marco "primer dólar" → objetivo redefinido como "primera operación PROCESADA" (SL antes de entrar, registrada, revisada 6/6)
- SYLLABUS v1.0 → v1.1: añadida la línea de Recurso en §M4, actualizado roadmap (Sprint 1.5 ✅, Sprint 2 🔜) y Registro de Versiones
- Creado docs/03-recursos/laboratorio/receta-primera-operacion.md: 12 pasos (0-11) con verificaciones por paso, Parte 0 de due diligence de bróker sin marcas, receta maestra EUR/USD sesión Londres-NY con horas Bolivia (UTC-4), fichas de variación XAU/USD e índices, caja "¿Y mi primer dólar?" (etapas demo → demo forward → real micro F4), checklist imprimible
- Números verificados: lote = riesgo$/(SL_pips × valor_pip): 20$/30 pips → 0,066 → 0,06 (18 $ = 0,9 %); oro: 20$/4 $ = 5 oz = 0,05 lotes (0,05 × 100 oz × 4 $ = 20 $ ✓); viaje asimétrico 32 vs 28 pips (2 × spread)
- Referenciado en README raíz (árbol + Sprint 1.5 + Inicio Rápido)

Stage Summary:
- Artefactos: receta-primera-operacion.md + SYLLABUS v1.1 + README raíz actualizado
- Decisiones: receta maestra EUR/USD (mercado más líquido para mecánica) con oro como primera variación; pasos 0-2 habilitados desde M2 (familiarización, cero órdenes); pasos 3-11 atados a M4; "procesada 6/6" como hito en lugar de dólares
- Estado: temario aprobado y v1.1 publicada. Siguiente: Sprint 2 (M2 · El Motor del Precio)

---
Task ID: sprint-2
Agent: Z.ai (Mentor Trading + Pedagogical Coach + Knowledge Architect)
Task: Construcción completa del Módulo 2 · El Motor del Precio

Work Log:
- Leído SYLLABUS §5 M2 (6 lecciones + lab + misión + quiz), PLANTILLA_MODULO y lecciones de M1 para mantener voz/formato §6.2
- Redactadas las 6 lecciones: 2.1 mecánica de subasta (bid/ask, taker/maker, viaje asimétrico 32/28 pips, spread como % del objetivo), 2.2 oferta y demanda (urgencia vs número, desequilibrio→expansión, oferta/demanda residual, caso melocotones actualizado), 2.3 liquidez (profundidad, barrida de stops con escenario numérico del institucional, SL por estructura), 2.4 forex y sesiones (pares/pips/lotes, 4 sesiones convertidas a Bolivia UTC-4 con aviso DST, ciclo diario, valor de pip en pares JPY ≈ 6,67 $), 2.5 personalidad de mercados (5 dimensiones, tabla comparativa EUR/USD vs XAU/USD vs US30 con mismo riesgo 1 %, concentración vs coleccionismo), 2.6 calendario macro e intermercados (NFP/IPC/FOMC en hora Bolivia, cadena tasas→DXY→oro/acciones/cripto, regla macro de formación ventana roja 15/15 y FOMC 30/30, costo de ignorarla con slippage 1,5R)
- Construido README del módulo como hub: objetivo, índice con tiempos, puente con la receta (pasos 0-2 habilitados), laboratorio (reloj de sesiones personalizado + mapa macro de 5 eventos), misión M-2 (3 sesiones de observación pura con ficha de 6 campos, regla cero órdenes), quiz de 10 preguntas con clave oculta, glosario del módulo (25 términos), referencias y navegación (M3 como texto, sin enlace roto)
- Creada journal/plantilla_journal_v0.csv (21 columnas: fechas, instrumento, dirección, orden, lote, entrada, SL, TP, resultados en pips/$/R, SL antes de entrar, setup, emociones pre/post, error, lección, ventana macro, captura) con 2 filas de ejemplo (una TP, una SL)
- Actualizado glosario maestro: +27 filas (25 términos M2 + recurso receta), total 66 entradas
- Actualizado README raíz: estados M2 🟢 / M3 🔜 Sprint 3, árbol con laboratorio/ y mod-02, notas de Sprint 1.5 y 2, Inicio Rápido
- Verificación numérica: 0,05 lotes × 40 pips × 10 $/pip = 20 $; USD/JPY pip ≈ 100 000 × 0,01 / 150 ≈ 6,67 $; spread sobre objetivo 2/20 = 10 % y 2/10 = 20 %; quiz pregunta 7 con respuesta 20 $ consistente

Stage Summary:
- Artefactos: mod-02-motor-del-precio/ completo (README + 6 lecciones) + journal/plantilla_journal_v0.csv + glosario maestro 66 entradas + README raíz
- Decisiones: horas del curso ancladas a Bolivia UTC-4 con aviso de DST por principios; datos BIS 2022 marcados (snapshot); rangos de ADR/spread marcados (ilustrativo); regla macro de formación (no estar dentro de ventanas rojas) establecida como estándar del programa y referenciada para M8/M9
- Estado: M1 🟢 M2 🟢. Siguiente: Sprint 3 (M3 · Anatomía del Gráfico) — se inicia a continuación en esta misma sesión

---
Task ID: sprint-3
Agent: Z.ai (Mentor Trading + Pedagogical Coach + Knowledge Architect)
Task: Construcción completa del Módulo 3 · Anatomía del Gráfico

Work Log:
- Leído SYLLABUS §5 M3 (6 lecciones + lab + misión) y aplicado el formato §6.2 con la voz de M1/M2
- Redactadas las 6 lecciones: 3.1 velas japonesas (OHLC, cuerpo/mechas/cierre como veredicto, fractalidad literal, lectura en 4 preguntas, descomposición cerrada de una vela D1 de XAU/USD, Dojima/Homma), 3.2 los 4 ciclos (acumulación→markup→distribución→markdown, Dow HH/HL, Weinstein Stages, clasificación en 3 preguntas con caso EUR/USD), 3.3 soportes y resistencias (zonas no líneas, 3 tipos, memoria de mercado, gradiente de fortaleza — muchos toques CONSUMEN, protocolo de marcado de 4 reglas, caso con R:B 1,75 rechazado por debajo de 1:2), 3.4 confirmación en 3 pasos (ruptura→cierre fuera→retesteo, polaridad, throwback, falso rompimiento como mecanismo, caso completo con R:B 3,1 y lote 0,14), 3.5 patrones elementales (catálogo de vela y figura como firmas de procesos, checklist de 5 preguntas, fiabilidad honesta marcada (snapshot), caso doble techo en US30 con lote por especificación), 3.6 rangos vs tendencias (régimen como permiso operativo, ~70 % en rango (aproximación), whipsaw como mecanismo de cobro, test de 3 marcas, casos A/B/C)
- Construido README del módulo: objetivo, índice, puente con la receta (Paso 3 completo tras M3), laboratorio de 10 episodios con Bar Replay + autoauditoría, misión M-3 (bitácora de 20 niveles con formato de fila y regla de anotación antes del desenlace), quiz de 10 preguntas con clave oculta, glosario del módulo (22 términos), referencias y navegación
- Corregidas erratas detectadas en la revisión: "distribucación"→"distribución" (3.2), "tuGreen light"→"la luz verde" y limpieza de una frase de borrador en el paso 3 (3.4), "bado"→"bando" (3.6)
- Actualizado glosario maestro: +22 términos M3, total 88 entradas
- Actualizado README raíz: M3 🟢, M4 🔜 Sprint 4 (incluye examen N1), árbol del repo, nota Sprint 3, Inicio Rápido

Stage Summary:
- Artefactos: mod-03-anatomia-del-grafico/ completo (README + 6 lecciones) + glosario maestro 88 entradas + README raíz
- Decisiones: el protocolo de confirmación en 3 pasos queda como estándar transversal del programa (lo citarán M5 BOS, M8 colocación de stops y el campo del journal en M9); el gradiente "más toques = más consumida" como criterio de zona; el test de 3 marcas para régimen; las cifras de fiabilidad de patrones siempre marcadas (snapshot)
- Estado: M1 🟢 M2 🟢 M3 🟢. Siguiente: Sprint 4 (M4 · Plataforma y Primera Ejecución + examen integrador N1) — al completarlo, la receta ejecuta sus pasos 3-11

---
Task ID: revision-visual
Agent: Z.ai (Knowledge Architect + Pedagogical Coach)
Task: Revisión visual del curso — inserción de diagramas Mermaid + paquete de descarga con visor

Work Log:
- Auditados los 3 módulos publicados + la receta para localizar los puntos de máxima carga conceptual sin apoyo visual
- Insertados 10 diagramas Mermaid nuevos (total repo: 12 contando el del SYLLABUS y el de la lección 1.3):
  1. receta-primera-operacion.md — flowchart TD de los 12 pasos con nodos de decisión (¿hay setup? / ¿6 de 6 procesada?) y bucle de corrección
  2. leccion-2-1 — flowchart TD: nacimiento de un tick (taker de 80 lotes consumiendo los niveles ask)
  3. leccion-2-2 — flowchart LR circular: equilibrio → desequilibrio → expansión → nuevo equilibrio
  4. leccion-2-3 — sequenceDiagram: anatomía de la barrida de stops (Retail / Precio / Institucional)
  5. leccion-2-4 — timeline: el día forex completo en hora Bolivia con el solapamiento destacado
  6. leccion-2-6 — flowchart TD: cadena causal macro (dato → expectativas → rendimientos → DXY → oro/EUR/acciones/cripto) reemplazando el esquema ASCII
  7. leccion-3-1 — flowchart TD: método de lectura de vela en 4 preguntas
  8. leccion-3-2 — flowchart LR: la rueda de 4 ciclos con los 2 errores del retail marcados
  9. leccion-3-4 — flowchart TD con decisiones: protocolo de confirmación en 3 pasos completo
  10. leccion-3-6 — flowchart TD: clasificador de régimen (3 marcas → tendencia/rango/transición → conducta)
- Criterio de inserción: solo donde el diagrama añade información que el texto no muestra bien (procesos, bucles, decisiones, secuencias); no se diagramaron tablas ni gradientes que ya funcionan como tablas
- Sintaxis Mermaid verificada: etiquetas entre comillas, <br/> para saltos, sin identificadores reservados (end), compatible con el render nativo de GitHub (mermaid v10+)
- Creado visor.html autocontenido en la raíz del repo: renderiza los 30 archivos md con marked + mermaid vía CDN, navegación lateral por grupos, enlaces internos .md reescritos a anclas del visor
- Empaquetado el repo completo en download/academia-trading.zip

Stage Summary:
- Artefactos: 10 diagramas Mermaid nuevos distribuidos en la receta y 9 lecciones; visor.html; academia-trading.zip
- Decisiones: Mermaid sobre imágenes porque GitHub lo renderiza nativamente, es versionable y editable; el visor.html es solo una capa de lectura (en GitHub los .md ya se ven completos); KaTeX no incluido en el visor por riesgo de manglar los $ de costos en el texto (en GitHub la notación $...$ sí se renderiza como matemática)
- Estado: N1 completo y visual. Siguiente: Sprint 4 (M4 + examen N1) cuando el estudiante lo pida

---
Task ID: sprint-4
Agent: Z.ai (Mentor Trading + Pedagogical Coach + Chief Risk Officer + Knowledge Architect)
Task: Construcción completa del Módulo 4 · Plataforma y Primera Ejecución + Examen integrador N1

Work Log:
- Leído SYLLABUS §5 M4 (6 lecciones + lab + misión + 🏆 evaluación N1) y PLANTILLA_MODULO; replicada la voz/formato §6.2 de M1-M3
- Redactadas las 6 lecciones: 4.1 layout profesional (D1/H4/H1/M15, watchlist ≤5, alertas, Bar Replay, atajos; 29 h/año devueltas por plantilla), 4.2 tipos de órdenes (tabla de garantías market/limit/stop/stop-limit/OCO, mermaid de decisión, OCO de la receta con buy limit 1,0824 + SL 1,0794 + TP 1,0884; stop-limit prohibido como SL), 4.3 los 4 costos (spread/comisión/slippage/swap con triple miércoles; mermaid de anatomía del costo con 1 lote: 39 $ ≈ 0,12R; tabla en 0,06 lote: 2,6 pips ≈ 0,09R; E_neto = E_bruto − c), 4.4 largos y cortos (sequenceDiagram del short en 5 pasos, borrow fee, squeeze GameStop, escalera vs ascensor; riesgo ilimitado del corto), 4.5 cuenta demo (qué simula y qué no, configuración realista no negociable, lectura del panel con margen ≈ 217 $, circuito demo → demo-forward → real micro), 4.6 el SL como ley (3 propiedades, mermaid de colocación por estructura, orden sagrado estructura→SL→lote, checklist 6/6, swing 1,0798 → SL 1,0794 = 30 pips → lote 0,06 → riesgo 18 $ = 0,9 %)
- Auditoría aritmética del sprint: detectado y corregido valor de pip de 0,06 lotes (0,6 $, no 6 $) en tabla de costos de 4.3 (total 1,92 $ ≈ 2,6 pips), factura mensual (38 $), Puntos clave (2,6 pips = 4,3 % del TP de 60, 26 % de un TP de 10), swaps de 4.4 (short +0,36 $/2 noches, ventaja 1,20 $, +36 $ por 60 pips), peor caso del long (≈ −6 500 $ nominal) y desglose del B8 del examen (75 pips × 0,6 $/pip = 45 $ = 2,5R)
- Construido README del módulo: hub con tabla de lecciones, puente con la receta (pasos 3-11 habilitados), laboratorio de las 4 órdenes (market, limit, OCO, stop de ruptura con capturas), misión M-4 (10 operaciones demo 6/6 con formato de fila y cero violaciones de SL), quiz de 10 preguntas con clave oculta, glosario de 23 términos, referencias
- Creado docs/03-recursos/evaluaciones/examen-n1.md: 30 preguntas cerradas (bloques A M1×7 / B M2×8 / C M3×8 / D M4×7) con umbral ≥ 24/30, 5 preguntas socráticas en vivo, checklist de ejecución de 6 casillas, tabla de registro y clave oculta en details
- Actualizado glosario maestro: +23 términos M4, total 111 entradas
- Actualizado README raíz (M4 🟢, M5 🔜 Sprint 5, árbol con mod-04 y evaluaciones/, nota Sprint 4, Inicio Rápido), SYLLABUS v1.2 (roadmap Sprints 2-4 ✅ + registro de versiones) y navegación del M3 (enlaces a M4 y examen N1)

Stage Summary:
- Artefactos: mod-04-plataforma-y-primera-ejecucion/ completo (README + 6 lecciones) + examen-n1.md + glosario maestro 111 entradas + README raíz + SYLLABUS v1.2 + M3 README actualizado
- Decisiones: el examen N1 vive en evaluaciones/ (no dentro del módulo) porque cubre los 4 módulos del nivel; el checklist de ejecución 6/6 de la lección 4.6 queda como estándar transversal (lo citarán M8 gestión y M9 journal); el circuito demo → demo-forward → real micro se mantiene coherente con la receta y el veto CRO del "primer dólar"; el costo en R (0,09R) presentado como tamaño-invariante para preparar M8/M9
- Estado: N1 COMPLETO (M1 🟢 M2 🟢 M3 🟢 M4 🟢 + Examen N1 listo). El estudiante estudia M1→M4, ejecuta la misión M-4 y rinde el examen; la certificación 🏆 del nivel exige los tres umbrales (misiones, examen ≥ 80 %, checklist sin violaciones)
- Siguiente: Sprint 5 (M5 · Estructura de Mercado y Liquidez — N2) cuando el estudiante lo pida

---
Task ID: fix-visor-1
Agent: Z.ai (Knowledge Architect + QA)
Task: Reparación del visor.html (se quedaba en "cargando…" sin renderizar nada)

Work Log:
- Diagnóstico: el script principal tenía un error de sintaxis JavaScript en el regex de extracción de mermaid (`/` sin escapar en `</code></pre>` y `([sS]*?)` en lugar de `([\s\S]*?)`), lo que mataba todo el script al parsear y dejaba el visor en "cargando…" permanente; verificado con node --check
- Reescrito el script del visor (scripts/visor_app.js): regex de mermaid corregido, try/catch global (los errores ahora se muestran en la barra de estado en vez de colgar el visor), renderizador markdown de respaldo propio (miniMd: títulos, tablas, listas, checklists ☐/☑, citas, código, enlaces, bloques mermaid) para que el visor funcione incluso sin internet (CDN bloqueado o offline), y resolución de enlaces internos por ruta relativa (antes los README.md ambiguos mapeaban al documento equivocado)
- Detectado y corregido un error real de sintaxis Mermaid en leccion-2-4.md: el diagrama `timeline` usaba períodos con dos puntos (`17:00–02:00`) que rompen el parser; convertido a `17h–02h` y eliminados los `:` del texto de eventos
- Detectado el problema de medición de Mermaid: los diagramas dentro de secciones `display:none` fallan el layout (bombas de "Syntax error in text" en 5 diagramas); descartadas dos variantes (render lazy por sección y cola serial) tras tests de estrés con navegación rápida; solución final: render único al inicio con todas las secciones con diagramas offscreen-visibles (clase .measuring) durante una sola pasada de mermaid.run
- Sincronizado el JSON embebido del visor con los .md de disco (scripts/sync_visor.py) y reempaquetado academia-trading.zip
- Extras: callouts de GitHub [!WARNING]/[!NOTE] convertidos a blockquotes con estilo de alerta; verificación end-to-end en navegador (39 secciones, 39 enlaces de nav, 18/18 diagramas renderizados, 0 errores con navegación acelerada a 200 ms, enlaces Módulo/Anterior/Siguiente apuntando a las secciones correctas, prueba de unit del miniMd en Node)

Stage Summary:
- Artefactos: visor.html v2 (funcional y probado), leccion-2-4.md corregido, academia-trading.zip actualizado, scripts auxiliares (scripts/visor_app.js, sync_visor.py en el workspace)
- Lección registrada: mermaid@10 falla silenciosamente si el contenedor no tiene layout en el momento de renderizar; el visor ahora renderiza todo en una pasada con secciones medibles
- Estado: visor operativo en local (doble clic), en preview sin internet (fallback miniMd) y en GitHub (los .md nativos). Siguiente: Sprint 5 (M5 · Estructura de Mercado y Liquidez — N2) cuando el estudiante lo pida

---
Task ID: fix-visor-2
Agent: Z.ai (Knowledge Architect + QA)
Task: Renderizado de matemática LaTeX en el visor (reporte del estudiante: fórmulas $$...$$ y $...$ se veían crudas)

Work Log:
- Confirmado el reporte: el visor no renderizaba LaTeX (decisión antigua evitaba KaTeX por riesgo de confundir los $ de precios con delimitadores matemáticos); revisión de capturas del estudiante y levantamiento del corpus: 12 fórmulas display $$...$$ (receta, lec 1-1, lec 1-4, agents) + ~30 inline $...$ conviviendo con decenas de precios "20 $", "0,6 $/pip"
- Añadido KaTeX 0.16.11 (CSS + JS por CDN) al head del visor
- Implementado extractMath/restoreMath (scripts/visor_app.js): extracción previa al render con marcadores %%MATHn%%, saltando bloques de código vallado; escáner inline con heurística estricta anti-falsos-positivos (rechaza contenido con espacio pegado a los delimitadores, **, ·, →, ¿, ¡, —; acepta comandos LaTeX, ^_ {}, operadores =<>≤≥ y identificadores simples) — validado con 19/19 casos reales del corpus en Node
- Render de respaldo sin KaTeX (offline): el TeX se muestra como <code> legible + aviso en la barra de estado
- Reformato del README raíz: los 6 renglones de estado de sprints estaban pegados sin línea en blanco y markdown los pintaba como un solo párrafo gigante (también en GitHub); convertidos a lista
- Verificación end-to-end en navegador: receta 2/2 fórmulas display renderizadas como fracciones con los precios intactos, lec 1-3 4/4 inline (E_negocio, N, E_por_operación > 0), examen 5/5, lec 1-1 8/8, 0 fallbacks, 0 $$ crudos, mermaid 18/18 sin regresiones

Stage Summary:
- Artefactos: visor.html v3 (KaTeX + escáner matemático), README.md reformatado, academia-trading.zip actualizado
- Decisión: los .md NO se tocan — la notación $...$/$$...$$ se mantiene nativa para GitHub, el visor hace el trabajo de renderizarla
- Estado: N1 completo con matemática legible. Siguiente: Sprint 5 (M5 · Estructura de Mercado y Liquidez — N2) cuando el estudiante lo pida
