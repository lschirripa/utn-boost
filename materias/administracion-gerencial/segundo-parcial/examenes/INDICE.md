# Índice de parciales — Segundo Parcial · Administración Gerencial (UTN.BA)

> **Para qué sirve:** igual que en el primer parcial, acá no hay hojas de examen sueltas sino
> **compilados armados por alumnos**: un `.docx` con 11 hojas fechadas (2012–2018) **y sus
> respuestas** (con la página del libro viejo entre paréntesis), un `.md` con 5 juegos de
> preguntas sin fecha (3 de ellos circulan también como aportes de foro) y **una foto** de
> una hoja tipeada. Este archivo es la **única representación textual** del dataset: cada
> pregunta transcripta tal cual, con **tags por tema**. Para cualquier análisis (frecuencias,
> brechas, simulacros) se grepea **este archivo**, nunca se re-leen el docx ni la foto.
>
> **Cómo buscar** (desde `examenes/`):
> ```bash
> grep -n "#BCG" INDICE.md                    # todas las preguntas de matriz BCG (la más tomada)
> grep -n "#Poder" INDICE.md                  # cualquier pregunta del bloque poder/autoridad
> grep -n "#Delegacion" INDICE.md             # bloque delegación / descentralización
> grep -n "#Crisis" INDICE.md                 # bloque crisis y cambio
> grep -n "#CincoFuerzas" INDICE.md           # cualquier fuerza de Porter
> grep -n "^## " INDICE.md                    # listar las 15 hojas de examen
> grep -n "RECICLADO" INDICE.md               # preguntas repetidas entre hojas
> grep -n "✅ resp" INDICE.md                 # preguntas con respuesta en el compilado
> ```
> **Mantenimiento:** al agregar un parcial nuevo, sumá su sección con los mismos tags y
> actualizá las tablas del final. Si una pregunta ya está indexada, marcala `[RECICLADO]`.

## Cómo está armado el dataset

- **Unidad de conteo = hoja de examen.** En una misma fecha la cátedra toma varios **temas**
  (Tema A / Tema B, Tema 1 / 2 / 3) con preguntas distintas del mismo pool; cada tema es una
  sección propia: **15 hojas** de **12 instancias**. Los porcentajes de `estrategia.md` se
  calculan sobre las 15 hojas.
- **Hojas incompletas.** Como en el 1P, el compilado registra solo las preguntas que el
  alumno se acordó o quiso responder: de las 11 hojas del docx, **solo una está completa**
  (2014-11-10); el resto trae 2, 3 o 4 de 5 (se anota `(n de 5 registradas)` y se conserva
  la numeración original, por eso hay saltos: P1, P3, P5). Eso **subestima** la frecuencia
  de todos los temas por igual: las frecuencias se leen como piso.
- **Formato del examen:** 5 preguntas teóricas a desarrollar, numeradas 1–5. En 2016 la P1
  fue un **V/F** con justificación (único caso). Se transcriben como `- **Pn)** enunciado →
  #Tag` (P = "pregunta", no "práctico"). Si la pregunta tiene respuesta escrita en el
  compilado se marca `✅ resp.` (y `(pág. N)` es la página del **libro viejo** que anotó el
  alumno; no coincide con el PDF 2026).
- **Archivos:** `2012-2018_compilado-preguntas-respuestas.docx` (11 hojas fechadas de 8
  instancias, con respuestas), `sin-fecha_compilado-preguntas.md` (5 juegos: A, B, C, D, E;
  **C y E resultaron ser las versiones completas** del 2015-11-09 Tema 2 y del 2014-11-10;
  A, B y D son los tres juegos que circulan como **aportes de foro** sobre el 2P, pegados por
  Lucho el 2026-11-09: ya estaban) y `sin-fecha_Parcial.jpg` (foto de una hoja tipeada, 5
  preguntas, sin fecha ni docente visibles; venía como `Webp.net-compress-image.jpg`).
