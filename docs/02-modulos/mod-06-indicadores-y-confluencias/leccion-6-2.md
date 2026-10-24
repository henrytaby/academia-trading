# Lección 6.2 · Medias móviles — el filtro de régimen

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 45–60 min de estudio |
| 🧱 Módulo | [M6 · Indicadores y Confluencias](README.md) |
| ⬅️ Anterior | [Lección 6.1 · Filosofía del indicador](leccion-6-1.md) |
| ➡️ Siguiente | [Lección 6.3 · Volatilidad y canales](leccion-6-3.md) |

---

## Por qué importa

La media móvil es el indicador más antiguo, más simple y más usado del mundo — y por eso mismo, el más maltratado: los vídeos la enseñan como "señal de compra cuando cruza" y terminan de destruir cuentas en rangos. Bien usada, la media móvil es otra cosa: el **filtro de régimen** de tu negocio — la versión cuantitativa y automática de la frase de sesgo que aprendiste a escribir en 5.1. En este programa, la media no da entradas: da *permiso de lado*. Y el sistema 20/50/200 te da tres capas de permiso que jerarquizan exactamente como tu top-down: macro, régimen, zona. Si el M5 te enseñó a leer quién controla la estructura, esta lección te da el medidor que lo verifica en un segundo — y que tu journal podrá auditar trimestre a trimestre.

## Concepto

**Media simple (SMA):** promedio aritmético de los últimos N cierres. Cada vela nueva entra, la más vieja sale: la media es una ventana deslizante que trata todos los datos por igual. Su virtud: estabilidad. Su costo: retardo uniforme — cuando el régimen ya cambió, la SMA sigue promediando el pasado.

**Media exponencial (EMA):** pondera más los datos recientes mediante un factor de suavizado:

$$EMA_t = \alpha \cdot P_t + (1-\alpha) \cdot EMA_{t-1}, \qquad \alpha = \frac{2}{N+1}$$

Con N = 20: $\alpha = 2/21 \approx 0{,}095$ — cada cierre nuevo entra con ~9,5 % de peso y el resto queda para la historia acumulada. Con N = 200: $\alpha = 2/201 \approx 0{,}010$ — la EMA 200 es un recuerdo largo de tendencia. La EMA reacciona antes que la SMA del mismo periodo; el precio a pagar es más nerviosismo en rangos.

**El sistema 20/50/200 — tres roles jerárquicos:**

| Media | Rol | Pregunta que responde | Análogo del M5 |
|---|---|---|---|
| EMA 200 | **Filtro macro** | ¿Hacia dónde NO opero nunca en contra? | Capa 1 · sesgo (D1/H4) |
| EMA 50 | **Régimen intermedio** | ¿La tendencia de mis swings vive o agoniza? | Capa 1 · invalidación |
| EMA 20 | **Zona dinámica** | ¿Dónde han estado girando los pullbacks? | Capa 2 · zonas |

La regla del programa: **el filtro macro se consulta una vez por sesión y no se discute**; el régimen intermedio acompaña la lectura de estructura; la zona dinámica es contexto para el pullback, nunca gatillo por sí sola.

**Cruces: golden y death cross.** El cruce dorado (*golden cross*) es la EMA 50 superando a la EMA 200; el cruce de la muerte (*death cross*), lo contrario. Son confirmaciones de régimen **muy tardías** — ocurren meses después de que la tendencia empezó. Su uso honesto: titular de contexto ("el régimen semanal cambió"); su uso deshonesto: señal de entrada. Si esperas el cruce para comprar, compras el final de la Etapa 2 o el inicio de la 3 (Weinstein, 6.7). Y en rango, los cruces de las medias rápidas se multiplican: cada cruce una señal falsa (*whipsaw*, M3).

**Soporte/resistencia dinámico:** en tendencia sana, los pullbacks tienden a girar cerca de una media que "empuja" por debajo (alcista) o encima (bajista). No es magia: si el régimen alcista hace que los pullbacks duren ~N velas, la media de N cierres coincidirá con el fondo típico del pullback *por construcción*. La media no atrae el precio: es el espejo estadístico del hábito del régimen.

## Analogía

La corriente de un río para un nadador de travesía. La EMA 200 es la dirección general del río (ir contra ella es suicida, sin excepciones); la EMA 50 es la corriente de la canal principal que empuja tu tramo; la EMA 20 es la borda variable de la orilla donde el agua retrocede. El buen nadador no decide el rumbo mirando la borda: la usa para descansar mientras el río avanza. Y el cruce de corrientes (golden cross) es el parte meteorológico de la semana pasada: útil para el contexto, inútil para decidir la brazada de ahora.

## Cómo se hace: el filtro aplicado al caso maestro

El mismo movimiento de la [Receta](../../03-recursos/laboratorio/receta-primera-operacion.md) *(ilustrativo)* — EUR/USD H4, día del pullback:

