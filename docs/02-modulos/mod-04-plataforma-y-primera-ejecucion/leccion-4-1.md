# Lección 4.1 · TradingView profesional

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 35–45 min de estudio + 30 min de configuración |
| 🧱 Módulo | [M4 · Plataforma y Primera Ejecución](README.md) |
| ⬅️ Anterior | — (primera lección del módulo) |
| ➡️ Siguiente | [Lección 4.2 · Tipos de órdenes](leccion-4-2.md) |

---

## Por qué importa

La plataforma es tu oficina: es donde ocurre todo lo que los 11 módulos anteriores han preparado. Y como toda oficina, el tiempo que pierdes buscando las herramientas es tiempo de trabajo perdido — pero en trading el problema es peor, porque la búsqueda casi siempre ocurre cuando el mercado se está moviendo. Un trader que no sabe montar un layout, fijar una alerta o retroceder el histórico pierde capacidades que el programa da por sentadas: el laboratorio de M3 usó Bar Replay y la [Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) asume que sabes leer un panel de cotización. Este módulo arranca con la herramienta porque la ejecución disciplinada empieza con una plataforma que se comporta de la misma manera cada día: mismo layout, misma watchlist, mismas alertas. La variedad es enemiga de la rutina, y la rutina de ejecución es lo que este módulo construye.

## Concepto

Usaremos TradingView como herramienta de análisis (cuenta gratuita basta para el N1; sin marcas: cualquier plataforma equivalente sirve si tiene las mismas funciones). Las piezas que el programa usa a diario:

1. **El gráfico y sus marcos temporales.** Cada gráfico muestra un instrumento en un marco (D1, H4, H1, M15…). Cambiar de marco NO cambia el mercado: cambia la resolución de la cámara (fractalidad de la [Lección 3.1](../mod-03-anatomia-del-grafico/leccion-3-1.md)).
2. **Escalas.** Lineal (por defecto) y logarítmica: en la logarítmica, la misma distancia vertical representa el mismo % de movimiento. Para el forex y los marcos intradía del programa, la lineal es suficiente; la logarítmica importa al mirar años de índices.
3. **Layout multitemporal.** Un mismo instrumento, varios paneles sincronizados (ej. D1 + H4 + H1 + M15). Es la configuración estándar del programa: análisis top-down en una sola pantalla.
4. **Watchlist.** Tu lista vigilada: los 5 instrumentos del programa (EUR/USD, XAU/USD, US30, y 2 de tu elección). Una watchlist corta y fija es una decisión de negocio (concentración de la [Lección 2.5](../mod-02-motor-del-precio/leccion-2-5.md)), no una limitación.
5. **Alertas.** Avisos cuando el precio toca un nivel (o un indicador se activa). Eliminan la vigilancia manual: tú defines la zona, la plataforma vigila. Tipos básicos: cruce de precio, cruce de línea/dibujo, y alertas recurrentes.
6. **Bar Replay.** La máquina del tiempo: reproduce el histórico vela a vela ocultando el futuro. Es el simulador de estudio del programa (laboratorios M3 y M9).

**Atajos esenciales** (los que se usan cada sesión):

| Atajo | Acción | Uso típico |
|---|---|---|
| `/` o coma | búsqueda de instrumento | cambiar de activo rápido |
| Alt + T / Alt + H | línea de tendencia / línea horizontal | marcar zonas (M3.3) |
| Rectángulo (`R`) | dibujar zona | el marcado estándar del programa |
| `Alt + R` | reproducir grabación de layout (replay) | practicar sin futuro |
| Ctrl + Z / Ctrl + Y | deshacer / rehacer dibujos | corregir marcado |
| Rueda + Shift | zoom horizontal rápido | moverse entre marcos de tiempo visuales |
| Doble clic en escala | ajustar escala automática | cuando el gráfico "se sale" |

*(los atajos exactos pueden variar por versión/idioma — los marcamos como orientativos)*

## Analogía

Una cabina de pilotos no tiene un solo interruptor fuera de sitio: cada palanca está siempre en el mismo lugar, y el piloto la opera sin mirar. Ese entrenamiento no es capricho — en plena turbulencia no hay tiempo de buscar. Tu plataforma es la cabina: cuando el precio llegue a tu zona (y llegará cuando estés lejos o ocupado), necesitas que tus manos sepan qué hacer sin pensar. El trader que cada día reorganiza sus gráficos, cambia de colores y prueba paneles nuevos está reorganizando la cabina en pleno vuelo. La rutina no es aburrimiento: es lo que libera tu atención para el mercado.

## Cómo se hace: montar el layout de trabajo del programa (una vez)

Configuración estándar, con pasos cerrados. Tiempo: 30 min la primera vez, 0 después.

