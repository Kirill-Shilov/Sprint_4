import allure
from pages.main_page import MainPage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class TestDropdownList:

    driver = None


    @classmethod
    def setup_class(cls):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        cls.driver = driver
        cls.actions = ActionChains(driver)


    def setup_method(self):
        self.page = MainPage(self.driver)
        self.page.get_url()


    def check_element(self, element_locator, text_locator, text):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.actions.move_to_element(element).click(element).perform()
        text_element = self.driver.find_element(*text_locator)
        WebDriverWait(self.driver, 3).until(expected_conditions.
            text_to_be_present_in_element(text_locator, text))
        return True


    @allure.title("Проверка 'Сколько это стоит'")
    def test_check_price(self):
        text = self.check_element(self.page.dropdown_element_0,
                                  self.page.element_text_0,
                                  self.page.expected_text_0)
        assert text


    @allure.title("Проверка 'Хочу сразу несколько'")
    def test_check_butch(self):
        text = self.check_element(self.page.dropdown_element_1,
                                  self.page.element_text_1,
                                  self.page.expected_text_1)
        assert text 


    @allure.title("Проверка 'Как рассчитывается время аренды'")
    def test_check_time(self):
        text = self.check_element(self.page.dropdown_element_2,
                                  self.page.element_text_2,
                                  self.page.expected_text_2)
        assert text 


    @allure.title("Проверка 'Можно ли заказать на сегодня'")
    def test_check_today(self):
        text = self.check_element(self.page.dropdown_element_3,
                                  self.page.element_text_3,
                                  self.page.expected_text_3)
        assert text


    @allure.title("Проверка 'Можно ли продлить заказ или вернуть раньше'")
    def test_check_prolong(self):
        text = self.check_element(self.page.dropdown_element_4,
                                  self.page.element_text_4,
                                  self.page.expected_text_4)
        assert text 


    @allure.title("Проверка 'Вы привоите зарядку вместе с самокатом?'")
    def test_check_charge(self):
        text = self.check_element(self.page.dropdown_element_5,
                                  self.page.element_text_5,
                                  self.page.expected_text_5)
        assert text


    @allure.title("Проверка 'Можно ли отменить заказ?'")
    def test_check_cancel(self):
        text = self.check_element(self.page.dropdown_element_6, 
                                  self.page.element_text_6, 
                                  self.page.expected_text_6)
        assert text


    @allure.title("Проверка 'Я жизу за МКАДом, привезёте?'")
    def test_check_mkad(self):
        text = self.check_element(self.page.dropdown_element_7, 
                                  self.page.element_text_7, 
                                  self.page.expected_text_7)
        assert text


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    
