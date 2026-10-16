# TOKENIA
Calculadora compartible de tokens y costos de API. Paleta inspirada en Avengers, Times New Roman. TOKENIA + VizData.

## Uso
Abre `index.html` con doble clic. Es un HTML autónomo, sin servidor y sin dependencias externas para tokenizar y calcular. Carga entrada y una muestra de salida, elige modelos, tarifas, volúmenes y moneda. Los textos quedan en tu navegador. Puedes exportar tu proyecto y un informe HTML.

OpenAI: js-tiktoken 1.0.21, o200k_base, solo los cuatro modelos documentados. Claude/Gemini y modelos personalizados: conteos nativos aportados por usuario; filas pendientes si faltan datos. Las tarifas iniciales proceden de la muestra del 09/10/2026: verifica vigencia y modalidad antes de presupuestar. Cálculo decimal con decimal.js 10.6.0. La salida es una muestra y no predice razonamiento interno ni factura completa.

## FIX Banxico
El HTML incluye la última copia verificada de SF43718 con fecha y fuente. Al abrirlo sin conexión conserva esa copia y permite cargar un archivo FIX JSON. El origen de un archivo aportado por usuario no se verifica automáticamente.

La web lee `fx.json` al abrir y cada hora. El flujo GitHub Actions consulta Banxico y publica el dato a las 01:17, 13:17 y 19:17 UTC (horarios orientativos; GitHub puede retrasar ejecuciones). Configura `BANXICO_TOKEN` como **secreto de Actions del repositorio**, nunca como archivo ni código HTML. Sin el secreto, se conserva el FIX original y su fecha. Los secretos no se incluyen en el sitio. La descarga del HTML conserva la copia incorporada al archivo; la web muestra la copia publicada más reciente. Las tarifas de modelos no se actualizan automáticamente.

## Publicación
Repositorio esperado: `marianaog30/tokenia`. Rama `main`. En Settings → Pages, usa **GitHub Actions** como fuente de publicación. El flujo `pages.yml` carga exclusivamente index.html, fx.json, LICENSES.txt y .nojekyll. No publica los textos que cargue cada visitante ni credenciales.

## Verificación
`validacion.json` registra comprobaciones de conteos, SHA-256, costes y conversión. Ejemplo: 61 entrada y 3142 salida a 0.15/0.60 USD por millón → 18.9435 USD por 10,000 llamadas; FIX 18.4163 → 348.86917905 MXN. Se redondea al presentar.


## Personalización y selección de modelos
Actualización del 16/10/2026: usa Motor / modelo para elegir qué modelo editar. Al elegirlo se añade a la comparación; los botones superiores permiten volver a los ya incluidos. Puedes excluirlo con la casilla o comparar solo el modelo seleccionado. El catálogo mantiene modelos disponibles al abrir proyectos anteriores.

En Haz TOKENIA tuyo puedes elegir Avengers, Rubí, Bosque u Océano, el usuario final o cliente y el uso personal, de cliente, equipo o académico. No crea una cuenta ni autenticación. La configuración se guarda en el JSON; la descarga de la calculadora incorpora nombre y temática, mientras que los textos del proyecto se conservan por separado en Guardar proyecto. El informe HTML también conserva nombre y temática.

Validación: importación de proyecto anterior con 16/48 tokens y USD 0.3120 por 10,000 llamadas; catálogo de seis modelos; selección de Gemini con conteos pendientes; cuatro paletas; JSON exportado con preferencias; HTML personalizado reabierto con Cliente de prueba y Rubí; informe HTML con nombre y paleta.
