# 📚 Documentación Completa de la API

## Información General

| Propiedad | Valor |
|-----------|-------|
| **Nombre** | Videojuegos Dashboard API |
| **Versión** | 1.0.0 |
| **Descripción** | API RESTful para acceder a datos de videojuegos, ventas por región, plataformas y más |
| **Base URL** | `http://localhost:5000` |
| **Formato de Respuesta** | JSON |

---

## Estructura de Respuestas

Todas las respuestas de la API siguen un formato consistente:

### Respuesta Exitosa (200 OK)
```json
{
  "status": "success",
  "data": {
    "key": "value"
  }
}
```

### Respuesta de Error (4xx, 5xx)
```json
{
  "status": "error",
  "message": "Descripción del error",
  "code": 400
}
```

---

## Endpoints de la API

### 1. Documentación de la API

#### GET `/api/v1/docs`
Obtiene la documentación completa de todos los endpoints disponibles.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "api": {
    "title": "Videojuegos Dashboard API",
    "version": "1.0.0",
    "description": "API para acceder a datos de videojuegos",
    "base_url": "http://localhost:5000",
    "timestamp": "2026-05-19T22:30:00"
  },
  "endpoints": { ... }
}
```

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/docs
```

---

### 2. Estadísticas Generales

#### GET `/api/v1/stats`
Obtiene estadísticas generales del dashboard.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "total_games": 7112,
    "total_platforms": 17,
    "total_genres": 12,
    "total_publishers": 278,
    "global_sales": 5442.86,
    "avg_rating": 7
  }
}
```

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/stats
```

---

### 3. Ventas por Región

#### GET `/api/v1/sales-by-region`
Obtiene las ventas totales por región.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "NA": 4296.49,
    "EU": 2771.36,
    "JP": 1291.36,
    "Other": 561.39
  }
}
```

**Regiones:**
- **NA**: América del Norte
- **EU**: Europa
- **JP**: Japón
- **Other**: Otros

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/sales-by-region
```

---

### 4. Top Plataformas

#### GET `/api/v1/top-platforms`
Obtiene las plataformas más populares ordenadas por ventas globales.

**Parámetros:**
| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `limit` | integer | 10 | Número de plataformas a retornar (máx: 50) |

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "platforms": ["PS2", "X360", "PS3", "Wii", "DS"],
    "sales": [965.91, 868.48, 793.33, 676.39, 385.21]
  }
}
```

**Ejemplos de Uso:**
```bash
# Top 10 plataformas (default)
curl http://localhost:5000/api/v1/top-platforms

# Top 5 plataformas
curl http://localhost:5000/api/v1/top-platforms?limit=5

# Top 20 plataformas
curl http://localhost:5000/api/v1/top-platforms?limit=20
```

---

### 5. Géneros por Ventas

#### GET `/api/v1/top-genres`
Obtiene todos los géneros ordenados por ventas globales.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "genres": ["Action", "Sports", "Shooter", "Racing", "Role-Playing"],
    "sales": [1751.29, 1330.77, 1251.53, 1027.88, 923.56]
  }
}
```

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/top-genres
```

---

### 6. Top Editores

#### GET `/api/v1/top-publishers`
Obtiene los editores más exitosos ordenados por ventas globales.

**Parámetros:**
| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `limit` | integer | 15 | Número de editores a retornar (máx: 100) |

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "publishers": ["Nintendo", "Electronic Arts", "Activision"],
    "sales": [1797.32, 1146.68, 1084.32]
  }
}
```

**Ejemplos de Uso:**
```bash
# Top 15 editores (default)
curl http://localhost:5000/api/v1/top-publishers

# Top 5 editores
curl http://localhost:5000/api/v1/top-publishers?limit=5
```

---

### 7. Distribución de Calificaciones

#### GET `/api/v1/rating-distribution`
Obtiene la distribución de calificaciones ESRB.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "ratings": ["E", "T", "M", "AO", "EC", "RP"],
    "counts": [1296, 1331, 1296, 95, 50, 44]
  }
}
```

**Calificaciones ESRB:**
- **E**: Everyone (Para todos)
- **T**: Teen (Adolescentes)
- **M**: Mature (Adultos)
- **AO**: Adults Only (Solo adultos)
- **EC**: Early Childhood (Primera infancia)
- **RP**: Rating Pending (Calificación pendiente)

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/rating-distribution
```

---

### 8. Distribución de Puntuaciones de Críticos

#### GET `/api/v1/critic-score-distribution`
Obtiene la distribución de puntuaciones de críticos.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "scores": ["Excelente", "Bueno", "Regular", "Malo"],
    "counts": [1997, 1575, 1234, 567]
  }
}
```

**Puntuaciones:**
- **Excelente**: Crítica muy positiva
- **Bueno**: Crítica positiva
- **Regular**: Crítica neutral
- **Malo**: Crítica negativa

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/critic-score-distribution
```

