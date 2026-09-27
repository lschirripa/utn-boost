# Patrones por fecha de mesa — finales de AM2

> Pregunta: ¿el final de una mesa (dic, feb, sep…) se parece al de la misma mesa del año
> anterior? ¿O hay otro patrón temporal? Fuente: los 24 finales de `examenes/INDICE.md`
> (2024-03-05 → 2026-07-28), agrupados por mesa y por año. Generado el 2026-09-26.

---

## 0. Respuesta corta

1. **No hay patrón «misma mesa, distinto año».** El final de septiembre 2025 no se parece
   al de octubre 2024 más de lo que se parece a cualquier otro. Con dos datos por mesa no
   se puede afirmar nada, y lo poco que comparten es lo que comparten todos los finales.
2. **Sí hay patrón «misma mesa, mismo año».** Las dos o tres fechas de una misma mesa
   comparten el esqueleto (mismas familias en los P, a veces el mismo ejercicio con otro
   campo). Y la primera fecha de una mesa suele reciclar la mesa anterior.
3. **El patrón fuerte es por año, no por mesa.** 2026 cambió el estilo: teóricos con
   Green/Gauss/Stokes en los 6 finales, Green desplazó a Stokes en los prácticos, la EDO
   de 2º orden casi desapareció y las integrales múltiples también.

**Consecuencia para el 2026-09-29:** los mejores predictores son `2026-07-14` y
`2026-07-28`, no los finales de septiembre anteriores. Esto confirma lo que ya dice el
Anexo A de `estrategia.md`, ahora con números.

---

## 1. El calendario real de mesas

| Mesa | Fechas en el dataset | Cuántas por año |
|---|---|---|
| feb/mar | 2024-03-05 · 2025-02-11, 02-18, 02-25 · 2026-02-10, 02-24 (=17/02), 03-03 | 3 |
| mayo | 2024-05-10 · 2025-05-20 · 2026-05-19 | 1 |
| julio | 2024-07-23, 07-30 · 2025-07-15, 07-29 · 2026-07-14, 07-28 | 2 (con 2 semanas entre sí) |
| sep/oct | 2024-10-09 · 2025-09-25 · **2026-09-29** | 1 |
| diciembre | 2024-12-03, 12-10, 12-17 · 2025-12-02, 12-09, 12-16 | 3 (semanales) |

Diez finales por año. El de septiembre es **la única fecha suelta** del segundo
cuatrimestre: no tiene «hermano» en la misma mesa, así que no se puede usar el truco
de la sección 3.

---

## 2. Septiembre 2024 vs septiembre 2025: ¿se parecen?

| | 2024-10-09 | 2025-09-25 |
|---|---|---|
| T1 | curva/punto regular (def. + demo) | conservativo (demo) + circulación con potencial |
| T2 | V/F: límite · cambio de variables/volumen | cambio de variables (enunciar + área, reciclado de un 2P de 2016) |
| P1 | plano tangente + flujo | derivada direccional + gradiente |
| P2 | flujo por Gauss | flujo por paraboloide abierto |
| P3 | derivada direccional + implícita | Taylor |
| P4 | EDO 2º orden | circulación por Stokes |

Lo que comparten: **flujo en un P**, **derivada direccional + gradiente en un P** y
**cambio de variables en un teórico**. Lo que no: en 2024 hubo EDO y plano tangente; en
2025 hubo Stokes y Taylor **y ninguna EDO**. Con n = 2, «derivada direccional en un P»
y «cambio de variables en un T» son coincidencias que no alcanzan para decidir nada.

Un detalle sí llama la atención: **el final de septiembre es el que la cátedra recicla
después**, no el que recicla antes:

- `2024-10-09 P1` (plano tangente + flujo) reaparece en `2025-12-09 P1`.
- `2024-10-09 P3` (derivada direccional con implícita) reaparece en `2024-12-17 P3` y `2026-07-28 P4`.
- `2025-09-25 P2` (flujo por paraboloide abierto) reaparece en `2025-12-09 P2` y `2026-03-03 P4`.

Es decir, en septiembre suelen **escribir ejercicios nuevos** (o traerlos de parciales
viejos, como el `T2b` de 2025) y esos ejercicios se reutilizan en diciembre y febrero.
Para vos eso significa que no hay «el ejercicio de septiembre» para cazar.

---

## 3. El patrón que sí existe: las fechas de una misma mesa comparten esqueleto

| Mesa | Fecha 1 | Fecha 2 | Qué comparten |
|---|---|---|---|
| jul 2025 | 07-15: P1 Stokes · P2 EDO2 · P3 volumen · P4 flujo | 07-29: P1 Stokes · P2 EDO2 · P3 área sup. · P4 flujo | **esqueleto idéntico, misma posición** |
| dic 2025 | 12-02: P2 Stokes · P4 flujo | 12-09: P3 Green · P4 EDO2 / 12-16: P2 Stokes · P3 flujo | 12-02 **recicla dos ítems de 07-15** (misma curva, mismo cilindro) |
| feb 2026 | 02-10: EDO1 · flujo · Green · implícita | 02-24: curva · Green+EDO1 · trabajo · gradiente | EDO1 + Green + ítem de 1P; Gauss en el T de ambos |
| jul 2026 | 07-14: plano tg · **flujo Gauss** · **circ. Green** · conservativo+EDO1 | 07-28: **flujo Gauss** · **circ. Green** · EDO2 · gradiente+implícita | flujo Gauss + Green + EDO + ítem de 1P; **Stokes como teórico en los dos** |

