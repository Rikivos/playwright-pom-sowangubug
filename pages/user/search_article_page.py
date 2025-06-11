import config
import time
from locators import search_locator as locsearch
from locators import button_locator as loc

class SearchArticlePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{config.BASE_URL}")

    def search(self):
        self.page.click(loc.AGREE_BUTTON)
        self.page.click(locsearch.SEARCH_BUTTON)
        self.page.fill(locsearch.SEARCH_INPUT, "olahraga")
        self.page.click(locsearch.SUBMIT_BUTTON)
        time.sleep(5)
        
