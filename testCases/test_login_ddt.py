import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL(self='')
    path="TestData/LoginData.xlsx"
    logger=LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("****************Test_002_DDT_Login*********************")
        self.logger.info("*********************** Verifying Login DDT test *******************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows=ExcelUtils.getRowCount(self.path,"Sheet1")
        print("Number of Rows in a Excel:",self.rows)
        lst_status=[]   # Empty list variable

        for r in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("*********************** Passed *******************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp=="Fail":
                    self.logger.info("*********************** Failed *******************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("*********************** Failed *******************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

                elif self.exp=="Fail":
                    self.logger.info("*********************** Passed *******************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*******Login DDT test passed******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*******Login DDT test Failed******")
            self.driver.close()
            assert False

        self.logger.info("***********End of Login DDT Test*************")
        self.logger.info("***********Completed TC_LoginDDT_002*************")



