import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import pathlib
from datetime import datetime
# Carpeta donde se guarda screenshot
target = pathlib.Path("reports/screenshots")
# Crear la carpeta si no existe
target.mkdir(parents=True, exist_ok=True)
# Fixture para inicializar y cerrar el navegador
@pytest.fixture
def driver():
    # Configuraciones Github Actions
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable=gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
        
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
# Fixture para realizar login antes de cada test que lo requiera   
@pytest.fixture
def logged_in_driver(driver):
    LoginPage(driver).open_page()
    return driver
# Fixture url base para API tests
@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"
# Fixture headers para API tests
@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_6f749bc69df646aeaccac5183440a6d1"}
# Crear un hook para agregar información al reporte de pytest
# Ejecutar codigo del test y luego se ejecuta el codigo del hook
@pytest.hookimpl(hookwrapper=True)
# Item representa el test que se esta ejecutando y Call representa la ejecucion interna del test
def pytest_runtest_makereport(item, call):
    # yield es una pausa en la ejecucion del hook para permitir que el test se ejecute
    outcome = yield
    report = outcome.get_result()
    # Setup es la preparacion del test, call es la ejecucion del test, teardown es la limpieza despues del test
    if report.when in ("setup", "call") and report.failed:
        # Obtener el driver del test
        driver = item.funcargs.get("driver",None)
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Generamos el archivo de screenshot
            file_name = target / f"{report.when}_{item.name}_{timestamp}.png"
            # Guardar screenshot
            driver.save_screenshot(str(file_name))