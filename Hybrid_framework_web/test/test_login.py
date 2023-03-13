import time

import pytest
from assertpy import assert_that
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()
        self.driver.find_element(By.ID, "email").send_keys("maulindesa@gmail.com")
        self.driver.find_element(By.ID, "pass").send_keys("maulin@123")
        self.driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@class='panel header']//span[@class='logged-in'][normalize-space()='Welcome, maulin desai!']").text
        assert_that("Welcome, maulin desai!").is_equal_to(actual_text)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//span[normalize-space()='Women']")).perform()
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[@id='ui-id-9']")).perform()
        self.driver.find_element(By.XPATH,"//a[@id='ui-id-11']").click()
    @pytest.mark.parametrize("jacket,Size", data_source.test_add_jacket_product_data)
    def test_product(self, jacket, Size):
            self.test_valid_login()
            j1 = self.driver.find_element(By.XPATH, "//a[@class='product-item-link'][normalize-space()='" + str(jacket) + "']").click()
            self.driver.find_element(By.XPATH,"//div[@option-label='" + str(Size) + "']").click()
            time.sleep(5)
