# Guion del video — TP Silksong

> Fuente: consigna del TP (`../enunciado.md`) y el TP armado (`exports/tp-silksong.pdf`).

---

## Lo que pide la consigna (y cómo lo cubrimos)

- **Duración: 4 a 6 minutos** (vale el 20 % del video). Apuntamos a **unos 5:10**, con margen
  para pausas y cambios de pantalla: pasarse de 6:00 resta.
- **Contenido:** cómo y por qué elegimos el problema, breve descripción, los cálculos y las
  conclusiones.
- **Todos los integrantes en cámara**, al menos en una parte. Lo cubrimos dos veces: todos
  juntos en la apertura y el cierre, y cada uno con su cara en un recuadro mientras habla.
- **"Explicaciones concisas y claras" vale el 50 %.** Por eso no se leen tablas ni se
  resuelven sistemas en cámara: se muestran en pantalla y se dice qué significan.

## Qué explicar bien y qué pasar rápido

| Explicar bien (es lo que se evalúa) | Pasar rápido o solo mostrar |
|---|---|
| Por qué elegimos el caso y qué es $y$ (jugadores **simultáneos**, no totales) | La tabla de los 14 meses: se muestra, no se lee |
| El "disfraz" del potencial: tomar logaritmo y llegar a una recta | Las tablas de sumatorias y los números del sistema: se muestran 3 segundos |
| Volver de $A_0$ a $a_0$ (el error típico de la unidad) | La resolución del sistema: "lo resolvimos con calculadora" |
| **El recíproco tiene el menor error y predice jugadores negativos** (la idea central) | El desarrollo del exponencial y del recíproco: solo el cambio de variable y el resultado |
| Por qué elegimos el potencial y la estimación de 4.467 | Las tablas de residuos completas |
| La confiabilidad: el modelo se queda corto y el rango 5.600–6.000 | Las fuentes, las fechas de la oferta de Steam, el mes de julio |
| La conclusión: el menor error no alcanza, el modelo tiene que tener sentido | GTA V: 15 segundos, como cierre |

## Reparto y tiempos

| Bloque | Quién | Tiempo | Tema | En pantalla |
|---|---|---|---|---|
| 0 | Todos | 0:00–0:12 | Saludo | Los 5 en cámara |
| 1 | Persona 1 | 0:12–1:15 | El problema, los datos y la nube | Tabla de datos, `nube.png` |
| 2 | Persona 2 | 1:15–2:20 | El método con el potencial, paso a paso | Paso 1 del potencial, tabla de sumatorias, `modelo-potencial-doble.png` |
| 3 | Persona 3 | 2:20–3:05 | Exponencial y recíproco | `modelo-exponencial-doble.png`, `modelo-reciproco-doble.png` |
| 4 | Persona 4 | 3:05–4:05 | Comparación, elección y estimación | Tabla d.1, `comparacion-cola.png`, fórmula de $\hat y(15)$ |
| 5 | Persona 5 | 4:05–5:05 | Confiabilidad, GTA V y conclusión | Tabla de residuos, tabla de validación, `silksong-vs-gta-v.png` |
| 6 | Todos | 5:05–5:10 | Cierre | Los 5 en cámara |

Los tiempos están calculados a unas 150 palabras por minuto (ritmo de charla tranquila). Si
en el ensayo alguien se pasa, recortar lo marcado como **[recortable]**.

---

## Bloque 0 — Apertura (todos, ~12 s)

> *Los cinco en cámara (grilla de la videollamada o juntos).*

**Cada uno dice su nombre, en orden:** "Juan Cruz", "Bautista", "Tomás", "Agustin",
"Luciano".

**Persona 1:** Somos del curso K3572 y este es nuestro trabajo de aproximación por mínimos
cuadrados.

## Bloque 1 — El problema y los datos (Persona 1, ~65 s)

> *En pantalla: primero la cara; después la tabla de datos y la nube de puntos.*

El 19 de noviembre sale GTA VI, uno de los juegos más esperados de todos los tiempos. Y con
los lanzamientos grandes pasa siempre lo mismo: el primer mes explotan de jugadores y después
la gente los va dejando. Nos preguntamos si se puede predecir cuántos jugadores le quedan a
un juego.

Como GTA VI todavía no salió, y no sale en PC, elegimos otro lanzamiento enorme y reciente:
**Hollow Knight: Silksong**, de septiembre de 2025.

Los datos son de **SteamCharts**, una página pública que registra cuánta gente juega cada
juego en Steam. Para cada mes tomamos el **promedio de jugadores simultáneos**: no cuántos lo
jugaron, sino cuántos estaban jugando al mismo tiempo. Tenemos 14 meses y queremos estimar
el 15: **noviembre de 2026**, que todavía no terminó.

En la nube se ve la forma: una caída enorme al principio (del primer al segundo mes se fue
el 69 % de los jugadores) y después una cola que baja muy despacio. Por eso probamos modelos
que caen y se van frenando.

## Bloque 2 — El método, con el potencial (Persona 2, ~65 s)

> *En pantalla: el Paso 1 del potencial ($y = a_0 x^{a_1} \Rightarrow \ln y = \ln a_0 + a_1
> \ln x \Rightarrow Y = A_0 + a_1 X$), después la tabla de sumatorias y el sistema, y al final
> el gráfico del modelo. Las fórmulas están escritas como se dicen.*

Probamos tres modelos: exponencial, potencial y recíproco. Ninguno es una recta, así que el
truco de la unidad es **disfrazarlos de recta**. Lo muestro con el potencial, que es el que
elegimos: "y igual a a-cero por x a la a-uno".

