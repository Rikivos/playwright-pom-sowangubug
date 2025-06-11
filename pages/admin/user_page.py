import config
import time
from locators import user_locator as loc

class UserPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{config.BASE_URL}/dashboard/users/create")

    def create_user(self):
        # self.page.click(loc.NEW_USER_BUTTON)
        self.page.fill(loc.NAME_INPUT, "Test User")
        self.page.fill(loc.USERNAME_INPUT, "testuser")
        self.page.fill(loc.EMAIL_INPUT, "testuser@example.com")
        self.page.fill(loc.PASSWORD_INPUT, "password")
        self.page.fill(loc.CONFIRM_PASSWORD_INPUT, "password")
        # self.page.click(loc.ROLE_SELECT)
        self.page.select_option(loc.ROLE_SELECT, "Admin")
        self.page.select_option(loc.STATUS_SELECT, "Aktif")
        self.page.fill(loc.ABOUT_INPUT, "Test User")
        self.page.click(loc.SAVE_BUTTON)
        # time.sleep(60)
