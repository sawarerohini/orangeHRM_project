from page_objects.login import Login
from page_objects.admin import Locations
from utility.create_webdriver import WebDriver
import pytest

LOCATIONS = [[{"name": "Canadian Regional HQ","city":"Ottawa"},True],[{"name": "rohini","city":"latur"}, False]]

@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    location_obj = Locations(driver)
    login_obj.login()
    yield login_obj, location_obj
    location_obj.logout()

@pytest.mark.parametrize("search_dict, present", LOCATIONS)
def test_search_location(setup, search_dict, present):
    login_obj, location_obj = setup
    location_obj.navigate_to_tab(location_obj.admin_tab)
    location_obj.go_to_locations_page()
    assert location_obj.search_location(search_dict) == present

