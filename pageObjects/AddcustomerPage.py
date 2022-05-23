import time
from selenium.webdriver.support.ui import Select

class AddCustomer():
    # Add Customer Page

    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//span[@class='nav-item'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender = "Gender_Male"
    rdFemaleGender = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompName_xpath = "//input[@id='Company']"
    ckboxTaxExp_xpath = "//input[@id='IsTaxExempt']"

    txtNewsletter_xpath = "//div[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    lstitemYour_store_name = "//li[contains(text(),'Your store name')]"
    lstitemTest_store_2 = "//li[contains(text(),'Test store 2')]"

    txtCustomerRole_xpath = "//div[@id='SelectedCustomerRoleIds_taglist']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForum_Moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpMgrofVendor_xpath = "//*[@id='VendorId']"

    ckboxActive_xpath = "//input[@id='Active']"

    txtAdminComment_xpath = "//textarea[@id='AdminComment']"

    btnSave_xpath = "//button[@name='save']"












