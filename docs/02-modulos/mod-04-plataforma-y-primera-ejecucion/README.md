# Módulo 4 · Plataforma y Primera Ejecución

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada en este repositorio constituye asesoría financiera.

| Campo | Detalle |
|---|---|
| 🧱 Nivel | 1 · Fundamentos |
| 📦 Módulo | 4 de 12 (FIT-12) |
| 🔬 Trazabilidad | 003 · M1.6, M4.3–4.4 · 004 · M5.1–5.5 · **Aporte propio:** protocolo de demo ordenado y el stop como ley desde el día uno |
| ⏱️ Duración estimada | 4,5 h de teoría + 5–7 h de laboratorio/misión/quiz |
| 📋 Estado | 🟢 Publicado (Sprint 4) |

---

## 🎯 Objetivo del Módulo

Dominar la **herramienta** y ejecutar tus **primeras órdenes en demo con control total de la mecánica** — no de la estrategia: eso se construye en N2. Al terminar este módulo tendrás un layout de trabajo fijo con alertas (M4.1), sabrás qué garantiza y qué no cada tipo de orden y montarás OCO completas sin dudar (M4.2), conocerás tu factura de costos al céntimo — spread, comisión, slippage, swap (M4.3) —, ejecutarás largos y cortos entendiendo la asimetría del riesgo (M4.4), operarás en una demo configurada como laboratorio honesto y no como casino (M4.5), y habrás convertido el Stop Loss en ley operativa: definido antes de entrar, colocado por estructura, jamás movido en contra (M4.6). Este módulo existe porque es el cierre del Nivel 1: de entender el negocio y leer el precio pasas a **tocar la herramienta** — y la certificación del nivel exige mecánica impecable, no predicciones acertadas.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 4.1 | [TradingView profesional](leccion-4-1.md) | Layout multitemporal D1/H4/H1/M15, watchlist de 5, alertas que invierten el flujo, Bar Replay como simulador; atajos esenciales; 29 h/año devueltas por una plantilla | 35–45 min |
| 4.2 | [Tipos de órdenes](leccion-4-2.md) | Market / Limit / Stop / Stop-Limit / OCO: qué garantiza cada una y qué no; TP=limit y SL=stop explican el viaje asimétrico; stop-limit prohibido como SL | 45–60 min |
| 4.3 | [El costo real de operar](leccion-4-3.md) | Las 4 cabinas del peaje: spread, comisión, slippage, swap (triple los miércoles); ≈ 2,6 pips ≈ 0,09R por operación tipo; E_neto = E_bruto − c | 45–60 min |
| 4.4 | [Largos y cortos](leccion-4-4.md) | Mecánica del short en 5 pasos; borrow fee y swap; el squeeze como cascada sin techo; suben en escalera, caen en ascensor; SL de ley absoluta en cortos | 40–50 min |
| 4.5 | [Cuenta demo](leccion-4-5.md) | Qué simula (mecánica) y qué no (psicología, slippage real); configuración realista no negociable; lectura del panel; el circuito demo → demo-forward → real micro | 40–50 min |
| 4.6 | [El Stop Loss como ley](leccion-4-6.md) | El SL marca la invalidación, no el dolor; 3 propiedades de la ley; orden sagrado estructura → SL → lote; checklist 6/6; sin SL no existe ni la fórmula de E | 45–60 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo se estudia **con la plataforma abierta**: cada lección termina pidiéndote tocar la herramienta — la teoría sin dedos no certifica mecánica.
>
> **Puente con la [Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md):** con M4, la receta ejecuta sus **pasos 3–11**: definición de setup, cálculo de posición, OCO frontal, ejecución, gestión, cierre, journal y checklist 6/6. Tu objetivo sigue siendo la **primera operación PROCESADA** — el primer dólar real sigue reservado para F4 (veto CRO del temario v1.1).

## 🧪 Laboratorio · Las 4 órdenes en demo

**Materiales:** cuenta demo configurada según la [Lección 4.5](leccion-4-5.md) (capital = tu plan real, riesgo 1 %) + layout de la [Lección 4.1](leccion-4-1.md).

**Procedimiento paso a paso** (cada orden se registra con captura ANTES de enviarla y DESPUÉS de cerrarla):

