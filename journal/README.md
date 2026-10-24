# journal/ — Diario de Operativa

> **Estado: activo (journal v1 desde Sprint 9).** El estudiante registra aquí su operativa (backtest, forward demo y, en su fase, real micro); los agentes solo leen y auditan según el protocolo de `agents.md` § 5.4.

## Contenido

| Archivo | Qué es | Estado |
|---|---|---|
| [`plantilla_journal_v1.md`](plantilla_journal_v1.md) | **El registro profesional (M9):** 24 columnas + taxonomía de errores E0–E7 + rutina de los 90 segundos + plantillas de acta semanal y mensual + changelog del sistema | 🟢 Activo |
| [`plantilla_journal_v1.csv`](plantilla_journal_v1.csv) | El CSV del v1 (24 columnas + 4 filas de ejemplo migradas del v0) | 🟢 Activo |
| [`plantilla_journal_v0.csv`](plantilla_journal_v0.csv) | El antecesor (Sprint 2): mecánica de la operación en 21 columnas | 🗄️ Histórico — migra sus filas al v1 |
| `reporte-m9.md` | El reporte estadístico de la Misión M-9 (lo crea el estudiante) | 📝 Pendiente del estudiante |

## El flujo del registro

1. **En la señal:** captura del gráfico (la evidencia) → orden con el lote de la calculadora (M8).
2. **Al cerrar la operación:** los 90 segundos — R real, etiqueta E0–E7 en caliente, emocional post, lección de una línea ([lección 9.5](../docs/02-modulos/mod-09-backtesting-journal-y-validacion/leccion-9-5.md)).
3. **Cada semana:** el acta semanal de 6 pasos ([lección 9.6](../docs/02-modulos/mod-09-backtesting-journal-y-validacion/leccion-9-6.md)) — 5 preguntas de auditoría, disparos ejecutados/debidos, UNA conclusión, decisión documentada o abstención.
4. **Cada mes:** el acta mensual — métricas contra los intervalos del backtest y la ventana de modificación (las 4 condiciones).
5. **Oráculo de verificación:** [`../scripts/core/metricas_backtest.py`](../scripts/core/metricas_backtest.py) calcula las 13 métricas del reporte desde el CSV.

> **La distinción central** (lección 9.5): **pérdida ≠ error**. La pérdida en plan (E0) es el coste estadístico del negocio; el error es la desviación del proceso — y una ganancia fuera de plan ES un error. La columna de etiquetas es el mapa de tu ejecución, no un tribunal.
