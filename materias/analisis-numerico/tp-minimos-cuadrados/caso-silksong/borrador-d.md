# Borrador del punto d) — Comparación, elección y estimación

> Fuente: `ajuste/resultados.json` (meses 1–14) y `validacion/resultados.json` (ajuste con los meses 1–11); criterios de la teórica y la práctica de ajuste (apuntes 01 y 02 de `segundo-parcial/`).

---

> **Notas para el grupo (no van al PDF).** El texto de abajo está escrito para pegar en el
> TP. Lo marcado `[a completar]` depende de algo que todavía no sabemos. Los números salen
> de `ajuste_mc.py` y se pueden verificar en `ajuste/reporte.md`.

## d.1 Comparación de los seis modelos

Para comparar usamos el **error cuadrático** de cada función final, calculado en las
variables originales (jugadores, no logaritmos ni inversas):

$$
E = \sum_{i=1}^{14} \left( y_i - \hat y_i \right)^2
$$

| Modelo | Función aproximante | $E$ | $\hat y(15)$ |
|---|---|---:|---:|
| Recíproco | $y = -17245{,}71 + \dfrac{190071{,}71}{x}$ | $1{,}82 \times 10^{9}$ | $-4.574$ |
| Potencial | $y = 122134{,}87\,x^{-1{,}22172}$ | $4{,}93 \times 10^{9}$ | $4.467$ |
| Parábola | $y = 153387{,}92 - 34583{,}52\,x + 1832{,}93\,x^2$ | $1{,}03 \times 10^{10}$ | $47.045$ |
| Recta | $y = 80070{,}53 - 7089{,}50\,x$ | $2{,}00 \times 10^{10}$ | $-26.272$ |
| Exponencial | $y = 57750{,}06\,e^{-0{,}19324\,x}$ | $2{,}13 \times 10^{10}$ | $3.182$ |
| Hiperbólico | $y = \dfrac{88855{,}72}{1{,}15366 + x}$ | $2{,}34 \times 10^{10}$ | $5.501$ |

![Los seis modelos en la zona de la predicción (meses 3 a 15)](ajuste/comparacion-cola.png)

## d.2 Criterio de elección

Si miráramos solo el error, el mejor sería el **recíproco**. Pero el ajuste no se hace para
pasar lo más cerca posible de los puntos: se hace para **predecir valores e interpretar
tendencias**. Por eso un polinomio interpolante, que tiene error cero, no es el mejor
ajuste. Además, si se sabe cómo se comporta el fenómeno, conviene usar un modelo de ese
tipo.

Elegimos en dos pasos:

1. **Descartar los modelos que contradicen el fenómeno.** La cantidad de jugadores no puede
   ser negativa, y un juego no recupera jugadores "solo", sin una actualización, una
   oferta o un evento que lo explique.
2. **Entre los que quedan, elegir el de menor error cuadrático.**

## d.3 Modelos descartados

- **Recíproco** (menor error): la curva corta el eje en $x \approx 11{,}02$. Desde el mes
  12 predice jugadores negativos, cuando el dato real del mes 12 es de 7.972 jugadores.
  Para noviembre da $-4.574$. Su error es bajo porque copia muy bien el pico del
  lanzamiento, pero describe mal justo la zona que queremos predecir.
- **Recta:** predice $-26.272$ jugadores. Además, una caída a ritmo constante no
  representa un fenómeno que cae rápido al principio y cada vez más lento.
- **Parábola:** tiene su mínimo en $x \approx 9{,}43$ con valores negativos y después
  sube, hasta $47.045$ jugadores en noviembre, como si el juego recuperara solo el público
  del segundo mes. Es el mismo problema de usar polinomios para estimar fuera de los
  datos.

## d.4 Elección: el modelo potencial

Quedan tres modelos que tienen sentido (siempre positivos, siempre decrecientes y cada vez
más lentos): exponencial, potencial e hiperbólico. Entre ellos, el **potencial** tiene el
menor error, unas cuatro veces menor que los otros dos:

| Modelo | $E$ |
|---|---:|
| **Potencial** | $\mathbf{4{,}93 \times 10^{9}}$ |
| Exponencial | $2{,}13 \times 10^{10}$ |
| Hiperbólico | $2{,}34 \times 10^{10}$ |

