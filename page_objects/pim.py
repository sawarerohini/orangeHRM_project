from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select



configuration_link = (By.XPATH,"//span[contains(text(), 'Configuration ')]")
employee_list_link = (By.LINK_TEXT,"Employee List")

#PIM
#Configaration


class Optional_Fields(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.optional_fields_link = (By.LINK_TEXT, "Optional Fields")
        self.Show_Nick_Name_Smoker_and_Military_Service_in_Personal_Details = (By.XPATH, "//p[contains(normalize-space(),'Show Nick Name')]/../..//input")
        self.Show_SSN_field_in_Personal_Detail = (By.XPATH, "//p[contains(normalize-space(),'Show SSN field')]/..//div")
        self.Show_SIN_field_in_Personal_Details = (By.XPATH, "//p[contains(normalize-space(),'Show SIN field ')]/..//div")
        self.Show_US_Tax_Exemptions_menu = (By.XPATH, "//p[contains(normalize-space(),'Show US ')]/..//div")
        self.save_btn = (By.XPATH, "//button[@type='submit']")

    def go_to_optional_fields_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(configuration_link).click()
        self.EF.find_element(self.optional_fields_link).click()

    def click_Show_Nick_Name_Smoker_and_Military_Service_in_Personal_Details(self):
        self.EF.find_element(self.Show_Nick_Name_Smoker_and_Military_Service_in_Personal_Details).click()

    def click_Show_SSN_field_in_Personal_Detail(self):
        self.EF.find_element(self.Show_SSN_field_in_Personal_Detail).click()


    def click_Show_SIN_field_in_Personal_Details(self):
        self.EF.find_element(self.Show_SSN_field_in_Personal_Detail).click()


    def click_Show_US_Tax_Exemptions_menu(self):
        self.EF.find_element(self.Show_US_Tax_Exemptions_menu).click()

    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

        try:
            self.EF.find_element((By.XPATH, "//div[@id='oxd-toaster_1']"))
            return True
        except TimeoutException:
            return False


# custom fields

class Custom_Fields(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.custom_fields_link = (By.LINK_TEXT, "Custom Fields")
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.add_field_name_txt = (By.XPATH, "//label[contains(text(),'Field Name')]/../..//input")
        self.screen_select_btn= (By.XPATH, "//label[contains(text(),'Screen')]/../..//i")
        self.type_select_btn= (By.XPATH,"//label[contains(text(),'Type')]/../..//i")
        self.save_btn = (By.XPATH, "//button[@type='submit']")
        self.save_successfully = (By.XPATH, "//div[@id='oxd-toaster_1']")

    def go_to_custom_fields_page(self):
        self.navigate_to_tab(self.pim_tab)
        self.EF.find_element(configuration_link).click()
        self.EF.find_element(self.custom_fields_link).click()

    def click_add_btn(self):
        self.EF.find_element(self.add_btn).click()


    def enter_fields_name(self, add_field_name_txt):
        self.EF.find_element(self.add_field_name_txt).clear()
        self.EF.find_element(self.add_field_name_txt).send_keys(add_field_name_txt)




    def screen_select(self):
        dropdown = Select(self.driver.find_element (By.XPATH, "//label[contains(text(),'Screen')]/../..//i"))
        dropdown.select_by_visible_text("CUSTOMFIELDS").click()

    def type_select(self):
        dropdown = Select(self.driver.find_element (By.XPATH, "//label[contains(text(),'Type')]/../..//i "))
        dropdown.select_by_index(1).click()

    def save_successfully (self,save_successfully ):
        pass


    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

    def save_custom_fields(self, save_dict: dict):
        self.enter_fields_name(save_dict.get('fields_name', ""))
        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH, "//div[@id='oxd-toaster_1']"))
            return True
        except TimeoutException:
            return False


# class Employee_List(Base):
#     def __init__(self,driver):
#         super().__init__(self)
#         self.driver=driver
#         self.employee_list_link = (By.LINK_TEXT,"Employee List")
#         self.expand_link = (By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill']")
#         self.
#










