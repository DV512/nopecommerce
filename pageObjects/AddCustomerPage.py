import time
from selenium.webdriver.support.ui import Select


class AddCustomers:
    #Add Customer Page
    InkCustomers_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    InkCustomers_menuItem_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath="//*[@id='Email']"
    textPassword_xpath="//*[@id='Password']"
    textFirstName_xpath ="//*[@id='FirstName']"
    textLastName_xpath="//*[@id='LastName']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    textDob_xpath="//*[@id='DateOfBirth']"
    txtCompanyName_xpath="//*[@id='Company']"
    txtCustomerRoles_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    listItemAdministrators_xpath="//li[contains(text(),'Administrators']"
    listItemForumModerators_xpath="//li[contains(text(),'Forum Moderators']"
    listItemGuests_xpath="//li[contains(text(),'Guests')]"
    listItemRegistered_xpath="//li[contains(text(),'Registered')]"
    listItemVendors_xpath="//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath="//*[@id='VendorId']"
    AdminComment_xpath="//*[@id='AdminComment']"
    bntSave_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__ (self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.InkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.InkCustomers_menuItem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()

        time.sleep(3)
        if role == 'Registered':
            self.listItem=self.driver.find_element_by_xpath(self.listItemRegistered_xpath)
        elif role=='Administrators':
            self.listItem=self.driver.find_element_by_xpath(self.listItemAdministrators_xpath)
        elif role=='Forum Moderators':
            self.listItem=self.driver.find_element_by_xpath(self.listItemForumModerators_xpath)
        elif role=='Guests':
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listItem=self.driver.find_element_by_xpath(self.listItemGuests_xpath)
        elif role=='Registered':
            self.listItem=self.driver.find_element_by_xpath(self.listItemRegistered_xpath)
        elif role=='Vendors':
            self.listItem=self.driver.find_element_by_xpath(self.listItemVendors_xpath)
        else:
            self.listItem=self.driver.find_element_by_xpath(self.listItemGuests_xpath)
        time.sleep(3)
        #self.driver.click()
        self.driver.execute_script("arguments[0].click();",self.listItem)

    def SetManagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def SetGender(self,gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def SetFirstName(self, fname):
        self.driver.find_element_by_xpath(self.textFirstName_xpath).send_keys(fname)

    def SetLastName(self, lname):
        self.driver.find_element_by_xpath(self.textLastName_xpath).send_keys(lname)

    def SetDod(self, dob):
        self.driver.find_element_by_xpath(self.textDob_xpath).send_keys(dob)

    def SetCompanyName(self,companyName):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(companyName)

    def SetAdminContent(self, Conent):
        self.driver.find_element_by_xpath(self.AdminComment_xpath).send_keys(Conent)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.bntSave_xpath).click()




