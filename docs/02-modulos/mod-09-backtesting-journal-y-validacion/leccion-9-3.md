# Lección 9.3 · Métricas del reporte — de 100 filas a una página que decide

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 60–75 min de estudio |
| 🧱 Módulo | [M9 · Backtesting, Journal y Validación](README.md) |
| ⬅️ Anterior | [Lección 9.2 · Protocolo de backtesting manual](leccion-9-2.md) |
| ➡️ Siguiente | [Lección 9.4 · Forward testing en demo](leccion-9-4.md) |

---

## Por qué importa

Cien filas honestas de journal son materia prima — no un reporte. Los datos no deciden nada por sí mismos: lo que decide es el conjunto **métricas + umbrales declarados antes**, leído como el tablero de instrumentos de un avión: zonas verdes y rojas pintadas en frío, antes del vuelo, para que ninguna lectura se contamine del deseo del piloto. Esta lección construye ese tablero: las 13 métricas del reporte mínimo con sus fórmulas exactas, sus umbrales de decisión y la aritmética del caso maestro completa. Su lección más incómoda — y la más valiosa — es la de los **costes**: el detalle "menor" de 0,08R por operación que la 7.4 anticipó se come exactamente un tercio de tu esperanza bruta, hunde el Profit Factor de 1,40 a 1,25 y sube el WR de equilibrio de 32,3 % a 34,8 %. El reporte que ignora los costes no es optimista: es falso. Al terminar puedes convertir tu CSV en la página que decide — la misma que la misión M-9 entrega y la Evaluación N3 auditará.

## Concepto

**Las fórmulas del reporte.** Con las definiciones de M7 (WR, R:B, E) y dos piezas nuevas (el coste c en R y el PF):

$$WR = \frac{\text{ganadoras}}{N} \qquad \bar{R}_g = \text{media de las ganadoras en R}$$

$$E_{\text{bruto}} = WR \times \bar{R}_g - (1-WR) \times 1 \qquad E_{\text{neta}} = E_{\text{bruto}} - c$$

$$PF_{\text{bruto}} = \frac{\sum \text{ganancias}}{\sum \text{pérdidas}} \qquad WR^*_{\text{neto}} = \frac{1+c}{\bar{R}_g + 1}$$

La fórmula del **WR de equilibrio neto** es nueva y es la más importante del lote: con coste c, cada ganadora rinde $\bar{R}_g - c$ y cada perdedora cuesta $1 + c$; el equilibrio exige $WR \times (\bar{R}_g - c) = (1-WR) \times (1+c)$, de donde sale $WR^* = \frac{1+c}{\bar{R}_g+1}$. Con R̄ 2,1 y c 0,08: $1{,}08/3{,}10 = 34{,}8$ % — cuatro puntos y medio por encima del 32,3 % bruto. **Los costes engargolan la meta**: el sistema que parecía necesitar 33 % de acierto necesita 35 % — y cada décima de coste adicional (spread en noticias, slippage) sube la barra.

**El reporte mínimo de una página** — las 13 métricas, sus umbrales *(declarados en tu lista PRE antes de mirar los datos)* y los valores del caso maestro *(ilustrativo: el sistema híbrido 2+4 con WR esperado 40 %, R̄ 2,1, c 0,08, N=100, riesgo 1 %)*:

