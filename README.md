# 🎓 Academia de Trading — Programa FIT-12

Programa de formación integral en trading construido **paso a paso con agentes IA**, basado en la auditoría de dos cursos de referencia (TradingLab 003 y 004) y en 9 vacíos curriculares detectados y cubiertos.

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada en este repositorio constituye asesoría financiera.

## 🧭 Documentos Rectores (leer en este orden)

1. [`agents.md`](agents.md) — instrucciones vinculantes para los agentes IA
2. [`docs/01-syllabus/SYLLABUS.md`](docs/01-syllabus/SYLLABUS.md) — temario rector (4 niveles × 12 módulos)
3. [`docs/00-analisis/analisis_cursos.md`](docs/00-analisis/analisis_cursos.md) — auditoría de los cursos fuente
4. [`docs/03-recursos/plantillas/PLANTILLA_MODULO.md`](docs/03-recursos/plantillas/PLANTILLA_MODULO.md) — formato estándar de módulo
5. [`worklog.md`](worklog.md) — bitácora de construcción

## 🗺️ Estructura del Repositorio

```text
academia-trading/
├── agents.md                  ← instrucciones para los agentes
├── README.md                  ← este archivo (portada + estado)
├── worklog.md                 ← bitácora de construcción (append-only)
├── docs/
│   ├── 00-analisis/           ← auditoría de cursos base
│   ├── 01-syllabus/           ← temario rector (v1.1)
│   ├── 02-modulos/            ← los 12 módulos del programa
│   │   ├── mod-01-negocio-trading/   (Sprint 1)
│   │   ├── mod-02-motor-del-precio/  (Sprint 2)
│   │   ├── mod-03-anatomia-del-grafico/ (Sprint 3)
│   │   ├── mod-04-plataforma-y-primera-ejecucion/ (Sprint 4)
│   │   ├── mod-05-estructura-de-mercado-y-liquidez/ (Sprint 5)
│   │   ├── mod-06-indicadores-y-confluencias/ (Sprint 6)
│   │   ├── mod-07-construccion-del-sistema/ (Sprint 7)
│   │   ├── mod-08-gestion-del-riesgo/ (Sprint 8)
│   │   ├── mod-09-backtesting-journal-y-validacion/ (Sprint 9)
│   │   ├── mod-10-psicotrading-cientifico/ (Sprint 10)
│   │   ├── mod-11-la-industria/ (Sprint 11)
│   │   └── mod-12-plan-trading-negocio/ (Sprint 12)
│   └── 03-recursos/           ← plantillas + glosario vivo + laboratorio + evaluaciones
│       ├── laboratorio/       ← receta de primera operación + 20 escenarios de sizing (M8)
│       └── evaluaciones/      ← exámenes N1, N2, N3 y final
├── journal/                   ← el registro del negocio: journal v1 (taxonomía E0-E7 + actas) + v0 histórico
└── scripts/core/              ← calculadoras Python del programa (position_sizing.py S8 · metricas_backtest.py S9)
```

## 📊 Estado del Programa

**Progreso global: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 — 12/12 módulos publicados (N1 ✅ · N2 ✅ · N3 ✅ · N4 ✅) — PROGRAMA COMPLETO 🏆.**

| Nivel | Módulo | Estado |
|---|---|---|
| 🧱 N1 | M1 · El Trading como Negocio y Ciencia | 🟢 Publicado (Sprint 1 ✅) |
| 🧱 N1 | M2 · El Motor del Precio | 🟢 Publicado (Sprint 2 ✅) |
| 🧱 N1 | M3 · Anatomía del Gráfico | 🟢 Publicado (Sprint 3 ✅) |
| 🧱 N1 | M4 · Plataforma y Primera Ejecución | 🟢 Publicado (Sprint 4 ✅) |
| 📐 N2 | M5 · Estructura de Mercado y Liquidez | 🟢 Publicado (Sprint 5 ✅) |
| 📐 N2 | M6 · Indicadores y Confluencias | 🟢 Publicado (Sprint 6 ✅) |
| 📐 N2 | M7 · Construcción del Sistema | 🟢 Publicado (Sprint 7 ✅) |
| 🛡️ N3 | M8 · Gestión del Riesgo | 🟢 Publicado (Sprint 8 ✅) |
| 🛡️ N3 | M9 · Backtesting, Journal y Validación | 🟢 Publicado (Sprint 9 ✅) |
| 🛡️ N3 | M10 · Psicotrading Científico | 🟢 Publicado (Sprint 10 ✅) |
| 💼 N4 | M11 · La Industria | 🟢 Publicado (Sprint 11 ✅) |
| 💼 N4 | M12 · Plan de Trading y Plan de Negocio | 🟢 Publicado (Sprint 12 ✅) |