1. **Orden market** — en el solapamiento Londres–NY, abre y cierra una posición mínima (0,01 lotes) EUR/USD en la misma vela. Anota: precio pedido vs precio ejecutado (la diferencia es spread + slippage vivo, [Lección 2.1](../mod-02-motor-del-precio/leccion-2-1.md) y [4.3](leccion-4-3.md)).
2. **Orden limit de entrada** — coloca un buy limit en el borde de una zona real de tu marcado (protocolo M3.3). Si no se llena en 24 h, muévela o retírala: anota la decisión. Si se llena, el paso 3 la recibe.
3. **OCO completa** — sobre la posición del paso 2 (o una nueva): SL por estructura tras el swing (con respiración) + TP por estructura con R:B ≥ 1:2, montados como paquete y **verificados en el panel antes de la sesión**.
4. **Orden stop de entrada (ruptura)** — coloca un buy stop 2 pips sobre una resistencia con ruptura ya confirmada en 3 pasos ([Lección 3.4](../mod-03-anatomia-del-grafico/leccion-3-4.md)), SL y TP por estructura. Observa qué hace la orden al tocar el nivel.
5. **Informe de laboratorio:** para cada orden: tipo elegido, qué garantizaba, qué riesgo de ejecución asumía y qué aprendiste del resultado — guardado en `journal/laboratorio-m4.md`.

**Entregable:** las 4 capturas + informe. El objetivo NO es ganar pips: es que tus manos sepan montar cada tipo sin consultar nada — la cabina de la [Lección 4.1](leccion-4-1.md) operada de memoria.

## 🎯 Misión

> [!IMPORTANT] Misión M-4 · 10 Operaciones Demo Procesadas
> **Objetivo:** certificar tu mecánica de ejecución: 10 operaciones demo completas donde lo evaluado no es acertar, sino **procesar impecablemente** — SL puesto antes de entrar en el 100 %, lote calculado desde el SL, OCO verificada y journal completo.
> **Entregable:** `journal/operaciones-demo-m4.md` (o la plantilla v0 CSV ampliada) con las 10 filas + capturas (gráfico al entrar con SL visible + panel al cerrar) + el análisis final.
> **Criterio de aceptación (por fila):** setup definido por escrito · SL colocado por estructura y montado ANTES de la entrada · lote desde el SL (riesgo ≤ 1 %, redondeo a la baja) · TP con R:B ≥ 1:2 · OCO verificada · fila del journal completa al cerrar. **Cero operaciones sin SL — una sola violación invalida la fila.**
> **Etiqueta en journal:** `mision-4-demo` · **Tiempo estimado:** 10 operaciones en 2–3 semanas (ritmo natural: máximo 1–2 por día; la velocidad no es la métrica).
> **Regla de oro:** la entrada puede ser simple (rechazo de zona confirmado, por ejemplo) — la sofisticación del setup no puntúa; la mecánica 6/6 sí. Esta misión certifica que el [checklist de la Lección 4.6](leccion-4-6.md) ya vive en tus dedos.

**Formato de fila (copiar por operación):**

```text
#N — fecha — instrumento — dirección (long/short)
Orden: [limit/stop + precio] — Lote: [calculado desde el SL] — Riesgo real: [$ y %]
SL: [precio — por qué estructura] — TP: [precio — R:B resultante]
OCO verificada: [sí — captura] — Resultado: [+/-R y $] — Costos observados: [$]
Checklist: [6/6] — Nota (1 línea): qué demostró esta operación sobre tu mecánica
```

## ✅ Evaluación / Criterio de Graduación — 🏆 Evaluación Nivel 1

El M4 no cierra un módulo: cierra **el Nivel 1 completo**. Criterio del SYLLABUS:

- **Misión M-4 completa:** 10/10 operaciones con checklist 6/6 — **cero violaciones de SL** (el criterio "sin violaciones" es absoluto).
- **Examen teórico integrador N1:** [30 preguntas sobre M1–M4](../../03-recursos/evaluaciones/examen-n1.md) — **≥ 24/30 (80 %)** para aprobar.
- **Checklist de ejecución sin violaciones:** revisión del journal con el agente: las 10 operaciones + el laboratorio muestran mecánica consistente (misma rutina, mismo checklist, sin improvisaciones de órdenes).
- **Entrevista socrática:** 5 preguntas abiertas del examen N1 respondidas en vivo con el agente (defensa de razonamiento, no memorización).