| # | Métrica | Fórmula / fuente | Caso *(ilustrativo)* | Umbral verde | Umbral rojo |
|---|---|---|---|---|---|
| 1 | N operado | conteo de filas | 100 | ≥ 100 | < 50 (decisión imposible) |
| 2 | WR medido | ganadoras / N | 40 % | ≥ 40 % neto | < WR* neto (34,8 %) |
| 3 | IC 95 % del WR | $\pm 1{,}96\sqrt{WR(1-WR)/N}$ | ±9,6 pp → [30,4; 49,6] | el peor caso sigue operable a 0,25 % | el mejor caso está bajo el equilibrio |
| 4 | R:B medio | $\bar{R}_g$ | 2,1R | ≥ 1,5 (plan M7) | < 1,2 |
| 5 | E bruta | $WR\bar{R}_g - (1-WR)$ | +0,24R | > 0 | ≤ 0 |
| 6 | Coste medio c | spread + slippage por op | 0,08R | ≤ 0,10R | > 0,15R (revisar broker/mercado) |
| 7 | E neta | E bruta − c | **+0,16R** | ≥ +0,10R | ≤ 0 (el sistema no paga) |
| 8 | WR de equilibrio neto | $(1+c)/(\bar{R}_g+1)$ | 34,8 % | — | referencia fija de la fila 2 |
| 9 | PF bruto | ΣG / ΣP | 1,40 | ≥ 1,3 | < 1,1 |
| 10 | PF neto | (ΣG − costes) / (ΣP + costes) | **1,25** | ≥ 1,2 | < 1,1 |
| 11 | Racha máxima medida | conteo de la muestra | ~9 esperada | ≤ 12 | ≥ 15 sin explicación (sospecha de régimen) |
| 12 | Max DD medido | de la curva de capital | −8,6 % (racha 9 al 1 %) | ≤ −10 % | > −15 % (línea de emergencia M8) |
| 13 | Disparos ejecutados / debidos | journal + actas | 100/100 | = 100 % | < 95 % (fuga de ejecución) |

*(a la tabla se añade el gráfico de la curva de capital — el ECG del negocio, 7.5 — que no se resume en un número: su pendiente, sus valles y su recuperación se miran, no se promedian.)*

**La aritmética completa del caso maestro.** Con WR 40 % y R̄ 2,1 en 100 operaciones: 40 ganadoras aportan $40 \times 2{,}1 = 84R$ bruto; 60 perdedoras cuestan 60R; E bruta $(84-60)/100 = +0{,}24R$; PF bruto $84/60 = 1{,}40$. Ahora el coste c = 0,08R por operación: las ganadoras netas rinden $84 - 100 \times 0{,}08 \times \frac{40}{40} = 84 - 3{,}2 = 80{,}8R$... más directo: cada ganadora rinde $2{,}02R$ y cada perdedora cuesta $1{,}08R$ → E neta $= 0{,}4 \times 2{,}02 - 0{,}6 \times 1{,}08 = 0{,}808 - 0{,}648 = +0{,}16R$; PF neto $= (0{,}4 \times 2{,}02)/(0{,}6 \times 1{,}08) = 0{,}808/0{,}648 = 1{,}25$. En 100 operaciones: $+16R$ netos acumulados → al 1 % con composición, $1{,}0016^{100} ≈ 1{,}173$ → **≈ +17 % de capital en el ciclo** *(ilustrativo, compuesto, sin aportes)*. El coste se comió $0{,}08/0{,}24 = 33$ % de la esperanza bruta — el ladrón silencioso que la 7.4 prometió medir.

**La decisión de 3 vías** — la tabla que convierte el reporte en decisión (los umbrales de las columnas verdes/rojas de arriba, leídos JUNTOS):

| Veredicto | Condiciones (todas) | Acción |
|---|---|---|
| 🟢 **Verde — aprobar** | WR ≥ 40 % neto · PF neto ≥ 1,25 · racha ≤ 12 · Max DD ≤ −10 % · disparos 100 % | El sistema opera al 1 % (M8) y pasa a forward (9.4); la muestra se congela y el changelog registra v1.1 vigente |
| 🟡 **Ámbar — provisional** | WR entre WR* (34,8 %) y 40 % · o PF neto 1,1–1,25 · o racha 13–14 · o DD −10…−15 % | Operar a 0,25–0,5 % SOLO en demo forward, seguir sumando muestra hacia N=200; sin cambios de reglas |
| 🔴 **Rojo — no operar** | WR < 34,8 % neto · o PF neto < 1,1 · o racha ≥ 15 sin explicación · o DD > −15 % | El sistema NO opera: volver al laboratorio de M7 con los datos (no con la desesperación); re-test completo tras cualquier modificación |

