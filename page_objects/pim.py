from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





configuration_link = (By.XPATH,"//span[contains(text(), 'Configuration ')]")
employee_list_link = (By.LINK_TEXT,"Employee List")
add_employee_link  = (By.XPATH,'//a[contains(text(),"Add Employee")]')

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
        self.navigate_to_tab(self.pim_tab)
        self.EF.find_element(configuration_link).click()
        self.EF.find_element(self.optional_fields_link).click()

    def click_Show_Nick_Name_Smoker_and_Mili0tary_Service_in_Personal_Details(self):
        self.EF.find_element(self.Show_Nick_Name_Smoker_and_Military_Service_in_Personal_Details).click()

    def click_Show_SSN_field_in_Personal_Detail(self):
        self.EF.find_element(self.Show_SSN_field_in_Personal_Detail).click()


    def click_Show_SIN_field_in_Personal_Details(self):
        pass

    def click_Show_US_Tax_Exemptions_menu(self):
        pass

    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

    def save_optional_fields(self,save):
        self.click_save_btn()
        try:
            WebDriverWait(self.EF, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='oxd-toaster_1']")))
            return save
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
        pass
        # dropdown = Select(self.driver.find_element (By.XPATH, "//label[contains(text(),'Screen')]/../..//i"))
        # dropdown.select_by_visible_text("CUSTOMFIELDS").click()

    def type_select(self):
        # dropdown = Select(self.driver.find_element (By.XPATH, "//label[contains(text(),'Type')]/../..//i "))
        # dropdown.select_by_index(1).click()
        self.EF.find_element(self.type_select_btn).click()
        self.EF.find_element(self.select_by_index(1)).click()

    def save_successfully (self,save_successfully ):
        pass


    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

    def save_custom_fields(self, save_dict: dict):
        self.enter_fields_name(save_dict.get("fields_name",""))
        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH, "//div[@id='oxd-toaster_1']"))
            return True
        except TimeoutException:
            return False


class Employee_List(Base):
    def __init__(self,driver):
        super().__init__(self)
        self.driver = driver
        self.employee_list_link = (By.LINK_TEXT,"Employee List")
        # self.expand_link = (By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill']")
        self.employee_name_txt = (By.XPATH,"//label[contains(text(),'Employee Name')]/../..//input")
        self.employee_id_txt = (By.XPATH,"//label[contains(text(),'Employee Id')]/../..//input")
        self.supervisor_name_txt = (By.XPATH,"//label[contains(text(),'Supervisor Name')]/../..//input")
        self.search_btn = (By.XPATH,"//button[@type='submit']")

    def go_to_employee_list_page(self):
        self.navigate_to_tab(self.pim_tab)
        self.EF.find_element(employee_list_link).click()

    def enter_employee_name(self,employee_name_txt):
        self.EF.find_element(self.employee_name_txt).clear()
        self.EF.find_element(self.employee_name_txt).send_keys(employee_name_txt)

    def enter_employee_id(self,employee_id_txt):
        self.EF.find_element(self.employee_id_txt).clear()
        self.EF.find_element(self.employee_id_txt).send_keys(employee_id_txt)

    def enter_supervisor_name(self,supervisor_name_txt):
        self.EF.find_element(self.supervisor_name_txt).clear()
        self.EF.find_element(self.supervisor_name_txt).send_keys(supervisor_name_txt)


    def click_search_btn(self):
        self.EF.find_element(self.search_btn).click()

    def search_employee_list(self,search_dict:dict):
        self.enter_employee_name(search_dict.get("employee_name",""))
        self.enter_employee_id(search_dict.get("employee_id",""))
        self.click_search_btn()
        try:
            self.EF.find_element(By.XPATH,f"//div[contains(text()='{search_dict.get('Anthony ')}')]")
            return True
        except TimeoutException:
            return False

class Add_Employee(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.add_employee_link = (By.XPATH, "//a[contains(text(),'Add Employee')]")
        self.first_name_txt = (By.XPATH, "//input[@name='firstName']")
        self.middle_name_txt = (By.XPATH, "//input[@name='middleName']")
        self.last_name_txt= (By.XPATH, '//input[@name="lastName"]')
        self.employee_id_txt= (By.XPATH,"//label[contains(text(),'Employee Id')]/../..//input")
        self.profile_image = (By.XPATH, "//div[@class='employee-image-wrapper']")
        self.save_btn = (By.XPATH, "//button[@type='submit']")

    def go_to_add_employee_page(self):
        self.navigate_to_tab(self.pim_tab)
        self.EF.find_element(add_employee_link).click()
        self.EF.find_element(self.add_employee_link).click()

    def enter_first_name(self,first_name_txt):
        self.EF.find_element(self.first_name_txt).clear()
        self.EF.find_element(self.first_name_txt).send_keys(first_name_txt)


    def enter_middle_name(self, middle_name_txt):
        self.EF.find_element(self.middle_name_txt).clear()
        self.EF.find_element(self.middle_name_txt).send_keys(middle_name_txt)

    def enter_last_name(self,last_name_txt):
        self.EF.find_element(self.last_name_txt).clear()
        self.EF.find_element(self.last_name_txt).send_keys(last_name_txt)


    def enter_employee_id(self,employee_id_txt):
        self.EF.find_element(self.employee_id_txt).clear()
        self.EF.find_element(self.employee_id_txt).send_keys(employee_id_txt)


    def add_profile_image(self,location):
        self.EF.find_element(self.profile_image).click()
        self.EF.find_element(self.profile_image).send_keys(location)

    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()


    def save_add_employee(self, save_dict: dict):
        self.enter_first_name(save_dict.get("first_name",""))
        self.enter_middle_name(save_dict.get("middle_name",""))
        self.enter_last_name(save_dict.get("middle_name",""))
        self.enter_employee_id(save_dict.get("employee_id",""))
        self.add_profile_image(save_dict.get("location",""))
        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH, "//div[@id='oxd-toaster_1']"))
            return True
        except TimeoutException:
            return False