---

### 9. Lista de Videojuegos

#### GET `/api/v1/games`
Obtiene lista de videojuegos con filtros y paginación.

**Parámetros:**
| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `platform` | string | "all" | Filtrar por plataforma |
| `genre` | string | "all" | Filtrar por género |
| `publisher` | string | "all" | Filtrar por editor |
| `page` | integer | 1 | Número de página |
| `per_page` | integer | 50 | Videojuegos por página (máx: 500) |

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "games": [
      {
        "Platform": "Wii",
        "Genre": "Sports",
        "Publisher": "Nintendo",
        "NA_Sales": 41.36,
        "EU_Sales": 28.96,
        "JP_Sales": 3.77,
        "Other_Sales": 8.45,
        "Global_Sales": 82.54,
        "Rating": "E",
        "Critic_Score_Class": "Bueno"
      }
    ],
    "total": 7112,
    "page": 1,
    "per_page": 50,
    "pages": 143
  }
}
```

**Ejemplos de Uso:**
```bash
# Obtener primeros 50 videojuegos
curl http://localhost:5000/api/v1/games

# Filtrar por plataforma PS2
curl "http://localhost:5000/api/v1/games?platform=PS2"

# Filtrar por género Action
curl "http://localhost:5000/api/v1/games?genre=Action"

# Filtrar por editor Nintendo
curl "http://localhost:5000/api/v1/games?publisher=Nintendo"

# Combinar filtros
curl "http://localhost:5000/api/v1/games?platform=PS2&genre=Action&page=2&per_page=25"
```

---

### 10. Opciones de Filtros

#### GET `/api/v1/filters`
Obtiene todas las opciones disponibles para filtros.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "platforms": ["DS", "GB", "GBA", "GC", "N64", "NES", "PS", "PS2", "PS3", "PSP", "Wii", "X360", "XB", "XOne"],
    "genres": ["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing", "Shooter", "Simulation", "Sports", "Strategy"],
    "publishers": ["Activision", "Electronic Arts", "Nintendo", "Sony Computer Entertainment", "Take-Two Interactive", ...]
  }
}
```

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/filters
```

---

### 11. Estadísticas de Plataforma

#### GET `/api/v1/platform-stats/<platform>`
Obtiene estadísticas detalladas de una plataforma específica.

**Parámetros de Ruta:**
| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `platform` | string | Nombre de la plataforma |

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "platform": "PS2",
    "total_games": 1169,
    "total_sales": 965.91,
    "avg_sales": 0.83,
    "top_genres": ["Action", "Sports", "Racing"],
    "top_publishers": ["Electronic Arts", "Activision", "Konami"]
  }
}
```

**Respuesta de Error (Plataforma no encontrada):**
```json
{
  "status": "error",
  "message": "Plataforma \"INVALID\" no encontrada",
  "code": 404
}
```

**Ejemplos de Uso:**
```bash
# Estadísticas de PS2
curl http://localhost:5000/api/v1/platform-stats/PS2

# Estadísticas de Xbox 360
curl http://localhost:5000/api/v1/platform-stats/X360
```

---

### 12. Estadísticas de Género

#### GET `/api/v1/genre-stats/<genre>`
Obtiene estadísticas detalladas de un género específico.

**Parámetros de Ruta:**
| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `genre` | string | Nombre del género |

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "genre": "Action",
    "total_games": 1698,
    "total_sales": 1751.29,
    "avg_sales": 1.03,
    "top_platforms": ["PS2", "X360", "PS3"],
    "top_publishers": ["Electronic Arts", "Activision", "Ubisoft"]
  }
}
```

**Ejemplos de Uso:**
```bash
# Estadísticas de Action
curl http://localhost:5000/api/v1/genre-stats/Action

# Estadísticas de Sports
curl http://localhost:5000/api/v1/genre-stats/Sports
```

---

### 13. Estadísticas de Editor

#### GET `/api/v1/publisher-stats/<publisher>`
Obtiene estadísticas detalladas de un editor específico.

**Parámetros de Ruta:**
| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `publisher` | string | Nombre del editor |

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "publisher": "Nintendo",
    "total_games": 385,
    "total_sales": 1797.32,
    "avg_sales": 4.67,
    "top_platforms": ["Wii", "DS", "N64"],
    "top_genres": ["Sports", "Action", "Racing"]
  }
}
```

**Ejemplos de Uso:**
```bash
# Estadísticas de Nintendo
curl http://localhost:5000/api/v1/publisher-stats/Nintendo

# Estadísticas de Electronic Arts
curl http://localhost:5000/api/v1/publisher-stats/"Electronic Arts"
```

