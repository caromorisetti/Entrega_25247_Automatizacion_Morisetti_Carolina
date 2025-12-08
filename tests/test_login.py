from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from utils.data import csv_login
from utils.logger import logger
# Prueba para comportamiento del login usando credenciales de un archivo CSV
@pytest.mark.parametrize("user,password,should_work",csv_login("data/data_login.csv"))
def test_login(logged_in_driver,user,password,should_work):
    logger.info(f"Probando login con usuario: {user}, password: {password}, se espera que funcione: {should_work}")
    driver = logged_in_driver    
    if should_work == 'true':
        logger.info("Verificando que se redirija al inventario")
        assert "inventory" in driver.current_url, "No se redirigio al inventario"
        logger.info("El login fue exitoso")
    elif should_work == 'false':
        logger.info("Verificando que aparezca el mensaje de error correspondiente")
        message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        logger.info(f"Mensaje de error recibido: {message}")
        assert "Epic sadface: Username and password do not match any user in this service" in message, "El mensaje de error no es correcto"