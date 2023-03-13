import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):
    """Run below method using two set of test data
    Admin, admin123, C:\Mine\Balaji-Profile_2023.pdf, File type not allowed
    Admin, admin123, C:\Mine\Balaji-Profile_2023.txt, File type not allowed

    Keep the test data in excel
    """

    @pytest.mark.parametrize('username,password,upload_file,expected_error',
                             data_source.test_invalid_profile_upload_data)
    def test_invalid_profile_upload(self,username,password,upload_file,expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(upload_file)
        actual_error = self.driver.find_element(By.XPATH, "//span[contains(normalize-space(),'not allowed')]").text
        assert_that(actual_error).contains(expected_error)

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
        #wait for the textbox contain the attribute value as firstname
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.text_to_be_present_in_element_attribute((By.NAME, "firstName"),"value",firstname))

        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")

        assert_that(expected_profile_header).is_equal_to(actual_profile_header)
        assert_that(expected_firstname).is_equal_to(actual_first_name)