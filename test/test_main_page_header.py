import allure
import pytest
from pages.main_page_header import Header


@pytest.mark.usefixtures('driver')
class TestHeader:

    driver = None


    @pytest.fixture(scope='function', autouse=True)
    def hadnle_setup_teardown(self, driver):
        self.driver = driver
        self.page = Header(self.driver)
        self.page.get_url()


    @allure.description('Проверка редиректа по клику на логотип "Самокат"')
    @allure.title('Самокат logo')
    def test_regirect_to_mainpage(self):
        page = self.page
        assert page.check_redirect_to_mainpage()


    @allure.description('Проверка перехода на сайт яндекса')
    @allure.title('Яндекс logo')
    def test_redirect_to_yandex(self):
        page = self.page
        assert page.check_redirect_to_yandex()

