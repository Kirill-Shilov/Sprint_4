import allure
import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures('driver', 'page')
@pytest.mark.parametrize('classname', [MainPage])
class TestDropdownList:
    driver = None


    @allure.title("Проверка 'Сколько это стоит'")
    def test_check_price(self, page):
        text = page.check_element(page.dropdown_element_0,
                                       page.element_text_0,
                                       page.expected_text_0)
        assert text


    @allure.title("Проверка 'Хочу сразу несколько'")
    def test_check_butch(self, page):
        text = page.check_element(page.dropdown_element_1,
                                       page.element_text_1,
                                       page.expected_text_1)
        assert text


    @allure.title("Проверка 'Как рассчитывается время аренды'")
    def test_check_time(self, page):
        text = page.check_element(page.dropdown_element_2,
                                       page.element_text_2,
                                       page.expected_text_2)
        assert text


    @allure.title("Проверка 'Можно ли заказать на сегодня'")
    def test_check_today(self, page):
        text = page.check_element(page.dropdown_element_3,
                                       page.element_text_3,
                                       page.expected_text_3)
        assert text


    @allure.title("Проверка 'Можно ли продлить заказ или вернуть раньше'")
    def test_check_prolong(self, page):
        text = page.check_element(page.dropdown_element_4,
                                       page.element_text_4,
                                       page.expected_text_4)
        assert text


    @allure.title("Проверка 'Вы привозите зарядку вместе с самокатом?'")
    def test_check_charge(self, page):
        text = page.check_element(page.dropdown_element_5,
                                       page.element_text_5,
                                       page.expected_text_5)
        assert text


    @allure.title("Проверка 'Можно ли отменить заказ?'")
    def test_check_cancel(self, page):
        text = page.check_element(page.dropdown_element_6,
                                       page.element_text_6,
                                       page.expected_text_6)
        assert text


    @allure.title("Проверка 'Я жизу за МКАДом, привезёте?'")
    def test_check_mkad(self, page):
        text = page.check_element(page.dropdown_element_7,
                                       page.element_text_7,
                                       page.expected_text_7)
        assert text

