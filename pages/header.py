from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Header:

    test_url = "https://qa-scooter.praktikum-services.ru/order"
    main_url = "https://qa-scooter.praktikum-services.ru/"

    header_logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    check_text = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
    yandex_logo = (By.XPATH, "//a[@href='//yandex.ru']")


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)


    def check_redirect_to_mainpage(self):
        self.driver.get(self.test_url)
        WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(self.check_text))
        self.driver.find_element(*self.header_logo_scooter).click()
        WebDriverWait(self.driver, 5).until(
                expected_conditions.url_to_be(self.main_url))
        return True


    def check_redirect_to_yandex(self):
        self.driver.get(self.main_url)
        WebDriverWait(self.driver, 5).until(
                expected_conditions.url_to_be(self.main_url))
        self.driver.find_element(*self.yandex_logo).click()
        if len(self.driver.window_handles) == 2:
            return True
        else:
            return False


    def get_url(self):
        self.driver.get(self.main_url)

