import requests
import pytest
from utils.logger import logger
# Obtener Usuario GET
def test_get_user(url_base, header_request):
    logger.info(f"Solicitud GET a {url_base}")
    # Realizar solicitud GET para obtener un usuario específico
    response = requests.get(f"{url_base}/2", headers=header_request)
    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200
    data = response.json()
    logger.info("Validando id dentro del usuario")
    # Verificar que el ID del usuario es correcto
    assert data["data"]["id"] == 2
# Crear Usuario POST
def test_create_user(url_base, header_request):
    payload = {
        "name": "Moana",
        "job": "Medica"
    }
    logger.info(f"Solicitud POST a {url_base}")
    # Realizar solicitud POST para crear un nuevo usuario
    response = requests.post(url_base, headers=header_request, json=payload)
    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 201
    data = response.json()
    logger.info("Validando id dentro del usuario")
    # Verificar que el nombre y trabajo del usuario creado son correctos
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
# Actualizar Usuario PUT
def test_update_user(url_base, header_request):
    payload = {
        "job": "Capitana"
    }
    logger.info(f"Solicitud PUT a {url_base}")
    # Realizar solicitud PUT para actualizar un usuario existente
    response = requests.put(f"{url_base}/2", headers=header_request, json=payload)
    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200
    data = response.json()
    logger.info("Validando id dentro del usuario")
    # Verificar que el nombre y trabajo del usuario actualizado son correctos
    assert data["job"] == "Capitana"
# Eliminar Usuario DELETE
def test_delete_user(url_base, header_request):
    logger.info(f"Solicitud DELETE a {url_base}")
    # Realizar solicitud DELETE para eliminar un usuario específico
    response = requests.delete(f"{url_base}/2", headers=header_request)
    logger.info(f"Status code: {response.status_code}")
    # Verificar que la respuesta tiene el código de estado 204 (No Content)
    assert response.status_code == 204