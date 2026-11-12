# Caso del TP: Hollow Knight: Silksong — jugadores en Steam después del lanzamiento

> Fuente de datos: [SteamCharts — Hollow Knight: Silksong (app 1030300)](https://steamcharts.com/app/1030300), tabla mensual pública, descargada el 2026-11-11.

---

## La pregunta

¿Cuántos **jugadores simultáneos promedio** va a tener Hollow Knight: Silksong en Steam en
**noviembre de 2026** (mes 15 desde el lanzamiento)? Se predice ahora y se compara con el
dato real cuando SteamCharts cierre el mes (o con el parcial "Last 30 Days" si la entrega
es antes).

- **x** = mes desde el lanzamiento (1 = septiembre 2025; el juego salió el 2025-09-04).
- **y** = promedio de jugadores conectados al mismo tiempo en ese mes ("Avg. Players" de
  SteamCharts), redondeado al entero. **No** es la cantidad de jugadores totales.

## Archivos

| Archivo | Qué es |
|---|---|
| `datos/steamcharts-silksong.csv` | Tabla cruda de SteamCharts (mes, promedio, pico), incluida la fila parcial "Last 30 Days". |
| `datos/datos.csv` | Datos del ajuste: meses 1–14 (sep 2025 – oct 2026). |
| `datos/datos-validacion.csv` | Meses 1–11, para ajustar y comparar contra los meses 12–14 reales. |
| `datos/steamcharts-gta-v.csv` | GTA V en Steam desde abril 2015 (para el gancho del video, no se ajusta). |
| `ajuste/` | Salida de `tools/ajuste_mc.py` (reporte paso a paso, JSON y gráficos). Regenerable. |
| `graficos.py` → `ajuste/comparacion-cola.png`, `ajuste/silksong-vs-gta-v.png` | Los 6 modelos con zoom en los meses 3–15 (en `comparacion.png` el mes 1 aplasta la cola). Correr después de `ajuste_mc.py`. |
| `actualizar_ultimos_30.py` | Para el día de la entrega (2026-11-17): baja el "Last 30 Days" de SteamCharts y lo completa en el d.7 de `borrador-d.md`. Después correr `armar_tp.py`. |
| `validacion/` | `ajuste_mc.py` sobre los meses 1–11 (para la prueba contra los meses 12–14). |
| `borrador-d.md` | Texto del punto d) (comparación, elección del potencial, estimación y confiabilidad). |
| `tp-fuente.md` | Texto del TP (carátula, a, b, aplicaciones/GTA, conclusiones, fuentes) con marcadores para c) y d). |
| `armar_tp.py` → `exports/tp-silksong.{md,html,pdf}` | Arma el TP completo (fuente + `ajuste/reporte.md` + `borrador-d.md`) y lo exporta. **El entregable sale de acá; no editar `exports/` a mano.** |

Regenerar todo (ajuste → gráficos → TP):

```bash
venv/bin/python tools/ajuste_mc.py materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/datos/datos.csv --modelos exponencial,potencial,reciproco --x0 15 --out-dir materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/ajuste
venv/bin/python materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/graficos.py
venv/bin/python materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/armar_tp.py
```

## Decisión 2026-11-12: el TP usa 3 modelos

El grupo decidió presentar **exponencial, potencial y recíproco** (la consigna pide "por lo
menos 3", con al menos uno no polinómico) para que entre en el video de 6 minutos. El
recíproco se queda porque es la lección central del d): menor error y predicción negativa.
`ajuste/` y `validacion/` se regeneraron con esos 3. Tampoco se muestra el desarrollo de la
resolución de los sistemas (Cramer/Gauss): en la práctica el profe dijo que no le interesa,
alcanza con la tabla, el sistema planteado y el resultado.

## Resultados con los 6 modelos (exploración inicial, meses 1–14, predicción para x = 15)

| Modelo | Función | E (SSE) | ŷ(15) | ¿Tiene sentido? |
|---|---|---:|---:|---|
| Recíproco | $-17245.71 + 190071.71/x$ | 1,82·10⁹ | **−4.574** | ❌ negativo (ya desde el mes 12) |
| Potencial | $122134.87\,x^{-1.22172}$ | 4,93·10⁹ | **4.467** | ✅ |
| Parábola | $153387.92 - 34583.52x + 1832.93x^2$ | 1,03·10¹⁰ | **47.045** | ❌ vuelve a subir |
| Recta | $80070.53 - 7089.50x$ | 2,00·10¹⁰ | **−26.272** | ❌ negativo |
| Exponencial | $57750.06\,e^{-0.19324x}$ | 2,13·10¹⁰ | **3.182** | ✅ (tiende a 0) |
| Hiperbólico | $88855.72/(1.15366 + x)$ | 2,34·10¹⁰ | **5.501** | ✅ |

Dato de referencia: "Last 30 Days" (2026-10-12 a 2026-11-11) = **5.702**.

## Validación (ajuste con meses 1–11, predicción de 12–14)

Reales: 7.972 / 7.116 / 6.108.

| Modelo | Predicción 12 / 13 / 14 | Error medio |
|---|---|---:|
| Hiperbólico | 5.884 / 5.431 / 5.042 | ≈ 22 % |
| Potencial | 4.787 / 4.291 / 3.878 | ≈ 39 % |
| Exponencial | 3.177 / 2.420 / 1.844 | ≈ 65 % |
| Recíproco | negativos | — |

## Puntos para el d) (confiabilidad)

- El error cuadrático está dominado por el **mes 1** (191 mil jugadores): el modelo que mejor
  "pega" el lanzamiento gana en E aunque prediga mal la cola, que es donde está x = 15.
- **Julio 2026** (mes 11) se sale de la curva (8.619 > 7.111 del mes anterior). Causa **a
  verificar** (¿oferta de verano de Steam?); no inventarla.
- **Sea of Sorrow**: expansión gratuita anunciada el 2025-12-15 para 2026, sin fecha
  confirmada en las notas encontradas. Si sale en noviembre, la predicción deja de valer (el
  modelo supone que no pasa nada nuevo). Es también el ejemplo real de "sacar una expansión
  para reactivar el juego".
- Vale **solo para este juego**: otro juego tiene otros coeficientes.

## Gancho del video: GTA V → GTA VI

GTA VI sale el **2026-11-19 solo en PS5/Xbox** (sin fecha oficial de PC). En Steam, GTA V
(abril 2015) cayó igual que Silksong los primeros 6 meses (192.714 → 25.388) y **desde
octubre 2015 volvió a subir** (47 mil en enero 2016) con las actualizaciones del Online: el
ajuste de los primeros meses habría fallado. Moraleja: el modelo predice "si no pasa nada
nuevo".

---

_Generado el 2026-11-11. Fuentes: SteamCharts (apps 1030300 y 271590), consigna en
`../enunciado.md`, `tools/ajuste_mc.py`._
