from page_objects.login import Login
from page_objects.pim import Custom_Fields
from utility.create_webdriver import WebDriver
import pytest

CUSTOMFIELDS = [{"fields_name":"song","type_select":"select_by_index(1)"}]
@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    custom_fields_obj = Custom_Fields(driver)
    login_obj.login()
    yield login_obj, custom_fields_obj
    custom_fields_obj.logout()

@pytest.mark.parametrize("save_dict", CUSTOMFIELDS)
def test_save_custom_fields(setup, save_dict):
    login_obj, custom_fields_obj = setup
    custom_fields_obj.navigate_to_tab(custom_fields_obj.pim_tab)
    custom_fields_obj.go_to_custom_fields_page()
    custom_fields_obj.click_add_btn()
    assert custom_fields_obj.save_custom_fields(save_dict)


