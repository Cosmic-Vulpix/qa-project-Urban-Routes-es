from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.CSS_SELECTOR, "button[type='button'].button.round")
    fee_card = "//div[@class='tariff-cards']"
    phone_field = (By.XPATH, "//div[@class='np-text']") #
    new_phone_field = (By.CSS_SELECTOR, "label.label[for='phone']")
    input_phone_field = (By.XPATH, "//input[@class='input']")
    next_button = (By.XPATH, "//button[@class='button full']")
    code_label = (By.XPATH, "//label[@class='label'][text()='Introduce el código']")
    code_phone_field = (By.CSS_SELECTOR, "input[type='text'][placeholder='xxxx']")
    confirm_button = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Confirmar')]")
    pay_label = (By.CLASS_NAME, "pp-text")
    add_paycard = (By.CLASS_NAME, "pp-plus-container")
    card_number = (By.XPATH, "//input[@id='number' and @name='number' and contains(@class, 'card-input')]")
    card_code = (By.XPATH, "//input[@id='code' and @name='code']")
    TAB = (By.CLASS_NAME,"card-wrapper")
    add_card_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    quit_pay = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    message_field = (By.CSS_SELECTOR, "input[type='text'][placeholder='Traiga un aperitivo']")
    blankets_and_tissues_slider = (By.XPATH, "(//span[@class= 'slider round'])[1]")
    ice_cream_slider = (By.XPATH, "(//div[@class='counter-plus'])[1]")
    take_taxi_button = (By.CSS_SELECTOR, "span.smart-button-secondary")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Establace la ruta
    def set_route(self, address_from, address_to):
        self.driver.find_element(*self.from_field).send_keys(address_from)
        self.driver.find_element(*self.to_field).send_keys(address_to)

    #Hace click al botón "Pedir Taxi"
    def click_taxi_button(self):
        self.driver.find_element(*self.taxi_button).click()

    #Selecciona una tarifa
    def set_fee(self, fee_option):
        select_fee = f"{self.fee_card}//div[text()='{fee_option}']"
        self.driver.find_element(By.XPATH, select_fee).click()

    #Hace click al campo de "Numero de telefono"
    def click_phone_number(self):
        self.driver.find_element(*self.phone_field).click()

    #Hace click en el nuevo campo de telefono
    def click_new_phone(self):
        self.driver.find_element(*self.new_phone_field).click()

    #Escribe el telefono en el campo "Número de telefono"
    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.input_phone_field).send_keys(phone_number)

    #Hace click en el botón "Siguiente"
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    #Introduce el código
    def set_phone_code(self, code):
        self.driver.find_element(*self.code_label).click()
        self.driver.find_element(*self.code_phone_field).send_keys(code)
        WebDriverWait(self.driver, 3)

    #Hace click en el botón "Siguiente"
    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    #Hace click en el botón "Método de pago"
    def click_pay_method(self):
        self.driver.find_element(*self.pay_label).click()

    #Hace click en "Agregar tarjeta"
    def click_add_paycard(self):
        self.driver.find_element(*self.add_paycard).click()

    #Introduce un número de tarjeta
    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number).send_keys(card_number)

    #Introduce el código de la tarjeta
    def set_card_code(self, card_code):
        self.driver.find_element(*self.card_code).send_keys(card_code)

    #Hace click en el botón agregar
    def click_add_button(self):
        self.driver.find_element(*self.TAB).click()
        self.driver.find_element(*self.add_card_button).click()

    #Salir de la ventana metodos de pago
    def quit_pay_window(self):
        self.driver.find_element(*self.quit_pay).click()

    #Escribe un mansaje para el conductor
    def input_message(self, message):
        element = self.driver.find_element(By.CSS_SELECTOR, "input#comment")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.find_element(*self.message_field).send_keys(message)
        WebDriverWait(self.driver, 3)

    #Pedir mantas y pañuelos
    def add_blankets_and_tissues(self):
        element = self.driver.find_element(*self.blankets_and_tissues_slider)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        WebDriverWait(self.driver, 3)

    #Pedir helados
    def add_ice_cream(self):
        element = self.driver.find_element(*self.ice_cream_slider)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        element.click()
        WebDriverWait(self.driver, 3)

    #Pedir el taxi
    def take_taxi(self):
        self.driver.find_element(*self.take_taxi_button).click()
        WebDriverWait(self.driver, 3)
