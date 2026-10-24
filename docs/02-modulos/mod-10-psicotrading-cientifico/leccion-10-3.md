# Lección 10.3 · Las 5 avaricias — la otra cara del mismo secuestro

| Campo | Detalle |
|---|---|
| ⏱️ Duración estimada | 50–65 min de estudio |
| 🧱 Módulo | [M10 · Psicotrading Científico](README.md) |
| ⬅️ Anterior | [Lección 10.2 · Los 5 miedos](leccion-10-2.md) |
| ➡️ Siguiente | [Lección 10.4 · Pérdida ≠ Error](leccion-10-4.md) |

---

## Por qué importa

Los 5 miedos (10.2) empujan desde dentro: son huida. Las 5 avaricias **jalan desde fuera**: son persecución — y en el registro del journal aparecen con etiquetas distintas (E1, E2, E4) pero la misma firma hormonal que estudiaste en 10.1: dopamina anticipando recompensa, PFC cediendo el volante. La razón de dedicarles una lección propia es que el trader razonable cree que sus errores son de miedo ("me faltó valentía") cuando la estadística de la industria dice lo contrario: la mayoría del daño a cuentas con sistema viene de **exceso**, no de defecto — más operaciones que las debidas, más tamaño que el presupuesto, entradas más tarde que la zona. La prueba de que son el mismo fenómeno que los miedos: los cinco miedos sin protocolo PRODUCEN las cinco avaricias (el miedo a quedarse fuera produce FOMO; el miedo a perder produce revancha que produce sobreapalancamiento; el miedo a equivocarse produce overtrading de "recuperación"). Esta lección las nombra una a una, muestra el coste exacto de cada una sobre el caso maestro (E +0,16R neto) y entrega lo único que las frena: **señales tempranas observables + pre-compromiso por escrito** — porque a diferencia del miedo, que aparece antes de la decisión, la avaricia aparece DURANTE: se siente bien mientras se comete.

## Concepto

**Las 5 avaricias del programa** — cada una con su definición operativa, sus señales tempranas (los detectores de 10.1 aplicados a este contenido) y su coste medible sobre el caso maestro:

| # | Avaricia | Definición operativa | Señales tempranas (antes del clic) | Coste sobre el caso maestro |
|---|---|---|---|---|
| 1 | **FOMO** (*fear of missing out*) | Impulso de entrar por ver el precio moverse sin ti, sin setup | Cursor al botón "solo por si acaso"; "ya se escapa"; pensar en la ganancia ANTES que en el riesgo; revisar otro instrumento en plena gestión | La entrada sin zona tiene E ≈ −coste = **−0,08R cada vez** (sin ventaja, solo pagas spread); 5 FOMO por semana = −0,4R regalaron |
| 2 | **Perseguir el precio** (*chasing*) | Entrar más allá de la zona definida, a mercado, "porque la idea sigue siendo buena" | La zona quedó 10-15 pips atrás y "igual vale"; aceptar entrada peora con el mismo SL/TP mental | Entrada 15 pips tarde con el mismo SL/TP: R:B cae de 2,1 a ~1,1 y la E de **+0,16R a −0,16R** (abajo, la cuenta completa) |
| 3 | **Sobreapalancamiento** (*overleveraging*) | Usar tamaño que el presupuesto no contempla: el lote "de la operación especial" | Recalcular el lote dos veces (la segunda más grande); "esta zona es distinta"; la calculadora da 0,06 y tú piensas en 0,2 | Riesgo 5 % en vez de 1 %: una racha de 5 pérdidas = **−22,6 %** de cuenta (0,95⁵) vs −4,9 % (0,99⁵); recuperar −22,6 % exige +29,2 % |
| 4 | **Exceso de riesgo** (*risk creep*) | El mismo 1 % pero "ensanchado": SL más lejos "para darle aire", riesgo real 1,5-2 % por operación | Medir el SL desde donde te gustaría que estuviera el precio; mover el SL tras entrar; justificar con "volatilidad" lo que es comodidad | SL 32 → 48 pips con el mismo lote: el riesgo por op pasa de 19,20 $ a **28,80 $ (+50 %)** — el top del 1 % roto con silencio aritmético |
| 5 | **Overtrading** (*overtrading*) | Operar más de lo que tu sistema dispara: ruido disfrazado de actividad | Contador de decisiones > 10-12; mirar TF menores "para encontrar algo"; abrir el libro de órdenes por aburrimiento | 20 operaciones debidas → 40 ejecutadas: las 20 de ruido cuestan 20 × 0,08R = **−1,6R/mes** y la mitad de tu esperanza (abajo) |

