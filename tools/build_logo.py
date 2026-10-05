"""Genera los archivos del logo de Pacerless como SVG (texto convertido a trazos) y PNG.

Uso: python3 tools/build_logo.py <peso> <carpeta_salida> <carpeta_con_outfit-<peso>.ttf>
Fuente: Outfit (SIL Open Font License 1.1). Ver assets/brand/logo/README.md para obtener los .ttf.
Requiere: pip install fonttools uharfbuzz cairosvg
"""
import sys
from pathlib import Path

import cairosvg
import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

WEIGHT = int(sys.argv[1]) if len(sys.argv) > 1 else 600
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "out")
OUT.mkdir(parents=True, exist_ok=True)

TINTA = "#111418"
HUESO = "#F5F2EC"
PULSO = "#FF5A36"

FONT_DIR = Path(sys.argv[3] if len(sys.argv) > 3 else ".")
TTF = FONT_DIR / f"outfit-{WEIGHT}.ttf"
tt = TTFont(TTF)
glyph_set = tt.getGlyphSet()
order = tt.getGlyphOrder()
hb_font = hb.Font(hb.Face(hb.Blob.from_file_path(str(TTF))))


def shape(text, tracking=0):
    """Devuelve [(nombre_glifo, x)] con kerning y el ancho total, en unidades de fuente."""
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hb_font, buf, {"kern": True})
    x, items = 0, []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        items.append((order[info.codepoint], x + pos.x_offset))
        x += pos.x_advance + tracking
    return items, x - tracking


def outline(items):
    """Trazo SVG (y invertida) y caja envolvente de una lista de glifos."""
    svg = SVGPathPen(glyph_set)
    bounds = BoundsPen(glyph_set)
    for name, x in items:
        for pen in (svg, bounds):
            glyph_set[name].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
    return svg.getCommands(), bounds.bounds  # (xmin, ymin, xmax, ymax) con y hacia abajo


def svg_doc(w, h, body, vb=None, bg=None, rx=0, title="Pacerless"):
    vb = vb or (0, 0, w, h)
    rect = f'<rect x="{vb[0]}" y="{vb[1]}" width="{vb[2]}" height="{vb[3]}" rx="{rx}" fill="{bg}"/>' if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}" '
        f'width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{rect}{body}</svg>\n'
    )


def save(name, svg, png_width=None):
    (OUT / f"{name}.svg").write_text(svg)
    if png_width:
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / f"{name}.png"), output_width=png_width)


# ---- Wordmark ---------------------------------------------------------------
items, adv = shape("pacerless")
d, (x0, y0, x1, y1) = outline(items)
ww, wh = x1 - x0, y1 - y0
pad = 0  # sin margen: el espacio de respeto lo define el uso
wm_vb = (x0, y0, ww, wh)
H = 400
W = round(H * ww / wh)

for tag, color in (("ink", TINTA), ("bone", HUESO)):
    save(f"pacerless-wordmark-{tag}",
         svg_doc(W, H, f'<path fill="{color}" d="{d}"/>', vb=wm_vb), png_width=2400)

# Versión principal e invertida con fondo, con margen generoso (1x de altura de "p")
m = wh * 0.9
bg_vb = (x0 - m, y0 - m, ww + 2 * m, wh + 2 * m)
BW = 1600
BH = round(BW * bg_vb[3] / bg_vb[2])
save("pacerless-logo-on-bone", svg_doc(BW, BH, f'<path fill="{TINTA}" d="{d}"/>', vb=bg_vb, bg=HUESO), png_width=1600)
save("pacerless-logo-on-ink", svg_doc(BW, BH, f'<path fill="{HUESO}" d="{d}"/>', vb=bg_vb, bg=TINTA), png_width=1600)

# ---- Versión con acento: punto final en Pulso -------------------------------
items_a, adv_a = shape("pacerless.")
dot_items = items_a[-1:]
word_items = items_a[:-1]
d_w, _ = outline(word_items)
d_dot, _ = outline(dot_items)
_, (ax0, ay0, ax1, ay1) = outline(items_a)
acc_vb = (ax0, ay0, ax1 - ax0, ay1 - ay0)
AW = round(H * acc_vb[2] / acc_vb[3])
save("pacerless-wordmark-accent",
     svg_doc(AW, H, f'<path fill="{TINTA}" d="{d_w}"/><path fill="{PULSO}" d="{d_dot}"/>', vb=acc_vb),
     png_width=2400)

# ---- Icono: "p" sola --------------------------------------------------------
p_items, _ = shape("p")
d_p, (px0, py0, px1, py1) = outline(p_items)
S = 512
pw, ph = px1 - px0, py1 - py0
scale = (S * 0.46) / ph          # la "p" ocupa ~46 % del alto del cuadro
cx = S / 2 - (px0 + pw / 2) * scale
cy = S / 2 - (py0 + ph / 2) * scale
p_body = f'<g transform="translate({cx:.2f} {cy:.2f}) scale({scale:.5f})"><path fill="{HUESO}" d="{d_p}"/></g>'
save("pacerless-icon", svg_doc(S, S, p_body, bg=TINTA, rx=int(S * 0.22), title="Pacerless"), png_width=512)
cairosvg.svg2png(bytestring=svg_doc(S, S, p_body, bg=TINTA, rx=int(S * 0.22)).encode(),
                 write_to=str(OUT / "favicon-32.png"), output_width=32)
cairosvg.svg2png(bytestring=svg_doc(S, S, p_body, bg=TINTA, rx=int(S * 0.22)).encode(),
                 write_to=str(OUT / "apple-touch-icon-180.png"), output_width=180)

print("ok", WEIGHT, "wordmark", round(ww), "x", round(wh), "->", OUT)
