# Análisis Numérico (AN)

- **Slug:** `analisis-numerico`
- **Estado:** cursando
- **Año/cuatrimestre:** 2026 · 2do cuatrimestre (clases los martes; profesor del repaso: Ing. Juan Paoli)
- **Carrera/facultad:** Ingeniería en Sistemas de Información · UTN.BA (plan K08, nivel 3; la materia es la ex "Matemática Superior", los exámenes viejos llevan ese nombre o "Modelos Numéricos")

## Evaluaciones

| Evaluación | Carpeta | Fecha | Estado |
|---|---|---|---|
| Primer parcial | `primer-parcial/` | 2026-10-06 | rendido |
| Segundo parcial | `segundo-parcial/` | **2026-11-24** | **próximo** |
| 1er recuperatorio (1P y 2P) | carpeta del parcial | **2026-12-01** (confirmado por Lucho el 2026-11-10: lo tiene que rendir) | pendiente |
| 2do recuperatorio (1P y 2P) | carpeta del parcial | _(a definir, finales de febrero 2027)_ | pendiente |
| Final | `final/` | _(a definir)_ | pendiente |

> Fechas del cronograma oficial 2026-2C (`fuentes/cronograma-2026-2C.pdf`): repaso del
> 1P el 2026-09-29, **1er parcial 2026-10-06**, 2do parcial 2026-11-24. Los recuperatorios
> se preparan en la carpeta de su parcial. Se aprueba con **6 puntos**; se **promociona con
> 8 en cada parcial** y 8 en el TP grupal (mínimos cuadrados, `fuentes/TP-minimos-cuadrados-consigna.pdf`).
> Ojo: `analisis-matematico-2` también figura `cursando` (final el 2026-09-22): las skills
> van a preguntar qué materia usar cuando no se dé la ruta explícita.

## Estructura del examen

- **Primer parcial (formato vigente, K3052 2025):** 4 ejercicios, uno por tema, en este
  orden fijo: **Ej1 Series de Fourier · Ej2 Transformada de Laplace · Ej3 Sistemas
  estables · Ej4 Transformada Z**. Cada ejercicio tiene 2–3 ítems (a/b/c) de **1 punto
  cada uno** (10 ítems en total); se aprueba con 6. Dos temas (Tema 1 / Tema 2) con los
  mismos tipos de ítem y datos distintos. Sin ejercicio de números complejos como tal
  (en 2024-2C todavía había un Ej1 de complejos y 5 ejercicios de 2 puntos; el cronograma
  2026 solo tiene un "repaso rápido de complejos", así que se asume el formato 2025).
  Los parciales viejos (2015–2022) tenían 5 ejercicios con un ítem de multiple choice
  justificado y un ejercicio de complejos; su contenido de Fourier/Laplace/sistemas/Z
  sigue siendo el mismo. Detalle por posición en `primer-parcial/estrategia.md`.
- **Segundo parcial (2025):** 5 ejercicios de 2 puntos: Ej1 Raíces · Ej2 Sistemas de
  ecuaciones lineales (Jacobi/Gauss-Seidel) · Ej3 Interpolación y ajuste · Ej4
  Integración numérica · Ej5 Ecuaciones diferenciales. Tipos de ítem por posición (4 hojas
  de 2025-1C, ver `segundo-parcial/examenes/INDICE.md`): **Ej1** separar raíces en
  intervalos `[a; a+1]` + Newton-Raphson o punto fijo (condiciones de convergencia / elegir
  `g`) + cantidad de iteraciones de bisección; **Ej2** decidir sin resolver si converge
  Jacobi/Gauss-Seidel (radio espectral, diagonal dominante con parámetro `k`), y en el 2do
  recuperatorio número de condición + una iteración de Gauss-Seidel; **Ej3** hallar los
  valores faltantes de una tabla para que el interpolante tenga cierto grado (diferencias
  divididas) + cuántos polinomios de grado n existen + un ajuste por mínimos cuadrados
  (recta, exponencial o potencial); **Ej4** mayor `h` racional no periódico para Trapecios
  acotando `|f''|` (Simpson solo en el 2do recuperatorio); **Ej5** Lipschitz + Euler en el
  parcial, Heun / RK4 / clasificar una fórmula multipaso en los recuperatorios.
