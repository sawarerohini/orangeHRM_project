from page_objects.login import Login
from page_objects.time import Employee_Timesheets
from utility.create_webdriver import WebDriver
import pytest

EMPLOYEE_NAME = [{"employee_name": ""}]

@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    employee_timesheets_obj = Employee_Timesheets(driver)
    login_obj.login()
    yield login_obj, employee_timesheets_obj
    employee_timesheets_obj.logout()

@pytest.mark.parametrize("view_dict, present", EMPLOYEE_NAME)
def test_view_employee_timesheets(setup, view_dict, present):
    login_obj, employee_timesheets_obj = setup
    employee_timesheets_obj.navigate_to_tab(employee_timesheets_obj.time_tab)
    employee_timesheets_obj.go_to_employee_timesheets_page()
    assert employee_timesheets_obj.view_employee_timesheets(view_dict) == present

