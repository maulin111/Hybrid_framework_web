import pytest
from selenium import webdriver

class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