**El coste de perseguir, contado completo** — la avaricia #2 con la aritmética de la Receta. Tu zona definida: entrada 1,0820, SL 1,0788 (32 pips), TP 1,0886 (66 pips) → R:B = 66/32 ≈ 2,06, y con tu WR 40 %: $E = 0{,}4 \times 2{,}06 - 0{,}6 \times 1 = +0{,}22R$ bruto (≈ +0,16R neto con costes — el caso maestro). Ahora el FOMO te hace entrar 15 pips más tarde, en 1,0835, "porque la idea sigue siendo buena":

$$\text{SL} = 1{,}0835 - 1{,}0788 = 47 \text{ pips} \qquad \text{TP} = 1{,}0886 - 1{,}0835 = 51 \text{ pips} \qquad R{:}B = \frac{51}{47} \approx 1{,}09$$

$$E = 0{,}4 \times 1{,}09 - 0{,}6 \times 1 = -0{,}16R \qquad WR^* = \frac{1+c}{\bar{R}+1} = \frac{1{,}08}{2{,}085} \approx 51{,}8\%$$

Mismo mercado, misma idea, misma dirección — pero la entrada tardía **convirtió la esperanza en negativa** con el mismo WR 40 %: ahora necesitarías un 51,7 % de acierto solo para empatar neto. Y el detalle perverso: la entrada tardía se siente MÁS segura (ya hay confirmación visible) — la avaricia siempre cobra en una moneda que el perseguidor no ve: la geometría de la operación.

**El coste del overtrading, contado completo** — la avaricia #5 con su impuesto de costes. Tu sistema dispara ~20 operaciones válidas al mes; tu E neta es +0,16R por operación → esperanza mensual planeada: $20 \times 0{,}16 = +3{,}2R$. Con FOMO/overtrading ejecutas 40: las 20 extra NO tienen la ventaja del sistema (sin setup no hay edge que cobrar) — su valor esperado es $0 - 0{,}08R = -0{,}08R$ cada una:

$$E_{\text{mes}} = 20 \times 0{,}16R + 20 \times (-0{,}08R) = 3{,}2R - 1{,}6R = +1{,}6R$$

**La mitad de tu negocio se dona al spread** — sin contar el peaje oculto: las 20 operaciones de ruido consumen decisiones de tu ventana de ejecución (10.7), generan etiquetas E1 que ensucian la muestra de M9, y fabrican el cansancio del que nace la revancha. El overtrading es la única avaricia que cobra doble: en costes visibles y en fatiga invisible.

**La asimetría que las define.** Los miedos duelen mientras se cometen; las avaricias **premian mientras se cometen** — esa es la razón de que el antídoto no pueda ser "darte cuenta": cuando te das cuenta, ya estás dentro de la operación. La única defensa que funciona es el **pre-compromiso** (*precommitment*): la decisión tomada ANTES del estímulo, con forma de regla verificable ajenamente — exactamente la lógica del candado de métricas declaradas de 9.1, aplicada a la conducta. La tabla de señales tempranas de arriba existe para convertir cada avaricia en un evento observable por tu propio journal: "recalculé el lote dos veces" es un hecho, no un juicio.

## Analogía

La máquina tragamonedas y el refuerzo intermitente. Los laboratorios de conducta descubrieron hace décadas que la programación de refuerzo más adictiva no es la constante ("pagar siempre") sino la **intermitente variable** ("pagar a veces, sin patrón predecible") — la paloma y la rata picotean hasta el agotamiento cuando el premio es aleatorio, y la conducta RESISTE más a la extinción que si pagara siempre. Las slots de casino son esa programación con luces: la anticipación (dopamina) hace el trabajo, no el premio. El FOMO es tu tragamonedas personal: el mercado mueve 80 pips, tu cerebro proyecta "podía ser mío", la anticipación dispara, y entras a mercado — el premio intermitente (a veces el perseguido "sale") refuerza exactamente la conducta que destruye tu esperanza. El casino no le exige al jugador "ser más fuerte": le construye el entorno (sin relojes, sin ventanas, fichas en vez de dinero). Tú tienes que hacerte el favor tú mismo: journal abierto, contador de decisiones visible, y la regla escrita ANTES de la sesión — porque cuando la slot suene, la única voz disponible será la tuya de 3 horas atrás.

## Cómo se hace: el pre-compromiso por escrito (1 página antes de la sesión)

