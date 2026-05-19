from flask import Flask, render_template, jsonify, request
import pandas as pd
import json
import os
from functools import wraps
from datetime import datetime

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'app', 'templates'), static_folder=os.path.join(os.path.dirname(__file__), 'app', 'static'))

# ==================== CONFIGURACIÓN ====================

API_VERSION = "1.0.0"
API_TITLE = "Videojuegos Dashboard API"
API_DESCRIPTION = "API para acceder a datos de videojuegos, ventas por región, plataformas y más"

# Cargar datos
DATA_PATH = os.path.join(os.path.dirname(__file__), 'app', 'static', 'data', 'dato.csv')
df = pd.read_csv(DATA_PATH)

# Limpiar datos: convertir columnas de ventas a numéricas
sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
for col in sales_columns:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

# ==================== DECORADORES ====================

def json_response(f):
    """Decorador para asegurar respuestas JSON con headers apropiados"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)
        if isinstance(response, dict):
            return jsonify(response)
        return response
    return decorated_function

def validate_params(required_params=None, optional_params=None):
    """Decorador para validar parámetros de request"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            required_params_list = required_params or []
            optional_params_list = optional_params or []
            
            # Validar parámetros requeridos
            for param in required_params_list:
                if param not in request.args:
                    return jsonify({
                        'error': f'Parámetro requerido faltante: {param}',
                        'status': 'error',
                        'code': 400
                    }), 400
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# ==================== RUTAS DE PÁGINAS ====================

@app.route('/')
def index():
    """Página de inicio del dashboard"""
    return render_template('index.html')

@app.route('/analytics')
def analytics():
    """Página de análisis de datos"""
    return render_template('analytics.html')

@app.route('/games')
def games():
    """Página de lista de videojuegos"""
    return render_template('games.html')

@app.route('/api-docs')
def api_docs():
    """Página de documentación de la API"""
    return render_template('api_docs.html')

# ==================== API ENDPOINTS - DOCUMENTACIÓN ====================

