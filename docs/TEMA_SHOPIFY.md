# Pacerless — Tema de Shopify: base y flujo de trabajo

## Decisiones

- Se trabaja **directo en código**, sin pasar por Figma.
- Base: **Tinker 4.2.0**, exportado de la tienda `pacerless-deqmxxns.myshopify.com` el 04/10/2026. Está en [`theme/`](../theme), sin cambios en el primer commit del tema.

## Las tres plantillas evaluadas

| | Debut (vintage) 17.1.0 | Tinker 4.2.0 | Horizon 4.2.0 |
|---|---|---|---|
| Arquitectura | Antigua: plantillas `.liquid`, sin bloques | Moderna: plantillas JSON y bloques | Igual que Tinker |
| Tamaño | 148 archivos | 481 archivos | 481 archivos |
| Estilo de fábrica | Clásico | Titulares serif (Instrument Serif) y cuerpo Instrument Sans, h1 de 72 px, esquinas de 10 px | Inter en todo, página angosta, h1 de 56 px, botones con esquinas de 14 px |
| Home de fábrica | Secciones antiguas | Hero, lista de productos, medio con contenido, lista de colecciones | Hero y lista de productos |
| Decisión | Descartada | **Elegida** | Referencia |

- **Tinker y Horizon comparten el mismo código** (42 secciones, 95 bloques, 145 snippets, 125 assets). Solo difieren 16 archivos de configuración: `settings_data.json`, `settings_schema.json`, los grupos de cabecera y pie, y las plantillas JSON. Cambiar de uno a otro es solo cambiar esa configuración.
- El Horizon exportado es el mismo que `Shopify/horizon` en GitHub (versión 4.2.0); solo difiere en líneas en blanco.
- **Por qué Tinker:** su home ya trae cuatro de las seis secciones planeadas: hero, "Arma tu kit" (lista de productos), guías (medio con contenido) y deportes (lista de colecciones). Su tipografía serif encaja con el tono editorial de la marca.
- **Por qué no Debut:** es un tema antiguo, sin bloques y sin plantillas JSON, que limita lo que se puede construir.

## Estructura del repo

```
theme/          tema de Shopify (la carpeta assets/ de un tema debe ser plana)
docs/           plan, brief, guía de marca, abastecimiento y este documento
assets/brand/   logo (SVG y PNG)
tools/          scripts auxiliares
```

## Validación

```bash
npm install @shopify/cli
shopify theme check --path theme
```

Resultado de la base sin cambios: **358 archivos, 6 avisos**, todos de origen Shopify: `ExcessiveSettingsCount` en `sections/header.liquid` y cinco `UnusedDocParam` en `snippets/divider.liquid`. La meta es no sumar avisos nuevos.

## Flujo de trabajo

1. Claude edita el tema en esta rama y lo valida con Theme Check.
2. El tema se sincroniza con Shopify mediante la integración de GitHub (Tienda online → Temas → Añadir tema → Conectar desde GitHub), eligiendo este repo y rama. Si la integración no admite la subcarpeta `theme/`, se publica el tema en la raíz de una rama aparte.
3. Se revisa la vista previa del tema en Shopify y se comparten capturas.
4. Se ajusta y se repite.

Alternativa para ver los cambios en vivo en tu computadora: `shopify theme dev --path theme`.

## Qué enviar de las referencias

Capturas de pantalla completas (por ejemplo en un PDF, como el de los logos). Con cuatro o cinco marcas basta. Por marca:
- Home completa en escritorio y en móvil.
- Una página de colección.
- Una ficha de producto.
- Una o dos líneas con lo que más te gusta de esa marca.

No se copia código ni diseño de las marcas de referencia: se estudian patrones de distribución, jerarquía, espaciado y tono.

## Límites del entorno de Claude

Desde la sesión de Claude no se puede acceder a `shopify.dev`, `myshopify.com`, el admin ni los sitios de referencia (los bloquea la red del entorno). Claude puede escribir y validar el código, pero no ver el resultado renderizado: ese ciclo depende de las capturas de la vista previa. Para cambiarlo hay que permitir esos dominios en la configuración de red del entorno (Network access → Custom → Allowed domains), en una sesión nueva.