La regla de lectura: **un solo rojo manda** (es una tabla de vetos, no de promedios — un PF neto de 1,05 no se "compensa" con un buen WR: es la señal de que los costes o el arquetipo no dan para el negocio). Y el caso del empate técnico: si dos métricas caen en ámbar y el resto en verde, la decisión es ámbar — la cautela se elige siempre que la evidencia no es clara; el costo de la cautela es tiempo, el costo del exceso de confianza se paga en inventario (8.2).

**La curva de capital y las rachas: qué mirar.** La curva esperada del caso *(ilustrativo)* sube ≈ +17 % en 100 ops con el valle característico: la racha esperada máxima es $\ln(100)/\ln(1/0{,}6) ≈ 9$ pérdidas → $0{,}99^9 = 0{,}9135$ → **−8,6 %** de drawdown. Lo que se mira en la curva: **(a) la pendiente media** (¿consistente con E neta +0,16R?, o escalones: pocas operaciones que hacen todo el trabajo = concentración peligrosa); **(b) los valles** (¿profundidad y duración dentro de lo que la estadística de 7.5 predice?); **(c) la recuperación** (¿la curva sale del valle al ritmo esperado?). Y lo que NO se espera: una línea recta — la recta es la firma del data-mining o del look-ahead; la curva honesta es dentada, con valles de −8 % que la 8.2 te enseñó a leer en meses de recuperación. Si tu muestra mide una racha ≥ 15 (P puntual $0{,}6^{15} ≈ 0{,}05$ % — aún sumando las ~86 ventanas de arranque, improbable): primero se audita la integridad del dato (9.1), luego se documenta como sospecha de cambio de régimen, y se decide en la ventana mensual (9.6) — nunca en caliente.

## Analogía

El tablero de instrumentos del avión. Un piloto no "siente" su altitud: la lee en el altímetro, con una zona verde pintada y una franja roja que el fabricante fijó en tierra, en frío, con datos de ingeniería — no con la opinión del piloto de turno. La razón es brutal y simple: en el vuelo, el juicio humano se degrada (fatiga, hipoxia, pánico) y las zonas pintadas son la memoria del ingeniero protegiendo al piloto de sí mismo. Tu reporte es ese tablero: los umbrales verdes/rojos se declaran en tu lista PRE (en tierra), y el piloto que lee el tablero después de 100 operaciones — cansado, con apego al resultado y con semanas de trabajo encima — obedece la zona pintada, no su sensación. Cuando un piloto ignora el indicador "porque esta vez es distinto", la industria tiene un nombre para el informe que sigue: lectura de la caja negra. Tu journal es tu caja negra (9.5) — por eso el reporte se escribe CON ella y no de memoria.

## Cómo se hace: construir el reporte con tu hoja de cálculo

1. **Exporta y valida el dataset.** Del journal v1 (CSV): 100 filas, sin campos vacíos, con etiqueta E0–E7 en todas. La validación primero: un WR calculado sobre filas incompletas es un número bonito sin significado. La calculadora Python del programa ([`metricas_backtest.py`](../../../scripts/core/metricas_backtest.py)) hace esta validación y calcula todo el reporte: tu hoja debe coincidir con ella (el oráculo de M8, ahora para métricas).
2. **Calcula las métricas en este orden:** N → WR → IC → R̄_g → E bruta → c medio → E neta → WR* neto → PF bruto → PF neto → racha máxima → Max DD (sobre la curva acumulada en R, convertible a % con el 1 %) → disparos. El orden importa: varias métricas se alimentan de las anteriores, y el WR de equilibrio neto se calcula antes de leer el WR medido (para saber contra qué comparas).
3. **Dibuja la curva de capital.** Serie acumulada de R por orden temporal (columna simple: suma de r_real fila a fila). Mírala con las 3 preguntas del concepto: pendiente, valles, recuperación. Cópiala al reporte (captura o dibujo a mano: vale).
4. **Rellena la tabla con veredictos.** Cada fila con su valor, su umbral y su color (🟢🟡🔴). Un reporte sin veredictos por fila es un borrador: la decisión se toma contra umbrales, no contra impresiones.
5. **Aplica la tabla de 3 vías y escribe la decisión.** Con fecha, con la fila roja o ámbar que la motivó, y con el destino: forward (verde), más muestra a tamaño reducido (ámbar), o laboratorio de M7 con los datos (rojo). La decisión va al changelog del sistema (9.6) — decidir sin documentar es no haber decidido.