Regla práctica: **el examen que viene se parece al anterior en el tiempo**, no al del
mismo mes del año pasado. La mesa anterior a la tuya es julio 2026.

---

## 4. La deriva por año (lo que cambió en 2026)

Número de finales del año en los que la familia aparece **en algún práctico**:

| Familia | 2024 (8) | 2025 (10) | 2026 (6) | Lectura |
|---|---|---|---|---|
| Flujo / Gauss | 7/8 | 9/10 | 5/6 | constante; cuando no está en P está en T (`2025-02-18`, `2026-02-24`) |
| Circulación por **Green** | 2/8 | 2/10 | **4/6** | subió: los dos de julio 2026 la tienen |
| Circulación por **Stokes** | 4/8 | 5/10 | **1/6** | bajó en P… porque pasó al teórico (ver abajo) |
| EDO **2º orden** | 4/8 | 6/10 | **1/6** | casi desapareció (sólo `2026-07-28 P3`) |
| EDO **1er orden** / líneas de campo | 3/8 | 2/10 | **3/6** | reemplazó a la de 2º orden, a veces mezclada con Green o conservativo |
| Trayectorias ortogonales | 1/8 | 2/10 | 1/6 | estable, baja |
| Integrales múltiples (masa/volumen/área) | 7/8 | 7/10 | **2/6** | bajó fuerte |
| Ítem de 1P (gradiente, implícita, plano tg, Taylor) | 7/8 | 6/10 | 5/6 | siempre hay uno |

Número de finales del año con la familia **en algún teórico** (enunciar / demostrar / V/F):

| Teórico | 2024 (8) | 2025 (10) | 2026 (6) | Lectura |
|---|---|---|---|---|
| Green (enunciar + área) | 2/8 | 1/10 | **3/6** | `02-10`, `03-03`, `05-19` |
| Stokes (enunciar) | 0/8 | 2/10 | **2/6** | **los dos últimos**: `07-14 T1`, `07-28 T2` |
| Gauss (enunciar + hipótesis) | 1/8 | 1/10 | **2/6** | `02-10 T1`, `02-24 T2` |
| Green ∪ Gauss ∪ Stokes | 3/8 | 3/10 | **6/6** | **en 2026 siempre hay uno de los tres** |
| Conservativo (independencia de trayectoria) | 4/8 | 5/10 | **1/6** | y ese uno (`07-28 T2b`) es un V/F, no la demo |
| Extremos (definir / Hessiano) | 4/8 | 4/10 | 1/6 | bajó |
| Cambio de variables | 2/8 | 3/10 | 2/6 | estable |
| Definiciones de 1P (diferenciabilidad, deriv. direccional, gradiente ⊥) | 6/8 | 8/10 | 3/6 | sigue apareciendo como el «otro» teórico |

---

## 5. Qué esperar el 2026-09-29 (esqueleto de julio 2026)

- **T1/T2:** uno de los dos pide **enunciar Green, Stokes o Gauss** (en 2026, siempre), con
  un inciso b) de V/F o de cálculo corto. El otro es una definición de 1P
  (diferenciabilidad, derivada direccional, gradiente) o extremos.
- **P:** flujo por Gauss (cerrado o con tapa) · circulación por Green (a veces con función
  desconocida o pregunta de conservativo) · una EDO, más probable de **1er orden** que de
  2º · un ítem de 1P (gradiente / implícita / plano tangente).
- Si reciclan, reciclan **julio 2026**, igual que `2025-12-02` recicló `2025-07-15`.

### Ajustes concretos al plan

1. **Teórico:** mantener **T-B (Green + área)** como el principal. Pero subir **T-C
   (Stokes)** y **T-D (Gauss)** de «enunciado leído» a «enunciado escrito de memoria con
   hipótesis»: son 10 min cada uno y en 2026 cubren el teórico obligatorio en 6 de 6.
   **T-A (independencia de trayectoria)** no se pidió como demostración en los últimos 7
   finales; pasa a tercer lugar, no se descarta.
2. **EDO:** las 3 que practicaste son de 2º orden. Sumar **una de 1er orden** (lineal o
   separable, incluso «hallar la línea de campo que pasa por P») y **una de trayectorias
   ortogonales**. 40 min en total. Ver machete §3.
3. **Circulación:** de las 5 que hiciste, asegurate de que **Green** sea la que sale sin
   pensar. Stokes hay que saberlo enunciar; calcularlo vale menos que hace un año.
4. **Simulacros:** si todavía no los hiciste cronometrados, usar `2026-07-14` y
   `2026-07-28` completos, en 2 h cada uno, eligiendo 3 de 6. Son el mejor «simulacro»
   que existe para esta mesa.

---

_Generado el 2026-09-26 a partir de `examenes/INDICE.md` (24 finales, 2024-03-05 → 2026-07-28).
Las familias se agruparon por tag: Flujo/Gauss = `#Flujo` ∪ `#Divergencia`; EDO1 = `#EDOPrimerOrden` ∪ `#LineasCampo`;
integrales múltiples = `#Volumen` ∪ `#MasaCuerpo` ∪ `#AreaRegion` ∪ `#AreaSuperficie` ∪ `#MasaChapa`._
