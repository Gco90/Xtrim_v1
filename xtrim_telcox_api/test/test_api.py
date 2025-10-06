# xtrim_telcox/tests/test_api.py
import pytest
#from src.app import app   # importa tu aplicación Flask
from src.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True  # modo test
    with app.test_client() as client:
        yield client

def test_consumo_status_code_ok(client):
    """
    Prueba que el endpoint principal de consumo devuelve un código 200 OK.
    """
    # Usamos el cliente para simular una petición GET a /api/consumo
    response = client.get('/api/consumo')
    
    # 1. Afirmación: Verifica el código de estado HTTP
    assert response.status_code == 200

def test_consumo_json_structure(client):
    """
    Prueba que la respuesta JSON contiene los campos esenciales.
    """
    response = client.get('/api/consumo')
    data = response.get_json()
    
    # 1. Afirmación: Verifica que la respuesta es un diccionario
    assert isinstance(data, dict)
    
    # 2. Afirmación: Verifica que los campos clave existen
    assert 'cliente' in data
    assert 'saldo_cuenta' in data
    assert 'datos_gb' in data
    assert 'minutos' in data
    
    # 3. Afirmación: Verifica el tipo de datos para evitar errores de frontend
    assert isinstance(data['datos_gb'], (int, float))
    assert isinstance(data['proximo_corte'], str)

def test_consumo_cliente_id_status_code_ok(client):
    """
    Prueba que el endpoint con ID de cliente devuelve un código 200 OK.
    """
    # Prueba con un ID de cliente específico, como 5
    response = client.get('/api/consumo/5')
    
    # Afirmación: Verifica el código de estado
    assert response.status_code == 200
    
    # Afirmación: Verifica que el nombre del cliente se actualizó
    data = response.get_json()
    assert data['cliente']['nombre'] == "Cliente 5"