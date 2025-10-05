# Reto de Desarrollo Fullstack - TelcoX: Módulo de Visualización de Consumo

## 1. Descripción del Proyecto

Este proyecto es la implementación de la prueba técnica para el cargo de Especialista de Desarrollo TI. El objetivo principal fue crear un **Módulo de Visualización de Consumo** para la plataforma de auto-gestión de TelcoX, demostrando capacidad de integración Fullstack y calidad de código.

El módulo cumple con:
1.  **Simulación BSS:** Se conecta a una API RESTful que simula el sistema BSS (Business Support System) para obtener datos de consumo, saldo, y detalles del cliente en tiempo real.
2.  **Interfaz Intuitiva:** Implementa una GUI limpia y responsiva en Angular, utilizando gráficos circulares y barras de progreso para visualizar el consumo de Datos, Minutos y SMS.
3.  **Manejo de Errores:** Incluye gestión de estados de carga y errores de conexión con el *backend*.

## 2. Tecnologías Utilizadas

| Componente | Tecnología | Versión Clave |
| :--- | :--- | :--- |
| **Backend (API)** | Python | 3.x |
| **Framework Web** | Flask | 2.x |
| **Frontend (GUI)** | Angular | 20.x |
| **Estilos** | Bootstrap 5, CSS3, Bootstrap Icons | 5.3.3 |
| **Despliegue (Recomendado)**| Docker | - |

## 3. Estructura de la API (Backend Ficticio)

El *backend* fue desarrollado en Python/Flask y simula el sistema BSS. Los datos son generados aleatoriamente (`random`) en cada llamada al *endpoint*.

### `backend/app.py` - Puntos Clave del Código
* **Simulación de Datos:** La función `make_mock_consumo()` genera datos aleatorios de consumo, simulando un sistema dinámico.
* **CORS:** `CORS(app)` está habilitado para permitir la comunicación segura desde el Frontend de Angular (normalmente en el puerto 4200) al Backend (puerto 5000).
* **Endpoints Implementados:**
    * `GET /api/consumo`
    * `GET /api/consumo/<int:cliente_id>`

*(Ver la sección de Documentación de API para más detalles sobre la estructura JSON.)*

## 4. Guía de Ejecución

Se recomienda el uso de dos terminales separadas, una para el Backend y otra para el Frontend.

### Requisitos Previos

* Python 3.x
* Node.js (v20+) y npm
* Angular CLI (v20+)
* Docker (Opcional, para contenerización)

### 4.1. Configuración e Inicio del Backend (Flask)

1.  **Navegar a la carpeta:** `cd backend/`
2.  **Crear y activar entorno virtual:** `python -m venv venv`
3.  **Instalar dependencias:** `pip install Flask flask-cors` (y `random` / `datetime` son nativos).
4.  **Iniciar el servidor:**
    ```bash
    python app.py
    ```
    *La API se ejecutará en `http://localhost:5000`.*

### 4.2. Configuración e Inicio del Frontend (Angular)

1.  **Navegar a la carpeta:** `cd telcox-app/` (o la carpeta de tu proyecto Angular)
2.  **Instalar dependencias:** `npm install`
3.  **Iniciar el servidor de desarrollo:**
    ```bash
    ng serve --open
    ```
    *La aplicación se abrirá en `http://localhost:4200` y automáticamente consumirá los datos de la API de Flask.*

## 5. Calidad del Código y Pruebas

### Frontend
* **Inyección de Dependencias:** Uso de `ConsumoService` para centralizar la lógica HTTP.
* **Bindings Dinámicos:** Utilización de `[style.--progress]` para inyectar variables CSS dinámicas, garantizando el correcto renderizado del gráfico circular sin problemas de *parsing*.

### Backend
* **Pruebas Unitarias:** Se realizaron pruebas con `pytest` y `pytest-html` para verificar la funcionalidad de los *endpoints* (ej. verificar el `status code 200` y la estructura de la respuesta JSON).

## 6. Manejo de Errores

El módulo Angular incluye un *hook* de error que verifica el `status` de la respuesta de la API. Si la API no está disponible (ej. error de red o 500), se muestra un mensaje de alerta visible (`alert-danger`) con la opción de reintentar la conexión.

**Autor:** Gianni Condo  
**Utima actualización:** Octubre 2025  
**Propósito:** Reto Técnico Especialista de Desarrollo TI Xtrim