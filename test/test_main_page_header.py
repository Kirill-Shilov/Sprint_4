import allure
import pytest
from pages.main_page_header import Header


@pytest.mark.usefixtures('driver', 'page')
@pytest.mark.parametrize('classname', [Header])
class TestHeader:

    driver = None


    @allure.description('Проверка редиректа по клику на логотип "Самокат"')
    @allure.title('Самокат logo')
    def test_regirect_to_mainpage(self, page):
        assert page.check_redirect_to_mainpage()


    @allure.description('Проверка перехода на сайт яндекса')
    @allure.title('Яндекс logo')
    def test_redirect_to_yandex(self, page):
        assert page.check_redirect_to_yandex()

