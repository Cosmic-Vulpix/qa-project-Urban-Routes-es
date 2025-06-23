import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from') #Campo de dirección "Desde"
    to_field = (By.ID, 'to') #Campo de dirección "Hasta"
    taxi_button = (By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[1]/div[3]/div[1]/button") #Botón para generar la ruta
    fee_card = "//div[@class='tariff-cards']" #Elemento de opciones de tarifa
    phone_label = (By.CLASS_NAME, "np-button") #Campo de telefono
    phone_field = (By.XPATH, "//div[@class='np-text']") #
    new_phone_field = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/label")
    input_phone_field = (By.XPATH, "//input[@class='input']")
    next_button = (By.XPATH, "//button[@class='button full']")
    code_label = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/label")
    code_phone_field = (By.CSS_SELECTOR, "input[type='text'][placeholder='xxxx']")
    confirm_button = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Confirmar')]")
    pay_label = (By.CLASS_NAME, "pp-text")
    add_paycard = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]")
    card_number = (By.XPATH, "//input[@id='number' and @name='number' and contains(@class, 'card-input')]")
    card_code = (By.XPATH, "//input[@id='code' and @name='code']")
    TAB = (By.CLASS_NAME,"card-wrapper")
    add_card_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    quit_pay = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    message_field = (By.CSS_SELECTOR, "input[type='text'][placeholder='Traiga un aperitivo']")
    blankets_and_tissues_slider = (By.XPATH, "(//span[@class= 'slider round'])[1]")
    ice_cream_slider = (By.XPATH, "(//div[@class='counter-plus'])[1]")
    take_taxi_button = (By.CSS_SELECTOR, "span.smart-button-secondary")
    taxi_coming_header = (By.XPATH, "//div[@class='order-header-title' and contains(text(), 'El conductor llegará en')]")


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

    #Establece tiempo de espera para que cargue las opciones de tarifas
    def wait_for_load_fees(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'tariff-cards')))

    #Selecciona una tarifa
    def set_fee(self, fee_option):
        select_fee = f"{self.fee_card}//div[text()='{fee_option}']"
        self.driver.find_element(By.XPATH, select_fee).click()

    #Hace click al campo de "Numero de telefono"
    def click_phone_number(self):
        self.driver.find_element(*self.phone_field).click()

    def wait_for_phone_window(self):
        WebDriverWait(self.driver,3).until(expected_conditions.presence_of_element_located(self.phone_field))

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
        time.sleep(1)

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
        time.sleep(3)

    #Pedir mantas y pañuelos
    def add_blankets_and_tissues(self):
        element = self.driver.find_element(*self.blankets_and_tissues_slider)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        time.sleep(1)

    #Pedir helados
    def add_ice_cream(self):
        element = self.driver.find_element(*self.ice_cream_slider)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        element.click()
        time.sleep(1)

    #Pedir el taxi
    def take_taxi(self):
        self.driver.find_element(*self.take_taxi_button).click()
        time.sleep(3)

    #Esperar a que aparezca la ventana de busqueda de conductor
    def wait_for_taxi(self):
        WebDriverWait(self.driver, 35).until(expected_conditions.presence_of_element_located(self.taxi_coming_header))
        time.sleep(3)


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    # 1.-Prueba para seleccionar la ruta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        #Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        #Establece la ruta
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # 2.-Prueba para seleccionar la tarifa Comfort
    def test_set_comfort(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        #Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

    # 3.- Rellenar número de teléfono
    def test_set_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Hace click en el campo del Número de telefono
        routes_page.click_phone_number()
        routes_page.wait_for_phone_window()

        #Hace click e ingresa un número en el nuevo campo del Número de telefono
        routes_page.click_new_phone()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()

        #Intercepta el código SMS y lo introduce en el campo del mismo
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(phone_code)
        routes_page.click_confirm_button()


    # 4.- Agrega una nueva tarjeta
    def test_set_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Hace click en el campo de "Método de pago"
        routes_page.click_pay_method()

        #Hace click en el botón para agregar tarjeta
        routes_page.click_add_paycard()

        #Ingresa número y código de tarjeta
        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)

        #Presiona "Siguiente" y el botón de cerrar ventana
        routes_page.click_add_button()
        routes_page.quit_pay_window()

    # 5.- Escribir mensaje al conductor
    def test_message (self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Centra y escribe un mensaje en el campo "Mensaje para el conductor
        routes_page.input_message(data.message_for_driver)

    # 6.- Pedir manta y pañuelos
    def test_add_BlanketsAndTissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Centra y activa la opción de mantas y pañuelos
        routes_page.add_blankets_and_tissues()

    # 7.- Pedir helados
    def test_add_icecream(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Centra y agrega dos helados
        routes_page.add_ice_cream()

    # 8.- Pedir Taxi
    def test_take_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        # Hace click en el campo del Número de telefono
        routes_page.click_phone_number()
        routes_page.wait_for_phone_window()

        # Hace click e ingresa un número en el nuevo campo del Número de telefono
        routes_page.click_new_phone()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()

        # Intercepta el código SMS y lo introduce en el campo del mismo
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(phone_code)
        routes_page.click_confirm_button()

        # Hace click en el campo de "Método de pago"
        routes_page.click_pay_method()

        # Hace click en el botón para agregar tarjeta
        routes_page.click_add_paycard()

        # Ingresa número y código de tarjeta
        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)

        # Presiona "Siguiente" y el botón de cerrar ventana
        routes_page.click_add_button()
        routes_page.quit_pay_window()

        #Pide el taxi
        routes_page.take_taxi()


    # 9.- Esperar a la ventana de información del conductor
    def test_wait_for_taxi_window(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        routes_page.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        # Hace click en el campo del Número de telefono
        routes_page.click_phone_number()
        routes_page.wait_for_phone_window()

        # Hace click e ingresa un número en el nuevo campo del Número de telefono
        routes_page.click_new_phone()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()

        # Intercepta el código SMS y lo introduce en el campo del mismo
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(phone_code)
        routes_page.click_confirm_button()

        # Hace click en el campo de "Método de pago"
        routes_page.click_pay_method()

        # Hace click en el botón para agregar tarjeta
        routes_page.click_add_paycard()

        # Ingresa número y código de tarjeta
        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)

        # Presiona "Siguiente" y el botón de cerrar ventana
        routes_page.click_add_button()
        routes_page.quit_pay_window()

        # Centra y escribe un mensaje en el campo "Mensaje para el conductor
        routes_page.input_message(data.message_for_driver)

        # Centra y agrega dos helados
        routes_page.add_ice_cream()

        #Pide el taxi y espera a que se muestre la información del conductor
        routes_page.take_taxi()
        routes_page.wait_for_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
