# Plan de estudio — Primer parcial · Análisis Numérico

> Examen: **martes 2026-10-06** · Hoy: viernes 2026-10-02 · **4 días restantes + la
> mañana/tarde del martes** (vie noche ≈ 3 h, sáb/dom/lun ≈ 8–9 h cada uno, mar liviano).
> Restricciones declaradas: **punto de partida en cero**; objetivo **promocionar (≥ 8)**;
> no trabaja: tiene el fin de semana y el lunes enteros.
> Fuentes: [`estrategia.md`](estrategia.md) · [`examenes/INDICE.md`](examenes/INDICE.md) ·
> [`examenes/resueltos/RESOLUCIONES-2025.md`](examenes/resueltos/RESOLUCIONES-2025.md) ·
> `../fuentes/formulas-y-metodos-manuscrito.pdf`.

---

## ⚠️ No entra todo: triaje para llegar a 8

Hay ≈ **28 h útiles** para 4 bloques 🔴 que arrancan de cero. Alcanza para las **cuatro
recetas** si cada bloque se cierra en un día y no se abre nada lateral. Lo que **cae**:

- Ecuaciones integrales con convolución (`#EcuacionIntegral`, 0/3 en 2025): solo un ejemplo leído, no practicado.
- Ecuaciones en diferencias de **2do orden** (`2x(n+2)…`): solo las de 1er orden (todas las de 2025).
- Corte de `|G|` por el eje real: 10 min de regla cualitativa, no ejercicios propios.
- Conjuntos de complejos, método gráfico del módulo, fasores, sistemas de EDO, sumas de series vía Fourier: **fuera**.
- El segundo simulacro a ciegas (`2024-2C T2`): fuera; queda solo `2025-1C_Recuperatorio.pdf`.

Lo que **no se negocia**, porque son los 8 puntos: Ej1a+b (2), Ej3 completo (3), Ej4 completo (2),
Ej2a o Ej2b (1). Ej1c (media onda, 1 punto de dibujo) y Ej2c (demostración de 2 líneas) son
el colchón para que un error en otro ítem no te baje de 8.

**Regla de trabajo:** cada ejercicio se hace **en papel, con reloj (25 min), sin mirar**, y se
corrige contra la hoja resuelta. Si un tipo de ítem sale bien dos veces seguidas, se cierra y
no se vuelve a tocar. Terminá cada bloque con `/registrar` (lo que falló manda el lunes).

### Qué apunte leer cada bloque (agregado 2026-10-02, apuntes en `apuntes/md/`)

Leé **solo la teoría visible y la sección "Lo que el profe remarca"**; los ejercicios del
apunte son para consultar cuando te trabás, no para hacer todos.

| Bloque | Antes de practicar (≈30 min) | Si te trabás |
|---|---|---|
| Fourier I (vie) | `01` teoría + `10` "Lo que el profe dice del parcial" | `16` (teórica STF) |
| Fourier II (sáb mañana) | `02` teoría (impar desplazada, dos condiciones ⇒ cuadruplicar) | `17` (teórica SEF), `07` ej. de Fourier |
| Laplace (sáb tarde/noche) | `14` "Lo que el profe remarca" + `04` recetas `t·f`, `f/t`, convolución | `15` (teórica), `04` ejercicios |
| Sistemas (dom) | `11` "Lo que el profe remarca" + `13` tabla de los seis casos de polos | `05` (13 ejercicios resueltos), `07` ej. 8–9 |
| Z (lun mañana) | `12` "Lo que el profe remarca" + `06` recetas (paridad, ROC, "una z afuera") | `06` ejercicios |
| Lun noche, después del simulacro | `07` y `10` completos: es el repaso del profe | — |

**Descartado sin culpa:** `03` (transformada de Fourier, el profe dijo que no se toma) y los
fasores de `16`.

---

## Plan día por día

