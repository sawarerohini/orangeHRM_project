from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.common.exceptions import TimeoutException

user_management_link = (By.XPATH, "//span[contains(text(), 'User Management')]")
job_link = (By.XPATH, "//span[contains(text(), 'Job ')]")
organization_link = (By.XPATH, "//span[contains(text(),'Organization ')]")
Qualifications_link = (By.XPATH,"//span[contains(text(), 'Qualifications ')]")

class Users(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.user_link = (By.LINK_TEXT, "Users")
        self.expand_search = (By.XPATH, "//button//i[contains(@class, 'caret-down-fill')]")
        self.search_username_txt = (By.XPATH, "//label[text()='Username']/../..//input")
        self.user_roll_ddl = (By.XPATH, "//label[text()='User Role']/../..//div[contains(@class,'select-wrapper')]")
        self.search_btn = (By.XPATH, "//button[@type='submit']")
        self.username_in_table = (By.XPATH, "//table[@id='resultTable']//a[contains(@href, 'saveSystemUser')]")

    def go_to_users_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(user_management_link).click()
        self.EF.find_element(self.user_link).click()

    def enter_username(self, username):
        self.EF.find_element(self.search_username_txt).clear()
        self.EF.find_element(self.search_username_txt).send_keys(username)

    def select_user_role(self, user_role):
        pass



    def enter_employee_name(self, employee_name):
        pass

    def select_status(self, status):
        pass

    def click_search_btn(self):
        self.EF.find_element(self.search_btn).click()

    def search_user(self, search_dict: dict):
        self.enter_username(search_dict.get('username', ""))
        self.select_user_role(search_dict.get('role', ""))
        self.enter_employee_name(search_dict.get('name', ""))
        self.select_status(search_dict.get('status', ""))
        self.click_search_btn()
        try:
            self.EF.find_element((By.XPATH, f"//div[text()='{search_dict.get('username')}']"))
            return True
        except TimeoutException:
            return False




#Job

class Job_Titles(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.job_title_link = (By.LINK_TEXT, "Job Titles")
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.add_job_title_txt = (By.XPATH, "//div[@class='oxd-form-row']/../..//input")
        self.add_description_txt = (By.XPATH, "//label[contains(text(),'Job Description')]/../..//textarea")
        self.add_note = (By.XPATH, "//label[placeholder='Add note']/../..//textarea")
        self.save_btn = (By.XPATH, "//button[@type='submit' ]")
        self.save_successfully = (By.XPATH, "//div[contains(@class, 'oxd-toast--success')]")
        # self.username_in_table = (By.XPATH, "//table[@id='resultTable']//a[contains(@href, 'saveSystemUser')]")

    def go_to_job_titles_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(job_link).click()
        self.EF.find_element(self.job_title_link).click()

    def click_add_btn(self):
        self.EF.find_element(self.add_btn).click()


    def enter_job_title(self, add_job_title_txt):
        self.EF.find_element(self.add_job_title_txt).clear()
        self.EF.find_element(self.add_job_title_txt).send_keys(add_job_title_txt)

    def enter_job_description(self, add_description_txt):
        self.EF.find_element(self.add_description_txt).clear()
        self.EF.find_element(self.add_description_txt).send_keys(add_description_txt)

    def enter_add_note(self, add_note):
        pass

    def save_successfully (self,save_successfully ):
        pass

    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

    def save_job_title(self, save_dict: dict):
        self.enter_job_title(save_dict.get('job_title', ""))
        self.enter_job_description(save_dict.get('description', ""))
        self.enter_add_note(save_dict.get('note', ""))
        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH, "//div[contains(@class, 'oxd-toast--success')]"))
            return True
        except TimeoutException:
            return False






class PayGrades(Base):
    def __init__(self, driver):
        self.driver = driver

class Employmentstatus(Base):
    def __init__(self, driver):
        self.driver = driver

class JobCategories(Base):
    def __init__(self, driver):
        self.driver = driver

class WorkShifts(Base):
    def __init__(self, driver):
        self.driver = driver

#Organization

