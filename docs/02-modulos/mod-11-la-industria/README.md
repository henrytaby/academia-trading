# Módulo 11 · La Industria: Brokers, Estafas y Capital Externo — la puerta de la profesión

> [!WARNING]
> **Contenido educativo.** La mayoría de los traders minoristas pierde dinero (estudios de reguladores estiman entre 70 % y 90 %). Nada aquí constituye asesoría financiera, legal ni fiscal.

| Campo | Detalle |
|---|---|
| 💼 Nivel | 4 · Profesionalización — primer módulo del N4 |
| 📦 Módulo | 11 de 12 (FIT-12) |
| 🔬 Trazabilidad | 003 · M4.1–4.2, M6.1–6.6 · 004 · M8.1–8.5 · **Aporte propio:** due diligence universal sin marcas, reglas finas de prop firms (vacío 6), fiscalidad por principios (vacío 7), tier list como snapshot |
| ⏱️ Duración estimada | 7–9 h de teoría + 8–12 h de laboratorio/misión (2–3 semanas reales) |
| 📋 Estado | 🟢 Publicado (Sprint 11) |

---

## 🎯 Objetivo del Módulo

Elegir infraestructura con criterio forense y entender el negocio de quien te ofrece capital (o te vende humo). Con el N3 cerrado, tu negocio tiene sistema, presupuesto, evidencia y conducta auditable — le falta decidir **con quién opera y de dónde saldrá el capital de escala**. Este módulo audita la industria con la misma matriz forense que el programa aplica a todo: el broker (11.1: A-Book vs B-Book, regulación estricta vs offshore, los 5 pilares de selección sin marcas), el radar de estafas que domina el ecosistema minorista (11.2: binarias con esperanza negativa construida, bots de martingala, MLM, gurús, indicadores repintantes — con el protocolo de verificación regulatoria universal), y el fenómeno del fondeo minorista (11.3: el embudo de fees donde ~92 % fracasa según la propia FTMO; 11.4: las reglas finas que son el examen real; 11.5: la matriz de riesgo dinámico 0,25-0,50 % y la decisión "todavía no"; 11.6: el árbol de las 4 puertas — evidencia, esperanza, consistencia de 6-12 meses, simulación — que separa a quien se capitaliza de quien es el producto). Cierra con el pilar que ninguno de los cursos audita (vacío 7): la **fiscalidad por principios** (11.7: capital vs actividad, el registro como defensa, declarar siempre, el profesional local). Al terminar tienes la matriz de due diligence probada en 6 proveedores reales, el informe de elección defendido y el plan de capitalización a 12 meses — los dos documentos que el M12 integrará al plan de negocio final.

## 📚 Lecciones

| # | Lección | Esencia | Tiempo |
|---|---|---|---|
| 11.1 | [Brokers de verdad](leccion-11-1.md) | A-Book vs B-Book (el flujo de tu orden en mermaid); qué protege y qué no la regulación; los 5 pilares con evidencia verificable por celda | 45–60 min |
| 11.2 | [Radar de estafas](leccion-11-2.md) | Las 5 del ecosistema minorista con su aritmética (binarias: −10 % por op al 50 %; martingala quiebra en la racha 8) + el protocolo de verificación regulatoria en 4 pasos | 45–60 min |
| 11.3 | [Prop firms: el negocio real](leccion-11-3.md) | El embudo de ingresos por fees en mermaid; ~92 % fracasa (FTMO) y ~0,07 % de éxito neto (datos filtrados MFF, no auditados); colapsos: MFF, TFT, True Forex Funds | 50–65 min |
| 11.4 | [Reglas finas de las prop firms](leccion-11-4.md) | Las 6 reglas que desaprueban (diario con flotantes, trailing vs estático, consistency, noticias, lotaje, copiado) + la lectura forense del contrato en 20 min | 45–60 min |
| 11.5 | [Matriz de riesgo para evaluaciones](leccion-11-5.md) | El sizing contra el límite contractual: racha esperada ≤ 50-60 % del drawdown; la escala dinámica 0,50→0,40→0,25→0 %; "todavía no" como decisión ganadora | 50–65 min |
| 11.6 | [Cuándo intentar una evaluación](leccion-11-6.md) | El árbol de las 4 puertas (evidencia → esperanza → consistencia de 6-12 meses → simulación); capitalizarse ≠ ser el producto; el plan de capitalización a 12 meses | 40–55 min |
| 11.7 | [Fiscalidad por principios](leccion-11-7.md) | Capital vs actividad económica; el registro como defensa (tu journal v1 ES el expediente); declarar siempre; las 6 preguntas al profesional local — sin recetas de un solo país | 35–50 min |

