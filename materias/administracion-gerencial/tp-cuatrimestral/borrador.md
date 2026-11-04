# TP Cuatrimestral AG 2C26 — Borrador (JPMorgan Chase)

> Fuente canónica del contenido del Slides. El deck se genera con `build_slides.py` → `exports/00_TP Cuatrimestral_Gx.pptx` y se sube a Drive (se convierte a Google Slides). Si se cambia algo acá, cambiarlo también en el script (o al revés).
> Google Slides (nativo, el entregable): https://docs.google.com/presentation/d/1tTJdOupXbTbHOzt2hcow5uC2tLUHzQyppOCO437tkXM/edit (en Mi unidad de Luciano; mover a la carpeta `Tps/tp cuatrimestral` del grupo).
> Generado el 2026-11-03; contrastado contra el libro de cátedra el 2026-11-04 (ver sección final). Sigue la plantilla obligatoria del `enunciado.md`, sección por sección.

---

## Portada

- Universidad Tecnológica Nacional · FRBA · Ingeniería en Sistemas de Información
- Administración Gerencial · Trabajo Práctico Cuatrimestral (2C26) · Curso K5571
- Empresa analizada: **JPMorgan Chase & Co.**
- Grupo: B _(confirmar: todas las entregas previas del grupo llevan el sufijo `_B`; el enunciado habla de "número de grupo")_

## 1. Datos del grupo

| Integrante | Rol gerencial | Responsabilidad principal |
|---|---|---|
| Germán Martín Bergera Vila | Gerente General | Estrategia, coordinación del equipo directivo y decisión final (estratega, planeador-organizador y líder-comunicador, según Sallenave) |
| Juan Ignacio Cobas | Operaciones | Procesamiento de pagos, mercados y servicios; continuidad operativa (árbitro de perturbaciones, según Mintzberg) |
| Matías Tadeo Rossi | Comercial / Marketing | Marca Chase, adquisición y retención de clientes, venta cruzada (enlace y portavoz) |
| Clara Belén Busca | RRHH | Talento, cultura, desarrollo de líderes y plan de sucesión (líder) |
| Franco Ezequiel Piccininno | Finanzas | Presupuesto (incluido el tecnológico), eficiencia y control de KPI (administrador de recursos) |
| Luciano Schirripa | Sistemas / Innovación | Plataformas tecnológicas, modernización (cloud), IA y ciberseguridad (monitor, difusor y emprendedor) |