- **Final:** _(completar cuando haya finales)_

## Temario por evaluación

- **Primer parcial:** repaso de números complejos (forma polar, potencias y raíces,
  logaritmo complejo, valor principal, conjuntos en el plano); **series de Fourier**
  trigonométrica y exponencial (coeficientes, valor medio, paridad, simetría de media
  onda, completar una función definida en medio período para forzar paridad/SMO/
  coeficientes reales o imaginarios, espectro de amplitudes y de fase, uso de la serie
  para sumar series numéricas); **transformada de Laplace** (definición, tablas,
  propiedades de traslación, multiplicación y división por t, derivadas, convolución,
  teoremas del valor inicial/final, antitransformada por fracciones simples, evaluación
  de integrales impropias, ecuaciones integrales/integro-diferenciales, sistemas de EDO);
  **sistemas estables** (función de transferencia, polos y ceros, estabilidad y elección
  de K, corte de |G(s)| por el eje real/imaginario, respuesta temporal al impulso/escalón/
  entrada dada, tipo de respuesta y valor estable, método gráfico del módulo);
  **transformada Z** (definición, serie geométrica y región de convergencia, sucesiones
  definidas por paridad de n, propiedades de desplazamiento y multiplicación por n,
  antitransformada, ecuaciones en diferencias con verificación, sumas de series
  numéricas vía Z, secuencias finitas).
- **Segundo parcial:** raíces de ecuaciones no lineales (bisección, punto fijo,
  Newton-Raphson, cotas de error e iteraciones), sistemas de ecuaciones lineales
  (convergencia de Jacobi y Gauss-Seidel), interpolación polinómica (existencia y grado)
  y ajuste por mínimos cuadrados (recta, exponencial, potencial), diferenciación e
  integración numérica (trapecios, elección de h por cota de error), ecuaciones
  diferenciales (constante de Lipschitz, Euler).

## Fuentes

- **Videos:** clases virtuales grabadas de la cátedra (Aula Virtual UTN; el índice de
  links con teórica/práctica/OneNote por tema está en `fuentes/clases-virtuales-links.pdf`,
  teóricas en SharePoint de la UTN y prácticas en Google Drive, ambas con cuenta institucional; solo el OneNote de la práctica de Z es público). Los **OneNote** de cada práctica son PDFs con la guía tipeada + resolución manuscrita del profesor: material ideal para `/apunte-doc`. Transcripciones cacheadas en `<eval>/apuntes/transcripts/`.
- **Permitido en el parcial:** `fuentes/AYUDAMEMORIA-OFICIAL.pdf` (4 págs: STF/SEF, propiedades y tabla de Laplace, propiedades y tabla de Z, Euler, binomio; las págs 1–3 son del 1P —la tabla de Z está en la pág. 3— y la pág. 4 es del 2P) + tabla de integrales. Nada más. El machete se arma como **complemento** de ese ayudamemoria (lo que NO está: regla par/impar, `Cₙ = ½(aₙ − j bₙ)`, media onda, fracciones simples, Ruffini, tabla polo → respuesta, ROC por geométricas, `Z{aⁿ/n!} = e^{a/z}`).
- **Documentos:** `fuentes/formulas-y-metodos-manuscrito.pdf` (hoja de fórmulas propia,
  6 páginas: Fourier, Laplace, sistemas estables, Z, fracciones simples; base del
  machete), `fuentes/metodo-fracciones-simples.pdf` (apunte de cátedra),
  `fuentes/cronograma-2026-2C.pdf`, `fuentes/TP-minimos-cuadrados-consigna.pdf`.
