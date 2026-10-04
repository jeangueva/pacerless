# Pacerless — Brief de marca y arquitectura de tienda

## 1. Decisiones tomadas

| Tema | Decisión | Qué implica |
|---|---|---|
| Modelo | **Marcas de terceros** | Somos un retailer curado. La ventaja no es el producto sino la **selección, la guía y los kits**. |
| Mercado | **Perú primero, otros países después** | Base en español y soles, pero con la tienda preparada para Shopify Markets. |
| Catálogo | **~20 productos, faltan fotos** | Lanzamiento corto y bien curado, con kits armados a partir de esos mismos productos. |
| Identidad | **Parte de cero** | Hay que definir concepto, tono, paleta y tipografías antes de diseñar el tema. |
| Shopify | **Cuenta creada, sin dominio** | El dominio no bloquea el desarrollo (se trabaja con la URL de Shopify), pero sí el lanzamiento. |

## 2. Posicionamiento

Al vender marcas de terceros, competimos contra marketplaces y tiendas grandes. Pacerless gana si se siente como **un entrenador que te arma el equipo**, no como un catálogo:

- **Curación:** pocos productos, cada uno elegido por una razón escrita ("por qué lo elegimos").
- **Kits por objetivo:** "Mi primer 10K", "Mi primer triatlón sprint", "Día de carrera", "Aguas abiertas".
- **Triatlón como hub:** es la intersección de nadar, pedalear y correr, y nadie en Perú lo cuenta bien.
- **Guía en la ficha:** para qué distancia y nivel sirve cada producto.

## 3. Identidad: tres direcciones para elegir

El nombre **Pacerless** ("sin liebre", sin marcapasos) sugiere correr tu propio ritmo. Sobre eso, tres caminos:

| | A. Tu ritmo | B. Sin liebre | C. Swim · Bike · Run |
|---|---|---|---|
| Idea | Cada atleta marca su propio ritmo. | Comunidad y energía, sin que nadie te marque el paso. | El triatlón como eje de todo. |
| Referencias | Tracksmith, Alo Yoga | Bandit, Gymshark | Triangl, Crossrope |
| Tono | Sereno, editorial, cuidado | Directo, enérgico, cercano | Claro, técnico, minimalista |
| Visual | Fondos claros, tipografía con carácter, mucho aire | Color fuerte, fotos de comunidad | Un solo color de acento, producto sobre fondo limpio |
| Riesgo | Puede sentirse frío o caro | Puede sentirse genérico | Puede dejar fuera al runner o nadador "solo" |

**Recomendación:** base **C** (por el hub de triatlón) con el tono de **A**. Es la combinación más fácil de sostener con un catálogo de terceros, porque no depende de tener atletas propios ni producción de contenido pesada.

Tono de voz propuesto: segunda persona ("tú"), frases cortas, técnico pero sin jerga, sin exageraciones. Ejemplo: "Para tu primer 10K no necesitas más que esto."

## 4. Arquitectura de la tienda

**Menú principal:** Triatlón · Running · Ciclismo · Natación · Kits · Marcas · Guías

**Colecciones.** Todas deberían ser colecciones automáticas de Shopify basadas en tags, para que al subir un producto con los tags correctos aparezca solo donde corresponde:

| Colección | Regla (tag) |
|---|---|
| Por deporte | `deporte:running`, `deporte:ciclismo`, `deporte:natacion`, `deporte:triatlon` |
| Por tipo | `tipo:gafas`, `tipo:casco`, `tipo:nutricion`, etc. |
| Por nivel | `nivel:inicial`, `nivel:intermedio`, `nivel:avanzado` |
| Por distancia | `distancia:5k-10k`, `distancia:21k`, `distancia:sprint`, `distancia:70.3` |
| Por marca | `marca:<nombre>` |

**Datos por producto (metafields):** marca, deporte(s), nivel, distancia ideal, "por qué lo elegimos", compatibilidad o guía de tallas.

**Home, en este orden:**
1. Hero con una sola promesa y un solo botón.
2. Cuatro tarjetas de deporte.
3. "Arma tu kit".
4. Productos estrella.
5. Guías de entrenamiento o equipo.
6. Garantía, envíos, devoluciones.

