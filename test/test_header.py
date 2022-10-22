import allure
from pages.header import Header
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


class TestHeader:
    
    driver = None


    @classmethod
    def setup_class(cls):
        service = Service(executable_path=GeckoDriverManager().install())
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(service=service, options=options)
        cls.driver = driver


    def setup_method(self):
        self.page = Header(self.driver)


    @allure.description('Проверка редиректа по клику на логотип "Самокат"')
    def test_regirect_to_mainpage(self):
        page = self.page
        page.check_redirect_to_mainpage()


    @allure.description('Неосилил тест, дзен блокиркует ботов')
    @allure.title('Неосилил')
    def test_1(self):
        page = self.page
        page.check_redirect_to_yandex()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
