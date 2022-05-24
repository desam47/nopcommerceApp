import random
import string

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddcustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL(self='')
    username = ReadConfig.getUseremail(self='')
    password = ReadConfig.getPassword(self='')
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Add Customer Test **********")

        self.addcust = AddcustomerPage(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerManuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("********** Providing Customer info **********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("Test123")
        self.addcust.setFirstName("TestFirstName")
        self.addcust.setLastName("TestLastName")
        self.addcust.selectGender("Male")
        self.addcust.setDOB("01/11/1991")
        self.addcust.setComapnyName("TestCompanyName")
        self.addcust.clickOnTaxExtempt()
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManageVendor("Vendor 2")
        self.addcust.setComment("This is test....")
        self.addcust.clickOnSave()

        self.logger.info("********** Saving Customer info **********")

        self.logger.info("********** Add Customer Validation Started **********")

        self.msg = self.driver.find_element_by_tag_name("body").text

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add Customer test Passed **********")
        else:
            self.driver.save_screenshot("Screenshots/test_addCustomer.png")
            self.logger.info("**********  Add Customer test is Failed ********** ")
            assert True == False

        self.driver.close()
        self.logger.info("**********  Ending Test_003 Add Customer Test ********** ")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