## Error común

**(1) Mirar solo el WR.** El WR sin el R:B no significa nada: 60 % con R:B 0,5 es $E = 0{,}6 \times 0{,}5 - 0{,}4 = -0{,}1R$ — un sistema PERDEDOR con "60 % de acierto". Las métricas se leen juntas o no se leen. **(2) Ignorar los costes.** El caso maestro lo demuestra: PF 1,40 bruto → 1,25 neto; WR de equilibrio 32,3 % → 34,8 %; un tercio de la esperanza evaporado. Todo umbral del programa es neto — el reporte que calcula bruto es publicidad, no auditoría. **(3) Leer la curva como una línea recta.** "Va hacia arriba, perfecto" — la pendiente media esconde si dos operaciones gigantes hacen todo el trabajo, si los valles exceden lo estadísticamente esperado, si la recuperación tarda el doble de lo que la E predice. La curva se mira; el promedio se calcula; ninguna de las dos cosas sustituye a la otra. **(4) Celebrar un PF > 3 con N=100.** M7 ya lo avisó y el reporte lo repite: PF > 3 en 100 operaciones es sospecha automática — de look-ahead, de data-mining, de muestra con régimen de moda o de costes no registrados. La E real de los sistemas operables es modesta (+0,1R a +0,3R netos); los milagros de backtest son el producto de salida más común del laboratorio amateur. **(5) Decidir con el número puntual y no con el conjunto.** WR 41 % no es verde si el PF neto es 1,05; racha 13 no es roja si el DD quedó en −9 % y el resto está verde. La tabla de 3 vías es un sistema de vetos: se lee completa, se decide completa, y el veredicto más restrictivo manda.

## Conexión cuantitativa

**Hacia 8.2:** el Max DD medido de la fila 12 reemplaza la estimación compuesta de la tabla de recuperación — ya no "espero −6 % por racha": mido el mío, y la decisión de sizing (1 % vs 0,25–0,5 %) se toma contra el dato. **Hacia 7.4:** la E neta es exactamente la esperanza aplicada de la matriz WR × R:B, ahora con el coste dentro — la fila de tu sistema en esa matriz era una hipótesis; el reporte la convierte en medición. **Hacia 9.4:** los umbrales de la tabla de 3 vías son los MISMOS que juzgarán el forward — "las métricas forward caen dentro de los intervalos del backtest" significa, concretamente, que el WR forward cae dentro del IC de la fila 3 y el PF neto cerca de la fila 10. **Hacia la misión M-9:** este reporte ES el entregable central — las 3 conclusiones y el changelog v1.2 se escriben sobre sus filas, no sobre la sensación del mes. Y hacia M12: el reporte de una página es el embrión del informe de resultados que tu plan de negocio presentará a quien financie tu operación — el formato se aprende ahora, con 100 filas propias, para no improvisarlo nunca.

---

## 🎯 Puntos clave