- **Docentes que aparecen:** Daniel Texido (2014-06-24, 2014-11-10, 2015-11-09, 2016-11-14) y
  Gastón Paccor (2015-11-05, dos temas). La hoja 2018-06-13 trae el curso (**K5051**) en vez
  del docente.
- **Fechas:** el 2P cae en **junio** (1C: 2012-06-25, 2014-06-24, 2018-06-13) o en
  **noviembre** (2C: 2014-11-06, 2014-11-10, 2015-11-05, 2015-11-09, 2016-11-14). El
  2014-11-06 y el 2014-11-10 son dos cursos distintos de la misma semana.

## Leyenda de tags

**Poder y autoridad (cap. X):** `#Poder` (paraguas) `#Influencia` `#PoderVsAutoridad`
`#FuentesPoder` (recompensa / coerción / legítimo / referente / experto) `#FormasExpresionPoder`
(descendente / ascendente / lateral) `#ModelosOrganizacion` (racional burocrático / colectivo
de consenso)

**Delegación y descentralización (cap. XI):** `#Delegacion` (paraguas) `#ConceptoDelegacion`
(qué es delegar, qué se delega, vs. participación) `#FactoresContingentesDelegacion`
`#MejorarDelegacion` (recomendaciones / requisitos) `#Centralizacion` `#TiposDescentralizacion`
(vertical / horizontal + ventajas)

**Ética, moral y RSE (cap. XII):** `#Etica` `#Moral` `#EticaVsMoral` `#RSE`

**Mobbing (cap. XIII):** `#Mobbing` (características, formas de expresión del acoso)

**Estrategia y planeamiento (cap. XIV):** `#Planeamiento` (paraguas) `#NivelesPlaneamiento`
(operativo / táctico / estratégico) `#PlaneamientoEstrategico` (características, objetivos)
`#CincoFuerzas` (paraguas Porter) `#Rivalidad` `#Sustitutos` `#Proveedores` `#Compradores`
`#CadenaValor` `#BCG` `#Escenarios` `#EstrategiasCrecimiento` `#EstrategiasSupervivencia`
`#TiposCambio` (compulsivo / imitativo / creador; "estrategia y cambio", págs. 98–99)

**Tablero de control (cap. XV):** `#TableroControl` (paraguas) `#PerspectivasTablero`
`#TiposTablero`

**Crisis (cap. XVI):** `#Crisis` (paraguas) `#TiposCrisis` `#Anomia`
`#ComportamientosCrisis` `#TiempoEnCrisis`

> Convención: `- **Pn)** enunciado → #TagPrincipal #TagSecundario`. Los paraguas `#Poder`,
> `#Delegacion`, `#Planeamiento`, `#CincoFuerzas`, `#TableroControl` y `#Crisis` van SIEMPRE
> junto al tag específico, para poder contar el bloque entero con un solo grep. Enunciados
> copiados tal cual del compilado (errores de tipeo corregidos, redacción intacta). «≈» marca
> una lectura dudosa.

---

## 2012-06-25  ·  compilado docx («2do Parcial 25-06-2012»)  ·  Tema A  ·  (4 de 5 registradas)

- **P1)** En el ejercicio del Poder, varios autores coinciden en que el mismo proviene de diversas fuentes. Describa las fuentes de poder vistas en la materia. ✅ resp. (recompensa, coerción, legítimo, referencia, experto) **[RECICLADO]** → #FuentesPoder #Poder
- **P2)** ¿Cuáles son los tipos básicos de Descentralización vistos en clase? Describa las ventajas que suelen atribuirse a la Descentralización. ✅ resp. (vertical / horizontal + 9 ventajas) **[RECICLADO]** → #TiposDescentralizacion #Delegacion
- **P3)** Entre las fuerzas que se analizan en el Modelo de las 5 Fuerzas de Porter se encuentra "La Intensidad de la Rivalidad". Describa qué factores se analizan dentro de esta fuerza en particular. ✅ resp. (crecimiento de la industria, costos fijos, diferenciación, concentración, identidad de marca, barreras de salida) → #Rivalidad #CincoFuerzas
- **P4)** Desarrolle el concepto básico de Moral. ✅ resp. (costumbres → normas; origen: usos y costumbres, tradición, ley) **[RECICLADO]** → #Moral

