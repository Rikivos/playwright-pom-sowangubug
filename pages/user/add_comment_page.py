import config
import time
from locators import comment_locator as loccomment
from locators import button_locator as loc

class AddCommentPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{config.BASE_URL}/postingan/hut-ri-ke-79-berbeda-dan-terpisah-tak-menjadikan-halangan-untuk-tetap-harmonis")

    def add_comment(self):
        self.page.click(loc.AGREE_BUTTON)
        self.page.fill(loccomment.NAME_INPUT, "Test Comment")
        self.page.fill(loccomment.EMAIL_INPUT, "testuser@example.com")
        self.page.fill(loccomment.COMMENT_INPUT, "Test Comment")
        self.page.click(loccomment.SUBMIT_BUTTON)
        time.sleep(5)
        
