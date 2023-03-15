import time

import pytest
from assertpy import assert_that
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()
        self.driver.find_element(By.ID, "email").send_keys("MAULINDESATEST@GMAIL.COM")
        self.driver.find_element(By.ID, "pass").send_keys("Maulin@123")
        self.driver.find_element(By.XPATH,
                                 "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
        actual_text = self.driver.find_element(By.XPATH,
                                               "//div[@class='panel header']//span[@class='logged-in'][normalize-space()='Welcome, maulin101 desai101!']").text
        assert_that("Welcome, maulin101 desai101!").is_equal_to(actual_text)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//span[normalize-space()='Women']")).perform()
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[@id='ui-id-9']")).perform()
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-11']").click()

    @pytest.mark.parametrize("username, password, expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.XPATH,
                                 "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
        actual_error = self.driver.find_element(By.XPATH,
                                                "//div[contains(text(),'Please enter a valid email address')]").text
        assert_that(expected_error).is_equal_to(actual_error)

    @pytest.mark.parametrize("jacket,Size", data_source.test_add_jacket_product_data)
    def test_product(self, jacket, Size):
        self.test_valid_login()
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//span[normalize-space()='Women']")).perform()
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[@id='ui-id-9']")).perform()
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-11']").click()
        j1 = self.driver.find_element(By.XPATH, "//a[@class='product-item-link'][normalize-space()='" + str(
            jacket) + "']").click()
        self.driver.find_element(By.XPATH, "//div[@option-label='" + str(Size) + "']").click()
        self.driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-50']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"))
        )
        self.driver.find_element(By.XPATH, "//span[@class='counter-number']").click()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='top-cart-btn-checkout']"))
        )
        self.driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()

    @pytest.mark.parametrize("firstname, lastname, street, city, State, Zipcode, Phonenumber",
                                 data_source.test_shipping_address_data)
    def test_shipping_Information(self, firstname, lastname, street, city, State, Zipcode, Phonenumber):
        self.test_product(jacket="Juno Jacket",Size="M")
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Shipping Address']"))
        )
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys(firstname)
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//input[@class='input-text'][@name='street[0]']").send_keys(street)
        self.driver.find_element(By.XPATH, "//input[@name='city']").send_keys(city)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='State/Province']/../../div/select").send_keys(
            State)
        self.driver.find_element(By.XPATH, "//input[@name='postcode']").send_keys(Zipcode)
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys(Phonenumber)
        self.driver.find_element(By.XPATH, "//input[@name='ko_unique_1']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Payment Method']"))
        )
