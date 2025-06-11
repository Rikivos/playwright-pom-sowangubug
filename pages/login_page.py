import config
import time
from locators import button_locator as loc

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{config.BASE_URL}/masuk")

    def login(self):
        self.page.click(loc.AGREE_BUTTON)
        self.page.fill(loc.EMAIL_INPUT, config.EMAIL)
        self.page.fill(loc.PASSWORD_INPUT, config.PASSWORD)
        self.page.click(loc.LOGIN_BUTTON)
        time.sleep(3)
