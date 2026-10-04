# Pacerless — Brief de marca y arquitectura de tienda

## 1. Decisiones tomadas

| Tema | Decisión | Qué implica |
|---|---|---|
| Modelo | **Productos genéricos comprados en Temu** | No hay marcas de terceros que mostrar: la marca es Pacerless. Ver [`ABASTECIMIENTO.md`](ABASTECIMIENTO.md) (riesgos y recomendación). |
| Mercado | **Perú primero, otros países después** | Base en español y soles, con la tienda preparada para Shopify Markets. |
| Catálogo | **~20 productos, faltan fotos** | Lanzamiento corto, con kits armados a partir de esos mismos productos. |
| Dirección de marca | **C (Swim · Bike · Run) con el tono de A (sereno y editorial)** | Ver [`GUIA_DE_MARCA.md`](GUIA_DE_MARCA.md). |
| Logo | **Hay que crearlo** | Brief de logo en la guía de marca. |
| Dominio | **pacerless.com** | Pendiente confirmar que esté libre y comprarlo. |
| Shopify | **Cuenta creada, sin dominio** | El desarrollo no depende del dominio, el lanzamiento sí. |

## 2. Posicionamiento

Con productos genéricos, el producto en sí no diferencia a Pacerless. Lo que sí puede diferenciarla:

- **Una marca clara:** Pacerless como marca de accesorios esenciales para quien entrena swim, bike y run.
- **Kits por objetivo:** "Mi primer 10K", "Mi primer triatlón sprint", "Día de carrera", "Aguas abiertas".
- **Triatlón como hub:** es la intersección de nadar, pedalear y correr.
- **Guía en la ficha:** para qué distancia y nivel sirve cada producto, escrito con honestidad.
- **Servicio local:** tiempos de entrega claros, garantía y atención por WhatsApp.

## 3. Arquitectura de la tienda

**Menú principal:** Triatlón · Running · Ciclismo · Natación · Kits · Guías

**Colecciones.** Todas automáticas de Shopify, basadas en tags, para que al subir un producto con los tags correctos aparezca solo donde corresponde:

| Colección | Regla (tag) |
|---|---|
| Por deporte | `deporte:running`, `deporte:ciclismo`, `deporte:natacion`, `deporte:triatlon` |
| Por tipo | `tipo:gorra`, `tipo:bolsa`, `tipo:gafas`, etc. |
| Por nivel | `nivel:inicial`, `nivel:intermedio`, `nivel:avanzado` |
| Por distancia | `distancia:5k-10k`, `distancia:21k`, `distancia:sprint`, `distancia:70.3` |

**Datos por producto (metafields):** deporte(s), nivel, distancia ideal, "para qué sirve", medidas o guía de tallas, materiales.

**Home, en este orden:**
1. Hero con una sola promesa y un solo botón.
2. Cuatro tarjetas de deporte.
3. "Arma tu kit".
4. Productos estrella.
5. Guías de entrenamiento o equipo.
6. Garantía, envíos, devoluciones.

**Ficha de producto:** galería, "ideal para" (distancia y nivel), guía de tallas o medidas, productos que se compran juntos, reseñas, tiempos de entrega y devolución visibles.

## 4. Catálogo y fotos

Catálogo de lanzamiento (~20 productos) y kits: ver [`ABASTECIMIENTO.md`](ABASTECIMIENTO.md).

**Fotos.** Las imágenes de Temu pertenecen a sus vendedores y no se deben reutilizar sin permiso. Reglas:
- **Fotos de producto:** propias (pidiendo muestras) o del proveedor con autorización.
- **Lifestyle, banners y fondos:** se pueden crear con Higgsfield o Canva.
- No generar con IA imágenes que muestren el producto "mejor" de lo que es.

## 5. Perú y expansión

- **Moneda y mercados:** define la moneda base de la tienda al inicio, porque cambiarla después es complicado. Luego se agregan países con Shopify Markets.
- **Pagos:** verifica qué pasarelas están disponibles para Perú. Lo habitual es tarjeta más Yape o Plin a través de Culqi, Niubiz, Izipay o Mercado Pago. Revisa la comisión adicional que Shopify cobra por transacción con pasarelas externas, según tu plan.
- **Comprobantes:** en Perú se necesitan boletas y facturas electrónicas (SUNAT). Shopify no las emite por sí solo; hace falta una integración o app. Confírmalo con tu contador antes de lanzar.
- **Envíos:** tarifas por zona (Lima, provincias) con Olva, Shalom o Urbaner. Define un monto de envío gratis.
- **Marca:** revisa disponibilidad del nombre Pacerless en INDECOPI y los usuarios en redes antes de invertir en identidad.

## 6. Dominio: pacerless.com

No pude comprobar desde esta sesión si está libre (la consulta fue bloqueada). Para confirmarlo:
1. En el admin de Shopify: Configuración → Dominios → buscar `pacerless.com`. O consultar en un registrador (Namecheap, GoDaddy, etc.).
2. Si está libre, comprarlo (en Shopify o en un registrador) y conectarlo como dominio principal.
3. Si está ocupado, alternativas: `pacerless.pe`, `pacerless.com.pe`, `getpacerless.com`, `pacerlessstore.com`.
4. Configurar correo del dominio (por ejemplo `hola@pacerless.com`).

## 7. Hoja de ruta

| Fase | Entregable | Estado |
|---|---|---|
| 0. Base | Dirección de marca, dominio, tipo de producto | Hecha (falta comprar el dominio) |
| 1. Marca | Paleta, tipografías, tono de voz, logo | Guía lista; falta crear el logo |
| 2. Diseño | Maquetas de home, colección y ficha (Figma o Canva) | Pendiente |
| 3. Tema | Tema base de Shopify personalizado en este repo | Pendiente |
| 4. Catálogo | ~20 fichas con tags y metafields, kits, importación por CSV | Pendiente |
| 5. Configuración | Pagos, envíos, impuestos, comprobantes, políticas, dominio | Pendiente |
| 6. Lanzamiento | Pruebas de compra, emails automáticos, SEO, anuncio | Pendiente |