> **Nota:** el programa avanza a razón de un sprint por módulo, según tu avance real. Las filas ⏳ **no son contenido perdido ni borradores ocultos**: son módulos aún no construidos — cuando llegue su sprint pasarán a 🟢 igual que M1-M12. La numeración (Sprint 5, 6, 7…) es el orden planificado en el [SYLLABUS](docs/01-syllabus/SYLLABUS.md) y puede ajustarse a tu ritmo.

- **Sprint 0 ✅:** estructura del repo + agents.md + SYLLABUS.md + análisis de cursos.
- **Sprint 1 ✅:** Módulo 1 completo — 6 lecciones + laboratorio de auditoría personal + misión (Carta de Expectativas + contrato anti-ludopatía) + quiz de graduación + glosario (38 términos).
- **Sprint 1.5 ✅:** temario v1.0 **aprobado por el estudiante** → v1.1 + recurso transversal [La Receta de tu Primera Operación](docs/03-recursos/laboratorio/receta-primera-operacion.md) (12 pasos, receta maestra EUR/USD + fichas oro/índices; objetivo: primera operación PROCESADA — veto CRO al marco "primer dólar").
- **Sprint 2 ✅:** Módulo 2 completo — 6 lecciones (subasta, oferta/demanda, liquidez, sesiones en hora Bolivia, personalidad de mercados, calendario macro) + laboratorio (reloj de sesiones + mapa macro) + misión M-2 (observación pura de 3 sesiones) + quiz + glosario (25 términos nuevos, total 66) + plantilla journal v0 (CSV).
- **Sprint 3 ✅:** Módulo 3 completo — 6 lecciones (velas, 4 ciclos, zonas S/R con gradiente, confirmación en 3 pasos, patrones con fiabilidad honesta, regímenes y whipsaw) + laboratorio (10 episodios con Bar Replay) + misión M-3 (bitácora de 20 niveles) + quiz + glosario (22 términos nuevos, total 88).
- **Sprint 4 ✅:** Módulo 4 completo — 6 lecciones (layout profesional, tipos de órdenes y OCO, los 4 costos, largos y cortos, demo ordenada, el SL como ley con checklist 6/6) + laboratorio (las 4 órdenes en demo) + misión M-4 (10 operaciones demo procesadas 6/6) + quiz + glosario (23 términos nuevos, total 111) + **Examen integrador N1** (30 preguntas ≥ 80 % + entrevista socrática + checklist de ejecución).
- **Sprint 5 ✅:** Módulo 5 completo — 6 lecciones (tendencia y secuencia HH/HL, BOS/CHoCH con nomenclatura unificada PA↔SMC, pools de liquidez y barridas, FVG y mitigación, order blocks sin misticismo, top-down de 3 capas) + laboratorio (top-down de 5 mercados con plantilla) + misión M-5 (15 análisis estructurales documentados) + quiz + glosario (24 términos nuevos, total 135) + 3 diagramas mermaid nuevos. Un solo caso maestro (la zona de la receta) atraviesa las 6 lecciones.
- **Sprint 6 ✅:** Módulo 6 completo — 8 lecciones (filosofía del indicador, medias móviles 20/50/200, ATR + Bollinger + Donchian, RSI/Estocástico/MACD con divergencias, volumen + VWAP + Volume Profile, Fibonacci/Elliott/armónicos con límites, etapas de Weinstein, radar de fiabilidad + regla del máximo 3) + laboratorio (dashboard de confluencias probado en 50 movimientos) + misión M-6 (informe comparativo de 3 herramientas) + quiz + glosario (24 términos nuevos, total 159) + 3 diagramas mermaid nuevos. El mismo caso maestro de la receta, ahora auditado con medidores (SL de 32 pips ≈ 1,52 ATR).
- **Sprint 7 ✅:** Módulo 7 completo — cierre del N2: 6 lecciones (filosofía/estrategia/sistema con el test del clon, los 10 componentes, catálogo de 4 arquetipos de setup, matriz WR × R:B de esperanza aplicada, métricas y estadística de rachas, criterios de robustez y el ciclo prohibido del data-mining) + laboratorio (Sistema v1.0 en 1 página con plantilla de 10 componentes) + misión M-7 (30 repeticiones del setup a ciegas con reporte de métricas) + quiz + glosario (20 términos nuevos) + 4 diagramas mermaid nuevos + **Evaluación Nivel 2** (examen-n2: 30 preguntas ≥ 80 % + 5 socráticas + checklist de entregables).
- **Sprint 8 ✅:** Módulo 8 completo — apertura del N3: 6 lecciones (preservación de capital como inventario, asimetría del drawdown con tabla completa, regla del 1 % y position sizing con fórmula universal, apalancamiento real con valor del pip por instrumento, riesgo de cartera y correlación con topes 2 % motor / 3 % global — aporte propio —, frenos de emergencia en cascada con protocolo de apagado — aporte propio —) + laboratorio (calculadora de position sizing en 3 pestañas con 3 casos de control + [`position_sizing.py`](scripts/core/position_sizing.py) del repo con 9 asserts) + misión M-8 (20 escenarios de sizing a mano ≥ 18/20, [hoja con clave](docs/03-recursos/laboratorio/mision-m8-escenarios.md)) + quiz con **umbral elevado ≥ 90 %** + glosario (22 términos nuevos, total real 199) + 3 diagramas mermaid nuevos.
- **Sprint 9 ✅:** Módulo 9 completo — la evidencia y la auditoría propia: 6 lecciones (epistemología del backtesting con N ≥ 100 e IC ±9,6 pp, protocolo manual con definición operativa de setup válido y rutina de 9 pasos, las 13 métricas del reporte con la tabla de decisión de 3 vías — los costes hunden el PF de 1,40 a 1,25 —, forward testing con el embudo de la evidencia, el Journal profesional con taxonomía E0-E7 y la distinción pérdida ≠ error — aporte propio —, revisión semanal/mensual con ventana de modificación y lista negra — aporte propio —) + laboratorio (backtesting ciego de 100 operaciones con journal v1) + misión M-9 (reporte de 13 métricas + 3 conclusiones + revisión simulada con el agente) + quiz (umbral 80 %) + glosario (25 términos nuevos, total 224) + 3 diagramas mermaid nuevos + [`metricas_backtest.py`](scripts/core/metricas_backtest.py) (calculadora de las 13 métricas, 6 bloques de asserts) + [journal v1](journal/plantilla_journal_v1.md) (CSV de 24 columnas + guía con actas).
- **Sprint 10 ✅:** Módulo 10 completo — cierre del N3: 7 lecciones (neurobiología del secuestro con 4 detectores, los 5 miedos de Douglas + 5 axiomas de la incertidumbre, las 5 avaricias con coste exacto — el chasing convierte la E de +0,16R en −0,16R —, la matriz proceso × resultado con la ganancia fuera de plan como error más peligroso, 4 sesgos con antídotos estructurales y el mapa del tilt, la dicotomía del control con σ ±1,52R contra señal +0,24R, la rutina diaria con ventana de 3 h e inacción estratégica) + laboratorio (protocolo de temperatura pre-sesión verde/ámbar/rojo + diario emocional estructurado) + misión M-10 (10 sesiones forward con checklist emocional pre/post y tasa de contención) + quiz ≥ 8/10 + glosario (27 términos nuevos, total 251) + 3 diagramas mermaid nuevos + **Evaluación N3** (examen-n3: 30 preguntas ≥ 80 % + 5 socráticas + entrevista de graduación con 3 casos reales del journal).
- **Sprint 11 ✅:** Módulo 11 completo — apertura del N4: 7 lecciones (brokers de verdad con A-Book/B-Book y los 5 pilares, radar de las 5 estafas con verificación regulatoria universal, prop firms con el embudo de fees y las cifras del sector, las 6 reglas finas con lectura forense del contrato, la matriz de riesgo dinámico 0,50→0,25 % con "todavía no", el árbol de las 4 puertas para intentar una evaluación, fiscalidad por principios con el expediente fiscal) + laboratorio (due diligence de 3 brokers + 3 prop firms con matriz universal de 25 puntos) + misión M-11 (informe de elección defendido en socrática + plan de capitalización a 12 meses) + quiz ≥ 8/10 + glosario (27 términos nuevos, total 278) + 3 diagramas mermaid nuevos.
- **Sprint 12 ✅:** Módulo 12 completo — cierre del programa: 7 lecciones (Plan de Trading documental de 10 secciones con test del clon, rutina semanal de 4 capas, dashboard de 12 KPIs con horas vs retorno, gestión patrimonial con 3 cubos y política de retiros, hoja de ruta de 5 fases con candados y escalera de riesgo 0 % → 1 %, biblioteca esencial del canon de 5, Constitución de mejora continua contra el nomadeo) + laboratorio (Plan de Trading v1.0 y Plan de Negocio) + misión final (examen integral de 50 preguntas ≥ 85 % + defensa socrática extendida) + quiz ≥ 8/10 + glosario (24 términos nuevos, total 302) + 3 diagramas mermaid nuevos + 🏆 **Certificación interna FIT-12** (examen-final.md).

