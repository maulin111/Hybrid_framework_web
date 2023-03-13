import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize(
        "username, password, firstname, middlename, lastname, expected_profile_header,expected_firstname",
        data_source.test_add_valid_employee_data
    )
    def test_add_valid_employee(self, username, password, firstname, middlename, lastname, expected_profile_header,
                                expected_firstname):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        actual_profile_header = self.driver.find_element(By.XPATH,
                                                         f"//h6[contains(normalize-space(),'{firstname}')]").text
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            expected_conditions.text_to_be_present_in_element_attribute((By.NAME, "firstName"), "value", firstname))

        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")

        assert_that(expected_profile_header).is_equal_to(actual_profile_header)
        assert_that(expected_firstname).is_equal_to(actual_first_name)

from utilities import data_source


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)

    @pytest.mark.parametrize("username, password, expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that(expected_error).is_equal_to(actual_error)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5").text
        assert_that("Login").is_equal_to(actual_header)

    def test_login_placeholders(self):
        actual_username_placeholder = self.driver.find_element(By.NAME, "username").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.NAME, "password").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)