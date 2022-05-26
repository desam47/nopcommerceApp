import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddcustomerPage:
    # Add Customer Page

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompName_xpath = "//input[@id='Company']"
    ckboxTaxExp_xpath = "//input[@id='IsTaxExempt']"

    txtNewsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    lstitemYour_store_name = "//li[contains(text(),'Your store name')]"
    lstitemTest_store_2 = "//li[contains(text(),'Test store 2')]"

    txtCustomerRole_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//span[normalize-space()='Administrators']"
    lstitemForum_Moderators_xpath = "//span[normalize-space()='Forum Moderators']"
    lstitemGuests_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitemRegistered_xpath = "//span[normalize-space()='Registered']"
    lstitemVendors_xpath = "//span[normalize-space()='Vendors']"

    drpMgrofVendor_xpath = "//select[@id='VendorId']"

    ckboxActive_xpath = "//input[@id='Active']"

    txtAdminComment_xpath = "//textarea[@id='AdminComment']"

    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def selectGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath)
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath)
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath)

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setComapnyName(self, cname):
        self.driver.find_element(By.XPATH, self.txtCompName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCompName_xpath).send_keys(cname)

    def clickOnTaxExtempt(self):
        self.driver.find_element(By.XPATH, self.ckboxTaxExp_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRole_xpath).click()
        time.sleep(3)
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemForum_Moderators_xpath)
        elif role == "Guests":
            self.driver.find_element(By.XPATH, "//ul[ @ id = 'SelectedCustomerRoleIds_taglist']//span[@title = 'delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == "Vendor":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        #time.sleep(3)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManageVendor(self, value):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpMgrofVendor_xpath))
        drpdown.select_by_visible_text(value)

    def setComment(self, comment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()