@app.route('/api/v1/docs')
@json_response
def get_api_docs():
    """
    Obtener documentación completa de la API
    
    Returns:
        dict: Información sobre la API y todos los endpoints disponibles
    """
    docs = {
        'api': {
            'title': API_TITLE,
            'version': API_VERSION,
            'description': API_DESCRIPTION,
            'base_url': request.host_url.rstrip('/'),
            'timestamp': datetime.now().isoformat()
        },
        'endpoints': {
            'documentation': {
                'url': '/api/v1/docs',
                'method': 'GET',
                'description': 'Obtener documentación completa de la API',
                'response': 'JSON con información de todos los endpoints'
            },
            'stats': {
                'url': '/api/v1/stats',
                'method': 'GET',
                'description': 'Obtener estadísticas generales del dashboard',
                'parameters': [],
                'response_example': {
                    'total_games': 7112,
                    'total_platforms': 17,
                    'total_genres': 12,
                    'total_publishers': 278,
                    'global_sales': 8920.56,
                    'avg_rating': 7
                }
            },
            'sales_by_region': {
                'url': '/api/v1/sales-by-region',
                'method': 'GET',
                'description': 'Obtener ventas totales por región',
                'parameters': [],
                'response_example': {
                    'NA': 4296.49,
                    'EU': 2771.36,
                    'JP': 1291.36,
                    'Other': 561.39
                }
            },
            'top_platforms': {
                'url': '/api/v1/top-platforms',
                'method': 'GET',
                'description': 'Obtener las 10 plataformas más populares',
                'parameters': [
                    {'name': 'limit', 'type': 'integer', 'default': 10, 'description': 'Número de plataformas a retornar'}
                ],
                'response_example': {
                    'platforms': ['PS2', 'X360', 'PS3'],
                    'sales': [1982.53, 1736.48, 1277.47]
                }
            },
            'top_genres': {
                'url': '/api/v1/top-genres',
                'method': 'GET',
                'description': 'Obtener géneros ordenados por ventas',
                'parameters': [],
                'response_example': {
                    'genres': ['Action', 'Sports', 'Shooter'],
                    'sales': [1751.29, 1330.77, 1251.53]
                }
            },
            'top_publishers': {
                'url': '/api/v1/top-publishers',
                'method': 'GET',
                'description': 'Obtener los 15 editores más exitosos',
                'parameters': [
                    {'name': 'limit', 'type': 'integer', 'default': 15, 'description': 'Número de editores a retornar'}
                ],
                'response_example': {
                    'publishers': ['Nintendo', 'Electronic Arts', 'Activision'],
                    'sales': [1797.32, 1146.68, 1084.32]
                }
            },
            'rating_distribution': {
                'url': '/api/v1/rating-distribution',
                'method': 'GET',
                'description': 'Obtener distribución de calificaciones ESRB',
                'parameters': [],
                'response_example': {
                    'ratings': ['E', 'T', 'M', 'AO'],
                    'counts': [1296, 1331, 1296, 95]
                }
            },
            'critic_score_distribution': {
                'url': '/api/v1/critic-score-distribution',
                'method': 'GET',
                'description': 'Obtener distribución de puntuaciones de críticos',
                'parameters': [],
                'response_example': {
                    'scores': ['Excelente', 'Bueno', 'Regular', 'Malo'],
                    'counts': [1997, 1575, 1234, 567]
                }
            },
            'games': {
                'url': '/api/v1/games',
                'method': 'GET',
                'description': 'Obtener lista de videojuegos con filtros y paginación',
                'parameters': [
                    {'name': 'platform', 'type': 'string', 'default': 'all', 'description': 'Filtrar por plataforma'},
                    {'name': 'genre', 'type': 'string', 'default': 'all', 'description': 'Filtrar por género'},
                    {'name': 'publisher', 'type': 'string', 'default': 'all', 'description': 'Filtrar por editor'},
                    {'name': 'page', 'type': 'integer', 'default': 1, 'description': 'Número de página'},
                    {'name': 'per_page', 'type': 'integer', 'default': 50, 'description': 'Videojuegos por página'}
                ],
                'response_example': {
                    'games': [
                        {
                            'Platform': 'Wii',
                            'Genre': 'Sports',
                            'Publisher': 'Nintendo',
                            'NA_Sales': 41.36,
                            'EU_Sales': 28.96,
                            'JP_Sales': 3.77,
                            'Other_Sales': 8.45,
                            'Global_Sales': 82.54,
                            'Rating': 'E',
                            'Critic_Score_Class': 'Bueno'
                        }
                    ],
                    'total': 7112,
                    'page': 1,
                    'per_page': 50,
                    'pages': 143
                }
            },
            'filters': {
                'url': '/api/v1/filters',
                'method': 'GET',
                'description': 'Obtener opciones disponibles para filtros',
                'parameters': [],
                'response_example': {
                    'platforms': ['DS', 'PS', 'PS2', 'PS3'],
                    'genres': ['Action', 'Adventure', 'Fighting'],
                    'publishers': ['Activision', 'Electronic Arts', 'Nintendo']
                }
            },
            'platform_stats': {
                'url': '/api/v1/platform-stats/<platform>',
                'method': 'GET',
                'description': 'Obtener estadísticas de una plataforma específica',
                'parameters': [
                    {'name': 'platform', 'type': 'string', 'description': 'Nombre de la plataforma'}
                ],
                'response_example': {
                    'platform': 'PS2',
                    'total_games': 1169,
                    'total_sales': 1982.53,
                    'avg_sales': 1.69,
                    'top_genres': ['Action', 'Sports'],
                    'top_publishers': ['Electronic Arts', 'Activision']
                }
            },
            'genre_stats': {
                'url': '/api/v1/genre-stats/<genre>',
                'method': 'GET',
                'description': 'Obtener estadísticas de un género específico',
                'parameters': [
                    {'name': 'genre', 'type': 'string', 'description': 'Nombre del género'}
                ],
                'response_example': {
                    'genre': 'Action',
                    'total_games': 1698,
                    'total_sales': 1751.29,
                    'avg_sales': 1.03,
                    'top_platforms': ['PS2', 'X360'],
                    'top_publishers': ['Electronic Arts', 'Activision']
                }
            },
            'search': {
                'url': '/api/v1/search',
                'method': 'GET',
                'description': 'Buscar videojuegos por criterios',
                'parameters': [
                    {'name': 'q', 'type': 'string', 'description': 'Término de búsqueda'},
                    {'name': 'type', 'type': 'string', 'default': 'all', 'description': 'Tipo de búsqueda: platform, genre, publisher, all'}
                ],
                'response_example': {
                    'results': [
                        {'platform': 'PS2', 'count': 1169},
                        {'platform': 'X360', 'count': 1155}
                    ],
                    'query': 'PS',
                    'total_results': 2
                }
            }
        }
    }
    return docs

