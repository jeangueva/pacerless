# Pacerless — Plan de tienda Shopify

Tienda de accesorios y productos para **triatlón, running, natación y ciclismo**.

## Idea central

Pacerless vende cuatro deportes, pero **el triatlón los une** (nadar + pedalear + correr).
Eso lo diferencia de una tienda genérica de deportes: el triatlón es el hub de la marca y los otros tres deportes son entradas.

## Referencias y qué tomar de cada una

| Referencia | Qué copiar |
|---|---|
| Tracksmith | Tono editorial, historias, tipografía cuidada. Marca premium sin ser cara. |
| Bandit Running | Comunidad, color y energía. Todo se siente hecho por runners. |
| Gymshark | Atletas y comunidad como motor, "drops", colecciones por objetivo. |
| Triangl | Fotografía limpia, fondos simples, un solo color de acento. Referencia para natación. |
| Aventon / State Bicycle | Fichas técnicas con comparadores, guía de tallas y financiamiento (bicis y productos caros). |
| Peloton / Crossrope | Kits y bundles, "elige tu nivel", contenido de entrenamiento unido a la venta. |
| Alo Yoga (es-pe) | Experiencia en español y para Perú, lifestyle y estética premium. |

## Arquitectura de la tienda

**Navegación:** Triatlón (hub) · Running · Ciclismo · Natación · Kits · Ofertas.
Dentro de cada deporte: filtros por tipo de producto, distancia o nivel, y clima o condición.

**Home (en este orden):**
1. Hero con una sola promesa y un solo botón.
2. Cuatro tarjetas de deporte.
3. "Arma tu kit": primer 10K, primer sprint triatlón, 70.3.
4. Productos estrella con reseñas.
5. Contenido y comunidad (planes de entrenamiento, atletas, carreras).
6. Garantía, envíos y devoluciones.

**Ficha de producto:** galería con video corto, guía de tallas o compatibilidad, "ideal para…" (distancia y nivel), productos que se compran juntos, reseñas con foto.

**Lo que más sube la venta:** kits y bundles con descuento escalonado, envío gratis sobre un monto, quiz corto tipo "¿qué necesitas para tu primera carrera?".

## Cómo trabajar con Claude

1. **Marca y estrategia:** brief, tono de voz, paleta, tipografías, estructura de catálogo y colecciones.
2. **Diseño:** maquetas en Figma o Canva. Imágenes y video de producto o lifestyle con Higgsfield.
3. **Tema de Shopify:** partir de un tema oficial (Horizon o Dawn) y personalizarlo con Claude Code y Shopify CLI. Código Liquid en un repo con git, con vista previa, sin tocar la tienda en vivo hasta aprobar.
4. **Catálogo:** importación masiva con CSV o la Admin API. Títulos, descripciones, SEO, handles y tags (adaptar la skill de fichas para Shopify a Pacerless).
5. **Configuración:** checklist paso a paso para lo que se hace en el admin (pagos, envíos, impuestos, dominio, políticas).
6. **Crecimiento:** emails automáticos (carrito abandonado, bienvenida, post-compra), SEO de colecciones, textos de anuncios y contenido para Instagram.

**Apps:** pocas, porque cada una ralentiza la tienda. Reseñas, email (Klaviyo o Shopify Email), bundles y, si hace falta, buscador o filtros.

**Si se vende en Perú:** pagos con tarjeta más Yape o Plin (Culqi, Niubiz o Mercado Pago), tarifas de envío por zona (Olva, Shalom, Urbaner) y moneda en soles.

## Decisiones tomadas

1. Modelo de negocio: **marcas de terceros**.
2. Mercado: **Perú primero, otros países después**.
3. Catálogo: **~20 productos al inicio, faltan fotos**.
4. Identidad: **se parte de cero**.
5. Estado de Shopify: **cuenta creada, sin dominio**.

## Siguiente paso

Primer entregable listo: [`BRIEF_MARCA_Y_ARQUITECTURA.md`](BRIEF_MARCA_Y_ARQUITECTURA.md) (marca, navegación, colecciones, home, kits y hoja de ruta). Siguiente: elegir dirección de marca, marcas y productos, y dominio.
