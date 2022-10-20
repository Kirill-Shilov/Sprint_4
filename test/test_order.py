import allure
from pages.order_page import OrderPage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


class TestOrder:

    driver = None


    @classmethod
    def setup_class(cls):
        service = Service(executable_path=GeckoDriverManager().install())
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=service, options=options)
        cls.driver = driver


    def setup_method(self):
        self.page = OrderPage(self.driver)
        self.page.get_url()


    @allure.description('Позитивный тест заказа с первым набором данных')
    @allure.title('Первый набор данных')
    def test_1(self):
        page = self.page
        page.close_cookie_popup()
        page.use_top_order_button()
        page.fill_fields_1(30, page.street_address_1)
        page.place_order_1()
        page.fill_fields_2(page.time_rent_select_1,
                           page.comment_text_1,
                           page.color_checkbox_1)
        page.place_order_2()
        page.make_order()
        page.wait_for_success()


    @allure.description('Позитивный тест заказа со вторым набором данных')
    @allure.title('Второй набор данных')
    def test_2(self):
        page = self.page
        page.close_cookie_popup()
        page.use_bottom_order_button()
        page.fill_fields_1(60, page.street_address_2)
        page.place_order_1()
        page.fill_fields_2(page.time_rent_select_2,
                           page.comment_text_2,
                           page.color_checkbox_2)
        page.place_order_2()
        page.make_order()
        page.wait_for_success()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
