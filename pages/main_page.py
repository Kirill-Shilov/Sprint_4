from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:

    order_button_top = [By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']"]
    order_button_bottom = [By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]"]
    
    url = "https://qa-scooter.praktikum-services.ru/"

    dropdown_element_0 = [By.XPATH, "//div[@id='accordion__heading-0']/parent::div"]
    dropdown_element_1 = [By.XPATH, "//div[@id='accordion__heading-1']/parent::div"]
    dropdown_element_2 = [By.XPATH, "//div[@id='accordion__heading-2']/parent::div"]
    dropdown_element_3 = [By.XPATH, "//div[@id='accordion__heading-3']/parent::div"]
    dropdown_element_4 = [By.XPATH, "//div[@id='accordion__heading-4']/parent::div"]
    dropdown_element_5 = [By.XPATH, "//div[@id='accordion__heading-5']/parent::div"]
    dropdown_element_6 = [By.XPATH, "//div[@id='accordion__heading-6']/parent::div"]
    dropdown_element_7 = [By.XPATH, "//div[@id='accordion__heading-7']/parent::div"]

    element_text_0 = [By.XPATH, "//div[@id='accordion__heading-0']/parent::div/following-sibling::div/p"]
    element_text_1 = [By.XPATH, "//div[@id='accordion__heading-1']/parent::div/following-sibling::div/p"]
    element_text_2 = [By.XPATH, "//div[@id='accordion__heading-2']/parent::div/following-sibling::div/p"]
    element_text_3 = [By.XPATH, "//div[@id='accordion__heading-3']/parent::div/following-sibling::div/p"]
    element_text_4 = [By.XPATH, "//div[@id='accordion__heading-4']/parent::div/following-sibling::div/p"]
    element_text_5 = [By.XPATH, "//div[@id='accordion__heading-5']/parent::div/following-sibling::div/p"]
    element_text_6 = [By.XPATH, "//div[@id='accordion__heading-6']/parent::div/following-sibling::div/p"]
    element_text_7 = [By.XPATH, "//div[@id='accordion__heading-7']/parent::div/following-sibling::div/p"]

    expected_text_0 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    expected_text_1 = "Пока что у нас так: один заказ — один самокат."
    " Если хотите покататься с друзьями, можете просто сделать несколько"
    " заказов — один за другим."
    expected_text_2 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим"
    " самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента,"
    " когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в"
    " 20:30, суточная аренда закончится 9 мая в 20:30."
    expected_text_3 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    expected_text_4 = "Пока что нет! Но если что-то срочное — всегда можно"
    " позвонить в поддержку по красивому номеру 1010."
    expected_text_5 = "Самокат приезжает к вам с полной зарядкой. Этого"
    " хватает на восемь суток — даже если будете кататься без"
    " передышек и во сне. Зарядка не понадобится."
    expected_text_6 = "Да, пока самокат не привезли. Штрафа не будет,"
    " объяснительной записки тоже не попросим. Все же свои."
    expected_text_7 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)


    def check_element(self, element_locator, text_locator, text):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.actions.move_to_element(element).click(element).perform()
        text_element = self.driver.find_element(*text_locator)
        WebDriverWait(self.driver, 3).until(expected_conditions.
            text_to_be_present_in_element(text_locator, text))
        return True


    def get_url(self):
        self.driver.get(self.url)

