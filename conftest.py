import pytest
from selenium import webdriver
from pages.login_page import LoginPage
# Fixture para inicializar y cerrar el navegador
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
# Fixture para realizar login antes de cada test que lo requiera   
@pytest.fixture
def logged_in_driver(driver,user,password):
    LoginPage(driver).open_page().do_login(user,password)
    return driver
# Fixture url base para API tests
@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"
# Fixture headers para API tests
@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_6f749bc69df646aeaccac5183440a6d1"}