# TP Cuatrimestral AG 2C26 — Borrador (JPMorgan Chase)

> Fuente canónica del contenido del Slides. El deck se genera con `build_slides.py` → `exports/00_TP Cuatrimestral_Gx.pptx` y se sube a Drive (se convierte a Google Slides). Si se cambia algo acá, cambiarlo también en el script (o al revés).
> Google Slides (nativo, el entregable): https://docs.google.com/presentation/d/1s5jMx-FPRXnaNnN7EL9gvb9tiH2SxPS2iy9QNtyR8Eo/edit (en Mi unidad de Luciano; mover a la carpeta `Tps/tp cuatrimestral` del grupo).
> Generado el 2026-11-03. Sigue la plantilla obligatoria del `enunciado.md`, sección por sección.

---

## Portada

- Universidad Tecnológica Nacional · FRBA · Ingeniería en Sistemas de Información
- Administración Gerencial · Trabajo Práctico Cuatrimestral (2C26) · Curso K5571
- Empresa analizada: **JPMorgan Chase & Co.**
- Grupo: _(confirmar número; el TP1 del grupo se entregó como `..._B`)_

## 1. Datos del grupo

| Integrante | Rol gerencial | Responsabilidad principal |
|---|---|---|
| Germán Martín Bergera Vila | Gerente General | Estrategia, coordinación del equipo directivo y decisión final (estratega, organizador y líder, según Sallenave) |
| Juan Ignacio Cobas | Operaciones | Procesamiento de pagos, mercados y servicios; eficiencia y continuidad operativa |
| Matías Tadeo Rossi | Comercial / Marketing | Marca Chase, adquisición y retención de clientes, venta cruzada |
| Clara Belén Busca | RRHH | Talento, cultura, desarrollo de líderes y plan de sucesión |
| Franco Ezequiel Piccininno | Finanzas | Presupuesto (incluido el tecnológico), eficiencia y control de KPI |
| Luciano Schirripa | Sistemas / Innovación | Plataformas tecnológicas, modernización (cloud), IA y ciberseguridad |