## 2012-06-25  ·  compilado docx («Tema B»)  ·  Tema B  ·  (4 de 5 registradas)

- **P1)** Dentro de la organización hay tres formas básicas de expresar el poder. Desarrolle cada una de ellas. ✅ resp. (descendente / ascendente / lateral) **[RECICLADO]** → #FormasExpresionPoder #Poder
- **P2)** En toda organización existen una serie de factores que condicionan o promueven la delegación. A estos se los denomina "Factores de contingencia en la Delegación". Mencione y describa los mismos. ✅ resp. (tamaño, importancia de la decisión, complejidad de la tarea, cultura, cualidades de los subordinados) **[RECICLADO]** → #FactoresContingentesDelegacion #Delegacion
- **P3)** Una de las herramientas utilizadas en las organizaciones es la matriz BCG. ¿Para qué sirve esta herramienta? ¿En qué consiste? ¿Cómo se utiliza o qué representa cada caso analizado? ✅ resp. (participación relativa, tasa de crecimiento; estrellas / vacas lecheras / dilemas / pesos muertos) **[RECICLADO]** → #BCG
- **P4)** Desarrolle el concepto básico de "Ética". ✅ resp. (reflexión del individuo sobre los valores; atributos) **[RECICLADO]** → #Etica

## 2014-06-24  ·  compilado docx («Parcial Texido 24/06/2014», Tema 2)  ·  Tema 2  ·  (3 de 5 registradas)

- **P1)** Explique en qué consiste una organización centralizada. ✅ resp. **[RECICLADO]** → #Centralizacion #Delegacion
- **P3)** Cadena de valor de Porter. ¿Se usa para el análisis del ambiente interno o externo? Explique. ✅ resp. (interno; 5 primarias + 4 de apoyo) **[RECICLADO]** → #CadenaValor
- **P5)** Mencione las características de la anomia. ✅ resp. (ausencia de normas; debilitamiento de los elementos reguladores; incongruencia entre lo estructural y las prácticas) → #Anomia #Crisis

## 2014-06-24  ·  compilado docx («Tema 3»)  ·  Tema 3  ·  (2 de 5 registradas)

> ⚠ «Tema 3» aparece en el docx a continuación del Tema 2 del 24/06/2014 sin fecha propia; se
> asume de la misma instancia.

- **P1)** Describir el proceso de influencia en la organización. ✅ resp. (uno o más individuos inducen a otros a hacer algo distinto de lo habitual) **[RECICLADO]** → #Influencia #Poder
- **P3)** Tipos de crisis y motivos por los que se generan. ✅ resp. (Suárez: sucesión, imagen, productos tóxicos, obsolescencia tecnológica, catástrofes, pérdida de competitividad) **[RECICLADO]** → #TiposCrisis #Crisis

## 2014-11-06  ·  compilado docx («2° Parcial 6/11/14»)  ·  (4 de 5 registradas)

- **P1)** Características del mobbing. ✅ resp. (hostigamiento psicológico sistemático, ≥1 vez por semana, >6 meses) **[RECICLADO]** → #Mobbing
- **P3)** Recomendaciones para mejorar la delegación. ✅ resp. (predisposición, qué delegar, elegir la persona, comunicar responsabilidades, conceder autoridad, ayuda, monitorear, evaluar) → #MejorarDelegacion #Delegacion
- **P4)** Comportamientos en situaciones de crisis. ✅ resp. (conformismo / innovación / ritualismo / escapismo) **[RECICLADO]** → #ComportamientosCrisis #Crisis
- **P5)** Estrategias de crecimiento. ✅ resp. (penetración de mercado, desarrollo de mercado, desarrollo de producto, diversificación) **[RECICLADO]** → #EstrategiasCrecimiento

