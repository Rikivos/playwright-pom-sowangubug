import pytest
import config
# from pages.login_page import LoginPage  
from pages.user.search_article_page import SearchArticlePage

@pytest.mark.search
def test_search_success(page):
    search_page = SearchArticlePage(page)
    search_page.navigate()
    search_page.search()


    
    # assert page.url == f"{config.BASE_URL}/dashboard"