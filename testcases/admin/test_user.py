from page_objects.login import Login
from page_objects.admin import Users
from utility.create_webdriver import WebDriver
import pytest

USERS = [[{"username": "Charlie.Carter"}, True],[{"username": "rohini"},False]]

@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    user_obj = Users(driver)
    login_obj.login()
    yield login_obj, user_obj
    user_obj.logout()

@pytest.mark.parametrize("search_dict, present", USERS)
def test_search_user(setup, search_dict, present):
    login_obj, user_obj = setup
    user_obj.navigate_to_tab(user_obj.admin_tab)
    user_obj.go_to_users_page()
    assert user_obj.search_user(search_dict) == present