# ==================== API ENDPOINTS - ESTADÍSTICAS ====================

@app.route('/api/v1/stats')
@json_response
def get_stats():
    """Obtener estadísticas generales del dashboard"""
    stats = {
        'status': 'success',
        'data': {
            'total_games': int(df.shape[0]),
            'total_platforms': int(df['Platform'].nunique()),
            'total_genres': int(df['Genre'].nunique()),
            'total_publishers': int(df['Publisher'].nunique()),
            'global_sales': float(df['Global_Sales'].sum()),
            'avg_rating': float(df['Rating'].nunique())
        }
    }
    return stats

@app.route('/api/v1/sales-by-region')
@json_response
def get_sales_by_region():
    """Obtener ventas por región"""
    regions = {
        'status': 'success',
        'data': {
            'NA': float(df['NA_Sales'].sum()),
            'EU': float(df['EU_Sales'].sum()),
            'JP': float(df['JP_Sales'].sum()),
            'Other': float(df['Other_Sales'].sum())
        }
    }
    return regions

@app.route('/api/v1/top-platforms')
@json_response
def get_top_platforms():
    """Obtener las plataformas más populares"""
    limit = request.args.get('limit', 10, type=int)
    top_platforms = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(limit)
    return {
        'status': 'success',
        'data': {
            'platforms': top_platforms.index.tolist(),
            'sales': [float(x) for x in top_platforms.values.tolist()]
        }
    }

@app.route('/api/v1/top-genres')
@json_response
def get_top_genres():
    """Obtener los géneros más populares"""
    top_genres = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
    return {
        'status': 'success',
        'data': {
            'genres': top_genres.index.tolist(),
            'sales': [float(x) for x in top_genres.values.tolist()]
        }
    }

@app.route('/api/v1/top-publishers')
@json_response
def get_top_publishers():
    """Obtener los editores más exitosos"""
    limit = request.args.get('limit', 15, type=int)
    top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(limit)
    return {
        'status': 'success',
        'data': {
            'publishers': top_publishers.index.tolist(),
            'sales': [float(x) for x in top_publishers.values.tolist()]
        }
    }

@app.route('/api/v1/rating-distribution')
@json_response
def get_rating_distribution():
    """Obtener distribución de calificaciones"""
    rating_dist = df['Rating'].value_counts().sort_index()
    return {
        'status': 'success',
        'data': {
            'ratings': rating_dist.index.tolist(),
            'counts': rating_dist.values.tolist()
        }
    }

@app.route('/api/v1/critic-score-distribution')
@json_response
def get_critic_score_distribution():
    """Obtener distribución de puntuaciones de críticos"""
    critic_dist = df['Critic_Score_Class'].value_counts()
    return {
        'status': 'success',
        'data': {
            'scores': critic_dist.index.tolist(),
            'counts': critic_dist.values.tolist()
        }
    }

# ==================== API ENDPOINTS - VIDEOJUEGOS ====================

