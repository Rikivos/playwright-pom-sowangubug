import config
import time
from locators import category_locator as loc

class CategoryPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{config.BASE_URL}/dashboard/categories/create")

    def create_category(self):
        self.page.fill(loc.TITLE_INPUT, "Test Category")
        self.page.fill(loc.DESCRIPTION_INPUT, "Test Category")
        # self.page.click(loc.IMAGE_UPLOAD, )
        time.sleep(25)
        self.page.select_option(loc.STATUS_SELECT, "Aktif")
        self.page.click(loc.SAVE_BUTTON)
        time.sleep(60)
