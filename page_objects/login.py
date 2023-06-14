from selenium.webdriver.common.by import By
from utility.elementry_functions import Elem_Func
from constants import USERNAME, PASSWORD


class Login:
    def __init__(self, driver):
        self.driver=driver
        self.EF=Elem_Func(self.driver)

        # Locators
        self.username_txt=(By.NAME, "username")
        self.password_txt=(By.NAME, "password")
        self.login_btn=(By.XPATH, "//button[@type='submit']")

    def goto_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self,username):
        self.EF.find_element(self.username_txt).clear()
        self.EF.find_element(self.username_txt).send_keys(username)

    def enter_password(self,password):
        self.EF.find_element(self.password_txt).clear()
        self.EF.find_element(self.password_txt).send_keys(password)

    def click_login_btn(self):
        self.EF.find_element( self.login_btn).click()

    def login(self,username=USERNAME, password=PASSWORD):
        self.goto_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()