@app.route('/api/v1/games', methods=['GET'])
@json_response
def get_games():
    """Obtener lista de videojuegos con filtros"""
    try:
        # Parámetros de filtro
        platform = request.args.get('platform', 'all')
        genre = request.args.get('genre', 'all')
        publisher = request.args.get('publisher', 'all')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 50))
        
        # Validar parámetros
        if page < 1:
            return {'status': 'error', 'message': 'page debe ser mayor a 0', 'code': 400}, 400
        if per_page < 1 or per_page > 500:
            return {'status': 'error', 'message': 'per_page debe estar entre 1 y 500', 'code': 400}, 400
        
        # Aplicar filtros
        filtered_df = df.copy()
        
        if platform and platform != 'all':
            filtered_df = filtered_df[filtered_df['Platform'] == platform]
        
        if genre and genre != 'all':
            filtered_df = filtered_df[filtered_df['Genre'] == genre]
        
        if publisher and publisher != 'all':
            filtered_df = filtered_df[filtered_df['Publisher'] == publisher]
        
        # Ordenar por ventas globales
        filtered_df = filtered_df.sort_values('Global_Sales', ascending=False)
        
        # Paginación
        total = len(filtered_df)
        start = (page - 1) * per_page
        end = start + per_page
        
        games_list = filtered_df.iloc[start:end].to_dict('records')
        
        # Convertir valores a tipos JSON serializables
        for game in games_list:
            for col in sales_columns:
                game[col] = float(game[col])
        
        return {
            'status': 'success',
            'data': {
                'games': games_list,
                'total': total,
                'page': page,
                'per_page': per_page,
                'pages': (total + per_page - 1) // per_page
            }
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e), 'code': 500}, 500

@app.route('/api/v1/filters')
@json_response
def get_filters():
    """Obtener opciones de filtros disponibles"""
    filters = {
        'status': 'success',
        'data': {
            'platforms': sorted(df['Platform'].unique().tolist()),
            'genres': sorted(df['Genre'].unique().tolist()),
            'publishers': sorted(df['Publisher'].unique().tolist())
        }
    }
    return filters

# ==================== API ENDPOINTS - ESTADÍSTICAS ESPECÍFICAS ====================

@app.route('/api/v1/platform-stats/<platform>')
@json_response
def get_platform_stats(platform):
    """Obtener estadísticas de una plataforma específica"""
    platform_data = df[df['Platform'] == platform]
    
    if platform_data.empty:
        return {'status': 'error', 'message': f'Plataforma "{platform}" no encontrada', 'code': 404}, 404
    
    return {
        'status': 'success',
        'data': {
            'platform': platform,
            'total_games': int(len(platform_data)),
            'total_sales': float(platform_data['Global_Sales'].sum()),
            'avg_sales': float(platform_data['Global_Sales'].mean()),
            'top_genres': platform_data['Genre'].value_counts().head(5).index.tolist(),
            'top_publishers': platform_data['Publisher'].value_counts().head(5).index.tolist()
        }
    }

@app.route('/api/v1/genre-stats/<genre>')
@json_response
def get_genre_stats(genre):
    """Obtener estadísticas de un género específico"""
    genre_data = df[df['Genre'] == genre]
    
    if genre_data.empty:
        return {'status': 'error', 'message': f'Género "{genre}" no encontrado', 'code': 404}, 404
    
    return {
        'status': 'success',
        'data': {
            'genre': genre,
            'total_games': int(len(genre_data)),
            'total_sales': float(genre_data['Global_Sales'].sum()),
            'avg_sales': float(genre_data['Global_Sales'].mean()),
            'top_platforms': genre_data['Platform'].value_counts().head(5).index.tolist(),
            'top_publishers': genre_data['Publisher'].value_counts().head(5).index.tolist()
        }
    }

@app.route('/api/v1/publisher-stats/<publisher>')
@json_response
def get_publisher_stats(publisher):
    """Obtener estadísticas de un editor específico"""
    publisher_data = df[df['Publisher'] == publisher]
    
    if publisher_data.empty:
        return {'status': 'error', 'message': f'Editor "{publisher}" no encontrado', 'code': 404}, 404
    
    return {
        'status': 'success',
        'data': {
            'publisher': publisher,
            'total_games': int(len(publisher_data)),
            'total_sales': float(publisher_data['Global_Sales'].sum()),
            'avg_sales': float(publisher_data['Global_Sales'].mean()),
            'top_platforms': publisher_data['Platform'].value_counts().head(5).index.tolist(),
            'top_genres': publisher_data['Genre'].value_counts().head(5).index.tolist()
        }
    }

