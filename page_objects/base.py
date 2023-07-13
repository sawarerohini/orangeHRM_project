from selenium.webdriver.common.by import By
from utility.elementry_functions import Elem_Func


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.EF = Elem_Func(self.driver)

        # Locators

        # Admin (user-management)
        self.admin_tab = (By.XPATH, "//a[contains(@href,'viewAdminModule')]")

        # PIM (configuration)
        # self.pim_tab = (By.XPATH, "//a[contains(@href,'viewPimModule')]")
        self.pim_tab = (By.LINK_TEXT,"PIM")
        # leave
        self.leave_tab = (By.LINK_TEXT, "Leave")
        # Time
        self.time_tab = (By.XPATH,"//a[@href='/web/index.php/time/viewTimeModule']")

        # Logout Locators
        self.user_profile = (By.CLASS_NAME, 'oxd-userdropdown')
        self.logout_link = (By.LINK_TEXT, "Logout")

    def click_user_profile(self):
        self.EF.find_element(self.user_profile).click()

    def click_logout_link(self):
        self.EF.find_element(self.logout_link).click()

    def logout(self):
        self.click_user_profile()
        self.click_logout_link()

    def navigate_to_tab(self, tab_link):
        self.EF.find_element(tab_link).click()

    # def navigate_to_page(self, menu_order):
    #     for menu in menu_order:
    #         if menu == menu_order[-1]:
    #             self.EF.find_element(menu).click()
    #
    #         else:
    #             self.EF.mouse_hover(menu)