Luciano va en Sistemas / Innovación porque trabaja en la empresa real y es donde pesa más el
conocimiento desde adentro (además la plantilla pide explícitamente "rol de los Sistemas de
Información"). El resto es asignación arbitraria, se puede rotar.

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

## 3. Liderazgo

| Campo | Contenido |
|---|---|
| Estilo de liderazgo | **Liderazgo situacional** (Hersey y Blanchard), con base demócrata y, en la cúpula, un estilo **orientado al logro** (ruta-meta): exigente, directo y basado en datos |
| Justificación (máx. 5 líneas) | Con más de 300.000 personas y negocios muy distintos, un único estilo no sirve. En las áreas reguladas (riesgo, compliance) los líderes **dirigen e instruyen**: procedimientos claros y control. En tecnología e innovación **delegan y apoyan**: equipos con autonomía, objetivos exigentes y seguimiento por métricas. Jamie Dimon (CEO desde 2005) fija la vara desde arriba con una cultura de "hacer negocios de primera clase, de una manera de primera clase" |
| Problema potencial | **Sucesión:** el liderazgo está muy asociado a la figura del CEO; un recambio mal preparado afecta la cultura. **Desajuste situacional:** aplicar el estilo "dirigir" de las áreas reguladas a equipos técnicos ya competentes genera frustración y fuga de talento (Herzberg: el control excesivo es un factor de higiene que desmotiva) |

## 4. Cadena de Valor de Porter

### Esquema (adaptado a un banco)

Actividades de apoyo:

| Actividad | En JPMorgan Chase |
|---|---|
| Infraestructura de la empresa ⚠️ | Gobierno corporativo, riesgo, compliance y legales; capital y licencias bancarias |
| Gestión de RRHH | Más de 300.000 personas; reclutamiento tecnológico en hubs (Buenos Aires, India, Reino Unido); desarrollo de líderes |
| Desarrollo tecnológico ★1 | US$19.800 millones por año; plataformas propias (Payments, Kinexys, LLM Suite); cloud y ciberseguridad |
| Abastecimiento | Proveedores de nube, datos de mercado, hardware y servicios; alianzas con fintechs y redes de tarjetas |

Actividades primarias:

| Actividad | En JPMorgan Chase |
|---|---|
| Logística de entrada | Captación de depósitos y fondos; ingreso de datos de clientes y de mercado |
| Operaciones ★2 | Procesamiento de pagos (≈ US$10 billones por día), crédito, trading y custodia |
| Logística de salida | Canales: app y web Chase, sucursales, cajeros, APIs para empresas |
| Marketing y ventas | Marca Chase, tarjetas Sapphire, banca privada, programas de recompensas |
| Servicio posventa | Atención 24/7, asesoramiento financiero, prevención de fraude |

### Análisis

| Campo | Contenido |
|---|---|
| Actividad donde se genera mayor valor (1) | **Desarrollo tecnológico.** Es lo que diferencia a JPM de un banco tradicional: las plataformas propias bajan el costo por transacción y permiten lanzar productos (Chase UK/Alemania, Kinexys) sin depender de terceros |
| Actividad donde se genera mayor valor (2) | **Operaciones.** La escala del procesamiento (pagos, mercados, custodia) genera ingresos por comisiones y datos que ningún competidor nuevo puede replicar rápido |
| Actividad problemática | **Infraestructura (riesgo y compliance) sobre sistemas heredados.** Cada cambio pasa por controles regulatorios y por sistemas legacy: la modernización compite con "mantener las luces prendidas" y frena el tiempo de salida al mercado |
| Rol de los Sistemas de Información | **No son soporte: son el núcleo.** Todas las actividades primarias corren sobre software propio: los SI integran datos (entrada), automatizan operaciones (STP), son el canal (app, APIs) y el control (fraude, compliance). El hub de Buenos Aires es parte de esa cadena |

## 5. Matriz BCG

Ejes: crecimiento del mercado (vertical) × participación relativa de mercado (horizontal).

| Producto / Servicio | Cuadrante BCG | Decisión estratégica |
|---|---|---|
| Chase: banca minorista en EE.UU. (cuentas, tarjetas, hipotecas) | Vaca lechera | Mantener y cosechar: financia la inversión tecnológica y la expansión |
| Banca de inversión y mercados (CIB) | Estrella | Invertir para sostener el liderazgo: trading electrónico y datos |
| JPMorgan Payments | Estrella | Invertir: pagos en tiempo real, expansión global, integración con Kinexys |
| Chase Reino Unido y Alemania (banca digital internacional) | Interrogante | Invertir con hitos: crecer hasta el punto de equilibrio o frenar |
| Kinexys (blockchain) e IA generativa (LLM Suite) | Interrogante | Invertir selectivamente: pilotos con casos de uso medibles |
| Chase Pay (billetera digital propia, discontinuada en 2019) | Perro | Desinvertir (ya ejecutado): apoyarse en Apple Pay, Google Pay y Zelle |

## 6. Decisiones estratégicas finales

Una decisión por gerente, cada una con su KPI de control (tablero de control, cap. XVII).

| Gerente | Decisión estratégica | KPI de control |
|---|---|---|
| Gerente General | Expansión europea de Chase (Reino Unido → Alemania) con hitos go/no-go | Clientes activos; fecha de punto de equilibrio del negocio |
| Operaciones | Escalar Payments: liquidación en tiempo real y automatización (STP) | Volumen diario procesado; % de operaciones sin intervención manual |
| Comercial / Marketing | Profundizar la relación con clientes Chase (venta cruzada: inversión, tarjetas) | Productos por cliente; NPS |
| RRHH | Plan de sucesión y desarrollo de líderes situacionales | % de puestos críticos con sucesor identificado; rotación voluntaria de talento clave |
| Finanzas | Disciplina del presupuesto tecnológico: más "cambio", menos "mantenimiento" | Ratio de eficiencia (gastos / ingresos); % del gasto tech en nuevas capacidades |
| Sistemas / Innovación | Modernización: migración a cloud, baja de legacy y despliegue de IA generativa | % de aplicaciones modernizadas; incidentes críticos por trimestre; % de empleados activos en LLM Suite |

## Fuentes

- Libro de cátedra: *Administración Gerencial* (Texido, 2026), caps. IV, V, VII, XVI y XVII.
- JPMorgan Chase & Co., Annual Report 2025 y resultados del 4T 2025 (SEC EDGAR).
- Reuters (2025-09): lanzamiento del banco digital Chase en Alemania en 2026.
- Bloomberg Línea (2024-12) y El Economista (2025): Buenos Aires Corporate Center y nueva sede en Núñez.
- Notas de prensa sobre el presupuesto tecnológico 2026 (≈ US$19.800 millones).

### Datos a verificar antes de entregar (marcados por Claude)

- Cantidad actual de tecnólogos (fuentes dan entre 50.000 y 65.000; se usó "más de 50.000").
- Si el banco digital en Alemania ya se lanzó en 2026 (estaba anunciado para el 2T 2026).
- Empleados del hub de Buenos Aires (≈ 3.800 según notas de 2025).
