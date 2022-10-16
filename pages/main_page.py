class MainPage:

    dropdown_element_0 = [By.XPATH, "//div[@id='accordion__heading-0']"]
    dropdown_element_1 = [By.XPATH, "//div[@id='accordion__heading-1']"]
    dropdown_element_2 = [By.XPATH, "//div[@id='accordion__heading-2']"]
    dropdown_element_3 = [By.XPATH, "//div[@id='accordion__heading-3']"]
    dropdown_element_4 = [By.XPATH, "//div[@id='accordion__heading-4']"]
    dropdown_element_5 = [By.XPATH, "//div[@id='accordion__heading-5']"]
    dropdown_element_6 = [By.XPATH, "//div[@id='accordion__heading-6']"]
    dropdown_element_7 = [By.XPATH, "//div[@id='accordion__heading-7']"]

    element_text_0 = [By.XPATH, "//div[@id='accordion__heading-0']/parent::div/following-sibling::div/p"]
    element_text_1 = [By.XPATH, "//div[@id='accordion__heading-1']/parent::div/following-sibling::div/p"]
    element_text_2 = [By.XPATH, "//div[@id='accordion__heading-2']/parent::div/following-sibling::div/p"]
    element_text_3 = [By.XPATH, "//div[@id='accordion__heading-3']/parent::div/following-sibling::div/p"]
    element_text_4 = [By.XPATH, "//div[@id='accordion__heading-4']/parent::div/following-sibling::div/p"]
    element_text_5 = [By.XPATH, "//div[@id='accordion__heading-5']/parent::div/following-sibling::div/p"]
    element_text_6 = [By.XPATH, "//div[@id='accordion__heading-6']/parent::div/following-sibling::div/p"]
    element_text_7 = [By.XPATH, "//div[@id='accordion__heading-7']/parent::div/following-sibling::div/p"]


    def __init__(self, driver):
        self.driver = driver


    def click_dropdown_element(element):
        self.driver.find_element(*element).click()


    def get_element_text(element_text):
        return self.driver.find_element(*element_text).text

