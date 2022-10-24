import allure
import pytest
from pages.header import Header
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


class TestHeader:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup_teardown(self):
        service = Service(executable_path=GeckoDriverManager().install())
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(service=service, options=options)
        self.driver = driver
        self.page = Header(self.driver)
        self.page.get_url()
        yield
        driver.quit()


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