> [!TIP]
> **Cómo estudiar este módulo:** dile a tu agente *"Siguiente lección"* y sigue el protocolo de sesión de estudio (§ 5.3 de `agents.md`). Este módulo se estudia **con tu journal v1 y tu reporte M-9/M-10 a mano**: las puertas del 11.6 y la simulación del 11.5 se responden con TUS números — sin ellos, el módulo es lectura; con ellos, es auditoría.
>
> **El caso maestro entra a la industria:** la operación de tu [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) *(ilustrativo)* — EUR/USD H4, E +0,16R neto, WR 40 % — ahora audita a sus proveedores: el broker que cobra 0,02R extra se come 4,8R/año (11.1); el desafío con drawdown 10 % recibe tu racha esperada de 7-9 al riesgo que la matriz apruebe (11.5); y la ganancia del caso maestro, neta de impuestos, es el número que el plan de capitalización a 12 meses compondrá (11.7).
>
> **Puente con M10 y M12:** del M10 heredas la conducta que el examen del 11.6 evalúa (6-12 meses de consistencia documentada) y los frenos que la matriz de 11.5 recalibra al límite ajeno. Hacia M12: la matriz de due diligence, el informe de elección y el plan de capitalización son tres de los bloques del **Plan de Trading y Plan de Negocio** final — este módulo fabrica sus insumos.

## 🧪 Laboratorio · Due diligence de 3 brokers y 3 prop firms

**Materiales:** las 7 lecciones + la matriz de criterios (crea `journal/matriz-due-diligence.md` con la plantilla de abajo) + acceso a los registros públicos de los reguladores + los estados/demo de prueba.

**La matriz universal (misma rúbrica para los 6 proveedores, sin publicidad):**

| Criterio | Puntuación | Fuente exigible |
|---|---|---|
| Regulación / estructura legal | 0-5 (binario: registro público no verifica = 0) | Registro oficial + warn lists |
| Modelo / transparencia | 0-5 (A/B-Book declarado · reglas con ejemplos numéricos) | Contrato/FAQ con números |
| Costos / reglas económicas | 0-5 (spread+comisión medida · fee, split, refembolso) | Medición propia + contrato |
| Retiros / pagos | 0-5 (velocidad documentada · historial de payouts verificable) | Agregadores independientes + reglas |
| Soporte / disputas | 0-5 (respuesta real probada · canal de disputa) | Prueba práctica |
| **Total** | **/25** | Cada celda con fuente citada |

**El protocolo en 4 líneas:** (1) pre-selección de 5-8 candidatos por fuentes múltiples (11.1 paso 2); (2) verificación regulatoria binaria de TODOS (protocolo de 11.2 — los que no pasan, fuera de la matriz); (3) puntuación de los 5 criterios con fuente por celda para los 3 finalistas de cada categoría; (4) prueba práctica: 2 semanas de demo medida en el broker finalista y la lectura forense del contrato en la prop firm finalista (11.4, los 20 minutos).

**Entregable:** `journal/matriz-due-diligence.md` con las 2 matrices completas (6 proveedores evaluados, 3 por categoría) + las capturas de las verificaciones regulatorias + el log de ejecución de la prueba práctica.

## 🎯 Misión