## 2014-11-10  ·  compilado docx («2° Parcial Texido 10/11/14») ≡ juego E del `.md`  ·  (5 de 5)

> Única hoja completa del docx. El juego E del `sin-fecha_compilado-preguntas.md` es la misma
> hoja, palabra por palabra (incluido el «según la definición de no sé qué autor»).

- **P1)** Está evaluando una matriz BCG, con una línea de producto "Estrella" y una línea de producto "Vaca Lechera", y viendo sus utilidades. ¿La utilidad de cuál de ellas invertiría? Justifique. ✅ resp. **[RECICLADO]** → #BCG
- **P2)** Definición técnica de productos sustitutos. ¿Qué implican en la práctica? ✅ resp. (ponen techo a la rentabilidad de la industria) **[RECICLADO]** → #Sustitutos #CincoFuerzas
- **P3)** Explique el poder de coerción. ✅ resp. **[RECICLADO]** → #FuentesPoder #Poder
- **P4)** Factores contingentes de la delegación. ✅ resp. **[RECICLADO]** (idéntica a la P2 del 2012-06-25 B) → #FactoresContingentesDelegacion #Delegacion
- **P5)** Características del planeamiento estratégico (según la definición de no sé qué autor). ✅ resp. (la respuesta desarrolla los 3 niveles: operativo / táctico / estratégico) **[RECICLADO]** → #PlaneamientoEstrategico #NivelesPlaneamiento #Planeamiento

## 2015-11-05  ·  compilado docx («2do Parcial 05-11-2015 Gastón Paccor», Tema 1)  ·  Tema 1  ·  (3 de 5 registradas)

- **P3)** ¿Qué es RSE? ✅ resp. (contribución activa y voluntaria al mejoramiento social, económico y ambiental) → #RSE
- **P4)** Según las fuerzas de Porter, ¿qué pasa si aumentan los proveedores? ✅ resp. (poder de negociación de los proveedores) → #Proveedores #CincoFuerzas
- **P5)** ¿Qué son las perspectivas de un tablero de control? ✅ resp. (cliente, económico-financiera, procesos internos, innovación y aprendizaje) → #PerspectivasTablero #TableroControl

## 2015-11-05  ·  compilado docx («2do Parcial 05-11-2015 Gastón Paccor», Tema 2)  ·  Tema 2  ·  (2 de 5 registradas)

- **P4)** En el modelo de las 5 fuerzas de Porter, ¿qué ocurre si aumenta la cantidad de compradores? ✅ resp. (palanca negociadora + sensibilidad al precio) → #Compradores #CincoFuerzas
- **P5)** Tipos de tableros de control. Explique. ✅ resp. (operativo / directivo / estratégico / integral) → #TiposTablero #TableroControl

## 2015-11-09  ·  compilado docx («2do parcial Daniel Texido 09/11/2015», Tema 2) + juego C del `.md`  ·  Tema 2  ·  (5 de 5)

> El docx trae solo P2–P4 con respuesta; el juego C del `sin-fecha_compilado-preguntas.md`
> tiene exactamente esas tres preguntas con la misma redacción más P1 y P5: es la hoja completa.

- **P1)** Dentro de las estrategias de crecimiento, decir la diferencia entre Penetración de Mercado y Desarrollo de Mercado. **[RECICLADO]** → #EstrategiasCrecimiento
- **P2)** ¿Por qué se dice que la ética nada tiene que ver con "seguir órdenes"? ✅ resp. (respuesta floja en el compilado: una línea) **[RECICLADO]** → #Etica
- **P3)** ¿Cómo funciona la Cadena de Valor? ¿Para qué sirve? ✅ resp. (factores internos → ventaja competitiva sostenible; 5 primarias + 4 de apoyo) **[RECICLADO]** → #CadenaValor
- **P4)** Diferencia entre Poder de Referente y Poder de Experto. ✅ resp. **[RECICLADO]** → #FuentesPoder #Poder
- **P5)** Defina ampliamente moral. Fuentes y ejemplos. **[RECICLADO]** → #Moral

