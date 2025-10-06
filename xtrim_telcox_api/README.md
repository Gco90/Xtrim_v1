# El Modulo API: Simulador BSS (Business Support System)

Este modulo implementa el **backend ficticio** requerido para el **Reto de Desarrollo Fullstack de TelcoX**.  
Su objetivo es **simular las respuestas de un sistema BSS**, proporcionando datos dinamicos (aleatorios) de **consumo, saldo y minutos** a la interfaz de usuario desarrollada en Angular.

La API fue desarrollada en **Python** utilizando el micro-framework **Flask**.

---

##  1. Tecnologías y Dependencias

- **Lenguaje:** Python 3.x  
- **Framework:** Flask  
- **Middleware:** Flask-CORS (permite peticiones desde el Frontend Angular)  
- **Entorno recomendado:** entorno virtual (`venv`)

---

##  2. Configuración y Ejecución

Sigue estos pasos para levantar el servidor API localmente:

### 1 Navega al directorio del proyecto

```bash
cd xtrim_telcox_api/
```

### 2 Crea y activa el entorno virtual

```bash
python -m venv venv
```

**En Linux/macOS:**
```bash
source venv/bin/activate
```

**En Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

### 3 Instala las dependencias

```bash
pip install Flask flask-cors
```

### 4 Ejecuta la aplicaci贸n

```bash
python src/app.py
```

El servidor se iniciará en:  
 **http://0.0.0.0:5000** o **http://localhost:5000**

---

##  3. Endpoints de la API RESTful

La API expone los siguientes endpoints en el puerto **5000**, bajo la ruta base `/api/`.

| Método | Endpoint | Parámetro | Descripción |
|:-------|:----------|:-----------|:-------------|
| **GET** | `/api/consumo` | N/A | Devuelve datos aleatorios para el cliente demo (**Gianni Condo**). Endpoint principal usado por el Frontend. |
| **GET** | `/api/consumo/<id>` | `cliente_id` *(int)* | Devuelve datos aleatorios para un cliente específico. Ejemplo: `/api/consumo/123`. |

---

##  4. Estructura de la Respuesta JSON (200 OK)

Todos los endpoints devuelven un objeto JSON con valores aleatorios para simular un sistema BSS en tiempo real.

###  Ejemplo de respuesta:

```json
{
  "cliente": {
    "id": 1,
    "nombre": "Gianni Condo"
  },
  "plan_actual": "Mega Fibra Plus",
  "saldo": 49.05,
  "datos_gb": 14.9,
  "datos_limite_gb": 20,
  "minutos": 173,
  "minutos_limite": 500,
  "sms": 186,
  "sms_limite": 500,
  "ultima_actualizacion": "2025-10-04T05:35:00.000000Z",
  "saldo_cuenta": 49.05,
  "proximo_corte": "2025-11-25",
  "ultima_factura": 45.99
}
```

---

##  5. Manejo de Errores

- **Error 500 Internal Server Error:**  
  Cualquier excepción no controlada dentro del código Python activará el manejador global de errores y devolverá un JSON como este:

  ```json
  { "error": "Internal Server Error" }
  ```

- **CORS:**  
  La configuración `CORS(app)` permite peticiones desde cualquier dominio, asegurando que el **Frontend Angular** pueda consumir la API sin restricciones de origen.

---

##  6. Pruebas Unitarias

El proyecto incluye pruebas automatizadas utilizando **Pytest**.

### Ejecutar pruebas:
```bash
pytest -v
```

### Generar reporte HTML:
```bash
pytest --html=report.html
```

El reporte se genera en la raíz del proyecto como `report.html`.

---

## 7. Estructura del Proyecto

```bash
xtrim_telcox_api/
 src/
    __init__.py
    app.py
tests/
    __init__.py
   test_app.py

README.md
```

---

**Autor:** Gianni Condo  
**Utima actualización:** Octubre 2025  
**Propósito:** Reto Técnico Especialista de Desarrollo TI Xtrim
