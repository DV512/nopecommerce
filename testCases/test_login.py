import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePagetitle(self, setup):
        self.logger.info("*********  Test_001_Login **************")
        self.logger.info("****************** Verifing home Page title ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************  Home Page title is passed  ****************")

        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePagetitle124.png")
            self.driver.close()
            self.logger.info("*********** Home Page title is failed **************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************  Verifing Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***********  Login Test is Passed ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            self.logger.info("*************** Login test is failed *************")
            assert False



