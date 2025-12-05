import data
from selenium import webdriver
from urban_routes_page import UrbanRoutesPage
from utils import is_countdown_timer_zero
from selenium.webdriver.support.ui import WebDriverWait


class TestUrbanRoutes:

    driver = None
    initial_header = None
    final_header = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    # Test1
    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # Test2
    def test_request_comfort_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_button()
        assert self.driver.find_element(*routes_page.comfort_button_container).get_attribute('class') == 'tcard active'

    # Test3
    def test_phone_verification(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_button()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_phone_next_button()
        routes_page.set_verification_code()
        routes_page.click_confirm_button_in_verification_popup()
        assert self.driver.find_element(*routes_page.phone_field).get_property('value') == data.phone_number

    #Test4
    def test_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method_field()
        routes_page.click_add_card_button()
        routes_page.set_card_number()
        routes_page.set_card_code()
        routes_page.press_tab_key()
        routes_page.click_add_card_confirm_button()
        routes_page.click_exit_button_in_payment_popup()
        assert self.driver.find_element(*routes_page.payment_method_selected).text == 'Tarjeta'

    #Test5
    def test_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_to_driver()
        assert routes_page.driver.find_element(*routes_page.message_to_driver_field).get_property('value') == data.message_for_driver

    #Test6
    def test_click_blankets_and_tissues_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        initial_state = routes_page.get_blankets_and_tissues_button_state()
        routes_page.click_blankets_and_tissues_button()
        final_state = routes_page.get_blankets_and_tissues_button_state()
        assert initial_state != final_state, "El estado del botón no cambió."

    #Test7
    def test_add_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        ice_cream_to_order = 2
        routes_page.click_add_ice_cream_button(ice_cream_to_order)
        assert self.driver.find_element(*routes_page.ice_cream_counter).text == str(ice_cream_to_order)

    #Test8
    def test_click_order_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.initial_header = routes_page.get_waiting_popup_header()
        routes_page.click_order_taxi_button()
        assert self.driver.find_element(*routes_page.waiting_popup_header).text == 'Buscar automóvil'

        wait = WebDriverWait(self.driver, 60)
        wait.until(lambda driver: is_countdown_timer_zero(driver, routes_page.order_countdown_timer))

    #Test9
    def test_driver_information_modal_displayed(self):
        routes_page = UrbanRoutesPage(self.driver)
        self.final_header = routes_page.get_waiting_popup_header()
        assert self.initial_header != self.final_header, "El encabezado del popup no cambió."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()