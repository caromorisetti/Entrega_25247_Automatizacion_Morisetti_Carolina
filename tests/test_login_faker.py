from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from utils.logger import logger
from utils.data import csv_login
from faker import Faker
# Prueba para comportamiento del login usando credenciales falsas generadas automáticamente con Faker
# Inicializamos Faker
fake = Faker()
@pytest.mark.parametrize("user,password,should_work", [
    (fake.user_name(), fake.password(), 'false'),
    (fake.user_name(), fake.password(), 'false')
])
def test_login(driver,user,password,should_work):
    logger.info(f"Probando login con usuario: {user}, password: {password}, se espera que funcione: {should_work}")
    login_page = LoginPage(driver)
    login_page.open_page()
    logger.info("Ejecutando login inválido")
    login_page.do_login(user, password)
    logger.info("Verificando usuario y password invalidos")
    if should_work == 'true':
        assert "inventory" in driver.current_url, "No se redirigio al inventario"
        logger.info("El login fue exitoso")
    elif should_work == 'false':
        logger.info("Verificando que aparezca el mensaje de error correspondiente")
        message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        logger.info(f"Mensaje de error recibido: {message}")
        assert "Epic sadface: Username and password do not match any user in this service" in message, "El mensaje de error no es correcto"
    