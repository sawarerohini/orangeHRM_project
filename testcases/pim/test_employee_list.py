from page_objects.login import Login
from page_objects.pim import Employee_List
from utility.create_webdriver import WebDriver
import pytest

EMPLOYEE_LIST = [[{"employee_name":"Anthony Nolan","employee_id":"0070"},True],
                 [{"employee_name":"rohini","employee_id":"80"},False]]

@pytest.fixture()
def setup():
    driver = WebDriver
    login_obj = Login(driver)
    employee_list_obj = Employee_List(driver)
    login_obj.login()
    yield login_obj.login,employee_list_obj
    employee_list_obj.logout()

@pytest.mark.paramiterize("search_dict, present",EMPLOYEE_LIST)
def search_employee_list(setup,search_dict, present):
    login_obj,search_employee_list_obj = setup
    search_employee_list_obj.navigat_to_tab(search_employee_list_obj.pim_tab)
    search_employee_list_obj.go_to_employee_list_page()
    assert search_employee_list_obj.search_employee_list(search_dict) == present







