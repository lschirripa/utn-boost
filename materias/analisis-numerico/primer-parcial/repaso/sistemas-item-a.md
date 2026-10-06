# Sistemas, solo el ítem a — polos, ceros, estabilidad, K y G(s)

> Para sacar 1 punto del Ej3 de forma mecánica. Fuente: `examenes/INDICE.md`, `RESOLUCIONES-2025.md`, guía 03 §4–§5. Todas las respuestas verificadas con sympy. Generado 2026-10-06.

## La receta (es una sola)

1. **Factorizá arriba y abajo.** Cuadráticas con la calculadora. Cúbicas por Ruffini: probá los divisores del término independiente ($\pm1, \pm2, \pm5, \pm10$…) hasta que uno dé $0$.
2. **Simplificá** el factor que esté en los dos. La raíz cancelada **no es ni polo ni cero**.
3. **Ceros** = raíces de lo que quedó arriba. **Polos** = raíces de lo que quedó abajo (cada complejo con su conjugado).
4. **Estable ⇔ ningún polo con parte real positiva.** Polo en $0$ o en $\pm bj$ simples: *marginalmente estable*, que la cátedra cuenta como **estable**.
5. **Si piden $K$:** encontrá el polo malo $p$ (parte real $> 0$). El numerador tiene que anularse ahí, $N(p) = 0$: despejás $K$ y después mostrás que el factor se cancela.
6. **Si dan la ecuación diferencial** con reposo: $y(0) = y'(0) = 0$ ⇒ $\mathcal{L}[y'] = sY$, $\mathcal{L}[y''] = s^2Y$. Transformás miembro a miembro, despejás y $G = Y/F$.

Fuera del ayudamemoria solo va de memoria el paso 4, el 5 y $G = Y/F$. Dentro, la transformada de la derivada: $\mathcal{L}[f'] = sF - f(0)$.

## Los nueve ítems a de los parciales, con respuesta

| Parcial | Enunciado del ítem a | Respuesta |
|---|---|---|
| **2025-1C T2** (reciclado 3 veces) | $G = \dfrac{10(s^2 - 4s + k)}{s^3 + 5s^2 + 4s - 10}$. Hallar $K$ para que sea estable. | Ruffini con $s=1$: $1+5+4-10 = 0$ ⇒ den $= (s-1)(s^2+6s+10)$, polos $1$ y $-3\pm j$. Polo malo $1$: $1 - 4 + k = 0$ ⇒ **$k = 3$**. Queda $G = \dfrac{10(s-3)}{s^2+6s+10}$. |
| **2025-1C rec** | $G = \dfrac{2(s^2+2s-3)}{(s-1)(s+2)(s^2+8s+17)}$. Polos, ceros, ¿estable? | Num $= 2(s+3)(s-1)$: se cancela $(s-1)$. **Cero: $-3$. Polos: $-2$, $-4 \pm j$. Estable.** |
| **2025-1C T1** | $f - 2y - 2y' = y''$ ($M=1$, $B=2$, $K=2$), reposo. Hallar $G(s)$. | $F - 2Y - 2sY = s^2Y$ ⇒ **$G = \dfrac{1}{s^2+2s+2}$**. Polos $-1 \pm j$: estable. |
| **R-F** (repaso 2026 = 2015-05-29 T2) | $G = \dfrac{25(s^2 - Ks + 12)}{(s^2+4s+5)(s^2-3s)}$. Hallar $K$ para que sea estable. | Den $= s(s-3)(s^2+4s+5)$, polos $0$, $3$, $-2\pm j$. Polo malo $3$: $9 - 3K + 12 = 0$ ⇒ **$K = 7$**. Queda $G = \dfrac{25(s-4)}{s(s^2+4s+5)}$; el polo en $0$ es marginal ⇒ estable. |
| **2022-10-11** | $G = \dfrac{17(s^2 + s - k)}{(s-2)(s^2+8s+17)}$. Hallar $k$. | Polo malo $2$: $4 + 2 - k = 0$ ⇒ **$k = 6$**. Num $= 17(s-2)(s+3)$; queda $\dfrac{17(s+3)}{s^2+8s+17}$, polos $-4\pm j$. |
| **2024-2C T2** (= 2024-1C T2) | $G = \dfrac{5(s^2 - ks - 2)}{(s^2+s-6)(s^2+2s+2)}$. Hallar $k$. | Den $= (s-2)(s+3)(s^2+2s+2)$. Polo malo $2$: $4 - 2k - 2 = 0$ ⇒ **$k = 1$**. Num $= 5(s-2)(s+1)$. |
| **2024-2C rec** | $G = \dfrac{34(s^3 - 3s^2 - as)}{(s-5)(s+b)(s^2+8s+17)}$. Todos los $a, b$ para que sea estable. | Num $= 34s(s^2 - 3s - a)$. Polo malo $5$: $25 - 15 - a = 0$ ⇒ **$a = 10$** (num $= 34s(s-5)(s+2)$). El polo $-b$ necesita parte real $\le 0$ ⇒ **$b \ge 0$** (con $b = 0$ se cancela con el cero en $0$). |
| **sin fecha K3521 T1** | $G = \dfrac{41(s^3+s^2) + 87s + 87}{s(s+3)(s^2+10s+29)}$. ¿Estable? | Num $= (s+1)(41s^2+87)$: nada se cancela. Polos $0$, $-3$, $-5 \pm 2j$. Ninguno a la derecha; el $0$ es simple ⇒ **estable (marginal)**. |
| **2015-05-29 T1** | $G = \dfrac{K(s^2-2s-3)}{(s-3)(s+2)(s^2+4)}$. ¿Estable? | Num $= K(s-3)(s+1)$: se cancela $(s-3)$. Cero $-1$; polos $-2$, $\pm 2j$. Nada a la derecha ⇒ **estable (marginal: oscila sin amortiguar)**. |

**Patrón:** en 6 de 9 el polo malo es un entero chico ($1$, $2$, $3$ o $5$) que sale probando divisores, y la cuadrática que queda siempre tiene raíces complejas con parte real negativa. Si tu $K$ no cancela nada, revisá la cuenta.

*Generado el 2026-10-06 desde `examenes/INDICE.md` y `guia/03-sistemas-desde-cero.md`; verificado con sympy.*
