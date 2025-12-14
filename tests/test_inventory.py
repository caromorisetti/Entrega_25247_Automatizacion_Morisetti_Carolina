from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
from utils.logger import logger
# Prueba para agregar un producto al carrito y validar el conteo e inventario
@pytest.mark.parametrize("user,password", [("standard_user","secret_sauce")])
def test_inventory(logged_in_driver,user,password):
     try: 
          driver = logged_in_driver
          logger.info(f"URL actual antes del login: {driver.current_url}")
          LoginPage(driver).do_login(user,password)
          logger.info(f"URL despues del login: {driver.current_url}")
          driver.implicitly_wait(3)
          inventory_page = InventoryPage(driver)
          logger.info("Página de inventario cargada")
          # Verificamos que hay productos en inventario
          assert len(inventory_page.get_products()) > 0, "No hay productos en inventario"
          # Verificar que el carrito está vacío inicialmente
          assert inventory_page.get_count_product() == 0, "El carrito está vacío inicialmente"
          logger.info("Carrito inicialmente vacío validado")
          logger.info("Agregando un producto al carrito")
          # Agregamos un producto al carrito
          inventory_page.add_product_to_cart()
          # Verificamos que el carrito tiene 1 producto
          assert inventory_page.get_count_product() == 1, "El carrito tiene 1 producto después de agregar"
          logger.info("Producto agregado al carrito correctamente")
          # Abrimos el carrito de compras
          inventory_page.open_shopping_cart()
     except Exception as e:
          print("Error durante la navegacion:", e)
          raise