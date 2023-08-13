from page_objects.login import Login
from page_objects.leave import Add_Entitlements
from utility.create_webdriver import WebDriver
import pytest

ENTITLEMENTS = [{"employee_name": "rani","entitlement":"abc"}]



@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    add_entitlements_obj = Add_Entitlements(driver)
    login_obj.login()

    yield login_obj, add_entitlements_obj
    add_entitlements_obj.logout()

@pytest.mark.parametrize("save_dict", ENTITLEMENTS)
def test_save_add_entitlements(setup, save_dict):
    login_obj, add_entitlements_obj = setup
    add_entitlements_obj.navigate_to_tab(add_entitlements_obj.leave_tab)
    add_entitlements_obj.go_to_add_entitlements_page()
    assert add_entitlements_obj.save_add_entitlements(save_dict)

    print("save",save_dict)
