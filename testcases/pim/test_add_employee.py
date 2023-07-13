from page_objects.login import Login
from page_objects.pim import Add_Employee
from utility.create_webdriver import WebDriver
import pytest

ADD_EMPLOYEE = [{"first_name": "rohini","middle_name":"saware","last_name":"dnyanoba","employee_id":"22","location":"C:\\ROHINI"}]

@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    add_employee_obj = Add_Employee(driver)
    login_obj.login()
    yield login_obj, add_employee_obj
    add_employee_obj.logout()

@pytest.mark.parametrize("save_dict", ADD_EMPLOYEE)
def test_save_add_employee(setup, save_dict):
    login_obj, add_employee_obj = setup
    add_employee_obj.navigate_to_tab(add_employee_obj.pim_tab)
    add_employee_obj.go_to_add_employee_page()
    assert add_employee_obj.save_add_employee(save_dict)

