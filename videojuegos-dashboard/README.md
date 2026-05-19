# 🎮 Dashboard de Videojuegos

Un dashboard interactivo desarrollado con **Flask** que visualiza datos fascinantes sobre la industria de los videojuegos, incluyendo ventas por región, plataformas populares, géneros, calificaciones y más.

## 📋 Características

### Sección 1: Inicio
- Nombre y descripción del sistema
- Menú de navegación intuitivo
- Tarjetas de estadísticas generales
- Información sobre el dashboard

### Sección 2: Análisis Dinámico
- **Ventas por Región**: Gráfico de dona mostrando ventas en América del Norte, Europa, Japón y otros
- **Top 10 Plataformas**: Gráfico de barras horizontal con las plataformas más exitosas
- **Ventas por Género**: Gráfico de barras con géneros ordenados por ventas
- **Distribución de Calificaciones ESRB**: Gráfico de barras con calificaciones (E, T, M, AO, etc.)
- **Puntuaciones de Críticos**: Gráfico de pastel mostrando distribución de calificaciones
- **Top 15 Editores**: Gráfico de barras con los editores más exitosos

### Sección 3: Catálogo de Videojuegos
- **Filtros Avanzados**: Por plataforma, género y editor
- **Tabla Interactiva**: Visualización de todos los videojuegos con información detallada
- **Paginación**: Navegación eficiente entre páginas (50 juegos por página)
- **Información Completa**: Plataforma, género, editor, ventas por región, ventas globales, calificación y puntuación de críticos

### Sección 4: Documentación de API
- **Página Interactiva**: Documentación completa de todos los endpoints
- **Pruebas en Tiempo Real**: Probar cada endpoint directamente desde el navegador
- **Ejemplos de Respuestas**: Ver formato JSON de cada endpoint
- **Información de Parámetros**: Detalles sobre parámetros requeridos y opcionales

## 🏗️ Estructura del Proyecto

```
videojuegos-dashboard/
├── app.py                          # Aplicación principal Flask con API
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este archivo
├── API_DOCUMENTATION.md            # Documentación completa de la API
└── app/
    ├── templates/                  # Plantillas HTML
    │   ├── base.html              # Template base con navbar y footer
    │   ├── index.html             # Página de inicio
    │   ├── analytics.html         # Página de análisis
    │   ├── games.html             # Página de catálogo
    │   └── api_docs.html          # Documentación interactiva de API
    └── static/
        ├── css/
        │   └── style.css          # Estilos principales
        ├── js/
        │   └── main.js            # JavaScript utilitario
        └── data/
            └── dato.csv           # Base de datos de videojuegos
```

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd videojuegos-dashboard
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Acceder al dashboard**
   - Abre tu navegador y ve a: `http://localhost:5000`

## 🎨 Tecnologías Utilizadas

### Backend
- **Flask**: Framework web ligero y flexible
- **Pandas**: Procesamiento y análisis de datos
- **Python**: Lenguaje de programación

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos y responsive
- **JavaScript**: Interactividad del lado del cliente
- **Chart.js**: Visualización de gráficos interactivos

### Datos
- **CSV**: Formato de almacenamiento de datos

## 📊 Endpoints de la API

### Estadísticas Generales
- `GET /api/v1/stats` - Obtener estadísticas generales del dashboard
- `GET /api/v1/health` - Verificar el estado de la API

### Análisis de Datos
- `GET /api/v1/sales-by-region` - Ventas por región
- `GET /api/v1/top-platforms` - Top 10 plataformas
- `GET /api/v1/top-genres` - Géneros ordenados por ventas
- `GET /api/v1/top-publishers` - Top 15 editores
- `GET /api/v1/rating-distribution` - Distribución de calificaciones ESRB
- `GET /api/v1/critic-score-distribution` - Distribución de puntuaciones de críticos

### Videojuegos
- `GET /api/v1/games` - Lista de videojuegos con filtros y paginación
  - Parámetros: `platform`, `genre`, `publisher`, `page`, `per_page`
- `GET /api/v1/filters` - Opciones disponibles para filtros

### Estadísticas Específicas
- `GET /api/v1/platform-stats/<platform>` - Estadísticas de una plataforma
- `GET /api/v1/genre-stats/<genre>` - Estadísticas de un género
- `GET /api/v1/publisher-stats/<publisher>` - Estadísticas de un editor

### Búsqueda y Documentación
- `GET /api/v1/search` - Búsqueda avanzada por criterios
- `GET /api/v1/docs` - Documentación completa de la API

## 🎯 Funcionalidades Principales

### 1. Visualización de Datos
- Gráficos interactivos usando Chart.js
- Múltiples tipos de gráficos (barras, dona, pastel)
- Datos actualizados en tiempo real