## 2016-11-14  ·  compilado docx («2do Parcial 14-11-2016 Texido», Tema B)  ·  Tema B  ·  (4 de 5 registradas)

- **P1)** Indique con "V" o "F" la validez de las siguientes afirmaciones: (a) La Autoridad sería el ejercicio de un poder que es acatado por quienes son objetos de él. (b) La influencia es el proceso por el cual uno o más individuos inducen a otro/s a hacer algo distinto de lo que harían habitualmente. ✅ resp. (a: FALSO — esa es la definición de poder; b: VERDADERO) **[RECICLADO]** (único V/F del dataset) → #PoderVsAutoridad #Influencia #Poder
- **P2)** ¿Cuáles son los motivos por los cuales un producto de nuestra cartera pasa de ser una Estrella a Incógnita? ✅ resp. (cae la participación relativa) **[RECICLADO]** → #BCG
- **P3)** Los primeros pasos en la construcción de los escenarios son críticos. ¿En qué consisten estos tres primeros pasos? Describa resumidamente cada uno de los componentes de los mismos. ✅ resp. (tema interno / factores clave / fuerzas directrices; después ranking, matriz de implicancias, indicadores) → #Escenarios
- **P5)** ¿Cuál es la diferencia entre producto competidor y producto sustituto? ¿Qué pasa en el primer caso cuando intentó elevar «≈ o bajar» en demasía el precio de mis productos? ¿Qué pasa en el segundo cuando el mercado intenta elevar el precio? ✅ resp. **[RECICLADO]** → #Sustitutos #CincoFuerzas

## 2018-06-13  ·  compilado docx («K5051 13-06-2018»)  ·  (3 de 5 registradas)

- **P1)** Mencione formas de expresión del acoso psicológico en el trabajo. ✅ resp. (medidas organizacionales, ataques a la pertenencia social, a la vida privada, discriminaciones, agresiones verbales/físicas) **[RECICLADO]** → #Mobbing
- **P3)** Niveles de planeamiento: explicar los distintos horizontes del planeamiento. ✅ resp. (operativo / táctico / estratégico) **[RECICLADO]** → #NivelesPlaneamiento #Planeamiento
- **P5)** Explique las distintas estrategias de supervivencia. ✅ resp. (refuerzo / redespliegue / acción política) → #EstrategiasSupervivencia

## sin fecha (juego A)  ·  `sin-fecha_compilado-preguntas.md` («2do Parcial:»)  ·  (5 de 5)  ·  ⚠ sin pistas de fecha; circula como aporte de foro

- **P1)** Describa el poder legítimo y el poder de coerción. **[RECICLADO]** → #FuentesPoder #Poder
- **P2)** ¿Qué es delegar? ¿En qué se diferencia de la "participación"? **[RECICLADO]** → #ConceptoDelegacion #Delegacion
- **P3)** Definición de ética y moral: ¿qué diferencia existe entre ambas? **[RECICLADO]** → #EticaVsMoral #Etica #Moral
- **P4)** ¿Para qué sirve la Cadena de Valor (de Michael Porter)? Describa las actividades que la componen. **[RECICLADO]** → #CadenaValor
- **P5)** ¿Cuál es la diferencia entre un producto estrella y un producto "vaca lechera"? **[RECICLADO]** → #BCG

## sin fecha (juego B)  ·  `sin-fecha_compilado-preguntas.md`  ·  (5 de 5)  ·  ⚠ sin pistas de fecha; circula como aporte de foro

