import pytest
import time

from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomers
from Utilities.CustomLogger import LogGen
import string
import random




class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("**** Test_003_AddCustomer ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setPassword(self.password)
        self.lp.setUserName(self.username)
        self.lp.clicklogin()
        self.logger.info("***** Login Sucessful ****")
        self.logger.info("***** Starting Add customer Test ***** ")
        self.addcust = AddCustomers(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("**** Providing customer info ****")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.SetGender("Female")
        self.addcust.SetFirstName("Divya")
        self.addcust.SetLastName("Vijayaraghavan")
        self.addcust.SetDod("05/05/2021")
        self.addcust.SetCompanyName("ABC Company")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.SetManagerOfVendor("Vendor 1")
        self.addcust.SetAdminContent("This is for testing")
        self.addcust.clickOnSave()
        self.logger.info("**** Saving customer info ****")
        self.logger.info("**** Add customer validation started")
        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*** Add customer test passed ****")
        else:
            self.driver.save_screenshot (".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*** Add customer Test Failed")
            assert True == False
            self.driver.close()
            self.logger.info("*** Ending Home Page Title Test ***")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for x in range(size))

