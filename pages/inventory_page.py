from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
# Clase Page Object para la página de inventario
class InventoryPage:
    # URL
    URL = "https://www.saucedemo.com/inventory.html"
    # Selectores
    _INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    _BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".inventory_item button")
    _BUTTON_REMOVE_FROM_CART = (By.CLASS_NAME, "btn_inventory")
    _SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   
    # Método para obtener los productos en inventario
    def get_products(self):
        # Esperar a que los productos estén visibles
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEM))
        products = self.driver.find_elements(*self._INVENTORY_ITEM)
        return products
    # Método para obtener los nombres de los productos
    def get_name_products(self):
        products = self.driver.find_element(self._INVENTORY_ITEM_NAME)
        return [product_name.text for product_name in products]
    # Método agregar producto al carrito
    def add_product_to_cart(self):
        products = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEM)) 
        button_product = products[0].find_element(*self._BUTTON_ADD_TO_CART)
        button_product.click()
    # Método para agregar producto por nombre
    def add_product_by_name(self,name_product):
        products = self.driver.find_elements(*self._INVENTORY_ITEM)   
        for product in products:
            name = product.find_element(*self._INVENTORY_ITEM_NAME).text.strip()
            if name.strip() == name_product.strip():
                button = product.find_element(*self._BUTTON_ADD_TO_CART)
                button.click()
                return self
        raise Exception(f"No se encontro el producto {name_product}")
    #Método para abrir carrito de compras
    def open_shopping_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable(self._SHOPPING_CART_LINK))
        cart_link.click()
    # Método para verificar el carrito
    def get_count_product(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._SHOPPING_CART_BADGE)) 
            contador_carrito = self.driver.find_element(*self._SHOPPING_CART_BADGE)
            return int(contador_carrito.text)
        except:
            return 0