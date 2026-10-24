# Lección 11.5 · Matriz de riesgo para evaluaciones — el sizing que sobrevive a su propia varianza

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 50–65 min de estudio |
| 🧱 Módulo | [M11 · La Industria](README.md) |
| ⬅️ Anterior | [Lección 11.4 · Reglas finas de las prop firms](leccion-11-4.md) |
| ➡️ Siguiente | [Lección 11.6 · Cuándo intentar una evaluación](leccion-11-6.md) |

---

## Por qué importa

Las dos lecciones anteriores entregaron el mapa del negocio (11.3) y la letra fina del examen (11.4). Esta lección entrega el **plan de sizing** — la traducción numérica de todo el módulo. El principio es el que tu N3 ya tenía (M8: el riesgo se calcula contra el límite de inventario, no contra el deseo) pero invertido en dirección: en tu cuenta propia el límite era TU línea de emergencia (−15 %); en una evaluación el límite es CONTRACTUAL (4-10 %), más corto, con reglas flotantes y con una condición única: **la varianza no negocia**. La matriz de riesgo dinámico que esta lección instala responde la pregunta práctica: ¿cuánto riesgo por operación le corresponde a un desafío cuya regla de drawdown ya consumí en parte? — y su respuesta es una escala (0,25-0,50 %) que baja conforme el margen se consume, la inversa exacta del instinto amateur (que sube el riesgo cuando se acerca al fracaso — el tilt de 10.5 con fee pagado). Y añade la pieza de honestidad que completa el módulo: la condición **"todavía no"** — la respuesta matemática legítima cuando tu propia evidencia dice que el desafío no cabe. Si terminas con una sola idea: **en una evaluación, el sizing se calcula contra el límite del contrato y contra tu racha esperada medida — y "todavía no" es una decisión ganadora, no una derrota.**

## Concepto

**La geometría del problema, con fórmula.** Tu peor enemigo dentro del desafío es tu racha esperada — la misma de siempre (M8/M10), ahora contra un límite contractual. Con riesgo $r$ por operación y racha de $n$ pérdidas:

$$DD_{racha} = 1 - (1-r)^n \qquad \text{con tu racha esperada } n = \frac{\ln(N)}{\ln(1/(1-WR))}$$

Para el caso maestro (WR 40 %, N ≈ 40 operaciones de un desafío típico de 2 fases): $n = \frac{\ln 40}{\ln(1/0{,}6)} = \frac{3{,}69}{0{,}511} \approx 7$ pérdidas seguidas esperadas en el periodo. La tabla de supervivencia:

| Riesgo por operación | DD de la racha de 7 | Contra límite 10 % estático | Contra límite 5 % diario (racha no aplica, pero 2 ops + flotante) | Veredicto |
|---|---|---|---|---|
| 1,0 % | $1-0{,}99^7 = 6{,}8$ % | Consume 68 % — fuera de la regla del margen | 2 ops + flotante roza el límite | **No cabe** |
| 0,5 % | $1-0{,}995^7 = 3{,}5$ % | Consume 35 % — margen justo | Con flotante 1,8 %: 2,8 % de 5 % — OK sin correlación | **Aceptable con disciplina** |
| 0,25 % | $1-0{,}9975^7 = 1{,}7$ % | Consume 17 % — margen amplio | 1,4 % + flotante: sobra | **El tamaño del programa para empezar** |

La lectura: el mismo sistema con la misma evidencia **cabe o no cabe según el sizing** — y "cabe" se define con la regla de margen del 11.4: la peor racha esperada consume ≤ 50-60 % del límite. Al 1 % no cabe; al 0,5 % cabe con disciplina; al 0,25 % cabe con aire. El objetivo de ganancia del desafío (+8-10 %) sigue alcanzable a 0,25-0,5 % — solo tarda más operaciones: el examen es de supervivencia a la varianza, no de velocidad.

**La matriz de riesgo dinámico** — la escala que ajusta el tamaño según el drawdown YA consumido (la regla del contrato manda; la matriz te mantiene lejos de ella):

