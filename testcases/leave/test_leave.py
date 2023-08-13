from page_objects.login import Login
from page_objects.leave import My_Leave
from utility.create_webdriver import WebDriver
import pytest

DATE = [{"search_from_date": "2023-04-01","search_to_date":"2024-06-03"}]

@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    my_leave_obj = My_Leave(driver)
    login_obj.login()
    yield login_obj, my_leave_obj
    my_leave_obj.logout()

# @pytest.mark.parametrize("search_dict, present", DATE)
@pytest.mark.parametrize("search_dict, present", [(DATE[0], True)])
def test_search_my_leave(setup, search_dict, present):
    login_obj, my_leave_obj = setup
    my_leave_obj.navigate_to_tab(my_leave_obj.leave_tab)
    my_leave_obj.go_to_my_leave_page()
    search_from_date = search_dict["search_from_date"]
    search_to_date = search_dict["search_to_date"]
    assert my_leave_obj.search_my_leave(search_dict)

# search_from_date, search_to_date