import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def setup_teardown():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()