1. **Escribe tu "contrato de tamaño" con número único.** "Riesgo por operación: 1 % de X. Cualquier cálculo que dé más, es una avaricia #3/#4 — no se ejecuta." La regla cubre el sobreapalancamiento (lote mayor) y el risk creep (SL ensanchado) a la vez: ambas terminan en el mismo número auditable — el riesgo en \$ del campo del journal.
2. **Declara el techo de operaciones del día/semana.** Tu sistema dispara ~2-3 señales por semana en 1H/H4 (si el tuyo dispara más, declara SU número): "más de N operaciones con señales = overtrading declarado". Al tocar el techo: plataforma cerrada, no "solo mirar". El contador de decisiones del journal es tu taxímetro.
3. **Define la regla de zona con tolerancia cero.** "Si el precio ya dejó la zona definida por mi componente 3, la operación no existe — perseguirla es avaricia #2." Añade la verificación de 2 segundos: antes de disparar, mira el precio de entrada planificado vs actual: si difiere más que tu tolerancia declarada, no hay operación. (Tu tolerancia del caso maestro: el componente 6 decía la zona de reacción 1,0820 ± un rango mínimo — decláralo en pips.)
4. **Instala el retardo de 90 segundos para cualquier modificación.** Toda entrada que no esté en el plan (zona, hora, instrumento) espera 90 segundos cronometrados con el protocolo de 10.1 (nombrar el estado, respirar). Si a los 90 s la "oportunidad" sigue justificándose por escrito (¿qué componente la autoriza?), repásala en la revisión — no en caliente. En el 95 % de los casos *(estimación operativa, no medida)*, a los 90 s la señal ya no existe o ya no te importa: el FOMO tiene vida media corta.
5. **Audita las avaricias en el acta semanal con la taxonomía.** Las 5 avaricias tienen etiqueta directa: FOMO/chasing → **E1/E2**; sobreapalancamiento/risk creep → **E4**; overtrading → **E1** (operar sin setup) o **E6** (ignorar frenos de sesión). Cuenta cuántas de tus 10 filas de la misión M-10 llevan cada una: esa es tu foto de cartera de avaricias — y la comparación con la semana siguiente es tu curva de progreso conductual.

## Error común

**(1) "Avaricia no tengo — yo solo quiero recuperar lo que perdí."** Eso no es avaricia, es **revancha** (el tilt, 10.5) — pero mira su mecánica: recuperar implica meter MÁS riesgo (sobreapalancamiento) MÁS rápido (chasing) MÁS veces (overtrading). La revancha es el kit completo de las 5 avaricias con el marketing del miedo #2. Mismo tratamiento: protocolo post-pérdida (10.1) antes de cualquier nueva entrada. **(2) Confundir "entradas más agresivas" con productividad.** El calendario del trader amateur mide actividad; el del profesional mide ejecución de señales. Operar 40 veces con E negativa no es "ser activo": es pagar peaje por aburrirse — la inacción estratégica (10.7) ES trabajo: protege la esperanza que ya fabricaste. **(3) Ajustar el pre-compromiso a mitad de sesión.** "Hoy el mercado está muy movido, voy a subir el techo a 6 operaciones" — la modificación del contrato EN la sesión es exactamente el data-mining de 9.1 pero con tu conducta: la muestra (tu disciplina) queda falsificada. Los techos se revisan en la ventana mensual (9.6), con evidencia, nunca en caliente. **(4) Creer que el problema es el instrumento.** "El oro me hace overtrading" — no: TU protocolo hace overtrading en cualquier instrumento que se mueva; cambiar de instrumento es mudar la slot de sala. El antídoto es conductual (techos, contador), no de menú. **(5) No registrar los casi-FOMO.** El impulso detectado y contenido también se registra (el journal v1 tiene el registro de no-disparos): es tu estadística de "cascadas cortadas" — y es el dato más motivador del módulo: ver 12 secuestros abortados en 2 semanas es la prueba de que el protocolo funciona.

## Conexión cuantitativa

**Hacia M8:** las 5 avaricias son las formas conductuales de romper cada tope que instalaste: sobreapalancamiento rompe el 1 %, risk creep rompe el top de cartera, overtrading rompe el disparo 100 %/100 %. Por eso M8 y M10 se estudian juntos: el freno es aritmético, el que intenta soltarlo es conductual. **Hacia 9.3:** la avaricia aparece en tus métricas con firma reconocible: R:B medio cayendo (chasing), coste medio subiendo (entradas a mercado), rachas de E1 en el gráfico de etiquetas (overtrading). **Hacia 10.4:** la avaricia produce su forma más peligrosa de error: la **ganancia fuera de plan** (el FOMO que "salió bien") — la siguiente lección formaliza por qué ese premio es el que más daño hace a largo plazo. **Hacia 10.5:** cuando las avaricias fallan (perdiste el perseguido), el residuo emocional (frustración) alimenta la revancha — el ciclo del tilt. **El número que auditará la Evaluación N3:** en tus 10 sesiones, ¿cuántas entradas E1/E2 y cuántos casi-FOMO registrados? El cociente [cortados / (cortados + ejecutados)] es tu tasa de contención — el programa espera que suba semana a semana.

