from page_objects.login import Login
from page_objects.admin import Skills
from utility.create_webdriver import WebDriver
import pytest

SKILLS = [{"name": "sweet","description":"tester"}]



@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    skills_obj = Skills(driver)
    login_obj.login()

    yield login_obj, skills_obj
    skills_obj.logout()

@pytest.mark.parametrize("save_dict", SKILLS)
def test_save_skills(setup, save_dict):
    login_obj, skills_obj = setup
    skills_obj.navigate_to_tab(skills_obj.admin_tab)
    skills_obj.go_to_skills_page()
    assert skills_obj.save_skills(save_dict)

    print("save",save_dict)
