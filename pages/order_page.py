import allure
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random
from faker import Faker


class OrderPage:

    url = "https://qa-scooter.praktikum-services.ru/order"
    start_url = "https://qa-scooter.praktikum-services.ru"
    #first page
    cookie_button = [By.XPATH, "//button[@class='App_CookieButton__3cvqF']"]
    name_field = [By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder = '* Имя']"]
    surename_field = [By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder = '* Фамилия']"]
    address_field = [By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder = '* Адрес: куда привезти заказ']"]
    station_field = [By.XPATH, "//input[@class = 'select-search__input' and @placeholder = '* Станция метро']"]
    firs_station_choise = [By.XPATH, "(//button[@class='Order_SelectOption__82bhS select-search__option'])[1]"]
    second_station_choise = [By.XPATH, "(//button[@class='Order_SelectOption__82bhS select-search__option'])[5]"]
    phone_field = [By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder = '* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Далее']"]
    #second page
    header = [By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Про аренду']"]
    time_delivery_field = [By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder='* Когда привезти самокат']"]
    time_rent_field = [By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"]
    time_rent_select_1 = [By.XPATH, "//div[@class='Dropdown-menu']//div[1]"]
    time_rent_select_2 = [By.XPATH, "//div[@class='Dropdown-menu']//div[2]"]
    color_checkbox_1 = [By.XPATH, "//div[contains(@class, 'Order_Checkboxes__3lWSI')]/label[1]"]
    color_checkbox_2 = [By.XPATH, "//div[contains(@class, 'Order_Checkboxes__3lWSI')]/label[2]"]
    comment = [By.XPATH, "//div[@class='Input_InputContainer__3NykH']/input[contains(@class, 'Input_Input__1iN_Z') and @placeholder='Комментарий для курьера']"]
    order_button = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']"]
    #third page
    want_to_order = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]
    yes_i_want = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(@class, 'Button_Button__ra12g') and text()='Да']"]
    #final page
    success = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and contains(text(), 'Заказ оформлен')]"]

    #data
    street_address_1 = "наб. Медицинская, д. 19 к. 2"
    street_address_2 = "пер. Лесный, д. 314 к. 6"
    comment_text_1 = "Какой-то комметарий 1"
    comment_text_2 = "Какой-то комметарий 2"

    fake = Faker(['ru_RU'])


    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)


    def wait_presence(self, element):
        WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(element))


    def wait_visibility(self, element):
        WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(element))


    @allure.step('Генерация номера телефона')
    def phone(self):
        return '+7' + str(random.randint(0000000000, 10000000000))


    @allure.step('Закрытие всплывающего окна с сообщением о куках')
    def close_cookie_popup(self):
        try:
            self.driver.find_element(*self.cookie_button).click()
        except:
            pass

    
    @allure.step('Нажатие на верхнюю кнопку "Заказать"')
    def use_top_order_button(self):
        self.driver.find_element(*MainPage.order_button_top).click()


    @allure.step('Нажатие на нижнюю кнопку "Заказать"')
    def use_bottom_order_button(self):
        self.driver.find_element(*MainPage.order_button_bottom).click()


    @allure.step('Заполнени полей первой страницы заказа')
    def fill_fields_1(self, station, street_address):
        d = self.driver
        a = self.action
        d.find_element(*self.name_field).send_keys(self.fake.first_name())
        d.find_element(*self.surename_field).send_keys(self.fake.last_name())
        d.find_element(*self.address_field).send_keys(street_address)
        dropdown = d.find_element(*self.station_field)
        a.move_to_element(dropdown).click().perform()
        element = d.find_element(*station)
        a.move_to_element(element).click().perform()
        d.find_element(*self.phone_field).send_keys(self.phone())


    @allure.step('Нажатие кнопки "Заказать" на первой странице заказа')
    def place_order_1(self):
        element = self.driver.find_element(*self.next_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.action.move_to_element(element).click().perform()
        self.wait_presence(self.header)


    @allure.step('Заполнени полей второй страницы заказа')
    def fill_fields_2(self, time_rent_select, comment_text, color):
        d = self.driver
        a = self.action
        d.find_element(*self.time_delivery_field).send_keys(
                str(self.fake.date_this_month(False, True)))
        d.find_element(*self.time_delivery_field).send_keys(Keys.ENTER)
        self.wait_presence(self.time_rent_field)
        dropdown = d.find_element(*self.time_rent_field)
        a.move_to_element(dropdown).click().perform()
        self.wait_presence(self.time_rent_select_1)
        select = d.find_element(*time_rent_select)
        a.move_to_element(select).click().perform()
        color_checkbox = d.find_element(*color)
        self.wait_presence(color)
        a.move_to_element(color_checkbox).click().perform()
        d.find_element(*self.comment).send_keys(comment_text)


    @allure.step('Нажатие кнопки "Заказать" на второй странице заказа')
    def place_order_2(self):
        self.driver.find_element(*self.order_button).click()


    @allure.step('Подтверждение заказа')
    def make_order(self):
        d = self.driver
        self.wait_visibility(self.want_to_order)
        d.find_element(*self.yes_i_want).click()


    @allure.step('Ожидание сообщения об успешном создании заказа')
    def wait_for_success(self):
        self.wait_visibility(self.success)

        
    @allure.step('Переход на главную страницу сайта')
    def get_url(self):
        self.driver.get(self.start_url)

