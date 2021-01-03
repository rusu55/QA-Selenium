import unittest
import time
from random import randint

from selenium import webdriver
from selenium.webdriver.support.select import Select


class AddEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='../browser_drivers/chromedriver.exe')
        self.driver.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_something(self):
        empId = randint(10000, 99999)
        expected_job_title = 'CEO'
        expected_employment_status = 'Full Time'
        expected_firstName = "Bogdan"
        expected_lastName = "Rusu"
        driver = self.driver

        # Login

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()

        time.sleep(3)
        welcome_text = driver.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_text)

        # Click the Add Button
        driver.find_element_by_id('btnAdd').click()
        time.sleep(2)

        # Enter First and Last Name
        driver.find_element_by_id('firstName').send_keys('Bogdan')
        driver.find_element_by_id('lastName').send_keys('Rusu')

        # Enter and remember ID
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys(empId)

        # Save the Employee
        driver.find_element_by_id('btnSave').click()
        time.sleep(3)

        #Add Job
        driver.find_element_by_link_text("Job").click()
        driver.find_element_by_id("btnSave").click()
        Select(driver.find_element_by_id("job_job_title")).select_by_visible_text(expected_job_title)
        Select(driver.find_element_by_id("job_emp_status")).select_by_visible_text(expected_employment_status)

        driver.find_element_by_id('btnSave').click()
        time.sleep(2)

        # Go to PIM page
        driver.find_element_by_id('menu_pim_viewPimModule').click()

        # Search the Employee
        driver.find_element_by_id('empsearch_id').send_keys(empId)
        driver.find_element_by_id('searchBtn').click()
        time.sleep(2)

        # Expected 1 record back

        self.assertTrue(len(driver.find_elements_by_xpath("//td[3]/a")) == 1)

        # Expected Correct Name and EmpId
        firstName = driver.find_element_by_xpath("//td[3]/a").text
        lastName = driver.find_element_by_xpath("//td[4]/a").text
        job_title = driver.find_element_by_xpath("//td[5]/a").text
        employment_status = driver.find_element_by_xpath("//td[6]/a").text

        self.assertEqual(expected_firstName, firstName)
        self.assertEqual(expected_lastName, lastName)
        self.assertEqual(expected_job_title, job_title)
        self.assertEqual(expected_employment_status, employment_status)


if __name__ == '__main__':
    unittest.main()
