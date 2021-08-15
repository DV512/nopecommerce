import pytest
import time
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomers
from pageObjects.SearchCustomer import SearchCustomer

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.logger.info("*** Search customer by Name ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*** Login successful ***")

        self.logger.info("*** Navigating to customer menu item page ***")
        self.addcust = AddCustomers(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("*** Sucessfully navigated to customer menu item page ***")

        time.sleep(3)
        self.logger.info("*** Starting to search customer by name ***")
        self.searchcust = SearchCustomer(self.driver)
        self.logger.info("*** Entering the name ***")
        self.searchcust.SetFirstName("Victoria")
        self.searchcust.SetLastName("Terces")
        self.logger.info("*** clicking on search ***")
        self.searchcust.clickSearch()
        time.sleep(5)
        status= self.searchcust.SearchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("*** TC_Search Customer by name_005 Finished  ***")
        self.driver.close()


