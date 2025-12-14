from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import logger
from pages.cart_page import CartPage
from utils.lector_json import read_json_products
import time
# Prueba para agregar productos al carrito usando datos de un archivo JSON
RUTA_JSON = "data/products.json"
@pytest.mark.parametrize("user,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("product",read_json_products(RUTA_JSON))
def test_cart_json(logged_in_driver, user, password, product):
    try:
        driver = logged_in_driver
        logger.info(f"URL antes del login: {driver.current_url}")
        LoginPage(driver).do_login(user,password)
        logger.info(f"URL después del login: {driver.current_url}")
        # Abrir la página de inventario
        inventory_page = InventoryPage(driver)
        # Agregar producto al carrito por nombre desde el JSON
        name_product = product["nombre"]
        logger.info(f"Producto a agregar al carrito (desde JSON): {name_product}")
        # Agregar al carrito el producto
        inventory_page.add_product_by_name(name_product)
        logger.info("Abriendo carrito de compras")
        # Abrir el carrito
        inventory_page.open_shopping_cart()
        # Esperar a que cargue
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        logger.info("Inicializando CartPage")
        cart_page = CartPage(driver)
        # Obtener lista de productos del carrito
        products = cart_page.get_name_products_cart()
        # Validación flexible
        assert name_product in products, f"El producto '{name_product}' NO está en el carrito. Contenido actual: {products}"
        logger.info("Producto validado correctamente en el carrito")
    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise