from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest
# Prueba para agregar un producto al carrito y verificarlo
@pytest.mark.parametrize("user,password", [("standard_user","secret_sauce")])
def test_inventory(logged_in_driver,user,password):
     try: 
          driver = logged_in_driver
          driver.implicitly_wait(3)
          # Navegar a la página de inventario
          inventory_page = InventoryPage(driver)
          # Agregar producto
          inventory_page.add_product_to_cart()
          # Abrir carrito de compras
          inventory_page.open_shopping_cart()
          # Validar que el producto agregado está en el carrito
          cartPage = CartPage(driver)          
          products_in_cart = cartPage.get_products_cart()
          assert len(products_in_cart) == 1, "El carrito no tiene el producto agregado"              
     except Exception as e:
          print("Error durante la navegacion:", e)
          raise