| Drawdown del límite ya consumido | Fase | Riesgo por operación | Disparos permitidos | Regla adicional |
|---|---|---|---|---|
| **0-20 %** | Zona verde | **0,50 %** | Los del sistema | Normal: temperatura, ventana, journal |
| **20-40 %** | Zona ámbar | **0,40 %** | Los del sistema | Nada de correlación intradía (tope motor estricto) |
| **40-60 %** | Zona naranja | **0,25 %** | Máx 2 por semana de calidad plena | Solo A-setup de tu checklist; nada de "casi" |
| **> 60 %** | Zona roja | **0 % nuevas aperturas** | 0 | Modo recuperación: gestión de abiertas + revisión — la cuenta vive para el próximo intento |

Dos propiedades que la hacen funcionar: *(1) es anticipada* — la zona la marca el dato (consumo del límite), no la sensación; es la temperatura de 10.6 aplicada al contrato. *(2) es la inversa del tilt* — donde el amateur sube el tamaño para "recuperar" (10.3), la matriz baja el tamaño para sobrevivir: cada escalón hacia abajo ES la cascada de M8 recalibrada al límite ajeno.

**"Todavía no": la cuarta salida de la matriz.** Si con tu evidencia medida (racha esperada real de tu forward, peor flotante intradía, coste medio) la configuración mínima (0,25 %) consume más del 60 % del límite — el desafío no cabe. La respuesta del programa no es "riesgo 0,15 %" (el objetivo de ganancia se vuelve inalcanzable en el tiempo del desafío y el fee se convierte en renta de la firma): es **posponer** — la decisión "todavía no" con su plan: más N de forward testing (reducir el IC de tu WR), mejor coste (elegir la sesión/par del pilar 3), o simplemente aceptar que tu sistema de 2-3 disparos/semana necesita tipos de desafío con más tiempo o límites más holgados. La comparación con el resto del programa es directa: "todavía no" es la roja de la tabla de 3 vías de 9.3 — una decisión informada que protege el inventario (aquí, el fee y la reputación de consistencia).

**La simulación previa (obligatoria antes de cualquier fee).** Con tu journal de forward (M9/M10) y las reglas finas del contrato (11.4), la simulación en 4 pasos: (1) extrae de TU registro: WR, R:B, coste medio, racha máxima medida, peor flotante intradía, concentración de ganancias por día; (2) aplica las reglas del contrato: racha esperada × riesgo vs límite total (estático o trailing); peor flotante + 2 ops vs límite diario; día máximo de ganancia vs consistency; (3) corre el veredicto de margen: ≤ 50-60 % de consumo en la peor racha = compra; > 60 % = "todavía no"; (4) registra la simulación en tu matriz de due diligence — el fee se compra con papel y pluma, no con entusiasmo.

## Analogía

El ascenso a altura y el oxígeno de reserva. Los montañistas planifican el oxígeno no para el ascenso ideal sino para el peor escenario razonable: si la reserva mínima es 50 % del tanque en el punto de giro, y tu ritmo normal consume 8 % por hora, el punto de giro se decide ANTES de salir — no en la montaña con el frío pidiendo "solo un poco más". El amateur del desafío sube el riesgo cuando el margen baja (el frío pidiendo más oxígeno); la matriz de riesgo dinámico es el plan de giro: la zona de consumo decide el ritmo, y "todavía no" es quedarse en el campamento base con vida y ganas — la montaña sigue ahí la próxima temporada, el tú sin inventario no.

## Cómo se hace: instalar tu matriz personal (el taller de 30 minutos)

1. **Extrae tus 5 números del journal:** WR forward (con su IC), R:B, coste medio por operación, racha máxima medida en 100 ops, peor flotante intradía medido. Si no tienes el peor flotante: se mide a partir de HOY (el journal v1 lo permite) — es la celda que el contrato necesita.
2. **Calcula tu racha esperada para el N del desafío** (fórmula ln con tu WR) y verifica contra tu racha MÁXIMA medida — si la medida supera la esperada por mucho (racha 12-14 con WR 40 %), usa la medida: tu muestra ya te habló.
3. **Escribe tu matriz en la hoja de temperatura del desafío:** los 4 escalones con tus números, pegada junto a la plataforma — el consumo del límite se marca al final de cada jornada (30 segundos, del journal).
4. **Define tu "todavía no" por escrito ANTES de pagar:** la condición exacta (consumo > 60 % del límite a 0,25 %, o peor flotante + 2 ops > límite diario) y qué harás en su lugar (N más grande, otra firma con límites más holgados, o nada — seguir construyendo evidencia).
5. **Ensaya la transición de escalones en la misión M-11:** la simulación de la matriz con tus datos reales de las 10 sesiones de M-10 — el taller es parte del entregable del laboratorio.

