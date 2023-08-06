from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.common.exceptions import TimeoutException

# my_leave_link = (By.LINK_TEXT,"My Leave")
entitlements_link = (By.XPATH,"//span[contains(text(),'Entitlements ')]")
configure_link = (By.XPATH,"//span[contains(text(),'Configure ')]")

class My_Leave(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.my_leave_link = (By.LINK_TEXT, "My Leave")
        self.expand_search = (By.XPATH, "//i[@class='oxd-icon bi-caret-up-fill']")
        self.search_from_date_txt = (By.XPATH, "//label[contains(text(),'From Date')]/../..//input")
        self.search_to_date_txt = (By.XPATH, "//label[contains(text(),'To Date')]/../..//input")
        self.search_btn = (By.XPATH, "//button[@type='submit']")
        self.username_in_table = (By.XPATH, "//table[@id='resultTable']//a[contains(@href, 'saveSystemUser')]")

    def go_to_my_leave_page(self):
        self.navigate_to_tab(self.leave_tab)
        self.EF.find_element(self.my_leave_link).click()


    # def enter_from_date(self,search_from_date ):
    #     self.EF.find_element(self.search_from_date_txt).clear()
    #     self.EF.find_element(self.search_from_date_txt).send_keys(search_from_date)
    #
    # def enter_to_date(self, search_to_date):
    #     self.EF.find_element(self.search_to_date_txt).clear()
    #     self.EF.find_element(self.search_to_date_txt).send_keys(search_to_date)

    def enter_from_date(self, search_from_date):
        self.EF.find_element(self.search_from_date_txt).clear()
        self.EF.find_element(self.search_from_date_txt).send_keys(search_from_date)

    def enter_to_date(self, search_to_date):
        self.EF.find_element(self.search_to_date_txt).clear()
        self.EF.find_element(self.search_to_date_txt).send_keys(search_to_date)


    def click_search_btn(self):
        self.EF.find_element(self.search_btn).click()


    def search_my_leave(self, search_dict: dict):
        # self.enter_from_date(search_dict.get('search_from_date', ""))
        # self.enter_to_date(search_dict.get('search_to_date', ""))
        self.enter_from_date(search_dict['search_from_date'])
        self.enter_to_date(search_dict['search_to_date'])

        self.click_search_btn()
        try:
            self.EF.find_element((By.XPATH, "//div[@class='oxd-toast oxd-toast--info oxd-toast-container--toast']"))
            return True
        except TimeoutException:
            return False


class Add_Entitlements(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.add_entitlements_link = (By.LINK_TEXT, "Add Entitlements")
        self.individual_employee_btn = (By.XPATH, "//label[contains(normalize-space(),'Individual Employee')]")
        self.employee_name_txt = (By.XPATH, "//label[contains(text(),'Employee Name')]/../..//input")
        self.entitlement_txt = (By.XPATH, "//label[contains(text(),'Entitlement')]/../..//input")
        self.save_btn = (By.XPATH, "//button[@type='submit']")

    def go_to_add_entitlements_page(self):
        self.navigate_to_tab(self.leave_tab)
        self.EF.find_element(entitlements_link).click()
        self.EF.find_element(self.add_entitlements_link).click()



    def click_endiuidual_employee(self):
        self.EF.find_element(self.individual_employee_btn).click()


    def enter_employee_name(self, employee_name):
        self.EF.find_element(self.employee_name_txt).clear()
        self.EF.find_element(self.employee_name_txt).send_keys(employee_name)


    def enter_entitlement(self,entitlement):
        self.EF.find_element(self.entitlement_txt).clear()
        self.EF.find_element(self.entitlement_txt).send_keys(entitlement)

    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()


    def save_add_entitlements(self, save_dict: dict):
        self.enter_employee_name(save_dict.get('employee_name', ""))
        self.enter_entitlement(save_dict.get('entitlement', ""))

        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH, "//div[@class='oxd-toast oxd-toast--info oxd-toast-container--toast']"))
            return True
        except TimeoutException:
            return False


class Holidays(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        self.holidays_link = (By.XPATH,"//a[contains(text(),'Holidays')]")
        self.add_btn = (By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']")
        self.name_txt = (By.XPATH,"//label[contains(text(),'Name')]/../..//input")
        self.date_txt = (By.XPATH,"//label[contains(text(),'Date')]/../..//input")
        self.repeats_annually_btn = (By.XPATH,"//input[@value='false']")
        self.save_btn = (By.XPATH,"//button[@type='submit']")
    def go_to_holidays_page(self):
        self.navigate_to_tab(self.leave_tab)
        self.EF.find_element(configure_link).click()
        self.EF.find_element(self.holidays_link).click()


    def click_add_btn(self):
        self.EF.find_element(self.add_btn).click()

    def enter_name_txt(self, name):
        self.EF.find_element(self.name_txt).clear()
        self.EF.find_element(self.name_txt).send_keys(name)

    def enter_date_txt(self, date):
        self.EF.find_element(self.date_txt).clear()
        self.EF.find_element(self.date_txt).send_keys(date)

    def click_repeats_annually_btn(self):
        self.EF.find_element(self.repeats_annually_btn).click()

    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

    def save_holidays(self, save_dict: dict):
        self.enter_name_txt(save_dict.get('name', ""))
        self.enter_date_txt(save_dict.get('date', ""))
        # // div[ @ id = 'oxd-toaster_1']

        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH, "//p[contains(normalize-space(),'Successfully Saved')]"))
            return True
        except TimeoutException:
            return False


