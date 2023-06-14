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


