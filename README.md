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
│   │   └── mod-04-plataforma-y-primera-ejecucion/ (Sprint 4)
│   └── 03-recursos/           ← plantillas + glosario vivo + laboratorio + evaluaciones
│       ├── laboratorio/       ← receta de primera operación
│       └── evaluaciones/      ← examen integrador N1
├── journal/                   ← plantillas y registros de operativa (journal v0 CSV listo)
└── scripts/core/              ← calculadoras y métricas Python (Sprint 5+)
```

## 📊 Estado del Programa

| Nivel | Módulo | Estado |
|---|---|---|
| 🧱 N1 | M1 · El Trading como Negocio y Ciencia | 🟢 Publicado (Sprint 1 ✅) |
| 🧱 N1 | M2 · El Motor del Precio | 🟢 Publicado (Sprint 2 ✅) |
| 🧱 N1 | M3 · Anatomía del Gráfico | 🟢 Publicado (Sprint 3 ✅) |
| 🧱 N1 | M4 · Plataforma y Primera Ejecución | 🟢 Publicado (Sprint 4 ✅) |
| 📐 N2 | M5 · Estructura de Mercado y Liquidez | 🔜 Sprint 5 — siguiente |
| 📐 N2 | M6 · Indicadores y Confluencias | ⏳ |
| 📐 N2 | M7 · Construcción del Sistema | ⏳ |
| 🛡️ N3 | M8 · Gestión del Riesgo | ⏳ |
| 🛡️ N3 | M9 · Backtesting, Journal y Validación | ⏳ |
| 🛡️ N3 | M10 · Psicotrading Científico | ⏳ |
| 💼 N4 | M11 · La Industria | ⏳ |
| 💼 N4 | M12 · Plan de Trading y Plan de Negocio | ⏳ |

- **Sprint 0 ✅:** estructura del repo + agents.md + SYLLABUS.md + análisis de cursos.
- **Sprint 1 ✅:** Módulo 1 completo — 6 lecciones + laboratorio de auditoría personal + misión (Carta de Expectativas + contrato anti-ludopatía) + quiz de graduación + glosario (38 términos).
- **Sprint 1.5 ✅:** temario v1.0 **aprobado por el estudiante** → v1.1 + recurso transversal [La Receta de tu Primera Operación](docs/03-recursos/laboratorio/receta-primera-operacion.md) (12 pasos, receta maestra EUR/USD + fichas oro/índices; objetivo: primera operación PROCESADA — veto CRO al marco "primer dólar").
- **Sprint 2 ✅:** Módulo 2 completo — 6 lecciones (subasta, oferta/demanda, liquidez, sesiones en hora Bolivia, personalidad de mercados, calendario macro) + laboratorio (reloj de sesiones + mapa macro) + misión M-2 (observación pura de 3 sesiones) + quiz + glosario (25 términos nuevos, total 66) + plantilla journal v0 (CSV).
- **Sprint 3 ✅:** Módulo 3 completo — 6 lecciones (velas, 4 ciclos, zonas S/R con gradiente, confirmación en 3 pasos, patrones con fiabilidad honesta, regímenes y whipsaw) + laboratorio (10 episodios con Bar Replay) + misión M-3 (bitácora de 20 niveles) + quiz + glosario (22 términos nuevos, total 88).
- **Sprint 4 ✅:** Módulo 4 completo — 6 lecciones (layout profesional, tipos de órdenes y OCO, los 4 costos, largos y cortos, demo ordenada, el SL como ley con checklist 6/6) + laboratorio (las 4 órdenes en demo) + misión M-4 (10 operaciones demo procesadas 6/6) + quiz + glosario (23 términos nuevos, total 111) + **Examen integrador N1** (30 preguntas ≥ 80 % + entrevista socrática + checklist de ejecución).

## 🚀 Inicio Rápido

- **Para el estudiante:** dile a tu agente *"Siguiente lección"* para estudiar la [Lección 1.1 · Qué es realmente el trading](docs/02-modulos/mod-01-negocio-trading/leccion-1-1.md) — **los Módulos 1 a 4 están publicados y listos**. Cuando llegues al M4, ejecuta los pasos 3–11 de la [Receta de tu Primera Operación](docs/03-recursos/laboratorio/receta-primera-operacion.md) y cierra el nivel con el [Examen N1](docs/03-recursos/evaluaciones/examen-n1.md).
- **Para un agente nuevo:** lee `agents.md` completo antes de tocar nada; después `worklog.md` y la tabla de estado de este README.

## ⚖️ Principios del Programa

1. Esperanza matemática como brújula: $E = (P_w \times W) - (P_l \times L)$
2. Regla 85/15 *(heurística)*: psicología + riesgo pesan más que la técnica
3. Preservación del capital antes que ganancia
4. Pedagogía activa: por qué → cómo → laboratorio → misión → evaluación
5. Honestidad radical: cifras etiquetadas, sin promesas, sin señales