- **TP grupal 2C 2026 (aproximación discreta por mínimos cuadrados):** consigna en
  `fuentes/TRABAJO PRACTICO 2do CUATRIMESTRE 2026 .pdf` (grupos de 4 a 6, PDF + video de
  4–6 min, nota ≥ 8 para promocionar; fecha de entrega la fija cada docente). Se trabaja en
  `tp-minimos-cuadrados/` (`enunciado.md`, `guia-tp.md` + `exports/`). Las cuentas del punto
  c)/d) salen con `tools/ajuste_mc.py`. Clases de ajuste (teórica + práctica, mp4 sin
  versionar) y OneNote `Ajuste.pdf` en `fuentes/clases/Ajuste-Aproximacion/`, pasadas a
  `segundo-parcial/ajuste/md/01–02`.
- **Clases grabadas (descargadas, en `fuentes/clases/<tema>/`, prefijo `T_` teórica / `P_` práctica; los mp4 no se versionan):** teórica STF, teórica SEF + transformada de Fourier, teórica Laplace, teórica aplicaciones de Laplace (`P_TLaplace.mp4`, que en realidad es la 2ª teórica), teórica y práctica de sistemas estables, teórica de Z y repaso del 1P. Transcriptas con `tools/transcribe_local.py` (Whisper large-v3-turbo en la Mac) a `primer-parcial/apuntes/transcripts/10–17`. **Las prácticas de Fourier, Laplace y Z están en Google Drive con descarga bloqueada por el dueño**: se cubren con sus OneNote (apuntes 01–06). El repaso descargado (`Repaso Primer Parcial.mp4`) es la grabación de SharePoint; el repaso 2026 del Ing. Paoli en Zoom está **roto** ("Esta grabación no existe"); en su lugar están las **fotos de la clase de repaso 2026 del curso** en `fuentes/clases/repaso-clase-2026/` (7 páginas), pasadas a `primer-parcial/repaso/practica-repaso-2026.md`.
- **Exámenes reales:** primer parcial: **16 hojas de examen distintas (11 instancias,
  2015 → 2025)** en `primer-parcial/examenes/`, indexadas en `INDICE.md`. 4 archivos son
  enunciados puros (2024-2C y 2025-1C, parcial + 1er recuperatorio), 14 están en
  `resueltos/` (8 resueltos a mano por alumnos con corrección del docente, 3 resueltos por
  la cátedra, 4 hojas de respuestas oficiales). Segundo parcial: **4 hojas de examen
  distintas (3 instancias, todas 2025-1C, K3052)** en `segundo-parcial/examenes/`,
  indexadas en `INDICE.md` el 2026-11-18: parcial Tema 1 y Tema 2 (2025-06-30), 1er
  recuperatorio (2025-07-07) y 2do recuperatorio (2025-07-11, cuyo enunciado solo existe
  dentro de su hoja de respuestas). Las 3 hojas de respuestas oficiales están en
  `resueltos/` y transcriptas en `resueltos/RESOLUCIONES-2025.md`.

### Fuentes del aula por tema (segundo parcial)

Tabla curada el 2026-11-18 desde el Aula Virtual (curso K3572) y `fuentes/clases-virtuales-links.pdf`.
Es la lista que usan las guías "desde cero" del 2P: **solo** estos archivos, en `fuentes/clases/<carpeta>/`.
Descartado del aula por no aportar al parcial: número áureo, planillas Excel de Jacobi/Gauss-Seidel,
Colabs de Python, videos externos de YouTube. **Ajuste por mínimos cuadrados no entra en el 2P 2026**
(se evaluó con el TP); sus apuntes quedan aparte en `segundo-parcial/ajuste/` (00 explicado paso a paso, 01 teórica, 02 práctica).

