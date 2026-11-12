"""Completa en borrador-d.md el promedio de "Last 30 Days" de SteamCharts (día de la entrega).

Pensado para correrlo el 2026-11-17: baja la página pública de Silksong en SteamCharts,
toma el promedio de jugadores de la fila "Last 30 Days" y lo escribe en el lugar marcado
`[a completar el 17/11]` de borrador-d.md. Después hay que regenerar el TP:

    venv/bin/python <caso>/actualizar_ultimos_30.py
    venv/bin/python <caso>/armar_tp.py
"""

from __future__ import annotations

import re
import urllib.request
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
URL = "https://steamcharts.com/app/1030300"
MARCA = "`[a completar el 17/11]`"


def ultimos_30() -> float:
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    m = re.search(r'Last 30 Days\s*</td>\s*<td class="right num-f[^"]*">([\d.,]+)</td>', html)
    if not m:
        raise SystemExit("No encontré la fila 'Last 30 Days' en SteamCharts")
    return float(m.group(1).replace(",", ""))


def main() -> None:
    d = AQUI / "borrador-d.md"
    txt = d.read_text(encoding="utf-8")
    if MARCA not in txt:
        raise SystemExit(f"No está la marca {MARCA} en borrador-d.md (¿ya se completó?)")
    v = ultimos_30()
    valor = f"**{v:,.0f}**".replace(",", ".")
    d.write_text(txt.replace(MARCA, valor), encoding="utf-8")
    print(f"✓ {date.today().isoformat()}: Last 30 Days = {v:.2f} → {valor} en borrador-d.md")
    if date.today().isoformat() != "2026-11-17":
        print("⚠ Hoy no es 2026-11-17: revisá las fechas del párrafo en borrador-d.md (d.7).")


if __name__ == "__main__":
    main()