Al aprobar todo: **N1 🏆 certificado** en el README raíz, y se abre N2 (M5 · Estructura de Mercado y Liquidez) — donde el precio desnudo de M3 se descodifica con la lógica institucional, y tu demo pasa a operar un sistema v1.0.

## 📝 Quiz de Graduación

1. Market, limit y stop: ¿qué garantiza cada una y qué no? Asigna un uso del programa a cada una.
2. ¿Por qué el TP se monta como limit y el SL como stop? ¿Qué fenómeno de la Lección 2.1 explica el viaje asimétrico?
3. Tu compañero monta el SL como stop-limit "para no pagar slippage". Descríbelo el escenario exacto en que su protección no lo protege.
4. Lista los 4 costos de operación. ¿Cuáles pagas en TODA operación y cuáles solo en algunas? ¿Por qué "cuenta sin comisiones" es una frase de marketing?
5. Cálculo: tu sistema tiene E bruto +0,20R, costo todo incluido 0,09R y opera 40 veces al mes con R = 20 $. ¿Cuál es tu E neto mensual en $ y qué porcentaje de la ventaja bruta se comió el peaje?
6. Enumera la mecánica del short en 5 pasos y explica por qué su riesgo sin SL es ilimitado mientras el del long está acotado.
7. Describe el short squeeze como bucle de 3 pasos. ¿Qué conducta del programa te saca del bucle antes de entrar?
8. Un estudiante practica en demo con 100 000 $ virtuales y lotes de 1.00. ¿Qué dos capacidades está entrenando mal y qué configuración exige el programa?
9. Calcula el margen usado de 0,10 lotes EUR/USD a 1,0900 con apalancamiento 1:30. Si tu margen libre se encoge operación tras operación, ¿qué te está diciendo el panel?
10. Enuncia las 3 propiedades de la ley del SL y explica por qué el lote se calcula DESPUÉS del SL — ¿qué deformación introduce invertir el orden?

<details>
<summary>Ver clave de respuestas</summary>

