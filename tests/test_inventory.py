from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
import pytest
# Prueba para agregar un producto al carrito y validar el conteo e inventario
@pytest.mark.parametrize("user,password", [("standard_user","secret_sauce")])
def test_inventory(logged_in_driver,user,password):
     try: 
          driver = logged_in_driver
          driver.implicitly_wait(3)
          inventory_page = InventoryPage(driver)
          # Verificamos que hay productos en inventario
          assert len(inventory_page.get_products()) > 0, "No hay productos en inventario"
          # Verificar que el carrito está vacío inicialmente
          assert inventory_page.get_count_product() == 0, "El carrito no está vacío inicialmente"
          # Agregamos un producto al carrito
          inventory_page.add_product_to_cart()
          # Verificamos que el carrito tiene 1 producto
          assert inventory_page.get_count_product() == 1, "El carrito no tiene 1 producto después de agregar"
          # Abrimos el carrito de compras
          inventory_page.open_shopping_cart()
     except Exception as e:
          print("Error durante la navegacion:", e)
          raise