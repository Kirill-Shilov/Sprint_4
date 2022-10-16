#import sys
#sys.path.append("..")
from ..pages.main_page import MainPage

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


a = MainPage()


class TestDropdownList:
    driver = None

    @classmethod
    def setup_class(cls):
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        cls.driver = driver

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    

