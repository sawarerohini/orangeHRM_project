from page_objects.login import Login
from page_objects.leave import Holidays
from utility.create_webdriver import WebDriver
import pytest

HOLIDAYS = [{"name": "mohini","date":"2024-06-03"}]

@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    holidays_obj = Holidays(driver)
    login_obj.login()
    yield login_obj, holidays_obj
    holidays_obj.logout()

@pytest.mark.parametrize("save_dict", HOLIDAYS)
def test_save_holidays(setup, save_dict):
    login_obj, holidays_obj = setup
    holidays_obj.navigate_to_tab(holidays_obj.leave_tab)
    holidays_obj.go_to_holidays_page()
    holidays_obj.click_add_btn()
    assert holidays_obj.save_holidays(save_dict)