1. **Activas las tres EMAs** y anotas: EMA 200 ≈ 1,0712 con pendiente positiva, EMA 50 ≈ 1,0771 creciente, EMA 20 ≈ 1,0806 creciente. Las tres escalonadas al alza: disposición clásica de Etapa 2 (6.7).
2. **Consulta del filtro macro (una vez, por escrito):** precio 1,0820 > EMA 200 1,0712 y media creciente → *"hoy solo se buscan largos; ningún corto entra al plan"*. Esa frase es el equivalente automático de la frase de sesgo de 5.1 — ahora con un medidor que tu journal puede registrar.
3. **Régimen intermedio:** el precio 1,0820 está por encima de la EMA 50 (1,0771): la secuencia HH/HL del M5 tiene respaldo numérico — no estás comprando un rebote dentro de una caída.
4. **Zona dinámica:** el pullback hacia la zona 1,0820–1,0824 coincide con la EMA 20 (1,0806) — confluencia entre la zona estructural del M5 y el hábito estadístico de los pullbacks. La zona mejora; el gatillo sigue siendo de estructura (3.4).
5. **Lo que NO se hizo:** no se operó ningún cruce (el golden cross ocurrió semanas atrás — ya estaba dentro del precio), no se usó la EMA 20 como entrada automática al primer toque, y ninguna media cambió el plan: el filtro confirmó el lado, la estructura dio la zona.

Fíjate en el patrón del módulo entero: cada medidor añade *auditoría*, ninguna añade *veredicto*.

## Error común

**(1) Operar cruces como entradas.** En rango multiplican falsas señales; en tendencia llegan tarde. El cruce 50/200 es contexto de régimen; el cruce de las rápidas (10/20) no se opera en este programa. **(2) Ajustar N hasta que "funcione".** Probar 25, luego 34, luego 50 hasta que el backtest "mejore" es overfitting (D6): el número óptimo del pasado es el óptimo del azar. El programa fija 20/50/200 por convención universal — la ventaja no está en el número, está en no cambiarlo. **(3) Discutir el filtro macro a mitad de sesión.** "Pero es que hoy el corto se ve perfecto" — el filtro existe precisamente para los días en que el corto se ve perfecto. Si lo discutes cada día, no existe. **(4) Usar la EMA 20 como SL.** El SL se fija por estructura y se audita con ATR (6.3); una media móvil es referencia de régimen, no orden de protección.

## Conexión cuantitativa

El filtro de régimen es auditable con tu journal desde el día uno: etiqueta cada operación con "a favor del filtro macro" / "contra el filtro macro". Al llegar a M9 tendrás la tabla: WR a favor vs WR contra, con TU datos. La hipótesis del programa *(heurística de trabajo, se auditará)*: la diferencia será material — el régimen es el multiplicador invisible de la [Lección 3.6](../mod-03-anatomia-del-grafico/leccion-3-6.md), y la EMA 200 es su medidor barato y replicable. Números de trabajo para dimensionar el efecto: si tu WR a favor es 45 % y en contra 35 %, con R:B 1:2 la esperanza por operación es $E_{fav} = 0{,}45 \times 2R - 0{,}55 \times 1R = 0{,}35R$ versus $E_{contra} = 0{,}35 \times 2R - 0{,}65 \times 1R = 0{,}05R$ — siete veces menos por la misma mecánica: el filtro no gana dinero, evita pagar por operar contracorriente.

---

## 🎯 Puntos clave

1. SMA promedia por igual (estable, retardada); EMA pondera lo reciente con $\alpha = 2/(N+1)$ (rápida, nerviosa).
2. El sistema 20/50/200 tiene roles: filtro macro (200), régimen (50), zona dinámica (20) — jerarquía igual que el top-down.
3. La media móvil da permiso de lado, jamás entradas: el gatillo sigue siendo de estructura.
4. Golden/death cross: confirmación tardía de régimen para contexto, no señal; en rango, cruces falsos.
5. Soporte dinámico = espejo estadístico del hábito de pullbacks del régimen, no imán.
6. El filtro se consulta por escrito y no se discute: si lo discutes cada día, no existe.

## 🔄 Autoevaluación rápida

1. Calcula el α de la EMA 50 y explica por qué la EMA 50 reacciona antes que la SMA 50.
2. En el caso maestro, ¿qué frase escribe el filtro macro y cuál fue el aporte real de la EMA 20 a la operación de la receta?
3. Tu compañero ajusta su media a N = 34 "porque en su backtest gana más". Dos objeciones del programa.

<details>
<summary>Ver respuestas</summary>

1. $\alpha = 2/(50+1) = 2/51 \approx 0{,}039$. Cada cierre nuevo entra con ~3,9 % de peso: la EMA 50 transmite los cambios recientes al instante, mientras la SMA 50 los diluye al mismo peso que los 49 días anteriores — por eso la EMA gira antes (y por eso también se equivoca antes en rangos).
2. Frase del filtro: *"precio 1,0820 sobre EMA 200 (1,0712) creciente: hoy solo largos"*. Aporte de la EMA 20 (≈ 1,0806): confluencia con la zona estructural 1,0820–1,0824 — el pullback giró donde la estructura y el hábito estadístico coincidían. No dio la entrada: la dio el gatillo de estructura (3.4).
3. (a) Overfitting (D6): ajustar N mirando el resultado del backtest optimiza el azar del pasado, no la lógica del futuro — la muestra "mejorada" está contaminada por la búsqueda misma. (b) Rompe la comparabilidad: sin N fijo no hay journal auditable (tu WR "a favor/contra" deja de ser comparable entre meses), y la ventaja del filtro nunca fue el número sino la constancia.

</details>