### 2. Filtrado Avanzado
- Filtrar por plataforma, género y editor
- Combinación de múltiples filtros
- Búsqueda instantánea

### 3. Paginación Eficiente
- 50 videojuegos por página
- Navegación entre páginas
- Información de página actual

### 4. Diseño Responsive
- Adaptable a dispositivos móviles
- Interfaz intuitiva y moderna
- Colores y tipografía profesionales

### 5. API RESTful Propia
- Endpoints bien estructurados con versionado
- Respuestas JSON consistentes
- Validación de parámetros
- Manejo robusto de errores
- Documentación interactiva

## 📱 Diseño Responsive

El dashboard está completamente optimizado para:
- **Desktop**: Experiencia completa con todos los gráficos
- **Tablet**: Diseño adaptado con grid fluido
- **Móvil**: Interfaz simplificada y fácil de navegar

## 🎨 Paleta de Colores

- **Primario**: #6366f1 (Índigo)
- **Secundario**: #ec4899 (Rosa)
- **Éxito**: #10b981 (Verde)
- **Advertencia**: #f59e0b (Ámbar)
- **Peligro**: #ef4444 (Rojo)
- **Información**: #3b82f6 (Azul)

## 📈 Estadísticas Disponibles

- Total de videojuegos en la base de datos
- Número de plataformas únicas
- Cantidad de géneros
- Cantidad de editores
- Ventas globales totales
- Distribución de ventas por región
- Calificaciones ESRB más comunes
- Puntuaciones de críticos

## 🔌 API Propia Desarrollada

El proyecto incluye una **API RESTful completa** desarrollada con Flask que maneja:

### Características de la API

✅ **Rutas Estructuradas**: Endpoints bien organizados con versioning (`/api/v1/`)
✅ **Respuestas Consistentes**: Todas las respuestas siguen un formato JSON estándar
✅ **Manejo de Errores**: Códigos de estado HTTP apropiados y mensajes de error descriptivos
✅ **Validación de Parámetros**: Validación automática de entrada
✅ **Documentación Interactiva**: Página de documentación con pruebas en tiempo real
✅ **Compatibilidad**: Endpoints legacy para compatibilidad hacia atrás

### Acceder a la Documentación de la API

Una vez que el servidor está corriendo, puedes acceder a la documentación interactiva en:

```
http://localhost:5000/api-docs
```

Desde ahí puedes:
- Ver todos los endpoints disponibles
- Probar cada endpoint en tiempo real
- Ver ejemplos de respuestas
- Entender los parámetros requeridos y opcionales

### Ejemplo de Uso de la API

```bash
# Obtener estadísticas generales
curl http://localhost:5000/api/v1/stats

# Obtener top 5 plataformas
curl "http://localhost:5000/api/v1/top-platforms?limit=5"

# Obtener videojuegos de PS2
curl "http://localhost:5000/api/v1/games?platform=PS2&page=1&per_page=10"

# Buscar plataformas con "PS"
curl "http://localhost:5000/api/v1/search?q=PS&type=platform"
```

Para más información, consulta el archivo `API_DOCUMENTATION.md`.

## 🔧 Configuración

### Variables de Entorno
Actualmente, la aplicación no requiere variables de entorno especiales. Todos los datos se cargan desde el archivo CSV.

### Personalización
- Modifica `app/static/css/style.css` para cambiar colores y estilos
- Edita `app/templates/` para modificar la estructura HTML
- Actualiza `app.py` para agregar nuevas rutas o funcionalidades

## 📝 Notas Importantes

- La base de datos se carga en memoria al iniciar la aplicación
- Los datos se procesan automáticamente para convertir formatos de números
- La aplicación está configurada para ejecutarse en `localhost:5000`
- El modo debug está habilitado para desarrollo
- La API implementa validación de parámetros y manejo de errores robusto
- Todos los endpoints retornan respuestas JSON estructuradas
- Los endpoints legacy (`/api/...`) se mantienen para compatibilidad

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solución**: Instala las dependencias con `pip install -r requirements.txt`

### Error: "Port 5000 already in use"
**Solución**: Cambia el puerto en `app.py` modificando `port=5000` a otro puerto disponible

### Los datos no se cargan
**Solución**: Verifica que el archivo `dato.csv` esté en `app/static/data/`

### Error en la API
**Solución**: Verifica el estado de la API visitando `http://localhost:5000/api/v1/health`

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

## 👨‍💻 Autor

Desarrollado como un proyecto de dashboard interactivo de videojuegos con API RESTful propia.

---

**¡Disfruta explorando los datos de videojuegos!** 🎮
