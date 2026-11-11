<!--
Fuente del TP. NO es el entregable: `armar_tp.py` lo combina con ajuste/reporte.md (punto c)
y borrador-d.md (punto d) y genera exports/tp-silksong.md + .html + .pdf.
Marcadores: {{MODELOS}} y {{PUNTO_D}}. Lo marcado [a completar] lo completa el grupo.
-->

# ¿Cuántos jugadores le quedan a Hollow Knight: Silksong?

## Aproximación discreta por mínimos cuadrados

| | |
|---|---|
| **Universidad** | Universidad Tecnológica Nacional — Facultad Regional Buenos Aires |
| **Materia** | Análisis Numérico |
| **Trabajo** | Trabajo Práctico — 2.º cuatrimestre 2026 |
| **Curso** | [a completar] |
| **Docente** | [a completar] |
| **Integrantes** | [a completar: nombre y legajo de cada integrante] |
| **Fecha de entrega** | [a completar] |

---

## a) El problema

### Contexto

*Hollow Knight: Silksong*, del estudio australiano Team Cherry, es la secuela de *Hollow
Knight* y uno de los juegos independientes más esperados de los últimos años: se anunció en
2019 y salió recién el **4 de septiembre de 2025**. En sus primeros tres meses vendió más de
7 millones de copias.

Como pasa con casi todos los lanzamientos grandes, la cantidad de gente jugando al mismo
tiempo explota el primer mes y después baja: los jugadores lo terminan, lo dejan o pasan a
otro juego. Esa caída no es pareja: es muy fuerte al principio y cada vez más lenta.

### ¿Para qué sirve predecirlo?

Para un estudio, saber **cuántos jugadores va a tener si no hace nada** sirve para decidir
**cuándo** conviene sacar una oferta, una actualización o una expansión que reactive el
juego, y para dimensionar servidores, soporte y comunidad. No es un caso hipotético: Team
Cherry anunció para 2026 *Sea of Sorrow*, una expansión gratuita de Silksong.

### Los datos

Usamos los datos públicos de **SteamCharts**, que registra cuántos jugadores tiene abierto
cada juego en Steam en todo momento. Para cada mes tomamos el **promedio de jugadores
simultáneos** (*Avg. Players*): no es la cantidad total de personas que jugaron, sino
cuántas, en promedio, estaban jugando al mismo tiempo. Datos descargados el 11 de noviembre
de 2026.

- $x$ = mes desde el lanzamiento (1 = septiembre 2025, …, 14 = octubre 2026). Empezamos en
  1 y no en 0 porque los modelos potencial y recíproco usan $\ln x$ y $1/x$.
- $y$ = jugadores simultáneos promedio en ese mes (redondeado al entero).

| Mes | $x$ | $y$ |
|---|:---:|---:|
| Septiembre 2025 | 1 | 191.124 |
| Octubre 2025 | 2 | 58.328 |
| Noviembre 2025 | 3 | 23.721 |
| Diciembre 2025 | 4 | 17.001 |
| Enero 2026 | 5 | 16.126 |
| Febrero 2026 | 6 | 10.613 |
| Marzo 2026 | 7 | 8.269 |
| Abril 2026 | 8 | 7.515 |
| Mayo 2026 | 9 | 6.967 |
| Junio 2026 | 10 | 7.111 |
| Julio 2026 | 11 | 8.619 |
| Agosto 2026 | 12 | 7.972 |
| Septiembre 2026 | 13 | 7.116 |
| Octubre 2026 | 14 | 6.108 |

### Lo que queremos saber

**¿Cuántos jugadores simultáneos promedio va a tener Silksong en noviembre de 2026**, es
decir, en $x = 15$? Es un valor que todavía no existe: el mes está en curso.

## b) Nube de puntos

![Nube de puntos: jugadores simultáneos promedio por mes](ajuste/nube.png)

Lo que se ve:

- **Caída muy fuerte al principio:** del mes 1 al 2 se fue el 69 % de los jugadores, y del 2
  al 3 otro 59 %.
