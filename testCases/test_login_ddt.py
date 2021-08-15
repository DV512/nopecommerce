import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import XLUtils
import time

class Test_001_DDTLogin:

    baseURL = ReadConfig.getApplicationURL()
    path = "/Users/jeevasubbiah/PycharmProjects/nopecommerce/TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************  Test_0022_DDT_Login **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("The number of Rows in Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            print("username:", self.user)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            print("password:", self.password)
            self.exp_result = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(2)
            print("waiting for 5 sec")

            self.act_title = self.driver.title
            self.exp_title = "Dashboard / nopCommerce administration"
            lst_status = []

            if self.exp_title == self.act_title:
                print("the title matches",self.driver.title)
                print(self.exp_result)
                if self.exp_result == "Pass":
                    print("inside loop 1")
                    time.sleep(2)
                    self.lp.clicklogout(self)
                    #self.driver.find_element_by_link_text("Logout").click()
                    self.logger.info("********** Passed ******")
                    lst_status.append("Pass")
                elif self.exp_result == "Fail":
                    self.logger.info("******** Fail **********")
                    lst_status.append("Fail")
            elif self.act_title != self.exp_title:
                if self.exp_result == "Pass":
                    self.logger.info("******* Fail ********")
                    lst_status.append("Fail")
                elif self.exp_result == "Fail":
                    self.logger.info ("***** passed *********")
                    lst_status.append("Pass")