1. **Abre 4 paneles del mismo instrumento** (ej. EUR/USD): D1 arriba, H4 y H1 al centro, M15 abajo. En TradingView: divide el área en 4 y fija el símbolo sincronizado entre paneles.
2. **Limpia el gráfico:** quita indicadores de fábrica. Por ahora solo precio (M6 añadirá indicadores con criterio).
3. **Guarda como plantilla del layout:** nombre `FIT12-trabajo`. Cada sesión se abre en 2 segundos con la misma disposición.
4. **Crea la watchlist `FIT12`:** EUR/USD, XAU/USD, US30, + 2 instrumentos de tu elección (máximo 5 en total, criterio de la Lección 2.5).
5. **Marca tus zonas de la semana** (protocolo M3.3) sobre H4/D1 y déjalas dibujadas en el layout: el gráfico debe mostrar tu análisis, no estar vacío.
6. **Pon 2–3 alertas por instrumento** en los bordes de tus zonas activas (ej. EUR/USD: alerta de cruce en 1,0824). Con alertas puestas, cerrar la plataforma es una decisión válida: la plataforma te avisará.
7. **Prueba Bar Replay:** abre EUR/USD H1, rebobina 20 días y avanza vela a vela describiendo (en voz alta) régimen, ciclo y zonas — el mismo ejercicio del laboratorio de M3.

**Chequeo de configuración completa:** el layout abre con 4 paneles, la watchlist tiene ≤ 5 instrumentos, hay zonas marcadas y ≥ 2 alertas activas por instrumento principal, y sabes lanzar un Replay sin buscar el botón.

## Error común

El primer error es **coleccionar en vez de operar**: 12 layouts, 30 indicadores, 4 plataformas instaladas y ninguna rutina. Cada reconfiguración parece progreso pero no deja estadística detrás — es el mismo mecanismo de "buscar el curso perfecto" de la [Lección 1.5](../mod-01-negocio-trading/leccion-1-5.md). El segundo error es **no usar alertas y vigilar el gráfico a mano**: además de devorar horas, te expone a decidir en tiempo real bajo emoción — la alerta existe para que el precio te busque a ti, y no al revés. El tercero es **practicar Replay "viendo el futuro"**: rebobinar, mirar 3 velas adelante "para contextualizar" y luego "predecir" es trampa estadística pura — el ejercicio solo vale si el futuro está genuinamente oculto cuando escribes tu predicción. Si te descubres mirando, esa repetición no cuenta.

## Conexión cuantitativa

El costo de la desorganización es medible. Rutina manual de preparar gráficos: 10 min/día; con layout guardado: 1 min. Diferencia: 9 min × 4 sesiones/semana × 48 semanas ≈ **29 horas al año** — una semana laboral completa gastada en clics que una plantilla hace gratis. Y el costo de vigilar sin alertas: 2 h de pantalla diaria "por si acaso" frente a la alternativa de trabajar con el precio como notificación: en un año son **≈ 480 horas** — el equivalente a 12 semanas de estudio del programa completo. La plataforma bien configurada no mejora tu E directamente, pero devuelve el tiempo con el que se construye todo lo demás: análisis, journal, laboratorio. En la [Lección 4.3](leccion-4-3.md) verás el otro costo de la plataforma — el que sí se paga en dinero.

---

## 🎯 Puntos clave

1. La plataforma es tu oficina: la rutina fija (layout, watchlist, alertas) es lo que libera atención para el mercado.
2. Layout multitemporal estándar del programa: D1 + H4 + H1 + M15 del mismo instrumento, sincronizados.
3. Watchlist de máximo 5 instrumentos: concentración por decisión de negocio (Lección 2.5), no limitación.
4. Las alertas invierten el flujo: defines la zona, la plataforma vigila; tú decides con calma cuando suena.
5. Bar Replay es el simulador oficial: solo cuenta la repetición con el futuro genuinamente oculto.
6. Una configuración mantenida durante meses produce datos comparables; la reorganización constante produce cero datos.

## 🔄 Autoevaluación rápida

1. ¿Por qué el programa fija una watchlist de 5 instrumentos en vez de dejar libre al estudiante? Conecta con la lección de personalidad de mercados.
2. Tu compañero dice: "no pongo alertas porque quiero ver las operaciones en vivo". ¿Qué dos costos le estás explicando?
3. ¿Qué convierte una repetición de Bar Replay en repetición válida — y qué la invalida?

<details>
<summary>Ver respuestas</summary>

1. Por concentración (Lección 2.5): cada instrumento tiene personalidad distinta (volatilidad, horario, spread, tamaño de rango) y operar 5 bien vence a vigilar 30 a medias. Además fija los datos: con la misma watchlist durante meses, tu journal produce estadística comparable — cada cambio de universo invalida el histórico.
2. (a) Costo de tiempo: horas de pantalla que el layout + alertas devuelven (≈ 480 h/año en el ejemplo de la lección). (b) Costo de decisión: mirar el precio en vivo invita a intervenir fuera de plan (improvisar entradas, adelantar confirmaciones); la alerta separa la observación (plataforma) de la decisión (tú, con checklist).
3. Es válida si el futuro está genuinamente oculto cuando escribes tu lectura (régimen, zonas, dirección ANTES de avanzar el replay). La invalida: mirar velas futuras "para contextualizar", ajustar el marcado después de ver dónde giró, o rehacer la predicción tras ver el desenlace — curvar la regla tras medir, igual que la regla de oro de la misión M-3.

</details>