## 🚀 Inicio Rápido

- **Para el estudiante:** dile a tu agente *"Siguiente lección"* para estudiar la [Lección 1.1 · Qué es realmente el trading](docs/02-modulos/mod-01-negocio-trading/leccion-1-1.md) — **los Módulos 1 a 9 están publicados y listos**. Cuando llegues al M4, ejecuta los pasos 3–11 de la [Receta de tu Primera Operación](docs/03-recursos/laboratorio/receta-primera-operacion.md) y cierra el N1 con el [Examen N1](docs/03-recursos/evaluaciones/examen-n1.md); continúa el N2 con el [M5](docs/02-modulos/mod-05-estructura-de-mercado-y-liquidez/README.md) y el [M6](docs/02-modulos/mod-06-indicadores-y-confluencias/README.md), ciérralo construyendo tu [Sistema v1.0 en el M7](docs/02-modulos/mod-07-construccion-del-sistema/README.md) + la [Evaluación N2](docs/03-recursos/evaluaciones/examen-n2.md), y abre el N3 blindando tu cuenta con el [M8 · Gestión del Riesgo](docs/02-modulos/mod-08-gestion-del-riesgo/README.md) — la calculadora de sizing y los frenos en cascada que tu negocio necesita antes de escalar — y demostrando que tu sistema tiene esperanza con el [M9 · Backtesting, Journal y Validación](docs/02-modulos/mod-09-backtesting-journal-y-validacion/README.md): 100 operaciones ciegas, el reporte de 13 métricas y el journal v1 con taxonomía de errores que auditará toda tu carrera. Cierra el N3 operando tu propia máquina con el [M10 · Psicotrading Científico](docs/02-modulos/mod-10-psicotrading-cientifico/README.md) — temperatura pre-sesión, los 5 miedos, las 5 avaricias y la rutina de ventana — y gradúala con la [Evaluación N3](docs/03-recursos/evaluaciones/examen-n3.md) y su entrevista de graduación. Abre el N4 eligiendo infraestructura con criterio forense en el [M11 · La Industria](docs/02-modulos/mod-11-la-industria/README.md) — brokers, radar de estafas, prop firms con sus reglas finas y fiscalidad por principios — y deja tu informe defendido y tu plan de capitalización a 12 meses. Cierra el programa con el [M12 · Plan de Trading y Plan de Negocio](docs/02-modulos/mod-12-plan-trading-negocio/README.md): tu Plan v1.0, tu hoja de ruta y la [Certificación FIT-12](docs/03-recursos/evaluaciones/examen-final.md) — y luego, el oficio.
- **Para un agente nuevo:** lee `agents.md` completo antes de tocar nada; después `worklog.md` y la tabla de estado de este README.

## ⚖️ Principios del Programa

1. Esperanza matemática como brújula: $E = (P_w \times W) - (P_l \times L)$
2. Regla 85/15 *(heurística)*: psicología + riesgo pesan más que la técnica
3. Preservación del capital antes que ganancia
4. Pedagogía activa: por qué → cómo → laboratorio → misión → evaluación
5. Honestidad radical: cifras etiquetadas, sin promesas, sin señales
