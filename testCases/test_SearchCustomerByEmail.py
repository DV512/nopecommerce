import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomers
from pageObjects.SearchCustomer import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("*** Search Customer by email ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*** Login successful ***")

        self.logger.info("*** Starting Search Customer by email ***")
        self.addcust = AddCustomers(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("*** Searching Customers by email ***")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.SetEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.SearchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*** TC_Search Customer by email_004 Finished ***")
        self.driver.close()