| Día | Foco | Entregable del día |
|---|---|---|
| **vie 2026-10-02 (noche, ≈3 h)** | 🔴 **Fourier I — la receta.** Leer `RESOLUCIONES-2025.md` Ej1a T1/T2/rec (30 min) + hoja de fórmulas p.1. Decisión fija: *reales/cosenos ⇒ par (bₙ=0)*, *imaginarios/senos ⇒ impar (a₀=aₙ=0)*; anotar `T, L, ω₀`; integral por partes; `cos(nπ)=(−1)ⁿ`; reindexar en `2k+1`. Después Ej1b: `2 sen x cos x = sen 2x` (un término), `cos³`/`sen³` por exponenciales. | **2025-1C T1 Ej1a** (π−t, par) y **2025-1C T2 Ej1a** (−π−t, impar) en papel, corregidos. `/registrar`. |
| **sáb 2026-10-03 (≈9 h)** | **Mañana 🔴 Fourier II:** `Cₙ = ½(aₙ − j bₙ)`, `C₀ = a₀/2`, valor medio, **media onda** (`f(t+T/2) = −f(t)`: gráfico + tramos, no la serie). **Tarde 🔴 Laplace I:** integral impropia = transformada evaluada; `L{t f} = −F'`; `L{f/t} = ∫_s^∞ F` (chequear el límite en 0); `L{aᵗ}` con su demostración. **Noche 🟠 Laplace II:** convolución ida y vuelta, `1/(s²+1)²` y `s²/(s²+1)²` (producto → suma). | Mañana: **2015-05-29 T1 Ej1** (`4/k`: k=2, SEF), **2025-1C T1 Ej1c** y **T2 Ej1c** (SMO), **sin-fecha K3521 T2 Ej3** (`3x`, cosenos + `Cₙ` sin integrar). Tarde: **2025-1C T1 Ej2a**, **2025-1C rec Ej2a**… ⚠ reservado: usar en su lugar **sin-fecha K3521 T2 Ej2** (`ln 2`, mismo ejercicio) y **sin-fecha K3521 T1 Ej2** (`4/289`); escribir **`L(2ᵗ)`** de memoria. Noche: **2025-1C T1 Ej2b**, **2025-1C T2 Ej2a/b**, **2024-2C rec Ej3a/b**. Leer (no hacer) **2024-1C T1 Ej2** como ejemplo de ecuación integral. `/registrar`. |
| **dom 2026-10-04 (≈9 h)** | 🔴 **Sistemas estables, el día entero (3 puntos).** Mañana: Ruffini → polo con Re>0 → **K que lo cancela**, polos/ceros, regla cualitativa del corte por el eje real (∞ en polos, 0 en ceros, lomo en complejos), tabla **polo → tipo de respuesta** (hoja de fórmulas p.4). Tarde: **respuesta temporal**: `Y = G·F`, fracciones simples (cover-up + coeficientes), completar cuadrados, partir en `(s+a)` + constante, **valor estable** = coeficiente de `A/s`. Noche: variantes (impulso `F=1`, entrada `e^{−t}`, `G(s)` desde la EDO con reposo) + repaso instrumental de complejos (30 min: raíces de `s²+6s+10`, polar). | Mañana: **2025-1C T2 Ej3a** (k=3), **2022-10-11 Ej5a/b**, **2024-2C rec Ej4a** (a y b). Tarde: **2025-1C T2 Ej3b/c** (el reciclado ×3; `y = −3 + 3cos t e^{−3t} + 19 sen t e^{−3t}`, oscilatoria amortiguada, estable −3), **2024-1C T1 Ej5** completo, **2024-2C T2 Ej4a/b**. Noche: **2025-1C T1 Ej3a/b** (sistema mecánico), **2024-1C T2 Ej4a/b** (impulso), **2015-05-29 T1 Ej3c** (`e^{−t}`). Cronómetro en todos. `/registrar`. |
| **lun 2026-10-05 (≈9 h)** | **Mañana 🔴 Z I:** sucesión por paridad → dos geométricas (`z^{−2k}`, `z^{−(2k+1)}`), **ROC = intersección**; sumas `Σ x(n)c^{−n} = X(c)` con tablas (`Z{aⁿ/n!} = e^{a/z}`, `Z{cos Ωn}`); secuencia finita por definición. **Mediodía 🔴 Z II:** ecuación en diferencias de 1er orden: `Z{x(n+1)} = zX − z x(0)`, fracciones simples sobre `X(z)/z`, tablas `aⁿ`, `n aⁿ`, **verificar `x(2)`**. **Tarde 🔴 Simulacro a ciegas:** `examenes/2025-1C_Recuperatorio.pdf`, 2 h de reloj, solo con la hoja de fórmulas (o la tabla que permita la cátedra). Corregir con `RESOLUCIONES-2025.md` → "Recuperatorio". **Noche:** `/machete` (hoja de fórmulas + lo que falló) y rehacer los ítems ❌ del simulacro. | Mañana: **2025-1C T1 Ej4a/b**, **2025-1C T2 Ej4a**, **2024-2C T2 Ej5a/b**, **sin-fecha K3521 T1 Ej5**. Mediodía: **2025-1C T2 Ej4b** (= sin-fecha K3521 T2 Ej5), **2015-05-29 T1 Ej4** y **T2 Ej4**, **2024-2C rec Ej5**. Tarde: simulacro completo con nota estimada (`/registrar`). Noche: `repaso/machete.md` cerrado. |
| **mar 2026-10-06 (liviano, antes del examen)** | 🟢 Repaso del machete (30 min). Rehacer **una vez** los dos ítems que peor salieron el lunes. Checklist de `estrategia.md` §6 de memoria: `L(aᵗ)`, regla par/impar, SMO, tabla polo → respuesta, ROC como intersección, propiedades de Z. **Nada nuevo.** | Examen. |

---

## Qué cambió respecto del plan anterior

- Se perdieron los días 23/9 → 1/10 (D1–D8 del plan previo): AM2 y Administración Gerencial ocuparon toda la ventana. Punto de partida: cero.
- De 13 días útiles a 4: cada bloque pasa a un solo día y cae lo lateral (triaje de arriba).
- Se saca el segundo simulacro (`2024-2C T2`); queda solo el recuperatorio 2025, que se hace el lunes a la tarde y no el domingo.
- El objetivo declarado pasa a ser **8 (promoción)**, no 6: por eso Ej3 y Ej4 (5 puntos de receta) tienen día completo y Ej2 queda en un ítem seguro + uno de colchón.

---

*Generado el 2026-10-02 con: MATERIA.md (examen 2026-10-06), estrategia.md (prioridades y banco, del 2026-09-10), registro.md (vacío, sin sesiones aún), que-saltear.md (no existe: no hay apuntes), input del usuario (arranca en cero; vie noche + sáb + dom + lun completos, martes liviano; busca ≥ 8).*