| Tema (ejercicio) | Carpeta | PDF de clase ("PARA DAR CLASES") | Teórico de cátedra | OneNote práctica | Videos → transcript |
|---|---|---|---|---|---|
| Raíces (Ej1) | `Raices/` | `Clase - Raices de ecuaciones no lineales.pdf` | `Teorico catedra 2.2 …` | `OneNote - Raices.pdf` (14 p.) | `T_Raices.mp4` → `10`, `P_Raices.mp4` → `11` |
| Sistemas lineales (Ej2) | `Sistemas de Ecuaciones Lineales/` | `Clase - Sistemas de ecuaciones lineales.pdf` | `Teorico catedra 2.3 …` | `OneNote - Sistemas de Ecuaciones Lineales.pdf` (19 p.) | `T_SEL.mp4` → `12`; práctica en Drive, **descarga bloqueada** |
| Interpolación (Ej3) | `Interpolacion/` | `Clase - Interpolacion general.pdf`, `Clase - Metodo de Lagrange.pdf`, `Clase - Metodo de Newton-Gregory.pdf` | `Teorico catedra 2.4 …` | `OneNote - Interpolacion.pdf` (13 p.) | `T_Interpolacion.mp4` → `13`; práctica en Drive, **descarga bloqueada** |
| Diferenciación e integración (Ej4) | `Integracion Numerica/` | `Clase - Diferenciacion e integracion numerica.pdf`, `Clase - Exactitud del metodo de Simpson.pdf` | `Teorico catedra 2.5 …` | `OneNote - Derivacion e Integracion Numerica.pdf` | `T_Dif-Int.mp4` → `14`, `P_Dif-Int.mp4` → `15` |
| Ecuaciones diferenciales (Ej5) | `Ecuaciones Diferenciales/` | `Clase - Metodos numericos para ecuaciones diferenciales.pdf` | `Teorico catedra 2.6 …` | `OneNote - Ecuaciones Diferenciales.pdf` (8 p.) | `T_ED.mp4` → `16`, `P_ED.mp4` → `17` |
| Repaso 2P | `repaso segundo parcial/` | — | — | `OneNote - Repaso Segundo Parcial.pdf` (15 p.) | video en Drive, **descarga bloqueada** |

Transversales: `fuentes/Guia-ejercicios-parte-2-calculo-numerico.pdf` (guía de ejercicios de la cátedra, 45 p.)
y la pág. 4 de `fuentes/AYUDAMEMORIA-OFICIAL.pdf` (lo único permitido en el examen). Los transcripts van a
`segundo-parcial/apuntes/transcripts/NN-….json`. Los videos de SharePoint se bajan desde Chrome con la cuenta
`@frba` (botón Descargar de Stream); los de Drive no tienen descarga ni transcripción habilitada.

## Leyenda de tags (para `examenes/INDICE.md`)

### Primer parcial

**Series de Fourier:** `#SerieTrigonometrica` `#SerieExponencial` `#CompletarFuncion`
(extender la función dada en medio período para forzar paridad / SMO / coeficientes
reales o imaginarios / valor medio) `#SimetriaMediaOnda` `#ValorMedio` `#Espectro`
`#SumaSerieNumerica` (usar la serie para sumar una serie numérica) `#Fasores`

**Transformada de Laplace:** `#TransformadaLaplace` (calcular una transformada o usar una
propiedad) `#IntegralPorLaplace` (evaluar `∫₀^∞` con la definición o con `L{f/t}`)
`#Antitransformada` `#Convolucion` `#EcuacionIntegral` (ecuaciones integrales e
integro-diferenciales) `#SistemaEDO`

**Sistemas estables:** `#Estabilidad` (hallar K o decidir si es estable) `#PolosCeros`
`#CorteEje` (corte de `|G(s)|` o `|Y(s)|` por el eje real o imaginario)
`#RespuestaTemporal` (respuesta al impulso / escalón / entrada dada) `#TipoRespuesta`
(oscilatoria, amortiguada, valor estable) `#ModuloGrafico` (`|G(a+bj)|` por vectores)
`#FuncionTransferencia` (obtener `G(s)` desde la ecuación diferencial)