Aplicamos logaritmo natural a los dos lados y renombramos: logaritmo de y pasa a ser "Y
mayúscula", logaritmo de x pasa a ser "X mayúscula", y logaritmo de a-cero, "A-cero". Queda
una recta: "Y igual a A-cero más a-uno X".

Desde ahí es mínimos cuadrados de una recta común: la tabla con las sumatorias de los 14
meses, el sistema de ecuaciones normales, y lo resolvemos con calculadora.

Pero ojo con el último paso: **A-cero no es a-cero**. Hay que volver: a-cero es "e a la
A-cero", que da 122.134. La función queda "y igual a 122.134 por x a la menos 1,22".

## Bloque 3 — Exponencial y recíproco (Persona 3, ~45 s)

> *En pantalla: el gráfico del exponencial y después el del recíproco, con su función.*

Los otros dos modelos siguen la misma receta, cambiando el disfraz.

En el **exponencial**, "y igual a a-cero por e a la a-uno x", tomamos logaritmo solo de y, y
la recta queda en x y logaritmo de y. Nos dio "57.750 por e a la menos 0,19 x".

En el **recíproco**, "y igual a a-cero más a-uno sobre x", no hace falta logaritmo: alcanza
con llamar X a "uno sobre x". Como y no cambia, los coeficientes salen directos, sin volver.
Nos dio "menos 17.246 más 190.072 sobre x".

**[recortable]** En el PDF están, para los tres modelos, la tabla de sumatorias, el sistema y la tabla de
residuos completa.

## Bloque 4 — Comparación, elección y estimación (Persona 4, ~60 s)

> *En pantalla: la tabla comparativa del d.1; después el gráfico de los tres modelos con
> zoom; al final la cuenta $\hat y(15) = 122.134 \cdot 15^{-1{,}22} \approx 4.467$.*

¿Cuál es el mejor? El criterio de la cátedra es el **error cuadrático**: cuánto se alejan,
al cuadrado, los datos reales de lo que predice cada modelo.

Y acá está lo más interesante del trabajo: el de **menor error es el recíproco**. Pero miren
qué predice para noviembre: **menos 4.574 jugadores**. Desde el mes 12 da negativos, cuando
ese mes había casi 8.000. Tiene poco error porque copia muy bien el primer mes, que con
191 mil jugadores pesa más que todo el resto junto.

Entonces elegimos en dos pasos: descartamos lo que no tiene sentido con el fenómeno y, entre
lo que queda, el de menor error. Entre exponencial y potencial, el **potencial** tiene un
error cuatro veces menor y describe mejor la forma: cada mes se va un porcentaje más chico
de jugadores.

Reemplazando x igual a 15: **unos 4.467 jugadores para noviembre**.

## Bloque 5 — Confiabilidad, GTA V y conclusión (Persona 5, ~60 s)

> *En pantalla: la tabla de residuos de los meses 11 a 14, la tabla de validación y al final
> el gráfico de Silksong contra GTA V.*

¿Es confiable? A favor: predecimos un solo mes hacia adelante. En contra: en los últimos
cuatro meses los datos reales quedaron entre un 20 y un 26 % **por encima** del modelo.
**[recortable]** Y cuando ajustamos solo con los primeros 11 meses para predecir los tres siguientes, que
ya conocíamos, también se quedó corto.

Si el patrón sigue, noviembre debería estar **entre 5.600 y 6.000 jugadores**, y SteamCharts
da 5.702 en los últimos 30 días: justo en el rango. El dato completo sale el 1 de diciembre.

Además, el modelo supone que no pasa nada nuevo. GTA V en Steam cayó igual que Silksong al
principio, pero las actualizaciones del modo online lo hicieron subir de nuevo. Por eso le
sirve a un estudio: le muestra qué pasa si no hace nada, para decidir cuándo sacar una
oferta o una expansión.

En resumen: **el menor error no alcanza; el modelo tiene que tener sentido**.

## Bloque 6 — Cierre (todos, ~5 s)

> *Los cinco en cámara.*

**Todos:** ¡Gracias!

---

## Producción

- **Cómo grabar:** lo más simple es una videollamada (Meet o Zoom) grabada, con la pantalla
  compartida mostrando los gráficos y la cámara del que habla visible en un recuadro. Así
  cada uno aparece en cámara en su bloque, que es lo que pide la consigna.
- **Grabar por bloques** y unirlos después es más fácil que hacerlo de una: si alguien se
  traba, se repite solo su parte.
- **Audio** (vale el 20 % junto con la imagen): cada uno en un lugar silencioso, con
  auriculares con micrófono. Probar el audio antes.
- **Pantalla:** los gráficos están en `caso-silksong/ajuste/` y las tablas se pueden
  capturar del PDF. Conviene armar unas pocas diapositivas con eso, una por momento del
  guion, en vez de scrollear el PDF en vivo.
- **Ensayar con cronómetro.** Si da más de 5:45, sacar lo marcado como **[recortable]** (unos 15 s).
  Si da menos de 4:30, hablar más despacio: también hay mínimo.
- **Subirlo** a YouTube como "no listado" o a Google Drive con acceso para "cualquier persona
  con el enlace". Probar el link en una ventana de incógnito antes de pegarlo al final del
  PDF.

---

_Generado el 2026-11-12. Fuentes: `../enunciado.md` (consigna y grilla del video),
`exports/tp-silksong.pdf` (resultados), `ajuste/` (gráficos)._
