# Guion del video — TP Silksong

> Fuente: consigna del TP (`../enunciado.md`) y el TP armado (`exports/tp-silksong.pdf`).

---

## Lo que pide la consigna (y cómo lo cubrimos)

- **Duración: 4 a 6 minutos** (vale el 20 % del video). Apuntamos a **unos 5:20**, con margen
  para pausas y cambios de pantalla: pasarse de 6:00 resta.
- **Contenido:** cómo y por qué elegimos el problema, breve descripción, los cálculos y las
  conclusiones.
- **Todos los integrantes en cámara**, al menos en una parte. Lo cubrimos con la cara de
  cada uno en un recuadro **durante todo su bloque** (sin saludo grupal: el video arranca
  directo con la introducción).
- **"Explicaciones concisas y claras" vale el 50 %.** Por eso no se leen tablas ni se
  resuelven sistemas en cámara: se muestran en pantalla y se dice qué significan.

## Qué explicar bien y qué pasar rápido

| Explicar bien (es lo que se evalúa) | Pasar rápido o solo mostrar |
|---|---|
| Cómo elegimos el caso (empezamos por GTA y por qué lo cambiamos) y qué es $y$ (jugadores **simultáneos**, no totales) | La tabla de los 14 meses: se muestra, no se lee |
| El "disfraz" del potencial: tomar logaritmo y llegar a una recta | Las tablas de sumatorias y los números del sistema: se muestran 3 segundos |
| Volver de $A_0$ a $a_0$ (el error típico de la unidad) | La resolución del sistema: en el PDF está con Cramer; en el video, solo "lo resolvemos" |
| **El recíproco tiene el menor error y predice jugadores negativos** (la idea central) | El desarrollo del exponencial y del recíproco: solo el cambio de variable y el resultado |
| Por qué elegimos el potencial y la estimación de 4.467 | Las tablas de residuos completas |
| La confiabilidad: el modelo se queda corto y el rango 5.600–6.000 | Las fuentes, las fechas de la oferta de Steam, el mes de julio |
| La conclusión: el menor error no alcanza, el modelo tiene que tener sentido | La vuelta a GTA V al final: 15 segundos |

## Reparto y tiempos

| Bloque | Quién | Tiempo | Tema | En pantalla |
|---|---|---|---|---|
| 1 | Persona 1 | 0:00–1:25 | Cómo elegimos el caso (de GTA a Silksong), los datos y la nube | `silksong-vs-gta-v.png` (solo la línea de GTA V, o el gráfico entero), tabla de datos, `nube.png` |
| 2 | Persona 2 | 1:25–2:30 | El método con el potencial, paso a paso | Paso 1 del potencial, tabla de sumatorias, `modelo-potencial-doble.png` |
| 3 | Persona 3 | 2:30–3:20 | Exponencial y recíproco | `modelo-exponencial-doble.png`, `modelo-reciproco-doble.png` |
| 4 | Persona 4 | 3:20–4:20 | Comparación, elección y estimación | Tabla d.1, `comparacion-cola.png`, fórmula de $\hat y(15)$ |
| 5 | Persona 5 | 4:20–5:25 | Confiabilidad, GTA V y conclusión | Tabla de residuos, tabla de validación, `silksong-vs-gta-v.png` |

Los tiempos están calculados a unas 150 palabras por minuto (ritmo de charla tranquila). Si
en el ensayo alguien se pasa, recortar lo marcado como **[recortable]**.

---

## Bloque 1 — Cómo elegimos el caso, los datos y la nube (Persona 1, ~85 s)

> *En pantalla: primero la cara; mientras habla de GTA V, el gráfico de Silksong contra
> GTA V; después la tabla de datos y la nube de puntos.*

La idea de este trabajo empezó con **GTA VI**, que sale el 19 de noviembre y es uno de los
juegos más esperados de la historia. Queríamos ver si, ajustando los datos de GTA V en
Steam, podíamos anticipar algo de GTA VI. Pero cuando nos metimos en los datos aparecieron
dos problemas: GTA VI sale solo en consolas, así que no va a tener datos en Steam para
comparar, y la curva de GTA V no es una caída: cada actualización de su modo online la
vuelve a subir. Ningún modelo de caída le servía.

Así que buscamos otro lanzamiento grande y reciente, pero sin modo online: **Hollow Knight:
Silksong**, de septiembre de 2025.

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
meses, el sistema de ecuaciones normales, y lo resolvemos.