> [!IMPORTANT] Misión M-11 · Informe de elección + plan de capitalización a 12 meses
> **Objetivo:** convertir la matriz del laboratorio en dos documentos de decisión: el **informe de elección** (con justificación puntual por criterio) y el **plan de capitalización** (propio vs fondeo) a 12 meses.
> **El informe de elección** *(plantilla — `journal/informe-m11.md`)*: elección de broker con la justificación por criterio (por qué ganó cada pilar, con los números de tu medición) + elección de prop firm SOLO si las 4 puertas del 11.6 están abiertas (si no: la decisión documentada de esperar y su ruta) + los riesgos aceptados por cada elección (qué celda quedó débil y por qué es tolerable).
> **El plan de capitalización a 12 meses:** línea base (tu capital propio, rendimiento medido, aportes esperados) · escenario fondeo (si aplica: fee, probabilidad medida con TUS datos, payout esperado, riesgo de contraparte cotizado — esperanza matemática completa, no el escenario bonito) · la regla de mezcla (el fondeo es rama opcional, nunca plan A ni rescate) · calendario de puertas (qué se abre cuándo y con qué evidencia) · y la línea fiscal: la consulta con el profesional local agendada antes de la Fase 4 (11.7).
> **Entregable:** `journal/informe-m11.md` con ambos documentos. **Criterio de graduación:** informe completo **defendido en sesión socrática** con el agente (el agente pregunta por criterio, número y fuente — la defensa usa tu matriz, no tu memoria) + **quiz de autoevaluación ≥ 8/10**. **Tiempo estimado:** 3-4 h tras cerrar el laboratorio.

## ✅ Evaluación / Criterio de Graduación

Criterio del SYLLABUS para este módulo:

- **Laboratorio completo:** matriz de due diligence con 6 proveedores (3+3), verificación regulatoria documentada y prueba práctica.
- **Informe de elección con justificación puntual por criterio** + **plan de capitalización a 12 meses** con la regla de mezcla y el calendario de puertas.
- **Defensa socrática del informe** con el agente (casos: el criterio que descartó al favorito del marketing, la puerta cerrada y su ruta, el tratamiento fiscal de un payout).
- **Quiz de autoevaluación ≥ 8/10 (80 %)**.

Al aprobar todo: se abre **M12 · Plan de Trading y Plan de Negocio** — el cierre del programa: tus 11 módulos de insumos se convierten en el documento operativo de tu negocio.

## 📝 Quiz de Autoevaluación — umbral ≥ 8/10 (80 %)

1. A-Book vs B-Book: dibuja el flujo de una orden en cada modelo, explica qué gana el broker en cada uno y las dos salvaguardas que gestionan el conflicto del B-Book.
2. Calcula: tu coste medio por operación baja de 0,10R a 0,075R cambiando de broker (20 operaciones/mes). ¿Cuánto R ahorras al año? Si tu E neta es +0,16R, ¿qué porcentaje de tu esperanza anual representa el ahorro?
3. Opciones binarias: demuestra con la fórmula E que un payout de 0,80 exige 55,6 % de acierto solo para empatar, y explica por qué la prohibición regulatoria a minoristas (UE/Reino Unido) es coherente con la aritmética.
4. Martingala: con inicio 0,5 %, calcula la exposición acumulada de la racha de 8 y de la racha de 9. ¿Qué racha esperada tiene un sistema con WR 40 % en 100 operaciones y qué significa eso para "bots que ganan todos los meses"?
5. Prop firms: dibuja el embudo de ingresos y explica por qué el fee de desafío es el INGRESO principal y el payout el COSTE del modelo. ¿Qué dos cifras públicas (una de FTMO, una de datos filtrados MFF) cuantifican el embudo?
6. Reglas finas: un desafío con drawdown total 10 % trailing llega a +7 % de ganancia. ¿Dónde está el suelo? ¿Sobrevive tu racha esperada de 7 pérdidas a 0,5 %? ¿Y a 0,25 %? Formula el veredicto de la matriz.
7. Matriz de riesgo dinámico: enumera los 4 escalones con su consumo de límite y su riesgo. ¿Por qué el escalón baja el riesgo cuando el amateur lo sube — y qué lección de M10 es su antídoto estructural?
8. Las 4 puertas: nómbralas con su evidencia y su fuente de datos. Tu estado: N=100 forward, E +0,05R (IC [−4 %, +14 %] del equilibrio), 5 meses de journal, simulación OK. ¿Veredicto del árbol y plan?
9. Fiscalidad: distingue "renta de capital" de "actividad económica" con los 4 factores que suelen empujar a la segunda. ¿Qué 3 piezas componen tu expediente fiscal y qué rutina mensual lo mantiene vivo?
10. Integración: un influencer te ofrece "el mejor desafío del mercado, 90 % de split, sin reglas de consistencia, pagos instantáneos" con enlace de afiliado. Analiza la oferta con los 5 instrumentos del módulo (pilares, radar, embudo, reglas finas, puertas) y formula la respuesta completa del programa.

