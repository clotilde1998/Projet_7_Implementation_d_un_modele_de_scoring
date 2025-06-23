from fastapi.testclient import TestClient
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from fastapi import status
import json
from api import app
 
client = TestClient(app)
 

def test_read_main():
    """Test l'endpoint racine de l'API."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}

 
def test_check_client_id():
    """Test la fonction check_client_id() de l'API avec un client existant."""
    url = "/209192"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == True  # Pas besoin de `json.loads()`, `response.json()` suffit
 
def test_check_client_id_2():
    """Test la fonction check_client_id() de l'API avec un client inexistant."""
    url = "/2091920"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == False
 
def test_get_prediction():
    """Test la fonction get_prediction() de l'API."""
    url = "/prediction/209192"
    response = client.get(url)
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, dict)
    assert "probability_default" in json_response
    assert isinstance(json_response["probability_default"], float)
 
def test_get_shap_values():
    """Test de la fonction get_shap_values() de l'API."""
    url = "/interpretabilite/209192"
    response = client.get(url)
 
    # Vérifiez le statut de la réponse
    assert response.status_code == 200
    # Afficher les valeurs SHAP
    shap_values = response.json()
    print("SHAP Values:", shap_values)