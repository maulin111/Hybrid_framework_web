import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()
        self.driver.find_element(By.ID, "email").send_keys("maulindesa@gmail.com")
        self.driver.find_element(By.ID, "pass").send_keys("maulin@123")
        self.driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@class='panel header']//span[@class='logged-in'][normalize-space()='Welcome, maulin desai!']").text
        assert_that("Welcome, maulin desai!").is_equal_to(actual_text)