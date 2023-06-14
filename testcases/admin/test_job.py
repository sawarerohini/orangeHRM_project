from page_objects.login import Login
from page_objects.admin import Job_Titles
from utility.create_webdriver import WebDriver
import pytest

JOB_TITLES = [{"job_title": "deta entry","description":"database"}]



@pytest.fixture()
def setup():
    driver = WebDriver()
    login_obj = Login(driver)
    job_title_obj = Job_Titles(driver)
    login_obj.login()

    yield login_obj, job_title_obj
    job_title_obj.logout()

@pytest.mark.parametrize("save_dict", JOB_TITLES)
def test_save_job_title(setup, save_dict):
    login_obj, job_title_obj = setup
    job_title_obj.navigate_to_tab(job_title_obj.admin_tab)
    job_title_obj.go_to_job_titles_page()
    job_title_obj.click_add_btn()
    assert job_title_obj.save_job_title(save_dict)


    print("save",save_dict)