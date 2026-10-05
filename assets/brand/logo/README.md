# Logo de Pacerless

Wordmark `pacerless` en **Outfit SemiBold (600)**, con el texto convertido a trazos (no necesita la fuente para usarse).
Colores de la guía: Tinta `#111418`, Hueso `#F5F2EC`, Pulso `#FF5A36`.

| Archivo | Uso |
|---|---|
| `pacerless-wordmark-ink.svg` / `.png` | Logo en Tinta, fondo transparente. Para fondos claros (cabecera de la tienda). |
| `pacerless-wordmark-bone.svg` / `.png` | Logo en Hueso, fondo transparente. Para fondos oscuros o sobre foto. |
| `pacerless-logo-on-bone.svg` / `.png` | Principal con fondo Hueso y margen. |
| `pacerless-logo-on-ink.svg` / `.png` | Invertida con fondo Tinta y margen. |
| `pacerless-wordmark-accent.svg` / `.png` | Nombre en Tinta con punto final en Pulso. Uso decorativo (redes, firmas, empaques). |
| `pacerless-icon.svg` / `.png` (512) | "p" en Hueso sobre Tinta, esquinas redondeadas. Avatar de redes. |
| `favicon-32.png`, `apple-touch-icon-180.png` | Favicon y icono para iPhone. |

**Shopify:** sube los PNG en el admin (logo y favicon). Usa los SVG en el código del tema.

**Reglas de uso**
- Margen mínimo alrededor del logo: la altura de la "p" del nombre.
- Alto mínimo del wordmark en pantalla: 20 px.
- No cambiar colores, no estirar, no añadir sombras ni degradados.
- El punto Pulso es decorativo: no usarlo para texto (contraste 2.8:1 sobre Hueso).

## Regenerar

```bash
pip install fonttools uharfbuzz cairosvg pillow
npm install @fontsource/outfit            # fuente abierta (SIL OFL 1.1)
python3 - <<'PY'
from fontTools.ttLib import TTFont
f = TTFont("node_modules/@fontsource/outfit/files/outfit-latin-600-normal.woff")
f.flavor = None
f.save("outfit-600.ttf")
PY
python3 tools/build_logo.py 600 assets/brand/logo .
```