<details>
<summary>Ver clave de respuestas</summary>

1. A-Book: tu orden → LP/agregador → mercado; el broker cobra comisión/spread sin riesgo direccional (tu pérdida no es su ganancia). B-Book: tu orden se internaliza — el broker es tu contraparte (tu pérdida ES su ganancia: conflicto estructural). Salvaguardas: regulación estricta (supervisión de ejecución, segregación, canal de disputa) + tu auditoría de ejecución real (coste medio, slippage, retiros en TU cuenta).
2. Ahorro: 0,025R × 20 × 12 = **6R/año**. Tu esperanza anual: 0,16R × 240 = 38,4R → el ahorro representa el **15,6 %** de tu esperanza anual — por eso el pilar de costos se mide con TU ejecución y no con marketing: el "pequeño" diferencial de spread es una sexta parte de tu negocio.
3. E = p×g − (1−p): empate en p* = 1/(1+g) = 1/1,8 = **55,6 %**. La prohibición es coherente con la aritmética: con payout fijo < 100 % y vencimientos ultracortos, la varianza impide una medición honesta de ese 55,6 % (el ruido domina la señal a escalas de minutos), el broker es contraparte fija (conflicto máximo) y la evidencia regulatoria de daños minoristas fue determinante — el producto tiene esperanza negativa estructural, no es "riesgo": es extracción con gráfico.
4. Racha de 8: 0,5 % × (2⁸−1) = 0,5 × 255 = **127,5 %** (quiebra); la de 9: 0,5 × 511 = 255,5 % (ya sin cuenta). Con WR 40 %, la racha esperada en 100 operaciones es ln(100)/ln(1/0,6) ≈ **9** — el bot martingala muere justo en la racha que SU propia distribución garantiza: los "12 meses verdes" son la curva truncada que no muestra el mes de la ruina.
5. Embudo: marketing → fee del desafío (INGRESO principal, no reembolsado en ~92 %) → filtro de objetivos/drawdown → minoría fondeada → payouts (COSTE del modelo + material de marketing). Las dos cifras: **~92 % de desafíos fracasan** (declaración pública de FTMO) y **~0,07 % de éxito neto** (análisis de datos filtrados de MFF, no auditado pero consistente con la estructura).
6. Suelo del trailing a +7 %: 10 % − 7 % = **−3 %** respecto al inicial. Racha de 7 a 0,5 %: 1 − 0,995⁷ = **3,5 %** → pasa por debajo del suelo: descalificación estructural. A 0,25 %: 1 − 0,9975⁷ = **1,7 %** → cabe con margen. Veredicto: el desafío con trailing se opera a 0,25 % (o se busca estático) — el trailing cambia el sizing, no la constancia.
7. Escalones: 0-20 % consumido → 0,50 % · 20-40 % → 0,40 % · 40-60 % → 0,25 % (máx 2 A-setups/semana) · >60 % → 0 % nuevas aperturas (modo recuperación). Baja porque el margen es el inventario: con el límite consumido, la misma racha esperada es letal — es la cascada de M8 recalibrada al contrato, y su antídoto estructural es el de 10.5 contra el tilt: la decisión la toma el DATO (consumo), no la sensación ni la urgencia.
8. Puertas: (1) evidencia — N ≥ 100 backtests + 20-30 forward con reporte (M9); (2) esperanza — E neta dentro de IC, verde o ámbar alto (tabla de 3 vías); (3) consistencia — 6-12 meses de journal conductual (M10); (4) simulación — reglas del contrato vs tus números (11.5). Tu estado: puertas 1 y 4 abiertas, puerta 2 CERRADA (el IC cruza el equilibrio: E +0,05R no autoriza), puerta 3 cerrada (5 de 6-12 meses). Veredicto: **todavía no** — ruta: más N de forward para estrechar el IC y más meses de consistencia; re-auditar en el acta mensual. El marketing te diría "ahora": exactamente la ventana que el árbol bloquea.
9. Capital: rendimientos de patrimonio (pasivos, tasas especiales/exenciones). Actividad: negocio (contabilidad, gastos, cotizaciones). Empujan a actividad: frecuencia/volumen, apalancamiento sistemático, derivados como principal, dependencia económica + animus. Expediente: journal v1 exportado + estados mensuales del broker + depósitos/extracciones y conversiones — rutina: descargar, archivar, CRUZAR journal vs estado (discrepancia = corrección de 30 días, no investigación de 10 meses), backup doble.
10. Análisis completo: (a) **pilares** — el enlace de afiliado invalida la independencia (el afiliado a veces gana con tus pérdidas): pista, no evidencia; (b) **radar** — "sin reglas de consistencia + pagos instantáneos" es el marketing de la firmeza nula: la falta de reglas también es riesgo (contraparte sin estructura); (c) **embudo** — condiciones óptimas de captación = la firma necesita volumen de fees: ¿de dónde vive si paga instantáneo y sin filtros?; (d) **reglas finas** — "sin consistencia" suele significar otras reglas más duras en letra pequeña (trailing, noticias): lectura forense antes de cualquier fee; (e) **puertas** — tu decisión no la toma la oferta: la toman tus 4 puertas (evidencia, esperanza, consistencia, simulación). Respuesta: archivar la oferta en la lista de candidatos, verificar regulador/estructura legal, y decidir con tu árbol — no con el enlace. La mejor oferta del mercado no abre puertas cerradas.