- **Después se frena:** del mes 7 en adelante los valores quedan entre 6.000 y 9.000
  jugadores, con una cola que baja muy despacio.
- **Un salto en julio de 2026** (mes 11), que sube de 7.111 a 8.619 sin que la tendencia lo
  explique. [a completar: causa]

La forma (decreciente, cada vez más lenta y siempre positiva) sugiere que una recta no va a
alcanzar y que conviene probar modelos no lineales.

## c) Ajuste de los modelos

Ajustamos **seis modelos** a los mismos 14 puntos: dos polinómicos (recta y parábola) y
cuatro no polinómicos (exponencial, potencial, recíproco e hiperbólico). Para los no
polinómicos primero llevamos el modelo a una **forma aparentemente lineal** con un cambio
de variables, resolvemos el sistema de ecuaciones normales de esa recta y después volvemos a
los parámetros originales.

En cada modelo seguimos los mismos pasos: cambio de variables (si hace falta), sistema de
ecuaciones normales, tabla de sumatorias, sistema con los valores, solución, función
aproximante con su gráfico y tabla de residuos con el error cuadrático en las variables
originales.

{{MODELOS}}

## d) Comparación, elección y estimación

{{PUNTO_D}}

## Aplicaciones: ¿qué le espera a GTA VI?

El 19 de noviembre de 2026 sale *Grand Theft Auto VI* (por ahora solo en PlayStation 5 y
Xbox Series, sin fecha confirmada para PC). Su antecesor, *GTA V*, salió en Steam en abril
de 2015, y sus datos públicos muestran lo que nuestro modelo **no** puede prever:

![Silksong y GTA V en Steam, en porcentaje del primer mes](ajuste/silksong-vs-gta-v.png)

- Los primeros meses, GTA V cayó igual que Silksong: de 192.714 jugadores promedio en abril
  de 2015 a 25.388 en septiembre (−87 %).
- **Desde octubre de 2015 volvió a subir**, hasta 46.993 en enero de 2016.
  [a completar: causa, ¿actualizaciones del modo online, ofertas de fin de año?]
- Un ajuste hecho con sus primeros seis meses habría predicho que seguía bajando, y se
  habría equivocado.

**Lo que esto enseña:** el ajuste predice qué pasa **si nada cambia**. Por eso le sirve al
estudio: le muestra la tendencia "natural" del juego para decidir cuándo intervenir. Si
GTA VI recibe actualizaciones como su antecesor, su curva no va a seguir un modelo de
caída; si Team Cherry lanza *Sea of Sorrow*, tampoco la de Silksong.

## Conclusiones

[a completar por el grupo: 3 a 5 líneas. Sugerencia: (1) el método de mínimos cuadrados
permitió estimar unos 4.467 jugadores para noviembre de 2026 con el modelo potencial; (2)
el modelo de menor error no siempre es el mejor para predecir: hay que mirar si tiene
sentido con el fenómeno; (3) la estimación es un piso: los residuos y la prueba con los
meses 12 a 14 indican que el valor real probablemente sea mayor; (4) el modelo solo vale si
no pasa nada nuevo, como muestra GTA V.]

## Video

[a completar: link de YouTube o Google Drive]

## Fuentes

- SteamCharts, *Hollow Knight: Silksong* (app 1030300): <https://steamcharts.com/app/1030300>
  (consultado el 2026-11-11).
- SteamCharts, *Grand Theft Auto V Legacy* (app 271590):
  <https://steamcharts.com/app/271590> (consultado el 2026-11-11).
- Gematsu, "Hollow Knight: Silksong sales top seven million; free expansion Sea of Sorrow
  announced" (diciembre 2025).
- Fecha de lanzamiento de GTA VI (19/11/2026, PS5 y Xbox Series): [a completar con la fuente
  oficial de Rockstar Games].
- Cátedra de Análisis Numérico, clases teórica y práctica de aproximación discreta por
  mínimos cuadrados (2.º cuatrimestre 2026).
