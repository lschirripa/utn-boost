# Resolución oficial del 1er parcial 2C 2026 (K3572)

> Fuente: `2026-10-06_Parcial_respuestas.pdf` (hoja OneNote del profesor, creada el 2026-10-01; examen del 2026-10-06; publicada en Avisos del aula el 2026-10-07). Enunciados en `../INDICE.md` (secciones 2026-10-06). Método y resultado tal como aparecen en la hoja; resultados verificados con sympy. La versión para estudiar, con todas las cuentas, es `../../apuntes/md/06-parcial-2026-resuelto.md`.

---

## Tema 1

- **Ej1a** — "Cosenos = par". Gráfico de la V; `f(t) = −t+2` en `(−2,0)`, `t+2` en `[0,2)`; `T=4, L=2, w0=π/2`. `a0/2 = 3` "por gráfico", `bm = 0`. `am = (2/2)∫₀²(t+2)cos(mπt/2)dt = [(−1)^m − 1]/(mπ/2)²` (tacha los términos con seno). m par → 0; m impar → `−8/(m²π²)`. **`S(t) = 3 − (8/π²) Σ_{k=0}^∞ cos[(2k+1)πt/2]/(2k+1)²`**.
- **Ej1b** — `Cm = ½(am − j·bm)` → **`Cm = −4/(m²π²)`** (no aclara m impar ni `C0`).
- **Ej1c** — `f(0) = 2 = S(0)` → **`Σ 1/(2k+1)² = π²/8`**.
- **Ej2a** — "Def. de transf. de Laplace": la integral es `L(sen t / t)` evaluada en 1. "Div. × t": `∫_s^∞ du/(u²+1) = π/2 − arctg(s)`; deja escrito `∃ lím_{t→0} sen t / t = 1`. **Resultado `π/4`**.
- **Ej2b** — "**No** usar 2da prop. de traslación porque necesitaría `t > 1`". Desarrolla `t³ − 3t² + 3t − 1` → **`(6 − 6s + 3s² − s³)/s⁴`**.
- **Ej3a** — `G = 3(s−1)(s+2)/(s³+5s²+3s−k)`; reemplaza `s = 1` en el denominador: **`k = 9`**. Ruffini → `(s−1)(s²+6s+9)`; **`G(s) = 3(s+2)/(s+3)²`**.
- **Ej3b** — plano con el cero en −2, el polo en −3 y el punto `1+j`; **`|G(1+j)| = 3·√10/17`**.
- **Ej3c** — `Y = 3(s+2)/(s(s+3)²) = A/s + B/(s+3)² + C/(s+3)`; `A = 6/9 = 2/3`, `B = −3/−3 = 1` (tapando), `2/3 + C = 0 → C = −2/3`. **`y(t) = 2/3 + t·e^{−3t} − (2/3)e^{−3t}`**.
- **Ej4a** — `zX − z·x(0) + 3X = 5z/(z−2)` → `X = (2z²+z)/((z−2)(z+3))`; `(2z+1)/((z−2)(z+3))` con `A = 1`, `B = 1` → **`x(n) = 2ⁿ + (−3)ⁿ`**; `x(3) = −19` por los dos caminos.
- **Ej4b** — `= Z[2n+3]` evaluada en `−4`; `Z[2n+3] = 2z/(z−1)² + 3z/(z−1)` → **`52/25`**.

## Tema 2

- **Ej1a** — "Cosenos = par": `f(t) = t²` en `(−2,2)`. `bm = 0`, `a0 = 8/3 → a0/2 = 4/3`. `am = (2/2)∫₀² t² cos(mπt/2) dt = 16(−1)^m/(m²π²)`. **`S(t) = 4/3 + (16/π²) Σ_{m=1}^∞ ((−1)^m/m²) cos(mπt/2)`** (en el recuadro el exponente `m` de `(−1)` quedó sin escribir).
- **Ej1b** — recuadra `Cm = 8(−1)^m/m²`. ⚠ Falta el `π²`: es **`Cm = 8(−1)^m/(m²π²)`**, `C0 = 4/3`.
- **Ej1c** — `S(0) = f(0) = 0` → **`Σ_{m=1}^∞ (−1)^m/m² = −π²/12`**.
- **Ej2a** — `L[sen(2t)·t²]` evaluada en 3 = derivada segunda de `2/(s²+4)`: `→ −4s/(s²+4)² → (12s²−16)/(s²+4)³`. **`92/2197`**.
- **Ej2b** — `sen(α−β) = sen α cos β − cos α sen β` → `½ sen(2t) − (√3/2)cos(2t)` → **`1/(s²+4) − (√3/2)·s/(s²+4)`**.
- **Ej3a** — marca `(s−2)` como "inestable"; `2² + 2 − k = 0` → **`k = 6`**; `G = 17(s+3)/(s²+8s+17)`.
- **Ej3b** — `Y(s) = 17(s+3)/(s(s²+8s+17))`; `z0 = −3, z1 = ∞`; `p0 = −4+j, p1 = −4−j, p2 = 0`. Corte: lomo en −4, toca el eje en −3, asíntota en 0.
- **Ej3c** — `A = 3`; `3 + B = 0 → B = −3`; `C = −7`. ⚠ El renglón dice `3(s²+8s+17) + Bs² + Cs = s + 3` y `24 + C = 1`: falta el factor 17 (es `= 17s + 51`, `24 + C = 17`). `Y = 3/s − (3(s+4) + 7 − 12)/((s+4)²+1)` → **`y(t) = 3 − 3cos(t)e^{−4t} + 5sen(t)e^{−4t}`**.
- **Ej4a** — `zX − z·x(0) = 3X + 2z/(z−1)` → `X = 2z²/((z−1)(z−3))`; `A = −1`, `B = 3` → **`x(n) = −1 + 3^{n+1}`**; `x(2) = 26` por los dos caminos.
- **Ej4b** — `= Z(n+1)` evaluada en 3; `z/(z−1)² + z/(z−1)` → **`9/4`**.

---

*Transcripto el 2026-11-26.*