## Error común

**(1) "A 0,25 % el desafío tarda demasiado."** El tiempo del examen no es tu enemigo: la varianza lo es — la mayoría de firmas serias no premia la velocidad (algunas la penalizan con mínimos de días de trading) y la consistency rule castiga exactamente la concentración rápida. Tardar más es el precio de sobrevivir a TU varianza normal. **(2) Subir el riesgo en la zona naranja "para salir del hoyo".** El tilt con fee pagado (10.5): la matemática es implacable — con el margen consumido, la misma racha esperada ya es letal; el escalón a 0,25 % no es miedo: es la cascada de M8 recalibrada. **(3) Comprar desafíos múltiples "para diversificar" a riesgo alto en cada uno.** Diversificar contrapartes (11.3) es prudencia; comprar 5 loterías simultáneas es 5 fees — la diversificación válida es de riesgo gestionado, no de apuestas duplicadas con la misma varianza. **(4) Ignorar el coste total de la "carrera de desafíos".** El aspirante que compra 6 desafíos al año a 150 $ con 92 % de fracaso espera gastar ~900 $ por... calcula su esperanza: la carrera de desafíos SIN evidencia previa es el fee de 11.3 comprado en serie — la única carrera que el programa valida empieza con el forward testing ya aprobado. **(5) Confundir "todavía no" con "nunca".** La condición es temporal y medible: más N reduce el IC, mejor coste reduce el consumo, un límite más holgado cambia la geometría — la puerta se abre con evidencia, no con deseo; y mantener la decisión documentada (changelog de tu plan de capitalización, misión M-11) es lo que la convierte en gestión y no en frustración.

## Conexión cuantitativa

**Hacia M8:** la matriz es tu cascada personal (−2/−4/−6 %) reescalada al límite contractual — el principio es el mismo: el riesgo baja cuando el inventario expuesto sube; aquí el "inventario" es el margen del contrato. **Hacia 9.3:** los 5 números de la simulación salen de tu reporte de métricas — la preparación del desafío ES la lectura de tu propio reporte con otros límites. **Hacia 10.6:** la matriz de riesgo dinámico es la dicotomía del control en su forma más pura: la zona la marca el dato (consumo), la decisión ya está escrita (escalón), y la varianza que no controlas no puede empujarte a romper tu propio protocolo. **Hacia 11.6:** "todavía no" conecta con el criterio honesto de la próxima lección — 6-12 meses de consistencia documentada: la matemática de esta lección le pone números al calendario.

---

## 🎯 Puntos clave

1. El sizing del desafío se calcula contra el **límite contractual y tu racha esperada medida** — con la regla de margen: la peor racha consume ≤ 50-60 % del límite (al 1 % el caso maestro consume 68 %: no cabe).
2. La **matriz de riesgo dinámico** escala 0,50 % → 0,40 % → 0,25 % → 0 % según el drawdown consumido — la inversa exacta del tilt: donde el amateur sube, la matriz baja.
3. **"Todavía no" es una decisión ganadora**: si ni 0,25 % cabe, el fee no se compra — se compra evidencia (más N), no esperanza; es la roja de la tabla de 3 vías aplicada al fee.
4. La **simulación previa obligatoria** usa tus 5 números del journal (WR, R:B, coste, racha, peor flotante) contra las reglas exactas del contrato — el fee se compra con papel y pluma.
5. El objetivo de ganancia sigue alcanzable a 0,25-0,5 %: el examen es de **supervivencia a la varianza**, no de velocidad — y las reglas finas (consistency, mínimos de días) castigan justo la prisa.

## 🔄 Autoevaluación rápida