---

### 14. Búsqueda

#### GET `/api/v1/search`
Busca videojuegos por criterios (plataforma, género, editor).

**Parámetros:**
| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `q` | string | **requerido** | Término de búsqueda |
| `type` | string | "all" | Tipo de búsqueda: platform, genre, publisher, all |

**Respuesta Exitosa:**
```json
{
  "status": "success",
  "data": {
    "query": "PS",
    "type": "platform",
    "results": [
      {"type": "platform", "name": "PS", "count": 490},
      {"type": "platform", "name": "PS2", "count": 1169},
      {"type": "platform", "name": "PS3", "count": 1155},
      {"type": "platform", "name": "PSP", "count": 1446}
    ],
    "total_results": 4
  }
}
```

**Ejemplos de Uso:**
```bash
# Buscar plataformas con "PS"
curl "http://localhost:5000/api/v1/search?q=PS&type=platform"

# Buscar géneros con "Action"
curl "http://localhost:5000/api/v1/search?q=Action&type=genre"

# Buscar en todo (plataformas, géneros, editores)
curl "http://localhost:5000/api/v1/search?q=Nintendo&type=all"
```

---

### 15. Health Check

#### GET `/api/v1/health`
Verifica el estado de la API.

**Parámetros:** Ninguno

**Respuesta Exitosa:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2026-05-19T22:30:00",
  "data_loaded": true,
  "total_records": 7112
}
```

**Ejemplo de Uso:**
```bash
curl http://localhost:5000/api/v1/health
```

---

## Códigos de Estado HTTP

| Código | Significado | Descripción |
|--------|-------------|-------------|
| 200 | OK | Solicitud exitosa |
| 400 | Bad Request | Parámetros inválidos |
| 404 | Not Found | Recurso no encontrado |
| 500 | Internal Server Error | Error interno del servidor |

---

## Ejemplos de Uso con cURL

### Obtener estadísticas generales
```bash
curl http://localhost:5000/api/v1/stats
```

### Obtener top 5 plataformas
```bash
curl "http://localhost:5000/api/v1/top-platforms?limit=5"
```

### Obtener videojuegos de PS2 página 2
```bash
curl "http://localhost:5000/api/v1/games?platform=PS2&page=2&per_page=25"
```

### Obtener estadísticas de Nintendo
```bash
curl "http://localhost:5000/api/v1/publisher-stats/Nintendo"
```

### Buscar plataformas con "X"
```bash
curl "http://localhost:5000/api/v1/search?q=X&type=platform"
```

---

## Ejemplos de Uso con Python

```python
import requests
import json

BASE_URL = "http://localhost:5000/api/v1"

# Obtener estadísticas
response = requests.get(f"{BASE_URL}/stats")
stats = response.json()
print(json.dumps(stats, indent=2))

# Obtener top plataformas
response = requests.get(f"{BASE_URL}/top-platforms", params={"limit": 5})
platforms = response.json()
print(json.dumps(platforms, indent=2))

# Obtener videojuegos con filtros
response = requests.get(f"{BASE_URL}/games", params={
    "platform": "PS2",
    "genre": "Action",
    "page": 1,
    "per_page": 10
})
games = response.json()
print(json.dumps(games, indent=2))
```

---

## Ejemplos de Uso con JavaScript

```javascript
const BASE_URL = "http://localhost:5000/api/v1";

// Obtener estadísticas
fetch(`${BASE_URL}/stats`)
  .then(response => response.json())
  .then(data => console.log(data));

// Obtener top plataformas
fetch(`${BASE_URL}/top-platforms?limit=5`)
  .then(response => response.json())
  .then(data => console.log(data));

// Obtener videojuegos con filtros
const params = new URLSearchParams({
  platform: "PS2",
  genre: "Action",
  page: 1,
  per_page: 10
});

fetch(`${BASE_URL}/games?${params}`)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## Notas Importantes

1. **Límites de Paginación**: El máximo de `per_page` es 500 para evitar sobrecargar el servidor.
2. **Compatibilidad**: Los endpoints legacy (`/api/...`) siguen siendo soportados para compatibilidad hacia atrás.
3. **CORS**: La API está configurada para aceptar solicitudes desde cualquier origen.
4. **Validación**: Todos los parámetros se validan antes de procesar la solicitud.
5. **Caché**: Los datos se cargan en memoria al iniciar la aplicación para mejor rendimiento.

---

## Soporte y Contacto

Para reportar problemas o sugerencias sobre la API, contacta al equipo de desarrollo.

**Última actualización:** Mayo 19, 2026
