from page_objects.login import Login
from page_objects.pim import Optional_Fields
from utility.create_webdriver import WebDriver
import pytest


@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    optional_fields_obj = Optional_Fields(driver)
    login_obj.login()
    yield login_obj, optional_fields_obj
    optional_fields_obj.logout()

@pytest.mark.parametrize("save",[True])
def test_save_optional_fields(setup, save):
    login_obj, optional_fields_obj = setup
    optional_fields_obj.navigate_to_tab(optional_fields_obj.pim_tab)
    optional_fields_obj.go_to_optional_fields_page()
    assert optional_fields_obj.save_optional_fields(save)
   