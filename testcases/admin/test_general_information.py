from page_objects.login import Login
from page_objects.admin import GeneralInformation
from utility.create_webdriver import WebDriver
import pytest

GENERALINFORMATION = [{"organization_name":"OrangeHRM","registration_number":"212342"}]

@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    generalinformation_obj = GeneralInformation(driver)
    login_obj.login()
    yield login_obj, generalinformation_obj
    generalinformation_obj.logout()

@pytest.mark.parametrize("save_dict", GENERALINFORMATION)
def test_save_generalinformation(setup, save_dict):
    login_obj, generalinformation_obj = setup
    generalinformation_obj.navigate_to_tab(generalinformation_obj.admin_tab)
    generalinformation_obj.go_to_general_information_page()
    generalinformation_obj.click_edit_scroll()
    assert generalinformation_obj.save_general_information(save_dict)