1. **Market:** garantiza ejecución, no precio (urgencia/emergencia). **Limit:** garantiza precio, no ejecución (entrada en zona + TP). **Stop:** al tocar el nivel dispara market — ejecuta casi seguro, precio no garantizado (SL + entradas por ruptura).
2. El TP es limit porque cobrar exige que el precio **llegue** (nadie te ejecuta la ganancia con urgencia); el SL es stop porque salir de emergencia exige **participación garantizada** al tocar el nivel. El viaje asimétrico sale del spread de la [Lección 2.1](../mod-02-motor-del-precio/leccion-2-1.md): con TP de 60 y SL de 30, el bid debe recorrer 62 hacia arriba y solo 28 hacia abajo.
3. Un gap (o requote violento) atraviesa su nivel sin operaciones a su precio: la limit que dispara el stop-limit queda fuera de mercado y **no se llena** — posición abierta sin protección mientras el precio corre. Ejemplo: SL en 1,0794, gap de 20 pips → su limit no llena y pierde 20+ pips extra mientras tanto. El stop simple habría ejecutado a mercado con ~1 pip de slippage.
4. **Siempre:** spread (+ comisión si la cuenta la cobra). **Condicionales:** slippage (noticias/gaps) y swap (posiciones overnight). "Sin comisiones" es marketing porque la comisión vive escondida en el spread más ancho: el costo correcto se compara todo incluido ([Lección 4.3](leccion-4-3.md)).
5. E neto = (0,20 − 0,09) × 40 × 20 $ = **+88 $/mes**. Ventaja bruta: 0,20 × 40 × 20 = 160 $ → el peaje se comió **45 %** de la ventaja bruta (0,09/0,20). El negocio real se planifica con E neto.
6. (1) Pedir prestadas → (2) vender → (3) esperar la caída → (4) recomprar más barato → (5) devolver; ganancia = venta − recompra − costos. El long sin SL pierde como máximo hasta precio 0 (acotado); el short debe recomprar para devolver y **el precio de recompra no tiene techo** → pérdida ilimitada.
7. (1) Subida → cortos en pérdida; (2) cortos cierran = recompra obligada = demanda compradora → sube más; (3) la subida liquida más cortos → más recompra: bucle sin techo. Conducta: SL montado antes de entrar y respetado (sales a −1R sin formar parte de la cascada).
8. Entrena mal: (a) el **tamaño** (jamás operará 1.00 con 2 000 $ reales — su mecánica de riesgo no se automatiza) y (b) la **frecuencia/seriedad** (operar como videojuego sin journal). El programa exige: capital del plan real, riesgo 1 %, apalancamiento real, lote micro resultante (0,05–0,06 en EUR/USD).
9. Nominal = 0,10 × 100 000 × 1,0900 = 10 900 $; a 1:30 → **≈ 363 $** de margen usado. Margen libre que se encoge sostenidamente = el tamaño de tus posiciones está comiéndose tu colchón: sobredimensionamiento — la señal del panel antes de cualquier margen call.
10. Las 3 propiedades: **definido antes de entrar** · **colocado por estructura** (tras el swing/zona con respiración) · **nunca se aleja del precio**. El lote se calcula después porque el SL es la entrada del cálculo (lote = riesgo $ ÷ (SL pips × valor pip)): invertir el orden significa "elegir" el stop para que quepa la apuesta deseada — deformar el análisis en favor del deseo, la definición operativa de apostar.

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| Orden market | *market order* | Ejecuta ya al mejor precio disponible: garantiza ejecución, no precio |
| Orden limit | *limit order* | Ejecuta solo a tu precio o mejor: garantiza precio, no ejecución |
| Orden stop | *stop order* | Dormida hasta que el precio toca el nivel; dispara market: SL y rupturas |
| Stop-limit | *stop-limit order* | Al tocar el nivel dispara una limit: puede no llenarse — prohibido como SL |
| OCO | *one-cancels-other* | Dos órdenes emparejadas (SL+TP): una ejecuta, la otra se cancela |
| Slippage | *slippage* | Diferencia entre el precio pedido y el obtenido; intermitente, concentrado en noticias/gaps |
| Comisión | *commission* | Cargo fijo por operación en cuentas raw/ECN; en las standard vive escondida en el spread |
| Swap | *swap / rollover* | Interés diario por posición overnight (diferencial de tasas); triple los miércoles |
| Cuenta raw/ECN | *raw/ECN account* | Spread mínimo + comisión fija; se compara todo incluido, nunca partida aislada |
| Margen | *margin* | Garantía retenida por la posición: nominal ÷ apalancamiento |
| Margen libre | *free margin* | Capital − margen usado − pérdidas flotantes; si se encoge, sobredimensionas |
| Apalancamiento | *leverage* | Multiplicador del nominal por cada $ de garantía; agranda el error, no el riesgo planeado |
| P/L flotante | *floating P/L* | Resultado si cerraras ahora: papel hasta que cierras |
| P/L realizado | *realized P/L* | Resultado definitivo al cerrar: el único que entra al journal |
| Posición corta | *short position* | Vender prestado para recomprar más barato; riesgo sin techo si no hay SL |
| Borrow fee | *borrow fee* | Interés anual por el préstamo de acciones en corto; entra en E como costo |
| Short squeeze | *short squeeze* | Cascada de recompras obligadas de cortos perdedores que acelera la subida |
| Gap risk | *gap risk* | Salto de precio que se salta tu nivel: exige tamaño menor en cortos y fines de semana |
| Breakeven | *break-even* | Mover el SL al precio de entrada cuando el trade avanza: gestión opcional (M8) |
| Layout | *layout* | Plantilla de gráficos fijos (D1/H4/H1/M15) que abre tu rutina idéntica cada día |
| Watchlist | *watchlist* | Lista vigilada de ≤ 5 instrumentos: concentración por decisión de negocio |
| Alerta | *price alert* | Aviso cuando el precio toca tu nivel: el precio te busca a ti |
| SL mental | *mental stop* | Stop sin orden en el bróker: no es SL — la ley exige la orden montada |

## 🔗 Referencias

- [SYLLABUS.md § 5 — N1, Módulo 4](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — aporte propio del módulo: protocolo de demo ordenado y stop como ley desde el día uno
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — sus pasos 3–11 se ejecutan con este módulo
- [Examen integrador N1](../../03-recursos/evaluaciones/examen-n1.md) — evaluación 🏆 del Nivel 1
- [Módulo 3 · Anatomía del Gráfico](../mod-03-anatomia-del-grafico/README.md) — anterior
- Módulo 5 · Estructura de Mercado y Liquidez — siguiente (N2; se publica en el Sprint 5)
