# 🔬 Análisis Forense de los Cursos Base — Informe ATR-001

> **Documento de referencia permanente del repositorio.**
> Todo módulo construido por los agentes debe ser coherente con las conclusiones de este informe.

| Campo | Detalle |
|---|---|
| 📋 Informe | ATR-001 — Análisis comparativo de cursos base |
| 📅 Fecha | 24 de octubre de 2026 |
| 🔎 Objetos analizados | `003_trading_completo_2026_guia_completa.html` · `004_la_industria_del_trading_guia_completa.html` |
| 🎥 Fuentes primarias | [Curso Completo de Trading 2026 — Álex Ruiz (7h 39m)](https://www.youtube.com/watch?v=TdEbkTk40qQ) · [La Industria del Trading me va a odiar por este curso gratis — Sáenz & Ruiz (11h 55m)](https://www.youtube.com/watch?v=lW9eGp-yOe8) |
| 🧭 Método | Lectura estructural completa · verificación conceptual contra teoría financiera estándar · auditoría pedagógica · detección de vacíos curriculares |
| ⚖️ Veredicto global | 003: **8/10** · 004: **8.5/10** — aptos como base curricular **con correcciones obligatorias** |

---

## 1. Objeto y Método

Este informe audita los dos compendios de estudio que sirven como material fuente del programa. El análisis se realizó en tres capas complementarias. Primero, una **verificación técnica** de cada afirmación cuantitativa y operativa contra la teoría financiera estándar (esperanza matemática, mecánica de órdenes, estadística de prop firms). Segundo, una **auditoría pedagógica** del orden, la profundidad y la progresión curricular de ambos programas. Tercero, una **detección de vacíos**, identificando los temas ausentes en ambos cursos que nuestro programa debe incorporar para ser completo. Las conclusiones alimentan directamente las decisiones de diseño documentadas en [`SYLLABUS.md`](../01-syllabus/SYLLABUS.md).

**Nota de contexto importante:** ambos compendios son guías de estudio derivadas de cursos gratuitos de YouTube del canal TradingLab, ya estructuradas con formato de cátedra universitaria (perfil de egreso, matriz de trazabilidad curricular, glosario indexado). Ese formato editorial es, en sí mismo, uno de los mejores insumos del análisis y se adopta íntegramente para este repositorio. Los compendios no fueron escritos por los instructores: son material derivado, por lo que este informe audita el **contenido pedagógico**, no la producción audiovisual.

## 2. Ficha Técnica Comparativa

| Campo | Curso 003 | Curso 004 |
|---|---|---|
| **Título** | Curso Completo de Trading 2026 (Actualizado) | La Industria del Trading me va a odiar por este curso gratis |
| **Instructores** | Álex Ruiz | Adrián Sáenz & Álex Ruiz |
| **Duración del video** | 7 h 39 min | 11 h 55 min |
| **Módulos teóricos** | 7 (con submódulos 1.1–7.5) | 10 (con submódulos 1.1–10.5) |
| **Sesiones prácticas** | 7 guías "Día" | 10 guías "Día" |
| **Área más fuerte** | Cuantificación, Psicotrading, Prop Firms | Técnica de canales/volatilidad, Auditoría de estafas, Rutina profesional |
| **Área más débil** | Fiscalidad 100 % española | Densidad excesiva; incoherencia con 003 sobre SMC/ICT |
| **Sesgo estilístico** | Recomienda Day Trading como "equilibrio perfecto" | Top-Down multitemporal + triple EMA 20/50/200 |
| **Pedagogía** | Expositiva, con analogías médicas | Expositiva, con laboratorios y rutinas |

## 3. Análisis del Curso 003 — "Curso Completo de Trading 2026"

### 3.1 ✅ Fortalezas verificadas

1. **Rigor cuantitativo real.** La fórmula de esperanza matemática $E = (P_w \times W) - (P_l \times L)$ está correctamente planteada, y el Módulo III demuestra numéricamente la idea más importante de todo el trading: el *Win Rate* es secundario frente al ratio Riesgo:Beneficio. El ejemplo comparativo (60 % de acierto con ratio moderado supera a 30 % de acierto con premio grande) es pedagógicamente excelente y matemáticamente correcto.
2. **Fórmula de *Position Sizing* correcta.** `Tamaño = (Capital × Riesgo) / |Entrada − Stop|` es la ecuación universal de la industria, presentada con la distinción crucial entre inversión (todo el capital en riesgo) y trading (solo la distancia al stop en riesgo).
3. **Honestidad de industria excepcional.** Las estadísticas de prop firms citadas (92 % de desafíos fracasan según el CEO de FTMO; ~0.07 % de éxito neto end-to-end en los datos filtrados de MyForexFunds) son cifras reales reportadas por la industria y coherentes con lo que documenta la comunidad. Desmontar las "5 grandes mentiras del marketing" (playa, una hora al día, rentable en 3 meses) es el mejor antídoto contra el humo que existe en español gratis.
4. **Psicotrading con base científica.** Neurobiología correcta (amígdala, cortisol, secuestro emocional), los 5 miedos de Mark Douglas correctamente atribuidos, las 6 cualidades de Steenbarger, y — joya del curso — la distinción **pérdida ≠ error** (una pérdida ejecutada bajo reglas es un trade perfecto; una ganancia fuera de plan es un error letal).
5. **Crítica madura a las modas.** La deconstrucción de SMC/ICT como re-etiquetado de la acción del precio clásica es una opinión defendible y valiosa que enseña al estudiante a no pagar por nombres nuevos de conceptos viejos.
6. **Formato editorial de cátedra.** Perfil de egreso, matriz de trazabilidad, glosario indexado y bibliografía real (Elder, Van Tharp, Douglas, Steenbarger, Rotella) — nivel universitario genuino.

### 3.2 ⚠️ Debilidades y errores detectados

| # | Hallazgo | Severidad | Detalle y corrección aplicada en nuestro programa |
|---|---|---|---|
| D1 | **Fiscalidad 100 % española** (IRPF 19–28 %, modelos 130/349/720/D6) | 🔴 Alta para no residentes en España | Casi media hora de contenido inaplicable fuera de España. Nuestro Módulo 11.7 enseña **principios fiscales universales** (trading propio vs actividad, registro de operaciones, obligación de declarar) con la consigna "verifica tu jurisdicción". |
| D2 | **Brokers solo europeos** (Trade Republic, IBKR, XTB, DeGiro) | 🔴 Alta para LatAm | Varios no aceptan clientes de LatAm o son imprácticos. Nuestro programa enseña los **criterios de selección** (regulación, ejecución, costos, retiros) en lugar de marcas concretas, más un laboratorio de *due diligence* aplicable a cualquier país. |
| D3 | **"Day Trading = punto de equilibrio perfecto"** presentado como recomendación pedagógica definitiva | 🟡 Media | Es una **opinión de estilo de vida**, no un hecho. Para un principiante con empleo u obligaciones, Swing suele producir mejor curva de aprendizaje (menos decisiones, menos comisiones). Nuestro Módulo 1 presenta el mapa completo de estilos y deja la elección al perfil del estudiante. |
| D4 | **Cifras ilustrativas sin fuente** (frecuencia de patrones "15/año vs 30/mes", simulación de 51 % anual) | 🟡 Media | Son pedagógicamente válidas pero estadísticamente no citables. Regla del repo: toda cifra no verificable se etiqueta como *ilustrativa*. |
| D5 | **"Ciclos lunares" listados en el catálogo de estrategias** sin etiqueta pseudocientífica | 🟡 Media | Está en el Módulo III como técnica clásica. Nuestro catálogo crítico (Módulo 6.8) rankea cada herramienta por **evidencia**, y lo lunar va al sótano, junto con astrología financiera. |
| D6 | **Tier List de prop firms congelada en el tiempo** | 🟡 Media | La propia historia que el curso documenta (colapsos de MyForexFunds, True Forex Funds, The Funded Trader) demuestra que una tier list envejece en meses. Nuestro programa enseña la **matriz de evaluación** (antigüedad, regulación, historial de pagos, reglas) y marca toda tier list como *snapshot*. |
| D7 | Fractalidad descrita como "exactamente igual" entre timeframes | 🟢 Baja | Es *autosimilar*, no idéntica: en timeframes bajos hay más ruido y el spread se come más margen. Corregido en Módulo 1.4 y 3.1. |

### 3.3 Veredicto 003

**8/10 — Aprobar con correcciones.** Es un curso honesto, cuantitativo y pedagógicamente sólido, con el mejor módulo de psicotrading y de prop firms disponibles en español gratuito. Sus debilidades no son conceptuales sino de **contexto geográfico** (fiscalidad y brokers españoles) y de **opiniones presentadas como hechos** (D3, D5). Es la base principal de nuestros Niveles 1 y 3.

## 4. Análisis del Curso 004 — "La Industria del Trading me va a odiar"

### 4.1 ✅ Fortalezas verificadas

1. **Cobertura técnica superior.** Es el único curso gratuito en español que integra con rigor *Bandas de Bollinger* (±2σ y el fenómeno de *walking the bands* correctamente explicado), *Canales de Donchian* con la historia real de las Tortugas (Richard Dennis y William Eckhardt), las **4 Etapas de Stan Weinstein** (el mejor filtro anticontratendencia que existe) y el uso profesional del **ATR** para stops dinámicos.
2. **El mejor módulo anti-estafa en español.** El Módulo VIII es oro puro: A-Book vs B-Book, demostración de la esperanza negativa de las opciones binarias ($E \approx -0.075$ con payout 85 % — el curso dice −0.10, mismo signo, misma conclusión), muerte por martingala, academias MLM y el fraude de los indicadores que *repintan*. Todo verificado y correcto.
3. **Matemática del riesgo impecable.** La asimetría del drawdown está correctamente demostrada (−50 % exige +100 % para volver al equilibrio), el *Daily Max Loss* de −2 % y el freno tras dos pérdidas consecutivas son protocolos profesionales reales.
4. **Operativa completa y correcta.** Taxonomía de órdenes (Market/Limit/Stop/Stop-Limit/OCO), mecánica del short selling con *borrow fees* y *short squeeze*, bid/ask, *slippage*, maker vs taker — todo verificado sin errores.
5. **Rutina y hábitos como módulo propio.** Sueño, ritmos circadianos, ventana de ejecución de 3 horas, fatiga decisional, **inacción estratégica** ("estar fuera del mercado es una posición") y protocolo post-mercado. Ningún otro curso gratuito da esto.
6. **Arquitectura pedagógica del cierre.** Las 4 fases del trader (incompetencia inconsciente → competencia inconsciente), la regla 85/15 y la filosofía estoica de la dicotomía del control constituyen un marco mental profesional.

### 4.2 ⚠️ Debilidades y errores detectados

| # | Hallazgo | Severidad | Detalle y corrección aplicada en nuestro programa |
|---|---|---|---|
| D1 | **Incoherencia entre cátedras sobre SMC/ICT** | 🟡 Media | El 003 deconstruye SMC como marketing; el 004 adopta su nomenclatura (CHoCH, liquidity grabs, imbalances) sin crítica. Un estudiante de ambos queda desorientado. Nuestro programa **unifica nomenclatura** (Módulo 5): enseñamos estructura y liquidez como fenómeno, y presentamos PA clásico vs SMC como dos vocabularios del mismo objeto. |
| D2 | **Scalping de cripto y algo trading para principiantes** con advertencias insuficientes | 🟡 Media | El submódulo 2.5 presenta taker fees y curve fitting (bien), pero ubicar scalping cripto en un curso para principiantes es como enseñar frenadas en derrape en la autoescuela. En nuestro syllabus, scalping y algorítmico quedan explícitamente fuera del alcance básico, con la razón documentada. |
| D3 | **Regla 85/15 presentada como medición** cuando es heurística | 🟢 Baja | "La estrategia es el 15 % y la psicología + riesgo el 85 %" es una metáfora pedagógica útil, no un dato medido. Se conserva como principio, etiquetada como heurística. |
| D4 | **Misma localización española/europea** en broker y fiscalidad (módulos compartidos con la cátedra) | 🔴 Alta para no residentes | Igual que en 003. Misma corrección: criterios universales + laboratorio de due diligence. |
| D5 | **Densidad inadecuada**: 10 módulos × solo 5 submódulos, ~72 min de video por módulo | 🟡 Media | El ritmo es de "bootcamp" y no da tiempo a consolidar. Nuestro programa reparte contenido equivalente en 12 módulos con laboratorios y misiones obligatorias entre lecciones. |
| D6 | Backtesting "N ≥ 100" sin advertencia suficiente de **overfitting / data-mining** | 🟢 Baja | Menciona curve fitting en algoritmos pero no el sesgo de ajustar reglas mirando el resultado del backtest manual. Corregido en Módulo 9.1. |

### 4.3 Veredicto 004

**8.5/10 — Aprobar con correcciones.** Más completo, más honesto y más profesional que el 003 en técnica y en protección del estudiante. Sus defectos son de **densidad** y de **coherencia interna** con la cátedra hermana. Es la base principal de nuestros Niveles 2 y 4.

---

## 5. Comparativa Cruzada por Áreas de Conocimiento

Escala de cobertura: **0** = ausente · **10** = completo y riguroso.

| Área | 003 | 004 | Mejor fuente | Nota |
|---|---:|---:|---|---|
| Fundamentos y filosofía del trading | 8 | 8 | Empate | Ambos desmontan mitos de industria |
| Acción del precio y estructura | 7 | 8 | 004 | 004 añade CHoCH, institucional y fractalidad aplicada |
| Velas japonesas y patrones | 7 | 7 | Empate | Ambos correctos, catálogo clásico |
| Indicadores y canales (Bollinger/Donchian/ATR/Weinstein) | 4 | 9 | **004** | 003 apenas los enumera |
| Fibonacci / Elliott / armónicos | 5 | 6 | 004 | Ambos sin crítica de subjetividad suficiente |
| Sistemas de trading y esperanza matemática | 9 | 8 | **003** | 003 demuestra numéricamente la superioridad del R:B |
| Órdenes y ejecución (market/limit/stop/OCO) | 8 | 9 | **004** | 004 añade OCO, maker/taker, borrow fees |
| Gestión del riesgo y position sizing | 8 | 9 | **004** | 004 añade asimetría de drawdown y freno diario |
| Backtesting y métricas | 6 | 8 | **004** | 003 lo menciona, 004 lo protocoliza (N ≥ 100) |
| Psicotrading | 9 | 8 | **003** | Douglas + Steenbarger + neurobiología más completos |
| Rutina y hábitos del trader | 4 | 9 | **004** | Módulo IX casi completo |
| Brokers y selección | 7 | 7 | Empate | Ambos con sesgo Europa/España |
| Estafas de la industria | 5 | 9 | **004** | Módulo VIII forense |
| Prop firms | 9 | 5 | **003** | 003 tiene estadísticas, tier list y matriz de drawdown |
| Fiscalidad | 8 (España) | 4 (España) | 003 | Solo útil en España; aquí se universaliza |
| Biblioteca y metodología de estudio | 9 | 6 | **003** | 7 libros analizados + pedagogía médica |

## 6. Insumos Adoptados para el Programa Propio

| Insumo | Origen | Destino en nuestro syllabus |
|---|---|---|
| Formato de cátedra (perfil de egreso, matriz de trazabilidad, glosario) | Ambos | Estructura de `SYLLABUS.md` |
| Epistemología del trading + 5 mentiras del marketing | 003 · M1.1, M1.3 | Módulo 1.1–1.2 |
| Mapa de estilos × mercados × vehículos | 003 · M1.1 (ampliado) | Módulo 1.3 |
| Sesiones de Forex y ciclo de volumen | 003 · M1.5 / 004 · M2.4 | Módulo 2.4 |
| Ciclos de mercado (acumulación → markdown) y Dow | Ambos | Módulo 3.2 |
| Confirmación en 3 pasos + polaridad | 003 · M2.5 | Módulo 3.4 |
| TradingView + órdenes + spread | 003 · M1.6, M4.3–4.4 / 004 · M5 | Módulo 4 |
| BOS/CHoCH, liquidez, imbalances, top-down | 004 · M2.2, M3 | Módulo 5 |
| Catálogo crítico de indicadores y canales | 004 · M4 / 003 · M3.3–3.4 | Módulo 6 |
| Sistema de trading formal + esperanza | 003 · M3.1–3.2 | Módulo 7 |
| Position sizing + asimetría drawdown + frenos | Ambos | Módulo 8 |
| Backtesting N ≥ 100 + métricas | 004 · M7 | Módulo 9 |
| Psicotrading completo (Douglas, Steenbarger, neurobiología) | 003 · M5 / 004 · M7.4–7.5 | Módulo 10 |
| Rutina, inacción estratégica, estoicismo, 85/15 | 004 · M9–M10 | Módulos 10.6–10.7 y 12.2 |
| Brokers A/B-Book + estafas | 004 · M8 / 003 · M4.1 | Módulo 11.1–11.2 |
| Prop firms: estadísticas + matriz de drawdown + criterio | 003 · M6 | Módulo 11.3–11.6 |
| Biblioteca esencial | 003 · M7.3 | Módulo 12.6 |

## 7. Vacíos Curriculares — Lo que NINGÚN curso cubre y nuestro programa sí

Estos nueve vacíos justifican la existencia de un programa propio además de los dos cursos:

1. **Riesgo de cartera y correlación entre posiciones.** Ninguno explica que operar EUR/USD largo + GBP/USD corto (o largo en ambos) es una **doble exposición al dólar** que multiplica el riesgo real por encima del 1 % nominal. Crítico y ausente → Módulo 8.5.
2. **Plan de Trading como documento formal completo.** 004 lo menciona (M6.5) sin plantilla. Nuestro Módulo 12.1 entrega la plantilla de 10 secciones → la culminación del programa.
3. **Journal sistemático con protocolo de revisión semanal/mensual.** Ambos mandan llevar bitácora; ninguno define **campos, etiquetas de error ni protocolo de auditoría propia** → Módulo 9.5–9.6.
4. **Calendario macro aplicado.** Mencionan NFP/IPC/FOMC pero nadie enseña *cómo se opera alrededor* de esos eventos (ventanas de prohibición, volatilidad pre/post, restricciones de noticias de las prop firms) → Módulos 2.6 y 11.4.
5. **Correlación intermercados.** DXY ↔ oro ↔ acciones ↔ cripto ↔ tasas: la cadena causal que mueve todo. Ausente en ambos → Módulo 2.6.
6. **Reglas finas de prop firms.** *Consistency rules*, restricción de copiado, límites de lotaje, políticas de noticias — lo que realmente desaprueba cuentas → Módulo 11.4.
7. **Fiscalidad universal.** Ambos asumen España. Nuestro enfoque: principios + verificación jurisdiccional → Módulo 11.7.
8. **El trading como negocio medible.** KPIs operativos (E, PF, DD, horas/ROI), separación de capital, política de retiros, contabilidad simple → Módulo 12.3–12.4.
9. **Pedagogía activa.** Ambos cursos son expositivos (mirar video). Nuestro programa es de **entrenamiento deliberado**: cada lección tiene laboratorio, cada módulo tiene misión evaluada y el agente tutor aplica método socrático → definido en `agents.md`.

## 8. Correcciones Técnicas Menores (erratas y precisiones)

| Afirmación de origen | Precisión aplicada |
|---|---|
| "Spread de EUR/USD de 1–2 pips" | Hoy en brokers ECN/RAW ronda 0.1–1 pip + comisión; el orden de magnitud del curso es conservador pero no falso. Se actualiza la cifra. |
| "Esperanza de binarias E = −0.10" | Con payout de 85 %: E = 0.85·p − (1−p) = 1.85p − 1 → E(50 %) = −0.075. Con payout 80 %: −0.10. El signo y la conclusión son correctos. |
| "Una vela mensual se compone de 22 velas diarias en Forex / 30 en cripto" | Correcto (días hábiles vs 24/7). Buen detalle a conservar. |
| "Mercado pasa el 70 % del tiempo lateral" | Cifra razonable coherente con la literatura de rangos; se conserva etiquetada como aproximación. |
| "Profit Factor > 1.5" como objetivo | Estándar razonable para sistemas discretos. Se conserva. |
| Weinsein (4 etapas) vs ciclos 003 (acumulación/markup/distribución/markdown) | Son el mismo mapa con dos nomenclaturas. El programa unifica: ciclos de mercado como concepto, etapas de Weinstein como herramienta de filtrado. |

## 9. Decisiones de Diseño Derivadas

1. **Arquitectura de 4 niveles × 12 módulos** (Fundamentos → Técnica → Gestión → Profesionalización), fusionando la progresión de ambos cursos y redistribuyendo la densidad excesiva del 004.
2. **Enfoque universal:** criterios y principios en lugar de marcas locales; fiscalidad universal; laboratorios de due diligence replicables desde cualquier país.
3. **Idioma:** español natural con terminología técnica en inglés (*Stop Loss*, *Pullback*, BOS, *Win Rate*), glosario al primer uso de cada término.
4. **Pedagogía activa:** formato estándar de módulo = lecciones + laboratorio + misión + evaluación con criterios de graduación.
5. **Trazabilidad total:** cada módulo del syllabus declara sus fuentes (003/004) y su aporte propio (vacíos del punto 7).
6. **Regla de cifras:** toda cifra sin fuente citable se etiqueta *ilustrativa*; toda tier list se etiqueta *snapshot con fecha*.

## 10. Registro de Versiones

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-10-24 | Informe inicial: análisis completo de ambos cursos, comparativa, insumos, vacíos y decisiones de diseño |

