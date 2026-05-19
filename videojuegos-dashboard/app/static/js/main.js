// ==================== UTILIDADES ====================

/**
 * Función para formatear números con separadores de miles
 */
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/**
 * Función para hacer peticiones GET a la API
 */
async function apiGet(endpoint) {
    try {
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error en petición API:', error);
        return null;
    }
}

/**
 * Función para mostrar notificaciones
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

/**
 * Función para validar si un elemento existe
 */
function elementExists(selector) {
    return document.querySelector(selector) !== null;
}

/**
 * Función para agregar clase a un elemento
 */
function addClass(selector, className) {
    const element = document.querySelector(selector);
    if (element) {
        element.classList.add(className);
    }
}

/**
 * Función para remover clase de un elemento
 */
function removeClass(selector, className) {
    const element = document.querySelector(selector);
    if (element) {
        element.classList.remove(className);
    }
}

/**
 * Función para toggle de clase
 */
function toggleClass(selector, className) {
    const element = document.querySelector(selector);
    if (element) {
        element.classList.toggle(className);
    }
}

// ==================== INICIALIZACIÓN ====================

document.addEventListener('DOMContentLoaded', () => {
    console.log('Dashboard de Videojuegos cargado correctamente');
    
    // Aquí se pueden agregar inicializaciones globales
    initializeTooltips();
});

// ==================== FUNCIONES DE INICIALIZACIÓN ====================

/**
 * Inicializar tooltips (si se usan)
 */
function initializeTooltips() {
    // Placeholder para inicialización de tooltips
}

/**
 * Función para animar números
 */
function animateNumber(element, target, duration = 1000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = formatNumber(Math.round(target));
            clearInterval(timer);
        } else {
            element.textContent = formatNumber(Math.round(current));
        }
    }, 16);
}

// ==================== FUNCIONES DE UTILIDAD PARA TABLAS ====================

/**
 * Función para ordenar tabla por columna
 */
function sortTable(table, column, order = 'asc') {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    rows.sort((a, b) => {
        const aValue = a.children[column].textContent;
        const bValue = b.children[column].textContent;
        
        if (!isNaN(aValue) && !isNaN(bValue)) {
            return order === 'asc' ? aValue - bValue : bValue - aValue;
        }
        
        return order === 'asc' 
            ? aValue.localeCompare(bValue) 
            : bValue.localeCompare(aValue);
    });
    
    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));
}

/**
 * Función para filtrar tabla
 */
function filterTable(table, searchTerm) {
    const rows = table.querySelectorAll('tbody tr');
    const term = searchTerm.toLowerCase();
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(term) ? '' : 'none';
    });
}

// ==================== FUNCIONES DE GRÁFICOS ====================

/**
 * Función para obtener colores para gráficos
 */
function getChartColors(count) {
    const colors = [
        '#6366f1', '#ec4899', '#f59e0b', '#10b981', '#3b82f6',
        '#8b5cf6', '#06b6d4', '#f43f5e', '#14b8a6', '#eab308'
    ];
    
    return colors.slice(0, count);
}

/**
 * Función para crear un gráfico de barras
 */
function createBarChart(canvasId, labels, data, label = 'Datos') {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;
    
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: '#6366f1',
                borderColor: '#6366f1',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

/**
 * Función para crear un gráfico de pastel
 */
function createPieChart(canvasId, labels, data, label = 'Datos') {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;
    
    return new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: getChartColors(labels.length),
                borderColor: '#fff',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
}

// ==================== FUNCIONES DE VALIDACIÓN ====================

/**
 * Validar email
 */
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Validar número
 */
function validateNumber(value) {
    return !isNaN(parseFloat(value)) && isFinite(value);
}

/**
 * Validar URL
 */
function validateURL(url) {
    try {
        new URL(url);
        return true;
    } catch (error) {
        return false;
    }
}

// ==================== FUNCIONES DE ALMACENAMIENTO ====================

/**
 * Guardar datos en localStorage
 */
function saveToLocalStorage(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
        return true;
    } catch (error) {
        console.error('Error guardando en localStorage:', error);
        return false;
    }
}

/**
 * Obtener datos de localStorage
 */
function getFromLocalStorage(key) {
    try {
        const value = localStorage.getItem(key);
        return value ? JSON.parse(value) : null;
    } catch (error) {
        console.error('Error obteniendo de localStorage:', error);
        return null;
    }
}

/**
 * Remover datos de localStorage
 */
function removeFromLocalStorage(key) {
    try {
        localStorage.removeItem(key);
        return true;
    } catch (error) {
        console.error('Error removiendo de localStorage:', error);
        return false;
    }
}

// ==================== FUNCIONES DE NAVEGACIÓN ====================

/**
 * Navegar a una página
 */
function navigateTo(path) {
    window.location.href = path;
}

/**
 * Recargar página actual
 */
function reloadPage() {
    window.location.reload();
}

/**
 * Volver a página anterior
 */
function goBack() {
    window.history.back();
}

// ==================== FUNCIONES DE SCROLL ====================

/**
 * Scroll suave a elemento
 */
function smoothScrollToElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

/**
 * Scroll al inicio de la página
 */
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ==================== EXPORTAR FUNCIONES ====================

// Las funciones están disponibles globalmente en el contexto del navegador