La forma también acompaña. El exponencial supone que cada mes se pierde **el mismo
porcentaje** de jugadores (con $e^{-0{,}19324} \approx 0{,}82$, un 18 % por mes), así que se
acerca rápido a cero. El potencial supone que el porcentaje que se pierde es **cada vez
menor**, que es lo que muestra la nube: del mes 1 al 2 se fue el 69 % de los jugadores, del
3 al 4 el 28 %, y del 8 al 9 solo el 7 %.

## d.5 Estimación para noviembre de 2026

Noviembre de 2026 es el mes $x = 15$:

$$
\hat y(15) = 122134{,}87 \cdot 15^{-1{,}22172} \approx 4.467
$$

**El modelo estima unos 4.467 jugadores simultáneos promedio en noviembre de 2026.**

## d.6 ¿Es confiable?

**A favor:**

- **Extrapolamos un solo mes.** Predecimos fuera del rango de los datos, pero muy cerca
  del último mes (14). Cuanto más lejos, menos confiable sería.
- **Los modelos razonables coinciden en el orden de magnitud.** Exponencial, potencial e
  hiperbólico dan entre 3.182 y 5.501 jugadores. Ninguno da 500 ni 50.000.

**En contra (por qué esperamos que el valor real sea mayor):**

- **Los residuos tienen un patrón.** En los meses 3 a 10 el modelo queda **por encima** de
  los datos, y en los meses 11 a 14 queda **por debajo**: los datos reales superaron al
  modelo entre un 20 % y un 26 %.

  | Mes | Real | Potencial | Diferencia |
  |---:|---:|---:|---:|
  | 11 | 8.619 | 6.525 | +24 % |
  | 12 | 7.972 | 5.867 | +26 % |
  | 13 | 7.116 | 5.320 | +25 % |
  | 14 | 6.108 | 4.860 | +20 % |

  Si ese patrón sigue, noviembre estaría más cerca de **5.600–6.000** jugadores que de
  4.467. El modelo **subestima la cola**: la comunidad que se queda jugando es más grande
  de lo que la curva supone.
- **Lo comprobamos con datos que ya conocíamos.** Ajustamos el potencial solo con los meses
  1 a 11 y predijimos los meses 12 a 14:

  | Mes | Real | Predicción | Error |
  |---:|---:|---:|---:|
  | 12 | 7.972 | 4.787 | −40 % |
  | 13 | 7.116 | 4.291 | −40 % |
  | 14 | 6.108 | 3.878 | −37 % |

  En los tres meses se quedó corto, siempre del mismo lado. Eso confirma que el modelo
  tiende a subestimar.
- **El mes 1 domina el error.** El lanzamiento (191.124 jugadores) es casi treinta veces
  más grande que los últimos meses. Un error chico en ese punto pesa más que todos los
  demás juntos, por eso el ajuste "prioriza" el lanzamiento sobre la cola. Por eso el
  recíproco tiene el menor error y aun así predice mal.
- **El modelo supone que no pasa nada nuevo.** En julio de 2026 (mes 11) los jugadores
  subieron de 7.111 a 8.619 sin que la curva lo explique: `[a completar: causa de la
  subida de julio]`. Team Cherry anunció para 2026 la expansión gratuita *Sea of Sorrow*,
  sin fecha confirmada al 2026-11-11. Si sale en noviembre, la predicción deja de valer.
- **Vale solo para este juego.** Otro juego, con otra reputación, precio y comunidad,
  tendría otros coeficientes. Lo que sí suele repetirse es la forma de la curva.

## d.7 Conclusión

El modelo potencial estima **4.467 jugadores simultáneos promedio** para noviembre de 2026.
Lo tomamos como un **piso** más que como un valor exacto: por el patrón de los residuos y
por la prueba con los meses 12 a 14, esperamos que el valor real sea mayor, del orden de
5.600–6.000 jugadores, siempre que no salga la expansión ni haya un evento que reactive el
juego.

`[a completar cuando cierre noviembre: dato real de SteamCharts y error de la predicción.
Si se entrega antes, usar como referencia el promedio de "Last 30 Days" de la fecha de
entrega (al 2026-11-11 era 5.702, del 12/10 al 11/11), aclarando que no es exactamente
noviembre.]`

---

_Generado el 2026-11-11. Fuentes: `ajuste/resultados.json` (tools/ajuste_mc.py sobre
`datos/datos.csv`), `validacion/resultados.json` (meses 1–11), SteamCharts
(app 1030300), criterios de `segundo-parcial/apuntes/md/01-…` (§4, comparación de errores)
y `02-…` (§3)._