1. Un desafío exige +8 % con drawdown total 10 % estático y diario 5 %. Tu evidencia: WR 42 %, racha esperada para 45 operaciones ≈ 7, peor flotante intradía 2,1 % a riesgo 0,5 %. Simula los tres chequeos (racha vs total; flotante + 2 ops vs diario; consumo vs regla de margen) y da el veredicto con el tamaño correcto.
2. Estás en la zona naranja (consumo 45 %) y aparece un A-setup de tu checklist en tu mejor sesión. ¿Qué sizing aplica y qué dos restricciones de la matriz hay que verificar antes de disparar? ¿Qué haría el tilt en tu lugar y por qué la matriz existe exactamente para ese momento?
3. Tu evidencia a N=100: WR medido 35 % (IC ±9,3 pp), R:B 2,0, coste 0,08R. El desafío que quieres compra exige constancia, no suerte. Calcula tu E neta y tu WR* neto, decide con la tabla de 3 vías y formula la decisión completa "todavía no": el veredicto, las 2 rutas de mejora con su mecanismo matemático (qué variable mueve cada una) y qué NO es la decisión (las dos lecturas falsas).

<details>
<summary>Ver respuestas</summary>

1. Racha de 7 a 0,5 %: $1-0{,}995^7 = 3{,}5$ % de 10 % = **35 % de consumo** — dentro de la regla de margen (≤ 50-60 %) ✓. Diario: peor flotante 2,1 % + 2 ops perdidas 1,0 % = **3,1 % de 5 % = 62 %** del límite diario — cabe pero al borde: la restricción adicional es cero correlación intradía (el flotante combinado de 2 correlacionadas puede doblar la excursión) y ninguna tercera operación el mismo día si hay flotante mayor a 1 %. Veredicto: el desafío cabe a 0,5 % en zona verde, con la matriz programada para bajar a 0,40 % al consumir 20 % del total — y la simulación se re-ejecuta con el drawdown real del contrato (¿estático o trailing? si es trailing, el chequeo de la racha se hace contra el peor suelo móvil, 11.4).
2. En zona naranja aplica **0,25 %** — y antes de disparar se verifican: (1) que sea un A-setup completo (todas las condiciones sí/no del checklist, la duda es un no — la matriz solo admite calidad plena en naranja) y (2) que el flotante esperado de la operación quepa en el límite diario restante con su peor excursión. El tilt operaría al tamaño de la zona verde (o más) "porque es una buena señal" — la matriz existe exactamente para ese momento: el dato (consumo 45 %) decide el tamaño, no la calidad de la señal ni el estado emocional; una buena señal a 0,25 % sigue siendo buena — una cuenta descalificada ya no está en el examen.
3. E neta: $0{,}35 \times 1{,}92 - 0{,}65 \times 1{,}08 = 0{,}672 - 0{,}702 = -0{,}03R$ — NEGATIVA en el punto estimado; WR* neto = 1,08/3,0 = **36,0 %** > tu 35 % medido; IC [25,7 %, 44,3 %] cruza el equilibrio ampliamente. Veredicto de la tabla de 3 vías: **roja** → "todavía no": la evidencia no autoriza el fee (comprar el desafío con E negativa es pagar por fracasar). Rutas de mejora: (1) **subir el R:B** (gestión de TP/parciales, salidas mejores): a R:B 2,4 la E pasa a +0,11R y el WR* baja a 31,8 % — tu 35 % ya lo supera: verde; (2) **bajar el coste** (sesión/par del pilar 3): a coste 0,03R la E pasa a +0,02R y el WR* a 34,3 % — tu 35 % supera el equilibrio por el mínimo: la ruta combinada (R:B 2,2 + coste 0,05) da margen cómodo. Y (3) más N: reduce el IC (±9,3 → ±6,6 a N=200) para que la decisión no dependa del intervalo. NO es: (a) "nunca" — las rutas son de tu ejecución y gestión, medibles en semanas-meses; (b) "riesgo menor o más temperancia" — el problema no es el sizing ni la conducta: es que la esperanza medida no paga el examen; ningún sizing convierte E negativa en positiva — primero la esperanza, después el fee.

</details>
