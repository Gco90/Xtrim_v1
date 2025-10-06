# Módulo de Auto-Gestión: Visualización de Consumo (Frontend)

Este proyecto implementa la interfaz de usuario (GUI) para el Módulo de Visualización de Consumo de TelcoX, desarrollado en Angular. Se conecta a una API RESTful que simula el sistema BSS (Business Support System) para ofrecer una experiencia de usuario intuitiva y de alto rendimiento.

## 1. Tecnologías y Versiones

Categoría	Tecnología	Versión	Notas
Framework	Angular	20.x	Desarrollado con Angular CLI.
Estilos	Bootstrap 5	5.3.3	Utilizado para layout responsivo.
Iconografía	Bootstrap Icons	npm package	Iconos vectoriales para la UI.
Comunicación	HttpClientModule		Usado para peticiones GET a la API RESTful.

## 2. Arquitectura y Estructura del Código

El proyecto sigue el patrón de separación de responsabilidades de Angular, utilizando Servicios para la gestión de datos y Componentes para la presentación.

### 2.1. Estructura de Componentes y Servicios

Archivo/Clase	Tipo	Responsabilidad
ConsumoService	Service	Centraliza toda la lógica de comunicación HTTP. Aísla al componente de los detalles de la API (URL, errores de red).
ConsumoComponent	Component	Lógica de presentación, gestión de estados (cargando, error) y binding de datos.
consumo.html	Template	Presentación de la GUI, uso de directivas (*ngIf) y bindings dinámicos.

### 2.2. Solución Avanzada para el Gráfico Circular (CSS Puros)

Para el indicador principal de Consumo de Datos Fijos/Móviles, se empleó una técnica de CSS puro (conic-gradient) combinada con un binding eficiente de Angular.

    Objetivo: Evitar librerías externas y el uso de calc(attr(...)) o grados (deg).

    Implementación: La variable CSS se inyecta con el número puro (ej. 75) y el CSS se encarga de aplicar la unidad de porcentaje.

 **Lógica de Binding:**

#### **1. HTML (Pasa el número puro):**
La función getDatosPercent() calcula el porcentaje y lo pasa como un número sin unidad a la variable CSS:
    ```HTML

    <div class="circular-progress" 
        [style.--progress]="getDatosPercent()">
    ```
#### **2. CSS (Aplica la unidad con calc()):**
El CSS utiliza calc() para tomar el número y multiplicarlo por 1%, convirtiéndolo en un valor de porcentaje válido para conic-gradient():
    ```CSS

    .circular-progress::before {
        /* ... */
        background: conic-gradient(
            #007bff 0% calc(var(--progress) * 1%), 
            transparent calc(var(--progress) * 1%) 100%
        );
    }
    ```
## **3. Integración Backend y Gestión de Errores**

**3.1. Conexión de API**

El servicio se conecta al endpoint de Flask: http://localhost:5000/api/consumo.

**3.2. Robustez y Manejo de Estados**

La aplicación gestiona los siguientes estados de la interfaz de usuario:
**Estado**	Indicador en UI	Lógica Controlada
**Cargando**	Muestra un spinner.	Se ejecuta al inicio (ngOnInit) y en la función Actualizar Datos.
**Éxito**	Muestra los datos y el panel de consumo.	Se activa cuando el servicio responde con 200 OK.
**Error**	Muestra una alerta con el código y un mensaje detallado.	Captura fallos de red (HttpErrorResponse) y errores del servidor. Proporciona un botón de Reintentar.

## 4. Guía de Ejecución

Esta aplicación requiere que el Servidor API RESTful (Flask) esté corriendo en http://localhost:5000.

Requisitos Previos

    Node.js (v20+), npm, y Angular CLI (v20+).

### 4.1. Instalación

    Navegue a la carpeta del proyecto Frontend.

    Instale las dependencias:
    ```Bash

    npm install
    ```
### 4.2. Inicio de la Aplicación

    Asegúrese de que el Backend de Flask esté activo en el puerto 5000.

    Inicie el servidor de desarrollo de Angular:
    ```Bash

    ng serve --open
    ```
La aplicación se abrirá en su navegador predeterminado en http://localhost:4200.

**Autor:** Gianni Condo  
**Utima actualización:** Octubre 2025  
**Propósito:** Reto Técnico Especialista de Desarrollo TI Xtrim