Pero ojo con el último paso: **A-cero no es a-cero**. Hay que volver: a-cero es "e a la
A-cero", que da 122.134. La función queda "y igual a 122.134 por x a la menos 1,22".

## Bloque 3 — Exponencial y recíproco (Persona 3, ~50 s)

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

## Bloque 5 — Confiabilidad, GTA V y conclusión (Persona 5, ~65 s)

> *En pantalla: la tabla de residuos de los meses 11 a 14, la tabla de validación y al final
> el gráfico de Silksong contra GTA V.*

¿Es confiable? A favor: predecimos un solo mes hacia adelante. En contra: en los últimos
cuatro meses los datos reales quedaron entre un 20 y un 26 % **por encima** del modelo.
**[recortable]** Y cuando ajustamos solo con los primeros 11 meses para predecir los tres siguientes, que
ya conocíamos, también se quedó corto.

Si el patrón sigue, noviembre debería estar **entre 5.600 y 6.000 jugadores**, y SteamCharts
da 5.702 en los últimos 30 días: justo en el rango. El dato completo sale el 1 de diciembre.

Además, el modelo supone que no pasa nada nuevo, y eso nos devuelve al principio: GTA V
cayó igual que Silksong los primeros meses, pero las actualizaciones del modo online lo
hicieron subir de nuevo. Por eso esto le sirve a un estudio: le muestra qué pasa si no hace nada, para decidir cuándo sacar una
oferta o una expansión.

En resumen: **el menor error no alcanza; el modelo tiene que tener sentido**. Gracias.

---

## Producción: cada uno graba su parte y se edita

**Cada uno graba solo su cara hablando; el que edita pone las diapositivas.** Nadie
comparte pantalla. En la edición, la diapositiva va de fondo y la cara del que habla en un
recuadro en una esquina, así cada uno queda en cámara durante todo su bloque, que es lo que
pide la consigna. Así todos los bloques se ven iguales, aunque cada uno grabe con otra
compu, y los cambios de pantalla siguen el guion (las indicaciones *En pantalla* de cada
bloque son para el que edita).

**Lo que tiene que respetar cada uno al grabar** (si no, los cortes se notan):

1. **Horizontal**, con la cámara a la altura de los ojos, la cara centrada y luz de frente
   (una ventana o una lámpara delante, nunca detrás). La compu o el celu sirven.
2. **Lugar silencioso y auriculares con micrófono.** El audio vale el 20 % junto con la
   imagen, y un audio malo entre cuatro buenos se nota mucho. Escuchar la grabación antes
   de mandarla.
3. **Dos segundos callado** antes de empezar y al terminar: el que edita corta ahí.
4. **Respetar el tiempo del bloque** (tabla de reparto), con cronómetro. Pasarse 10 s está
   bien; 30 s, no: el total no puede pasar de 6:00.
5. **Decir el texto con palabras propias**, sin leerlo de la pantalla con la vista
   corrida. Se puede grabar en partes (un párrafo por toma) y el que edita las une.
6. **Mandar el archivo** como `bloque-N-apellido.mp4` a la carpeta compartida, con una
   fecha límite que dé al menos dos días para editar.

**El que edita:**

- Arma las diapositivas antes de que lleguen los videos (los gráficos están en
  `caso-silksong/ajuste/` y las tablas se capturan del PDF), una por cada indicación
  *En pantalla* del guion.
- Une los cinco bloques sin transiciones vistosas (un corte directo o un fundido corto),
  iguala el volumen entre bloques y revisa que el total quede entre 4:30 y 6:00. Si se pasa,
  primero saca lo marcado como **[recortable]** (unos 15 s).
- Antes de subirlo, el grupo mira el video completo una vez para chequear números y
  nombres contra el PDF.

**Subirlo** a YouTube como "no listado" o a Google Drive con acceso para "cualquier persona
con el enlace". Probar el link en una ventana de incógnito antes de pegarlo al final del
PDF.

---

_Generado el 2026-11-12 (actualizado: sin saludo grupal, introducción con la historia de GTA;
2026-11-13: cada uno graba su parte por separado y se edita). Fuentes: `../enunciado.md` (consigna y grilla del video),
`exports/tp-silksong.pdf` (resultados), `ajuste/` (gráficos)._
