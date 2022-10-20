from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Header:

    header_logo_scooter = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    test_url = "https://qa-scooter.praktikum-services.ru/order"
    main_url = "https://qa-scooter.praktikum-services.ru/"
    yandex_url = "https://dzen.ru/?yredirect=true"
    check_text = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    yandex_logo = [By.XPATH, "//a[@href='//yandex.ru']"]
    dzen_element = [By.XPATH, "//a[@href='https://ya.ru/?open_keyboard=1']"]


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)


    def check_redirect_to_mainpage(self):
        self.driver.get(self.test_url)
        WebDriverWait(self.driver, 3).until(
                expected_conditions.presence_of_element_located(self.check_text))
        self.driver.find_element(*self.header_logo_scooter).click()
        WebDriverWait(self.driver, 3).until(
                expected_conditions.url_to_be(self.main_url))



    def check_redirect_to_yandex(self):
        try:
            self.driver.get(self.main_url)
            WebDriverWait(self.driver, 2).until(
                    expected_conditions.url_to_be(self.main_url))
            self.driver.implicitly_wait(2)
            self.driver.find_element(*self.yandex_logo).click()
            self.driver.find_element(*self.dzen_element)
        except:
            pass


