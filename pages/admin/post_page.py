import config
import time
from locators import post_locator as loc

class PostPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{config.BASE_URL}/dashboard/posts/create")

    def create_post(self):
        self.page.fill(loc.TITLE_INPUT, "Test Post")
        self.page.fill(loc.CONTENT_INPUT, "Test Post")
        self.page.spa(loc.CATEGORY_SELECT, "Olahraga")
        time.sleep(5)
        self.page.fill(loc.KEYWORDS_INPUT, "olahraga")
        self.page.select_option(loc.STATUS_SELECT, "Draft")
        # self.page.click(loc.SAVE_BUTTON)
        time.sleep(60)
