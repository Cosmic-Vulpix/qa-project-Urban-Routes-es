from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Waiters:

    tariffs = (By.CLASS_NAME, 'tariff-cards')
    phone_window = (By.CLASS_NAME, "head")
    taxi_window = (By.XPATH, "//div[@class='order-header-title']")
    taxi_coming_header = (By.XPATH,"//div[@class='order-header-title' and contains(text(), 'El conductor llegará en')]")

    def __init__(self, driver):
        self.driver = driver

    #Establece tiempo de espera para que cargue las opciones de tarifas
    def wait_for_load_fees(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.tariffs))

    #Espera a la ventana de teléfono
    def wait_for_phone_window(self):
        WebDriverWait(self.driver,3).until(expected_conditions.presence_of_element_located(self.phone_window))

    def wait_for_taxi_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.taxi_window))

    # Esperar a que aparezca la ventana de busqueda de conductor
    def wait_for_taxi(self):
        WebDriverWait(self.driver, 35).until(expected_conditions.presence_of_element_located(self.taxi_coming_header))
        WebDriverWait(self.driver, 3)