</details>

## 📖 Glosario del Módulo

| Término | Inglés | Definición |
|---|---|---|
| A-Book | *A-book* | Modelo donde el broker transmite tu orden al mercado y cobra comisión/spread: sin riesgo direccional propio, conflicto estructural bajo |
| B-Book | *B-book* | Modelo donde el broker internaliza la orden y ES tu contraparte: legal y funcional, pero exige regulación fuerte y auditoría de ejecución propia |
| Regulación estricta | *tier-1 regulation* | Supervisión con teeth: segregación de fondos, fondo de compensación, reportes, canal de disputa — lo que la licencia "de registro" no da |
| Segregación de fondos | *client fund segregation* | Tu capital en cuentas bancarias separadas del capital de la firma: el requisito regulatorio que protege la custodia |
| Jurisdicción offshore | *offshore jurisdiction* | Marco con licencia de registro sin supervisión real del cliente: operar ahí = asumir el riesgo de custodia completo por cuenta propia |
| Afiliado | *affiliate (CPA/revenue share)* | Intermediario que cobra por referirte — a veces un % de TUS pérdidas: su ranking es pista, nunca evidencia |
| Opciones binarias | *binary options* | Pago fijo < 100 % por acertar dirección a plazo fijo: esperanza negativa estructural (payout 0,80 exige 55,6 % de acierto solo para empatar) |
| Martingala | *martingale* | Duplicar tamaño tras cada pérdida: la racha n acumula r(2ⁿ−1) — el quiebra llega antes que la racha esperada de tu WR |
| Indicador repintante | *repainting indicator* | El que reescribe sus señales históricas con datos nuevos: look-ahead como producto — se detecta con el test del replay/screenshot |
| Esquema MLM | *MLM scheme* | Modelo cuyo plan de ingresos real paga por reclutar, no por enseñar: la prueba de salida lo delata |
| Gurú de trading | *trading guru* | El que monetiza audiencia (lujo alquilado, testimonios filtrados) y no ofrece cuenta auditada de terceros: prueba social fabricada |
| Warn list | *warning list* | La lista de alerta del regulador: las firmas denunciadas aparecen ahí antes de colapsar — paso 3 de la verificación |
| Due diligence | *due diligence* | La investigación forense de un proveedor con matriz de criterios y fuente por celda — la misma rúbrica para todos, sin marcas |
| Prop firm | *proprietary trading firm (retail)* | Firma que vende desafíos y "fondea" aprobadros: su ingreso principal son los fees de los que fracasan |
| Desafío | *challenge* | El examen de evaluación (objetivo + drawdown + reglas finas): el producto que la firma vende |
| Fee del desafío | *challenge fee* | El precio del intento (típicamente no reembolsado salvo condiciones): el ingreso principal del modelo |
| Cuenta fondeada | *funded account* | La cuenta del aprobado — a menudo demo con premio: el payout depende de la solvencia y voluntad de la contraparte |
| Profit split | *profit split* | El reparto de ganancias (típicamente 70-90 % al trader): competitivo por marketing, secundario en el modelo de ingresos |
| Drawdown trailing | *trailing drawdown* | El límite total cuyo suelo sube con tu equity pico: al pico +7 %, tu suelo puede estar en −3 % — cambia el sizing del desafío |
| Consistency rule | *consistency rule* | Ningún día puede representar más del X % del beneficio: castiga la concentración (y el día de noticias) en el payout |
| Riesgo dinámico | *dynamic risk sizing* | La escala 0,50→0,40→0,25→0 % según el drawdown consumido: la cascada de M8 recalibrada al límite del contrato |
| "Todavía no" | *not yet* | La decisión ganadora cuando la simulación no pasa: se compra evidencia, no esperanza — posponer es gestión |
| Racha esperada vs límite | *expected streak vs limit* | La regla de margen del programa: la peor racha esperada consume ≤ 50-60 % del drawdown total — si no, el fee no se compra |
| Plan de capitalización | *capitalization plan* | El documento a 12 meses: línea base propia + fondeo como rama opcional con contraparte cotizada — nunca plan A ni rescate |
| Renta de capital | *capital income* | La clasificación fiscal de los rendimientos de patrimonio: la que tiende tu perfil de baja frecuencia — se confirma con profesional local |
| Actividad económica | *business income* | La clasificación de negocio: frecuencia, apalancamiento, derivados y dependencia económica empujan hacia ella |
| Expediente fiscal | *tax record file* | Journal + estados mensuales + movimientos de dinero, archivados y cruzados cada mes: la defensa que se construye fila por fila |

