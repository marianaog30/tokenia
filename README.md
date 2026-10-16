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

Actualización del 16/10/2026. Configura tu informe incluye Proyecto, ¿Para quién es el informe? y Temática del informe. Los destinatarios son Dirección de operaciones, Dirección general, Finanzas y presupuesto, Equipo técnico, Cliente, Audiencia académica o Uso personal. Las temáticas son Académica, Ejecutiva, Financiera, Técnica y Comercial. Cambian el objetivo y las notas de lectura del informe, conservando los mismos cálculos. El nombre opcional y la paleta visual están en un desplegable adicional. La selección se guarda en el JSON y en la calculadora descargada; el contexto seleccionado también aparece en el informe HTML exportado. No crea una cuenta ni autenticación.

Motor / modelo elige qué modelo editar y lo añade a la comparación. Los botones de modelos incluidos permiten volver a ellos. Puedes excluir un modelo con la casilla o comparar solo el seleccionado. Abrir un proyecto anterior mantiene el catálogo disponible.

Validación: proyecto anterior con 16/48 tokens y USD 0.3120 por 10,000 llamadas; desplegable de seis modelos; selección de Gemini con conteos pendientes; cuatro paletas; exportación y reapertura de HTML personalizado; informe para Finanzas con temática Financiera que incluye Control del presupuesto y conserva los mismos importes.

La paleta visual de Avengers se mantiene fija por indicación de Mariana Orozco. Los proyectos con otras paletas se adaptan a Avengers al abrirse. Los desplegables de destinatario y temática del informe permanecen disponibles.

## Tarifas de Claude y Gemini verificadas el 16 de octubre de 2026
Claude Opus 5: entrada 5 y salida 25 USD por millón. Gemini 2.5 Pro: entrada 1.25 y salida 10 USD por millón hasta 200,000 tokens de entrada; al superar ese umbral, 2.5 y 15. Fuente solicitada: GPT for Work; contraste oficial de Anthropic y Google. API estándar sin caché ni Batch.

Las tarifas no cambiaron frente a la muestra original; se verificó de nuevo su vigencia y se agregó trazabilidad visible en cada modelo. El botón Aplicar tarifas verificadas permite llevarlas a un proyecto guardado sin sustituir automáticamente sus tarifas editadas. La fuente no cuenta los tokens nativos de los textos de un proyecto. Sus valores iniciales 100 de entrada y 500 de salida son datos de ejemplo y no se reutilizan como medición. Los conteos siguen pendientes hasta aportarlos del proveedor.

## Tabla comparativa
La tabla agrupa las filas por escenario y muestra tokens de entrada/salida por modelo, costo por llamada, volúmenes y diferencia respecto al menor costo. La moneda aparece en el título de tabla. El menor costo se identifica con ▲ y una etiqueta textual. Se eliminó la información del tokenizador de esta tabla; el método y la evidencia siguen disponibles en la sección de auditoría. Los conteos faltantes permanecen pendientes. La tabla es desplazable con teclado y conserva encabezados y grupos al exportarse al informe HTML.

## Reserva de presupuesto
La A inspirada en Avengers se llena con el porcentaje restante del presupuesto para el modelo, escenario y volumen elegidos. Define importe y moneda USD/MXN; MXN usa el FIX con fecha visible. Muestra reserva, consumo y déficit. Sin presupuesto o conteos completos, indica pendiente. Guarda la configuración en el proyecto JSON y la vista en el informe HTML. El porcentaje es una proyección textual, no consumo facturado.

## Descarga PDF
El botón Descargar informe PDF genera directamente un archivo local con presupuesto, tabla comparativa, sensibilidad, fuentes, fecha FIX y textos originales. No requiere servidor de PDF ni envía los textos a terceros. Usa jsPDF 4.2.1 y jsPDF-AutoTable 5.0.9 integrados en el HTML. Páginas A4 horizontales y texto seleccionable; símbolos fuera de la fuente Times se sustituyen por [símbolo], sin alterar los conteos originales. Conserva el JSON para los originales exactos.