**Transformada Z:** `#TransformadaZ` `#ROC` (región de convergencia) `#AntitransformadaZ`
`#EcuacionDiferencia` `#SumaSeriePorZ` `#SecuenciaFinita`

**Números complejos:** `#Complejos` `#PotenciasRaices` `#LogaritmoComplejo`
`#ConjuntosComplejos`

**Forma de la consigna (no tema):** `#MultipleChoice` `#VoF` `#Demostracion`

### Segundo parcial

**Raíces de ecuaciones:** `#SepararRaices` (hallar un intervalo `[a; a+1]` para cada raíz,
gráficamente) `#Biseccion` `#CotaIteraciones` (cuántas iteraciones garantizan un error dado;
¿suficientes o necesarias?) `#PuntoFijo` (verificar las condiciones de convergencia de una
`g(x)`, elegir entre dos `g`, iterar) `#NewtonRaphson`

**Sistemas de ecuaciones lineales:** `#Jacobi` `#GaussSeidel` `#ConvergenciaIterativos`
(decidir, sin resolver, si el método converge) `#RadioEspectral` `#DiagonalDominante`
`#NumeroCondicion` (bien / mal condicionado con `‖A‖·‖A⁻¹‖`)

**Interpolación y ajuste:** `#GradoPolinomio` (condiciones sobre los parámetros de la tabla
para que el interpolante tenga cierto grado; hallar los valores faltantes)
`#CantidadPolinomios` (¿cuántos polinomios de grado n pasan por los puntos?)
`#DiferenciasDivididas` (armar el polinomio de Newton) `#AjusteRecta` `#AjusteExponencial`
`#AjustePotencial` `#ErrorAjuste`

**Integración numérica:** `#Trapecios` `#EleccionH` (mayor `h` racional no periódico, o
número de subintervalos, que garantiza la cota de error) `#Simpson`

**Ecuaciones diferenciales:** `#Lipschitz` `#Euler` `#Heun` `#RungeKutta4` `#Multipaso`
(clasificar una fórmula: explícita/implícita, cantidad de pasos)

## Estado del material

| Evaluación | Apuntes | INDICE | Estrategia | Poda | Plan | Registro | Flashcards | Machete | Simulacros |
|---|---|---|---|---|---|---|---|---|---|
| Primer parcial (2026-10-06, rendido) | ✅ 15 (01–07 desde los OneNote de práctica, 10–17 desde las clases grabadas transcriptas con Whisper local) | ✅ 16 hojas / 11 instancias + 14 resueltos | ✅ (+ actualización 2026-10-02) | — | ✅ (3 días, recalculado 2026-10-03 alrededor de las guías lineales `guia/01–04`) | ✅ (vacío) | — | ✅ (`primer-parcial/repaso/machete.md` + `exports/machete.pdf`, 2026-10-05; complemento del ayudamemoria) | — |
| **Segundo parcial (2026-11-24)** | ✅ 6 (01–05 guías "desde cero" de raíces, sistemas lineales, interpolación, diferenciación/integración y ecuaciones diferenciales, con todos los ítems de parcial 2025 y del repaso como "tu turno" + checkpoint, numeradas igual que el ejercicio del parcial; 06 práctica del repaso 2026, 15 ejercicios; aparte, en `ajuste/`, 00–02 de **ajuste por mínimos cuadrados**, fuera de alcance en 2026) | ✅ 4 hojas / 3 instancias (2025-1C) + 3 hojas de respuestas transcriptas en `resueltos/RESOLUCIONES-2025.md` | ✅ (2026-11-19; dataset chico, complementado con el repaso 2026 y las notas "En clase") | — | ✅ (5 días, 2026-11-19; núcleo de cada guía por día, `08` a ciegas + simulacro el 2026-11-23) | ✅ (vacío) | — | — | — |
