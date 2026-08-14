📊 Monitoreo de Sensores UTEQ
Sistema web para monitoreo en tiempo real de sensores ambientales en el Campus La María de la Universidad Técnica Estatal de Quevedo (UTEQ).

🚀 Características
Dashboard de Sensores: Visualiza datos en tiempo real de temperatura, humedad y otros parámetros ambientales
Gestión de Ubicaciones: Navega entre diferentes sensores distribuidos en el campus
Interfaz Responsiva: Diseño optimizado para desktop y dispositivos móviles
Integración Firebase: Backend en la nube para almacenamiento y sincronización de datos
Routing Dinámico: Navegación fluida entre sensores usando React Router
Localización: Formatos de fecha y hora adaptados a la zona horaria de Ecuador (America/Guayaquil)
🛠️ Stack Tecnológico
React 19.2 - Librería UI moderna
Vite 8.2 - Build tool de alto rendimiento
Firebase 12.17 - Backend y base de datos en la nube
React Router DOM 7.18 - Enrutamiento de aplicación
Oxlint - Linting de código
ESLint & TypeScript - Tipado estático y validación de código
📁 Estructura del Proyecto
.
├── public/                 # Activos estáticos y recursos públicos
│   └── screenshots/        # Capturas de pantalla de la aplicación
├── src/
│   ├── components/         # Componentes reutilizables
│   │   ├── Navbar.jsx      # Barra de navegación
│   │   └── SensorCard.jsx  # Tarjeta para mostrar datos de sensores
│   ├── pages/              # Páginas principales
│   │   ├── Dashboard.jsx   # Vista principal con datos del sensor
│   │   └── Ubicaciones.jsx # Página de selección de sensores
│   ├── hooks/              # Hooks personalizados
│   │   └── useSensorData.js # Hook para obtener datos de sensores
│   ├── services/           # Servicios externos
│   │   └── firebase.js     # Configuración y funciones Firebase
│   ├── App.jsx             # Componente raíz
│   ├── main.jsx            # Punto de entrada de la aplicación
│   └── styles.css          # Estilos globales
├── index.html              # Archivo HTML principal
├── package.json            # Dependencias y scripts del proyecto
├── vite.config.js          # Configuración de Vite
└── README.md               # Este archivo
⚙️ Instalación y Configuración
Requisitos Previos
Node.js 18+
npm o yarn
Pasos de Instalación
Clonar el repositorio

git clone <repository-url>
cd monitoreo-sensores-uteq
Instalar dependencias

npm install
Configurar Firebase

Actualiza las credenciales en src/services/firebase.js con tu proyecto Firebase
Iniciar servidor de desarrollo

npm run dev
📝 Scripts Disponibles
npm run dev - Inicia el servidor de desarrollo con HMR
npm run build - Compila la aplicación para producción
npm run preview - Vista previa de la compilación de producción
npm run lint - Ejecuta Oxlint para validar el código
🔗 Rutas de la Aplicación
Ruta	Descripción
/	Redirecciona al primer sensor disponible
/sensor/:sensorId	Dashboard con datos del sensor especificado
/ubicaciones	Página para seleccionar y ver todos los sensores
*	Redirecciona a /ubicaciones (página 404)
📱 Componentes Principales
Dashboard.jsx
Página principal que muestra:

Información del sensor (nombre, zona, estado de conexión)
Tarjetas con valores actuales (temperatura, humedad, etc.)
Datos históricos del sensor
Opciones para cambiar de sensor
SensorCard.jsx
Componente para mostrar:

Icono del parámetro
Título del parámetro
Valor actual y unidad de medida
Navbar.jsx
Barra de navegación principal de la aplicación

🎨 Diseño y Estilos
Archivo principal de estilos: src/styles.css
Estilos del componente App: src/App.css
Estilos globales: src/index.css
🚢 Deployment
Para compilar la aplicación para producción:

npm run build
Los archivos compilados se generarán en la carpeta dist/

📞 Soporte
Para reportar problemas o sugerencias, contacta al equipo de desarrollo de UTEQ.