Luciano va en Sistemas / Innovación porque trabaja en la empresa real y es donde pesa más el
conocimiento desde adentro (además la plantilla pide explícitamente "rol de los Sistemas de
Información"). El resto es asignación arbitraria, se puede rotar. Los papeles entre paréntesis
son los del cap. IV (Sallenave: estratega, planeador-organizador, líder-comunicador) y el cap. V
(los 10 papeles de Mintzberg: representante, líder, enlace; monitor, difusor, portavoz;
emprendedor, árbitro, administrador de recursos, negociador).

## 2. Empresa analizada

| Campo | Contenido |
|---|---|
| Tipo | Real |
| Rubro | Servicios financieros globales (banca minorista, banca de inversión, pagos y gestión de patrimonios) con desarrollo tecnológico propio a escala de empresa tech |
| Tamaño | Más de 300.000 empleados en más de 100 países; activos por ≈ US$4 billones; presupuesto tecnológico 2026 ≈ US$19.800 millones (≈ US$1.200 millones en IA) y más de 50.000 tecnólogos. Centro en Buenos Aires desde 2014 (≈ 3.800 personas, nueva torre en Núñez) |
| Mercado objetivo | Personas y pymes (Chase, en EE.UU. y ahora Reino Unido y Alemania); empresas, gobiernos e inversores institucionales (CIB); grandes patrimonios (AWM) |

**Descripción breve:** JPMorgan Chase & Co. es el banco más grande de Estados Unidos y uno de
los mayores del mundo. Opera en tres segmentos: banca de consumo (Chase), banca comercial y de
inversión (CIB) y gestión de activos y patrimonios (AWM). Se diferencia por construir su propia
tecnología: plataformas de pagos que mueven del orden de US$10 billones por día, Kinexys
(blockchain), LLM Suite (IA generativa interna) y una red global de centros tecnológicos, entre
ellos el Buenos Aires Corporate Center. Por eso lo analizamos como empresa tecnológica: su
producto corre sobre software propio y su mayor inversión es en tecnología.

## 3. Liderazgo (cap. VII)

| Campo | Contenido |
|---|---|
| Estilo de liderazgo | **Liderazgo situacional** (Hersey y Blanchard) con base demócrata en los niveles gerenciales. En la cúpula, **liderazgo transformacional** con rasgos carismáticos (Jamie Dimon, CEO desde 2005): metas desafiantes y una visión que trasciende lo transaccional |
| Justificación (máx. 5 líneas) | Con más de 300.000 personas no sirve un único estilo: el líder adapta su comportamiento al **grado de desarrollo de cada colaborador** (competencia y disposición). A un ingeniero senior del hub de Buenos Aires se le **delega**; a un recién ingresado se lo **dirige** o **instruye**. Dimon fija metas exigentes y una cultura de "negocios de primera clase, de una manera de primera clase", e inspira a trascender el interés individual: el rasgo del líder transformacional |
| Problema potencial | **Dependencia del líder carismático:** cuando la confianza extrema del líder le impide escuchar y tolerar que lo desafíen, pasa a ser una carga para la organización (House); con Dimon de 70 años, el riesgo concreto es una **sucesión mal preparada**. **Desajuste situacional:** dirigir y controlar a equipos competentes y dispuestos (cuando corresponde delegar) es redundante con la estructura de la tarea (ruta-meta) y actúa como factor higiénico que desmotiva (Herzberg) |

## 4. Cadena de Valor de Porter (cap. XIV)

### Esquema (adaptado a un banco; nombres según el libro)

Actividades de apoyo:

| Actividad | En JPMorgan Chase |
|---|---|
| Infraestructura gerencial ⚠️ | Gestión general, planificación y finanzas; riesgo, compliance, legales y asuntos regulatorios; capital y licencias bancarias |
| Gestión de recursos humanos | Más de 300.000 personas; reclutamiento tecnológico en hubs (Buenos Aires, India, Reino Unido); desarrollo de líderes |
| Desarrollo de la tecnología ★1 | US$19.800 millones por año; plataformas propias (Payments, Kinexys, LLM Suite); cloud y ciberseguridad |
| Adquisiciones | Proveedores de nube, datos de mercado, hardware y servicios; alianzas con fintechs y redes de tarjetas |

Actividades primarias:

| Actividad | En JPMorgan Chase |
|---|---|
| Logística de entrada | Captación de depósitos y fondos; ingreso de datos de clientes y de mercado |
| Operaciones ★2 | Procesamiento de pagos (≈ US$10 billones por día), crédito, trading y custodia |
| Logística de salida | Canales: app y web Chase, sucursales, cajeros, APIs para empresas |
| Comercialización y ventas | Marca Chase, tarjetas Sapphire, banca privada, programas de recompensas |
| Servicio post-venta | Atención 24/7, asesoramiento financiero, prevención de fraude |

El "margen" de la derecha es la diferencia entre lo que paga el cliente y los costos totales, y
depende de cómo se administre la cadena completa (Porter, en el libro).

### Análisis

| Campo | Contenido |
|---|---|
| Actividad donde se genera mayor valor (1) | **Desarrollo de la tecnología.** Es lo que diferencia a JPM de un banco tradicional: las plataformas propias bajan el costo por transacción y permiten lanzar productos (Chase UK/Alemania, Kinexys) sin depender de terceros. Es el "know-how" que atraviesa toda la cadena |
| Actividad donde se genera mayor valor (2) | **Operaciones.** La escala del procesamiento (pagos, mercados, custodia) genera ingresos por comisiones y datos que ningún competidor nuevo puede replicar rápido. Porter: se puede ser el mejor en marketing, pero no es ventaja si no se equipara con las operaciones |
| Actividad problemática | **Infraestructura gerencial (riesgo y compliance) sobre sistemas heredados.** Cada cambio pasa por controles regulatorios y por sistemas legacy: la modernización compite con "mantener las luces prendidas" y frena el tiempo de salida al mercado |
| Rol de los Sistemas de Información | **No son soporte: son el núcleo.** Todas las actividades primarias corren sobre software propio: los SI integran datos (entrada), automatizan operaciones (STP), son el canal (app, APIs) y el control (fraude, compliance). El hub de Buenos Aires es parte de esa cadena |

## 5. Matriz BCG (cap. XIV)

Ejes según el libro: **crecimiento de la demanda** (vertical) × **participación relativa en el
mercado** (horizontal). Cuadrantes: Estrellas, Dilemas, Vacas lecheras, Pesos muertos (perros).
Lógica del portafolio: las vacas lecheras generan el efectivo que necesitan estrellas y dilemas.

| Producto / Servicio | Cuadrante BCG | Decisión estratégica |
|---|---|---|
| Chase: banca minorista en EE.UU. (cuentas, tarjetas, hipotecas) | Vaca lechera | Seguir explotando sin grandes inversiones nuevas: financia la inversión tecnológica y la expansión |
| Banca de inversión y mercados (CIB) | Estrella | Inversión impulsora para sostener la participación: trading electrónico y datos |
| JPMorgan Payments | Estrella | Invertir: pagos en tiempo real, expansión global, integración con Kinexys |
| Chase Reino Unido y Alemania (banca digital internacional) | Dilema | Invertir con hitos: crecer hasta el punto de equilibrio (y volverse estrella) o frenar |
| Kinexys (blockchain) e IA generativa (LLM Suite) | Dilema | Invertir selectivamente: pilotos con casos de uso medibles |
| Chase Pay (billetera digital propia, discontinuada en 2019) | Peso muerto (perro) | No invertir para mantenerlo vivo (ya ejecutado): apoyarse en Apple Pay, Google Pay y Zelle |

## 6. Decisiones estratégicas finales (cap. XV)

Una decisión por gerente, con su indicador estratégico y la perspectiva del tablero de control
a la que pertenece (cliente, económico-financiera, procesos internos, innovación y aprendizaje).
Es un tablero de control **estratégico**: información para la alta dirección sobre el
posicionamiento a largo plazo.

| Gerente | Decisión estratégica | KPI de control | Perspectiva |
|---|---|---|---|
| Gerente General | Expansión europea de Chase (Reino Unido → Alemania) con hitos go/no-go | Clientes activos; fecha de punto de equilibrio del negocio | Cliente / Económico-financiera |
| Operaciones | Escalar Payments: liquidación en tiempo real y automatización (STP) | Volumen diario procesado; % de operaciones sin intervención manual | Procesos internos |
| Comercial / Marketing | Profundizar la relación con clientes Chase (venta cruzada: inversión, tarjetas) | Productos por cliente; NPS | Cliente |
| RRHH | Plan de sucesión y desarrollo de líderes situacionales | % de puestos críticos con sucesor identificado; rotación voluntaria de talento clave | Innovación y aprendizaje |
| Finanzas | Disciplina del presupuesto tecnológico: más "cambio", menos "mantenimiento" | Ratio de eficiencia (gastos / ingresos); % del gasto tech en nuevas capacidades | Económico-financiera |
| Sistemas / Innovación | Modernización: migración a cloud, baja de legacy y despliegue de IA generativa | % de aplicaciones modernizadas; incidentes críticos por trimestre; % de empleados activos en LLM Suite | Procesos internos / Innovación y aprendizaje |

## Fuentes

- Libro de cátedra: *Administración Gerencial* (Texido, 2026), caps. IV y V (el gerente: Sallenave y Mintzberg), VII (liderazgo), VIII (motivación: Herzberg), XIV (estrategia y planeamiento: cadena de valor y BCG) y XV (tablero de control).
- JPMorgan Chase & Co., Annual Report 2025 y resultados del 4T 2025 (SEC EDGAR).
- Reuters (2025-09): lanzamiento del banco digital Chase en Alemania en 2026.
- Bloomberg Línea (2024-12) y El Economista (2025): Buenos Aires Corporate Center y nueva sede en Núñez.
- Notas de prensa sobre el presupuesto tecnológico 2026 (≈ US$19.800 millones).

### Datos a verificar antes de entregar (marcados por Claude)

- Cantidad actual de tecnólogos (fuentes dan entre 50.000 y 65.000; se usó "más de 50.000").
- Si el banco digital en Alemania ya se lanzó en 2026 (estaba anunciado para el 2T 2026).
- Empleados del hub de Buenos Aires (≈ 3.800 según notas de 2025).

## Contraste con el libro de cátedra (2026-11-04)

Qué se verificó contra `fuentes/ADMINISTRACION GERENCIAL COMPLETO - V1.1.8 - 2026.pdf` y qué se corrigió:

| Tema | Lo que dice el libro | Qué se cambió en el TP |
|---|---|---|
| Numeración | Estrategia y planeamiento = cap. **XIV**; Tablero de control = **XV**; Crisis y cambio = XVI | Corregido en todo el TP (antes decía XVI/XVII) y en `MATERIA.md` |
| Sallenave (cap. IV) | Tres papeles: **estratega, planeador-organizador, líder-comunicador** | Nombres exactos en la fila del Gerente General |
| Mintzberg (cap. V) | 10 papeles en 3 esferas (interpersonal, informacional, decisional) | Cada gerente del grupo lleva su papel entre paréntesis |
| Tipología elemental (cap. VII) | Autócratas, demócratas, paternalistas | "Base demócrata" se mantiene |
| Situacional (cap. VII) | Variable contingente = **grado de desarrollo del colaborador** (capacidad + disposición); dirigir / instruir / apoyar / delegar | Antes la justificación elegía el estilo por área (regulada vs. tecnológica): mal aplicado. Reescrita según competencia y disposición del colaborador |
| Ruta-meta (cap. VII) | Cuatro comportamientos (director, apoyador, participativo, orientado a logros); **no abarca el liderazgo de toda la organización**; el comportamiento del líder es ineficaz si es redundante con la estructura de la tarea | Se dejó de usar ruta-meta para describir al CEO; se usa la idea de redundancia para el "desajuste situacional" |
| Carismático / transformacional (cap. VII) | House: confianza extrema, carácter dominante, fuerte convicción; pasada la crisis "puede convertirse en una carga... le impide escuchar". Transformacional: inspira a trascender el interés personal | Dimon se describe como líder transformacional con rasgos carismáticos; el problema potencial sale textualmente de la advertencia del libro |
| Herzberg (cap. VIII) | El **control** figura entre los factores periféricos / higiénicos: su ausencia desmotiva, su presencia no motiva | Se mantiene la mención en el problema potencial |
| Cadena de valor (cap. XIV) | Primarias: logística de entrada, operaciones, logística de salida, **comercialización y ventas, servicio post-venta**. Apoyo: **adquisiciones, desarrollo de la tecnología, gestión de RRHH, infraestructura gerencial**. Margen = precio menos costos totales, depende de toda la cadena. "Se puede ser el mejor en marketing pero no es ventaja si no se equipara con las operaciones" | Nombres alineados al libro; cita de Porter incorporada a "mayor valor (2)"; infraestructura gerencial descripta con "gestión general, planificación, finanzas, legales" |
| BCG (cap. XIV) | Ejes: **participación relativa en el mercado** y **crecimiento de la demanda**. Cuadrantes: Estrellas, **Dilemas**, Vacas lecheras, **Pesos muertos (perros)**. Estrellas: inversión impulsora; vacas: explotar sin nuevas inversiones; dilemas: decisión incierta, pueden volverse estrellas; pesos muertos: ninguna inversión nueva | Terminología y decisiones alineadas (antes decía "interrogante", "crecimiento del mercado") |
| Tablero de control (cap. XV) | Indicadores estratégicos; cuatro **perspectivas**: cliente, económico-financiera, procesos internos, innovación y aprendizaje; tablero operativo / directivo / **estratégico** | Columna "Perspectiva" agregada a las decisiones; nota de que es un tablero estratégico |
| Empresa (sección 2) | No aplica: datos públicos de JPMorgan, no del libro | Sin cambios |
