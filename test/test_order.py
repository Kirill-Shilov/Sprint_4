import allure
import pytest
from pages.order_page import OrderPage


@pytest.mark.usefixtures('driver')
class TestOrder:

    driver = None


    @pytest.fixture(scope='function', autouse=True)
    def hadnle_driver(self, driver):
        self.driver = driver
        self.page = OrderPage(self.driver)
        self.page.get_url()


    @allure.description('Позитивный тест заказа с первым набором данных')
    @allure.title('Первый набор данных')
    def test_1(self):
        page = self.page
        page.close_cookie_popup()
        page.use_top_order_button()
        page.fill_fields_1(page.firs_station_choise, page.street_address_1)
        page.place_order_1()
        page.fill_fields_2(page.time_rent_select_1,
                           page.comment_text_1,
                           page.color_checkbox_1)
        page.place_order_2()
        page.make_order()
        assert page.wait_for_success()


    @allure.description('Позитивный тест заказа со вторым набором данных')
    @allure.title('Второй набор данных')
    def test_2(self):
        page = self.page
        page.close_cookie_popup()
        page.use_bottom_order_button()
        page.fill_fields_1(page.second_station_choise, page.street_address_2)
        page.place_order_1()
        page.fill_fields_2(page.time_rent_select_2,
                           page.comment_text_2,
                           page.color_checkbox_2)
        page.place_order_2()
        page.make_order()
        assert page.wait_for_success()

