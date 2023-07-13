from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.common.exceptions import TimeoutException

time_sheets_link = (By.XPATH,"//span[contains(text(),'Timesheets')]")
class Employee_Timesheets(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.employee_timesheets_link = (By.XPATH, "//a[contains(text(),'Employee Timesheets')]")
        self.view_employee_name_txt = (By.XPATH, "//label[contains(text(),'Employee Name')]/../..//input")
        self.view_btn = (By.XPATH, "//button[@type='submit']")
        self.username_in_table = (By.XPATH, "//table[@id='resultTable']//a[contains(@href, 'saveSystemUser')]")

    def go_to_employee_timesheet_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(time_sheets_link).click()
        self.EF.find_element(self.employee_timesheets_link).click()

    def enter_employee_name_txt(self, employee_name):
        self.EF.find_element(self.view_employee_name_txt).clear()
        self.EF.find_element(self.view_employee_name_txt).send_keys(employee_name)



    def click_view_btn(self):
        self.EF.find_element(self.view_btn).click()

    def view_employee(self, view_dict: dict):
        self.enter_employee_name_txt(view_dict.get('employee_name', ""))

        self.click_view_btn()
        try:
            self.EF.find_element((By.XPATH, f"//div[text()='{view_dict.get('username')}']"))
            return True
        except TimeoutException:
            return False



