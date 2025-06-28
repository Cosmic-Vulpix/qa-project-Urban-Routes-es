import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from WaitHelpers import Waiters
from UrbanRoutes import UrbanRoutesPage
from Helpers import Get_phone_code, retrieve_phone_code


class Tests:

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
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        #Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()

        #La tarifa "comfort" está selccionada
        routes_page.set_fee('Comfort')
        comfort_fare = self.driver.find_element(By.XPATH, "//button[@data-for='tariff-card-4']")
        assert "active" in comfort_fare.get_attribute("class")

    # 3.- Rellenar número de teléfono
    def test_set_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Hace click en el campo del Número de telefono
        routes_page.click_phone_number()
        wait.wait_for_phone_window()

        #Hace click e ingresa un número en el nuevo campo del Número de telefono
        routes_page.click_new_phone()
        routes_page.set_phone_number(data.phone_number)

        # Verifica que el número ingresado coincide con el que está en el campo
        get_phone = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        assert get_phone.get_attribute("value") == data.phone_number

        routes_page.click_next_button()

        #Intercepta el código SMS y lo introduce en el campo del mismo
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(phone_code)
        routes_page.click_confirm_button()


    # 4.- Agrega una nueva tarjeta
    def test_set_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Hace click en el campo de "Método de pago"
        routes_page.click_pay_method()

        #Hace click en el botón para agregar tarjeta
        routes_page.click_add_paycard()

        #Ingresa número de tarjeta
        routes_page.set_card_number(data.card_number)

        # Verificar número de tarjeta
        get_card_number = self.driver.find_element(By.CSS_SELECTOR, "input#number[name='number']")
        assert get_card_number.get_attribute("value") == data.card_number

        #Ingresar código de tarjeta
        routes_page.set_card_code(data.card_code)

        #Verificar código de tarjeta
        get_card_code = self.driver.find_element(By.CSS_SELECTOR, "input#code[name='code']")
        assert get_card_code.get_attribute("value") == data.card_code

        routes_page.click_add_button()

        #Verificar que se agrego nueva tarjeta
        assert 'Tarjeta' in self.driver.find_element(By.XPATH, "//div[@class='pp-row'][2]/div[@class='pp-title']").text

        routes_page.quit_pay_window()

    # 5.- Escribir mensaje al conductor
    def test_message (self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Centra y escribe un mensaje en el campo "Mensaje para el conductor
        routes_page.input_message(data.message_for_driver)

        #Verificar mensaje al conductor
        get_message = self.driver.find_element(*routes_page.message_field)
        assert get_message.get_attribute('value') == data.message_for_driver

    # 6.- Pedir manta y pañuelos
    def test_add_BlanketsAndTissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Centra y activa la opción de mantas y pañuelos
        routes_page.add_blankets_and_tissues()

        #Verificar que se ha marcado el checkbox
        checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        assert checkbox.is_selected(), "El checkbox NO está marcado"

    # 7.- Pedir helados
    def test_add_2_icecream(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        #Centra y agrega dos helados
        routes_page.add_ice_cream()

        # Verificar que se ha marcado el checkbox
        current_value = self.driver.find_element(By.XPATH, "//div [@class='counter-value']").text
        assert current_value == '2'

    # 8.- Pedir Taxi
    def test_take_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        # Hace click en el campo del Número de telefono
        routes_page.click_phone_number()
        wait.wait_for_phone_window()

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

        get_taxi_window = self.driver.find_element(By.XPATH, "//div[@class='order-header-title' and text()='Buscar automóvil']")
        wait.wait_for_taxi_window()
        assert get_taxi_window.is_displayed()


    # 9.- Esperar a la ventana de información del conductor
    def test_wait_for_driver_window(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        wait = Waiters(self.driver)

        # Introduce las direcciones
        address_from = data.address_from
        address_to = data.address_to

        # Establece la ruta
        routes_page.set_route(address_from, address_to)
        routes_page.click_taxi_button()

        # Selecciona la tarifa deseada, EX: 'Comfort'
        wait.wait_for_load_fees()
        routes_page.set_fee('Comfort')

        # Hace click en el campo del Número de telefono
        routes_page.click_phone_number()
        wait.wait_for_phone_window()

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
        wait.wait_for_taxi()

        get_driver_coming = self.driver.find_element(By.XPATH, "//div[@class='order-header-title']")
        assert get_driver_coming.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