**Ficha de producto:** galería, "ideal para" (distancia y nivel), "por qué lo elegimos", guía de tallas o compatibilidad, productos que se compran juntos, reseñas.

## 5. Catálogo de lanzamiento (~20 productos)

Distribución sugerida: unos 4 a 5 productos por deporte, más el triatlón con productos propios (los que solo ese deporte necesita). Las marcas y productos concretos los defines tú.

| Deporte | Tipos de producto a considerar |
|---|---|
| Natación | Gafas, gorro, antiempañante, bolsa estanca, boya de aguas abiertas |
| Running | Cinturón de hidratación, gorra, calcetines, nutrición (geles), lentes |
| Ciclismo | Casco, luces, bidones, kit de reparación, bomba, guantes |
| Triatlón | Cinturón porta-número, cordones elásticos, bolsa de transición, lubricante antirozaduras |

**Kits.** Los kits son bundles hechos con esos mismos productos (no son productos nuevos), con descuento por llevar el conjunto:
- Mi primer 10K
- Mi primer triatlón sprint
- Día de carrera
- Aguas abiertas

## 6. Fotos de producto

Como vendes marcas de terceros, la regla es:

- **Fotos de producto:** usar las que entregue la marca o el distribuidor (material de prensa), con su autorización. No generar imágenes de productos de terceros con IA, porque pueden mostrar algo que el producto no es.
- **Lifestyle, banners y fondos:** sí se pueden crear con Higgsfield o Canva (atletas, escenas de entrenamiento, banners de colecciones).
- **Fotos propias:** vale la pena hacerlas para los 5 a 8 productos estrella.

## 7. Perú y expansión

- **Moneda y mercados:** define la moneda base de la tienda al inicio, porque cambiarla después es complicado. Luego se agregan países con Shopify Markets.
- **Pagos:** verifica qué pasarelas están disponibles para Perú. Lo habitual es tarjeta más Yape o Plin a través de Culqi, Niubiz, Izipay o Mercado Pago. Revisa la comisión adicional que Shopify cobra por transacción con pasarelas externas, según tu plan.
- **Comprobantes:** en Perú se necesitan boletas y facturas electrónicas (SUNAT). Shopify no las emite por sí solo; hace falta una integración o app. Conviene confirmarlo con tu contador antes de lanzar.
- **Envíos:** tarifas por zona (Lima, provincias) con Olva, Shalom o Urbaner. Define un monto de envío gratis.
- **Marca:** antes de invertir en identidad, revisa disponibilidad del nombre Pacerless como marca (INDECOPI), dominio y usuarios en redes.

## 8. Dominio

Se puede construir todo sin dominio, usando la URL de la tienda en Shopify. Hay que resolverlo antes de lanzar:
1. Revisar disponibilidad de `pacerless.com`, `pacerless.pe` o `pacerless.com.pe`.
2. Comprarlo (en Shopify o en un registrador) y conectarlo como dominio principal.
3. Configurar correo del dominio (por ejemplo `hola@pacerless...`).

## 9. Hoja de ruta

| Fase | Entregable |
|---|---|
| 0. Base | Elegir dirección de marca, nombre/dominio, lista de marcas y productos. |
| 1. Marca | Paleta, tipografías, tono de voz, logo (si falta), guía de estilo. |
| 2. Diseño | Maquetas de home, colección y ficha (Figma o Canva). |
| 3. Tema | Tema base de Shopify personalizado en este repo, con vista previa. |
| 4. Catálogo | ~20 fichas con tags y metafields, kits, importación por CSV. |
| 5. Configuración | Pagos, envíos, impuestos, comprobantes, políticas, dominio. |
| 6. Lanzamiento | Pruebas de compra, emails automáticos, SEO, anuncio. |

## 10. Lo que necesito de ti para seguir

1. **Dirección de marca:** A, B, C o la combinación recomendada (C con tono de A).
2. **Marcas y productos:** qué marcas vas a vender y si ya tienes la lista de los ~20 productos con precios.
3. **Logo:** si ya existe alguno o hay que crearlo.
4. **Dominio:** cuál prefieres comprar.
