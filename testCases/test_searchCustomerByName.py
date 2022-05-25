import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddcustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL(self='')
    username = ReadConfig.getUseremail(self='')
    password = ReadConfig.getPassword(self='')
    logger = LogGen.loggen()

    def test_addNewCustomer(self, setup):
        self.logger.info("********** Search Customer By Name test started **********")
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

        self.logger.info("********** Search Customer By Name **********")

        self.sc = SearchCustomerPage(self.driver)
        self.sc.setFirstname("Arthur")
        self.sc.setLastname("Holmes")
        self.sc.clickOnSearch()
        time.sleep(3)
        name = self.sc.searchCustomerByName("Arthur Holmes")
        print(name)
        assert True == name
        self.logger.info("********** Search Customer By Name test Completed **********")

        self.driver.close()