import pytest
import config
from pages.login_page import LoginPage  # sesuaikan path sesuai foldermu
from pages.admin.category_page import CategoryPage

@pytest.mark.category
def test_category_success(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login()

    category_page = CategoryPage(page)
    category_page.navigate()
    category_page.create_category()
    
    # assert page.url == f"{config.BASE_URL}/dashboard"