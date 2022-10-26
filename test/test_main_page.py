import allure
import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures('driver')
class TestDropdownList:

    driver = None


    @pytest.fixture(scope='function', autouse=True)
    def hadnle_driver(self, driver):
        self.driver = driver
        self.page = MainPage(self.driver)
        self.page.get_url()


    @allure.title("Проверка 'Сколько это стоит'")
    def test_check_price(self):
        text = self.page.check_element(self.page.dropdown_element_0,
                                       self.page.element_text_0,
                                       self.page.expected_text_0)
        assert text


    @allure.title("Проверка 'Хочу сразу несколько'")
    def test_check_butch(self):
        text = self.page.check_element(self.page.dropdown_element_1,
                                       self.page.element_text_1,
                                       self.page.expected_text_1)
        assert text


    @allure.title("Проверка 'Как рассчитывается время аренды'")
    def test_check_time(self):
        text = self.page.check_element(self.page.dropdown_element_2,
                                       self.page.element_text_2,
                                       self.page.expected_text_2)
        assert text


    @allure.title("Проверка 'Можно ли заказать на сегодня'")
    def test_check_today(self):
        text = self.page.check_element(self.page.dropdown_element_3,
                                       self.page.element_text_3,
                                       self.page.expected_text_3)
        assert text


    @allure.title("Проверка 'Можно ли продлить заказ или вернуть раньше'")
    def test_check_prolong(self):
        text = self.page.check_element(self.page.dropdown_element_4,
                                       self.page.element_text_4,
                                       self.page.expected_text_4)
        assert text


    @allure.title("Проверка 'Вы привозите зарядку вместе с самокатом?'")
    def test_check_charge(self):
        text = self.page.check_element(self.page.dropdown_element_5,
                                       self.page.element_text_5,
                                       self.page.expected_text_5)
        assert text


    @allure.title("Проверка 'Можно ли отменить заказ?'")
    def test_check_cancel(self):
        text = self.page.check_element(self.page.dropdown_element_6,
                                       self.page.element_text_6,
                                       self.page.expected_text_6)
        assert text


    @allure.title("Проверка 'Я жизу за МКАДом, привезёте?'")
    def test_check_mkad(self):
        text = self.page.check_element(self.page.dropdown_element_7,
                                       self.page.element_text_7,
                                       self.page.expected_text_7)
        assert text

