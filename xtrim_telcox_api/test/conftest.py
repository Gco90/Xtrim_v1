# backend/tests/conftest.py

import pytest
from src.app import app as flask_app # Importa la app de tu app.py

@pytest.fixture
def client():
    # Establece la aplicación en modo de prueba para capturar errores de forma limpia
    flask_app.config['TESTING'] = True
    
    # Crea el cliente de prueba de Flask
    with flask_app.test_client() as client:
        yield client # Devuelve el cliente al test que lo solicite