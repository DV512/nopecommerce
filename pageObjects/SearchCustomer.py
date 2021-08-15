class SearchCustomer:
    #Add customer Page
    txtEmail_id = "SearchEmail"
    txtfirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tableSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def SetEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def SetFirstName(self, fname):
        self.driver.find_element_by_id(self.txtfirstName_id).clear()
        self.driver.find_element_by_id(self.txtfirstName_id).send_keys(fname)

    def SetLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfCols(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def SearchCustomerByEmail(self,email):
        flag=False
        for r in range (1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag


    def SearchCustomerByName(self, name):
        flag=False
        for r in range (1, self.getNoOfRows()+1):
            table=self. driver.find_element_by_xpath(self.table_xpath)
            nameid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if nameid == name:
                flag = True
                break
        return flag


