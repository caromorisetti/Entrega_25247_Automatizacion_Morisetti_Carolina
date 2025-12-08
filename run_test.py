import pytest

#Lista archivos a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart_json.py",
    "tests/test_login_faker.py"
]
#Argumento para ejecutar las pruebas: Reporte HTML y archivo
pytest_args = test_files + ["-v", "--html=report.html", "--self-contained-html"]    
pytest.main(pytest_args)