## 🔗 Referencias

- [SYLLABUS.md § 8 — N4, Módulo 11](../../01-syllabus/SYLLABUS.md)
- [analisis_cursos.md](../../00-analisis/analisis_cursos.md) — trazabilidad 003 · M4.1-4.2, M6.1-6.6 y 004 · M8.1-8.5; aportes propios: due diligence universal sin marcas, reglas finas de prop firms (vacío 6), fiscalidad por principios (vacío 7), tier list como snapshot
- [Módulo 10 · Psicotrading Científico](../mod-10-psicotrading-cientifico/README.md) — anterior: la conducta documentada que la puerta 3 del 11.6 audita
- [Módulo 8 · Gestión del Riesgo](../mod-08-gestion-del-riesgo/README.md) — la cascada que la matriz de riesgo dinámico recalibra al límite del contrato
- [La Receta de tu Primera Operación](../../03-recursos/laboratorio/receta-primera-operacion.md) — el caso maestro: su coste medio audita el pilar de costos y su E alimenta el plan de capitalización
- [Plantilla journal v1](../../../journal/plantilla_journal_v1.md) — los 5 números de la simulación y el expediente fiscal que ya llevas desde M9
- [Módulo 12 · Plan de Trading y Plan de Negocio](../mod-12-plan-trading-negocio/README.md) — el siguiente: la matriz, el informe y el plan de capitalización se integran al documento final del negocio