- **P1)** Formas de expresión del poder. **[RECICLADO]** → #FormasExpresionPoder #Poder
- **P2)** Tipos de descentralización. **[RECICLADO]** → #TiposDescentralizacion #Delegacion
- **P3)** Si la curva de crecimiento de la demanda de un producto se está amesetando, ¿significa que va camino a convertirse en una "vaca lechera" o en un "dilema"? Justificar. **[RECICLADO]** (variante de razonamiento sobre los ejes de la matriz) → #BCG
- **P4)** Tipos de cambios por los que pasan las organizaciones, ¿y cuál de ellos es el que está estrechamente ligado a la estrategia? (compulsivo / imitativo / creador: cap. XIV, no el de crisis) → #TiposCambio #Planeamiento
- **P5)** Comportamientos en situaciones de crisis. **[RECICLADO]** → #ComportamientosCrisis #Crisis

## sin fecha (juego D)  ·  `sin-fecha_compilado-preguntas.md`  ·  (5 de 5)  ·  ⚠ sin pistas de fecha; circula como aporte de foro

- **P1)** Diferencia entre Poder y Autoridad. Dar ejemplos de cada uno. **[RECICLADO]** → #PoderVsAutoridad #Poder
- **P2)** Definición de organización centralizada. Mencionar los tipos de descentralización. **[RECICLADO]** → #Centralizacion #TiposDescentralizacion #Delegacion
- **P3)** Explicar los 3 niveles de planeamiento y sus características. **[RECICLADO]** → #NivelesPlaneamiento #Planeamiento
- **P4)** Explicar el concepto de delegación. ¿Qué se delega? **[RECICLADO]** → #ConceptoDelegacion #Delegacion
- **P5)** Explicar la afirmación "La noción de tiempo se convierte en un factor central en las situaciones de crisis". → #TiempoEnCrisis #Crisis

## sin fecha (foto)  ·  `sin-fecha_Parcial.jpg` (foto de hoja tipeada)  ·  (5 de 5)  ·  ⚠ sin fecha ni docente visibles; es la única hoja que pregunta los modelos de organización (racional burocrático / colectivo de consenso), tema que el libro trata al final del cap. X

- **P1)** Cuando se estudian los distintos modelos de organización, aparecen el Racional Burocrático y el Colectivo de Consenso. Explique las características de cada uno de estos modelos. ¿Es posible que coexistan ambos modelos dentro de una organización? → #ModelosOrganizacion #Poder
- **P2)** Defina el concepto de Moral. ¿Cuáles son sus orígenes? ¿Qué relación existe entre lo moral y lo legal? **[RECICLADO]** (variante: suma la relación con lo legal) → #Moral
- **P3)** Defina Planeamiento Estratégico, no desde la etimología de la frase, sino desde sus características. ¿Cómo se definen los objetivos? **[RECICLADO]** → #PlaneamientoEstrategico #Planeamiento
- **P4)** Cuando definimos la Matriz de Portafolio, o Matriz BCG, ¿qué diferencia hay entre los productos Estrella y los Vaca Lechera? ¿Qué medidas hay que tomar con cada uno de ellos? ¿Por qué hay que tomar dichas medidas? **[RECICLADO]** → #BCG
- **P5)** ¿Cómo definiría Crisis en una organización? ¿Qué afecta? Mencione al menos cuatro situaciones de crisis vistas. **[RECICLADO]** → #TiposCrisis #Crisis

---

## Índice inverso: tema → hojas (para búsqueda rápida)

