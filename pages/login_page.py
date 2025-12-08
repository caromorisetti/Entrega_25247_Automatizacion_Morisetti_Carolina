from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Clase Page Object para la página de login
class LoginPage:
    # URL
    URL = "https://www.saucedemo.com/"    
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   
    # Método para abrir la página de login   
    def open_page(self):
        self.driver.get(self.URL)
        return self
    # Método usuario
    def enter_user(self, user):
        input = self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))
        input.clear()
        input.send_keys(user)
        return self
    # Método password
    def enter_password(self, password):
        input = self.driver.find_element(*self._PASSWORD_INPUT)
        input.clear()
        input.send_keys(password)
        return self
    # Método click boton login
    def click_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        button.click()
        return self
    # Método login completo
    def do_login(self, user, password):
        self.enter_user(user)
        self.enter_password(password)
        self.click_button()
        return self
    # Método para obtener el mensaje de error
    def get_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3")))
        return div_error.text
    