1. El reporte mínimo: **13 métricas con umbrales declarados antes** + la curva de capital — se lee completa y el veto más restrictivo manda.
2. Los costes son la primera auditoría: c = 0,08R se come el 33 % de la E bruta (PF 1,40 → 1,25) y sube el WR de equilibrio a **WR* = (1+c)/(R̄+1) = 34,8 %**.
3. La decisión es de 3 vías — 🟢 aprobar al 1 % · 🟡 provisional a 0,25–0,5 % y más muestra · 🔴 no operar — y frente a la duda se elige la cautela.
4. La curva esperada del caso: +17 % en 100 ops con un valle de −8,6 % (racha ~9) — la recta perfecta es la firma del sesgo, no del talento.
5. Racha ≥ 15 o PF > 3 con N=100: primero se audita la integridad del dato, se documenta la sospecha y se decide en la ventana — nunca en caliente.

## 🔄 Autoevaluación rápida

1. Mini-dataset de 10 operaciones: 4 ganadoras de +2,0R, +1,8R, +2,4R, +2,2R; 6 perdedoras de −1R; coste 0,08R por op. Calcula WR, R̄_g, E bruta, E neta, PF bruto y PF neto (números exactos).
2. Demuestra con la fórmula por qué el WR de equilibrio sube de 32,3 % a 34,8 % cuando añades c = 0,08R con R̄ 2,1 — y explica qué le pasa a la zona ámbar de la tabla de 3 vías.
3. Tu muestra de 100 mide: WR 42 %, PF neto 1,30, racha máxima 13, Max DD −11 %, disparos 97/100. Aplica la tabla de 3 vías fila por fila y escribe la decisión con su justificación (¿por qué la racha no la vuelve roja y qué hace la fila de disparos?).

<details>
<summary>Ver respuestas</summary>

1. WR = 4/10 = **40 %**. R̄_g = (2,0+1,8+2,4+2,2)/4 = 8,4/4 = **2,1R**. E bruta = 0,4×2,1 − 0,6×1 = 0,84 − 0,6 = **+0,24R**. E neta = 0,4×(2,1−0,08) − 0,6×(1+0,08) = 0,808 − 0,648 = **+0,16R**. PF bruto = 8,4/6 = **1,40**. PF neto = (8,4−0,32)/(6+0,48) = 8,08/6,48 = **1,25**. (Es el caso maestro en miniatura: con N=10 el IC sería ±30 pp — el mismo resultado con 10 filas no decide nada; la muestra mínima existe por una razón.)
2. Equilibrio: $WR \times (\bar{R}_g - c) = (1-WR) \times (1+c)$ → $WR^* = \frac{1+c}{\bar{R}_g+1}$. Bruto (c=0): 1/3,1 = 32,3 %. Neto (c=0,08): 1,08/3,10 = 34,8 %. La zona ámbar se ENGARGOLA por arriba: su límite inferior era el equilibrio, y el equilibrio real está 2,5 pp más alto — un WR medido de 34 %, que el bruto celebraría ("sobre equilibrio"), está BAJO el neto: es rojo. Consecuencia práctica: todos los umbrales del programa se calculan netos, porque el coste no es opcional — se paga en cada operación exista o no en tu hoja.
3. Fila a fila: WR 42 % ≥ 40 % → 🟢 · PF neto 1,30 ≥ 1,25 → 🟢 · racha 13 → **🟡** (umbral verde ≤ 12, rojo ≥ 15: zona ámbar — documentar, no reaccionar) · Max DD −11 % → 🟡 (verde ≤ −10 %, rojo > −15 %) · disparos 97/100 = 97 % → **🟡** (verde = 100 % exacto, rojo < 95 %: la fuga del 3 % queda en ámbar y la revisión semanal la nombra). Veredicto global: **ámbar** — el veto más restrictivo manda: el sistema sigue a 0,25–0,5 % en demo forward, se documenta la racha de 13 como observación (dentro de lo plausible a N=100 con WR 40 %: la cola estadística existe), y la conclusión 1 de la misión nombra la fuga de disparos como el dato más débil. No es verde: dos ámbar no se compensan con tres verdes — la cautela es la decisión por defecto cuando la evidencia no es limpia.

</details>