| Tag | Aparece en |
|---|---|
| `#Poder` (cualquier pregunta del bloque) | 2012-06-25 (A, B), 2014-06-24 (T3), 2014-11-10, 2015-11-09, 2016-11-14, sin-fecha A, B, D, foto — **10 de 15 hojas** |
| `#FuentesPoder` | 2012-06-25 (A), 2014-11-10, 2015-11-09, sin-fecha A |
| `#FormasExpresionPoder` | 2012-06-25 (B), sin-fecha B |
| `#PoderVsAutoridad` | 2016-11-14, sin-fecha D |
| `#Influencia` | 2014-06-24 (T3), 2016-11-14 |
| `#ModelosOrganizacion` | sin-fecha foto |
| `#Delegacion` (cualquier pregunta del bloque) | 2012-06-25 (A, B), 2014-06-24 (T2), 2014-11-06, 2014-11-10, sin-fecha A, B, D — **8 de 15** |
| `#TiposDescentralizacion` | 2012-06-25 (A), sin-fecha B, sin-fecha D |
| `#Centralizacion` | 2014-06-24 (T2), sin-fecha D |
| `#FactoresContingentesDelegacion` | 2012-06-25 (B), 2014-11-10 |
| `#ConceptoDelegacion` | sin-fecha A, sin-fecha D |
| `#MejorarDelegacion` | 2014-11-06 |
| `#BCG` | 2012-06-25 (B), 2014-11-10, 2016-11-14, sin-fecha A, B, foto — **6 de 15** |
| `#CincoFuerzas` (cualquier fuerza) | 2012-06-25 (A), 2014-11-10, 2015-11-05 (T1, T2), 2016-11-14 — **5 de 15** |
| `#Sustitutos` | 2014-11-10, 2016-11-14 |
| `#Rivalidad` | 2012-06-25 (A) |
| `#Proveedores` | 2015-11-05 (T1) |
| `#Compradores` | 2015-11-05 (T2) |
| `#CadenaValor` | 2014-06-24 (T2), 2015-11-09, sin-fecha A |
| `#Crisis` (cualquier pregunta del bloque) | 2014-06-24 (T2, T3), 2014-11-06, sin-fecha B, D, foto — **6 de 15** |
| `#TiposCrisis` | 2014-06-24 (T3), sin-fecha foto |
| `#ComportamientosCrisis` | 2014-11-06, sin-fecha B |
| `#Anomia` | 2014-06-24 (T2) |
| `#TiposCambio` (cap. XIV) | sin-fecha B |
| `#TiempoEnCrisis` | sin-fecha D |
| `#Planeamiento` (niveles, características o tipos de cambio) | 2014-11-10, 2018-06-13, sin-fecha B, D, foto — **5 de 15** |
| `#NivelesPlaneamiento` | 2014-11-10, 2018-06-13, sin-fecha D |
| `#PlaneamientoEstrategico` | 2014-11-10, sin-fecha foto |
| `#Moral` | 2012-06-25 (A), 2015-11-09, sin-fecha A, sin-fecha foto |
| `#Etica` | 2012-06-25 (B), 2015-11-09, sin-fecha A |
| `#EticaVsMoral` | sin-fecha A |
| `#RSE` | 2015-11-05 (T1) |
| `#Mobbing` | 2014-11-06, 2018-06-13 |
| `#EstrategiasCrecimiento` | 2014-11-06, 2015-11-09 |
| `#EstrategiasSupervivencia` | 2018-06-13 |
| `#Escenarios` | 2016-11-14 |
| `#TableroControl` | 2015-11-05 (T1, T2) — solo con Paccor |
| `#PerspectivasTablero` | 2015-11-05 (T1) |
| `#TiposTablero` | 2015-11-05 (T2) |

## Preguntas recicladas (idénticas o casi entre hojas)