---

## 🎯 Puntos clave

1. Las 5 avaricias (FOMO, chasing, sobreapalancamiento, risk creep, overtrading) **jalan desde fuera y premian mientras se cometen** — por eso el antídoto no es darse cuenta, es pre-compromiso escrito.
2. La geometría manda: perseguir 15 pips la entrada del caso maestro cae el R:B de 2,1 a 1,1 y la E de **+0,16R a −0,16R** — la entrada tardía se siente más segura y matemáticamente mata la ventaja.
3. El overtrading cobra doble: impuesto de costes (−1,6R/mes en el caso maestro: la mitad de la esperanza) y consumo de la ventana decisional que fabrica fatiga y revancha.
4. El riesgo "ensanchado" es el robo silencioso: SL 32 → 48 pips con el mismo lote = +50 % de riesgo por operación — auditable en un solo campo del journal (riesgo en \$).
5. Cada avaricia tiene **etiqueta E y señal temprana observable**: el acta semanal convierte la psicología en estadística de contención ([cortados/(cortados+ejecutados)]).

## 🔄 Autoevaluación rápida

1. Calcula el R:B y la E bruta de la entrada perseguida a 1,0840 (20 pips tarde) con el mismo SL 1,0788 y TP 1,0886. ¿A partir de cuántos pips de retraso la E bruta se vuelve negativa con WR 40 %?
2. Tu techo declarado son 3 operaciones/semana y llevas 4 el miércoles (todas "razonables"). Formula la respuesta del protocolo en 3 pasos y explica qué métrica del journal valida tu decisión el viernes.
3. Clasifica estas 5 conductas con avaricia #1-#5 y etiqueta E: (a) SL de 40 pips "para que respire" cuando tu regla manda 32; (b) lote 0,15 "solo en esta zona de H4 tan clara"; (c) cuarta operación del día en TF de 5 min porque "se veía limpia"; (d) compra a mercado 20 pips tras la zona "porque la idea era buena"; (e) abrir XAU/USD "solo para mirar" durante la gestión de una posición.

<details>
<summary>Ver respuestas</summary>

1. Entrada 1,0840 (d = 20 pips): SL = 52 pips, TP = 46 pips → R:B = 46/52 ≈ 0,88; E = 0,4 × 0,88 − 0,6 × 1 = **−0,25R bruto**. El cruce a cero: $0{,}4 \times \frac{66-d}{32+d} = 0{,}6 \Rightarrow \frac{66-d}{32+d} = 1{,}5 \Rightarrow d = 7{,}2$ — **la E bruta ya es negativa a ~8 pips de retraso** (R:B < 1,5). La degradación no es lineal: a 15 pips la E ya perdió casi toda su ventaja y sigue hundiéndose (a 20: −0,25R; a 25: R:B = 41/57 ≈ 0,72 → −0,31R) — la lección: el chasing no cobra proporcional, cobra en curva.
2. (1) Cerrar la plataforma al tocar el techo — la regla se declaró ANTES y las 4 "razonables" no cambian el contrato (lo razonable es lo que el plan dispara, no lo que justifica tu memoria); (2) registrar en el journal la violación del techo (etiqueta E6: freno ignorado — el techo ES un freno de M8/M10) y el estado emocional que la empujó; (3) dejar la revisión para el acta del viernes. Métrica que valida: el conteo de disparos **debidos** — si el sistema solo generó 2 señales y ejecutaste 4, la brecha (2 extra) es overtrading medible; si el sistema generó 4 y ejecutaste 4, el techo estaba mal calibrado y se ajusta en la ventana mensual (9.6) — con evidencia, no en miércoles.
3. (a) **Risk creep (#4)** → E4 en su forma conductual (sizing efectivo fuera de presupuesto). (b) **Sobreapalancamiento (#3)** → E4 directo (2,5× el riesgo declarado). (c) **Overtrading (#5)** → E1 (operar sin setup: tu sistema no dispara en 5 min por aburrimiento) + E6 si ya había techo. (d) **Chasing (#2)** → E2 (entrada fuera de regla). (e) **FOMO (#1) en incubación** — sin etiqueta E todavía (no hay operación), pero va al registro de no-disparos/casi-eventos: la señal temprana exacta que el pre-compromiso debe cortar.

</details>