class GeneralInformation(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.general_information_link = (By.XPATH, "//li//a[contains(text(),'General Information')]")
        self.edit_scroll = (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-left']")
        self.organization_name_txt = (By.XPATH, "//label[@class='oxd-label oxd-input-field-required']/../..//input")
        self.registration_number_txt = (By.XPATH," //label[contains(text(),'Registration Number')]/../..//input")
        self.email_text = (By.XPATH, "//input[@class='oxd-input oxd-input--active']")
        self.address_street1_txt = (By.XPATH, "//input[@class='oxd-input oxd-input--active']")
        self.city_txt = (By.XPATH, "//input[@class='oxd-input oxd-input--active']" )
        self.country_ddl = (By.XPATH, "//label[text()='Country']/../..//div[contains(@class,'oxd-select-wrapper')]")
        # self.country_dll.select_by_visible_text("Angola")

        self.save_btn = (By.XPATH, "//button[@type='submit']")
        self.save_successfully = (By.XPATH,"//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']")

        # self.username_in_table = (By.XPATH, "//table[@id='resultTable']//a[contains(@href, 'saveSystemUser')]")

    def go_to_general_information_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(organization_link).click()
        self.EF.find_element(self.general_information_link).click()

    def click_edit_scroll(self):
        self.EF.find_element(self.edit_scroll).click()

    def enter_organization_name_txt(self, organization_name):
        self.EF.find_element(self.organization_name_txt).clear()
        self.EF.find_element(self.organization_name_txt).send_keys(organization_name)

    def enter_registration_number_txt(self, registration_number):
        self.EF.find_element(self.registration_number_txt).clear()
        self.EF.find_element(self.registration_number_txt).send_keys(registration_number)

    def enter_email_txt(self, email_txt):
        pass

    def enter_address_street1_txt(self, address_street1):
        pass

    def enter_city_txt(self,city_txt):
        pass

    def select_country_ddl(self,country):
        pass
        # self.EF.Country .find_element(country.select_by_visible_text("Angola"))
        #
        # country.select_by_visible_text("Angola")
    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

    def save_general_information(self, save_dict: dict):
        self.enter_organization_name_txt(save_dict.get('organization_name', ""))
        self.enter_registration_number_txt(save_dict.get('registration_number', ""))
        self.enter_email_txt(save_dict.get('email', ""))
        self.enter_address_street1_txt(save_dict.get('address_street1', ""))
        self.enter_city_txt(save_dict.get('city', ""))
        # self.select_country(save_dict.get('country', ""))
        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH," //div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']"))
            return True
        except TimeoutException:
            return False

#organization_link = (By.XPATH, "//span[contains(text(),'Organization ')]")
#organization_link = (By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span/i")


class Locations(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.locations_link = (By.LINK_TEXT,"Locations")
        self.expand_search = (By.XPATH, "//button//i[@class='oxd-icon bi-caret-down-fill']")
        self.search_Name_txt = (By.XPATH, "//label[text()='Name']/../..//input")
        self.search_city_txt = (By.XPATH, "//div//label[contains(text(),'City')]/../..//input")
        self.country_ddl = (By.XPATH, "//label[text()='country']/../..//div[contains(@class,'oxd-select-wrapper')]")
        self.search_btn = (By.XPATH, "//button[@type='submit']")

    def go_to_locations_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(organization_link).click()
        self.EF.find_element(self.locations_link).click()

    def enter_name(self, name):
        self.EF.find_element(self.search_Name_txt).clear()
        self.EF.find_element(self.search_Name_txt).send_keys(name)

    def enter_city(self, city):
        self.EF.find_element(self.search_city_txt).clear()
        self.EF.find_element(self.search_city_txt).send_keys(city)

    def select_country(self,country):
        pass



    def click_search_btn(self):
        self.EF.find_element(self.search_btn).click()

    def search_location(self, search_dict: dict):
        self.enter_name(search_dict.get('name', ""))
        self.enter_city(search_dict.get('city', ""))
        self.select_country(search_dict.get('country',""))
        self.click_search_btn()
        try:
            self.EF.find_element((By.XPATH, f"//div[text()='{search_dict.get('name')}']"))
            return True
        except TimeoutException:
            return False


# class structure(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
#Qualifications

class Skills(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.Skills_link = (By.LINK_TEXT, "Skills")
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.add_Name_txt = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']/../..//input")
        self.add_description_txt = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']/../..//textarea")
        self.save_btn = (By.XPATH, "//button[@type='submit']")
        self.save_succesfully =(By.XPATH,"//div[@class='oxd-toast-container oxd-toast-container--bottom']")

    def go_to_skills_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(Qualifications_link).click()
        self.EF.find_element(self.Skills_link).click()
        self.EF.find_element(self.add_btn).click()

    def click_add_btn(self):
        self.EF.find_element(self.add_btn).click()

    def enter_name(self, name):
        self.EF.find_element(self.add_Name_txt).clear()
        self.EF.find_element(self.add_Name_txt).send_keys(name)

    def enter_description(self, description):
        self.EF.find_element(self.add_description_txt).clear()
        self.EF.find_element(self.add_description_txt).send_keys(description)


    def click_save_btn(self):
        self.EF.find_element(self.save_btn).click()

    def save_skills(self, save_dict: dict):
        self.enter_name(save_dict.get('name', ""))
        self.enter_description(save_dict.get('description', ""))
        self.click_save_btn()
        try:
            self.EF.find_element((By.XPATH, "//div[@class='oxd-toast-container oxd-toast-container--bottom']"))
            return True
        except TimeoutException:
            return False

# class Education(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class Licenses(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class Languages(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class Memberships(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# Nationalities

# class Nationalities (Base):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver


# # Corporate Branding
# class CorporateBranding(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# Configuration
# class EmailConfiguration(Base):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#

# class EmailSubscription(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class Localization(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class LanguagePackages(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class Modules(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class SocialMediaAuthentication(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
# class RegisterOAuthClient(Base):
#     def __init__(self, driver):
#         self.driver = driver
#
#