- **Matriz BCG** → 2012-06-25 B (completa), 2014-11-10 (¿en cuál invertiría?), 2016-11-14 (estrella → incógnita), sin-fecha A (estrella vs. vaca lechera), sin-fecha B (demanda que se ameseta: ¿vaca o dilema?), sin-fecha foto (estrella vs. vaca + medidas). **(6 veces — el tema más repetido del dataset; casi siempre con una pregunta de razonamiento, no solo definir los cuadrantes)**
- **Fuentes de poder** (las 5, o un par a comparar) → 2012-06-25 A (todas), 2014-11-10 (coerción), 2015-11-09 (referente vs. experto), sin-fecha A (legítimo y coerción). **(4 veces)**
- **Moral: definición, orígenes/fuentes** → 2012-06-25 A, 2015-11-09, sin-fecha A (vs. ética), sin-fecha foto (+ relación con lo legal). **(4 veces)**
- **Ética** → 2012-06-25 B (definición), 2015-11-09 ("nada tiene que ver con seguir órdenes"), sin-fecha A (vs. moral). **(3 veces)**
- **Tipos de descentralización** (+ ventajas, o + organización centralizada) → 2012-06-25 A, sin-fecha B, sin-fecha D. **(3 veces)**; **organización centralizada** → 2014-06-24 T2, sin-fecha D.
- **Cadena de valor: para qué sirve + actividades** → 2014-06-24 T2 (¿interno o externo?), 2015-11-09, sin-fecha A. **(3 veces)**
- **Niveles de planeamiento** → 2014-11-10 (como respuesta a "características del planeamiento estratégico"), 2018-06-13 (horizontes), sin-fecha D. **(3 veces)**; **características del planeamiento estratégico** → 2014-11-10, sin-fecha foto (+ cómo se definen los objetivos).
- **Factores contingentes de la delegación** → 2012-06-25 B, 2014-11-10 (misma pregunta, misma respuesta). **(2 veces)**
- **Qué es delegar / qué se delega** → sin-fecha A (vs. participación), sin-fecha D. **(2 veces)**
- **Formas de expresión del poder** (descendente / ascendente / lateral) → 2012-06-25 B, sin-fecha B. **(2 veces)**
- **Poder vs. autoridad** → 2016-11-14 (V/F), sin-fecha D (con ejemplos). **(2 veces)**; **influencia** → 2014-06-24 T3, 2016-11-14.
- **Productos sustitutos** (definición técnica / vs. competidor) → 2014-11-10, 2016-11-14. **(2 veces)**
- **Tipos de crisis** → 2014-06-24 T3, sin-fecha foto (definición + qué afecta + 4 situaciones). **(2 veces)**; **comportamientos en crisis** → 2014-11-06, sin-fecha B. **(2 veces)**
- **Mobbing** → 2014-11-06 (características), 2018-06-13 (formas de expresión del acoso). **(2 veces)**
- **Estrategias de crecimiento** → 2014-11-06 (las 4), 2015-11-09 (penetración vs. desarrollo de mercado). **(2 veces)**

## Equivalencias (mismo examen, no practicar dos veces)

- Juego **C** del `.md` ≡ 2015-11-09 Tema 2 del docx (el `.md` es la versión completa, 5 preguntas).
- Juego **E** del `.md` ≡ 2014-11-10 del docx (idéntica, palabra por palabra).
- Los juegos **A, B y D** del `.md` son los mismos tres juegos que circulan como **aportes de foro** sobre el 2P (pegados el 2026-11-09): no se agregan de nuevo.
- 2012-06-25 Tema A y Tema B, 2014-06-24 Tema 2 y Tema 3, y 2015-11-05 Tema 1 y Tema 2 son
  pares de la misma instancia: **15 hojas = 12 instancias**.

## Fuera de dataset

- _(nada: los tres archivos de la carpeta son del segundo parcial)_

---

*Índice generado el 2026-11-09 a partir de la lectura del texto del docx (extraído con
Python desde el XML), del `.md` y de la foto (con visión) — 3 archivos, 15 hojas de examen
de 12 instancias. Las hojas del compilado son transcripciones de alumnos: suelen faltar
preguntas (se anota cuántas hay) y las fechas y páginas son las que ellos escribieron (las
páginas corresponden a una edición vieja del libro, no al PDF 2026).*
