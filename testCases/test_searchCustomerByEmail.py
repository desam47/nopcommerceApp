import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddcustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL(self='')
    username = ReadConfig.getUseremail(self='')
    password = ReadConfig.getPassword(self='')
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addNewCustomer(self, setup):
        self.logger.info("********** Search Customer By Email test started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********** Login Successful **********")

        self.addcust = AddcustomerPage(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerManuItem()

        self.logger.info("********** Search Customer By Email **********")

        self.sc = SearchCustomerPage(self.driver)
        self.sc.setEmail("james_pan@nopCommerce.com")
        self.sc.clickOnSearch()
        time.sleep(3)
        email = self.sc.searchCustomerByEmail("james_pan@nopCommerce.com")
        print(email)
        assert True == email
        self.logger.info("********** Search Customer By Email test Completed **********")

        self.driver.close()