# ==================== API ENDPOINTS - BÚSQUEDA ====================

@app.route('/api/v1/search')
@json_response
def search():
    """Buscar videojuegos por criterios"""
    query = request.args.get('q', '').strip()
    search_type = request.args.get('type', 'all')
    
    if not query:
        return {'status': 'error', 'message': 'Parámetro "q" es requerido', 'code': 400}, 400
    
    results = []
    
    if search_type in ['platform', 'all']:
        platforms = df[df['Platform'].str.contains(query, case=False, na=False)]['Platform'].unique()
        for platform in platforms:
            count = len(df[df['Platform'] == platform])
            results.append({'type': 'platform', 'name': platform, 'count': count})
    
    if search_type in ['genre', 'all']:
        genres = df[df['Genre'].str.contains(query, case=False, na=False)]['Genre'].unique()
        for genre in genres:
            count = len(df[df['Genre'] == genre])
            results.append({'type': 'genre', 'name': genre, 'count': count})
    
    if search_type in ['publisher', 'all']:
        publishers = df[df['Publisher'].str.contains(query, case=False, na=False)]['Publisher'].unique()
        for publisher in publishers:
            count = len(df[df['Publisher'] == publisher])
            results.append({'type': 'publisher', 'name': publisher, 'count': count})
    
    return {
        'status': 'success',
        'data': {
            'query': query,
            'type': search_type,
            'results': results,
            'total_results': len(results)
        }
    }

# ==================== ENDPOINTS LEGACY (compatibilidad) ====================

@app.route('/api/stats')
def get_stats_legacy():
    """Endpoint legacy para compatibilidad"""
    return get_stats()

@app.route('/api/sales-by-region')
def get_sales_by_region_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_sales_by_region()
    if isinstance(data, tuple):
        return data
    return data.get_json()

@app.route('/api/top-platforms')
def get_top_platforms_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_top_platforms()
    if isinstance(data, tuple):
        return data
    return data.get_json()

@app.route('/api/top-genres')
def get_top_genres_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_top_genres()
    if isinstance(data, tuple):
        return data
    return data.get_json()

@app.route('/api/top-publishers')
def get_top_publishers_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_top_publishers()
    if isinstance(data, tuple):
        return data
    return data.get_json()

@app.route('/api/rating-distribution')
def get_rating_distribution_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_rating_distribution()
    if isinstance(data, tuple):
        return data
    return data.get_json()

@app.route('/api/critic-score-distribution')
def get_critic_score_distribution_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_critic_score_distribution()
    if isinstance(data, tuple):
        return data
    return data.get_json()

@app.route('/api/games', methods=['GET'])
def get_games_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_games()
    if isinstance(data, tuple):
        return data
    return data.get_json()

@app.route('/api/filters')
def get_filters_legacy():
    """Endpoint legacy para compatibilidad"""
    data = get_filters()
    if isinstance(data, tuple):
        return data
    return data.get_json()

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Manejar errores 404"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint no encontrado',
        'code': 404,
        'path': request.path
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Manejar errores 500"""
    return jsonify({
        'status': 'error',
        'message': 'Error interno del servidor',
        'code': 500
    }), 500

@app.errorhandler(400)
def bad_request(error):
    """Manejar errores 400"""
    return jsonify({
        'status': 'error',
        'message': 'Solicitud inválida',
        'code': 400
    }), 400

# ==================== HEALTH CHECK ====================

@app.route('/api/v1/health')
@json_response
def health_check():
    """Verificar el estado de la API"""
    return {
        'status': 'healthy',
        'version': API_VERSION,
        'timestamp': datetime.now().isoformat(),
        'data_loaded': True,
        'total_records': len(df)
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
