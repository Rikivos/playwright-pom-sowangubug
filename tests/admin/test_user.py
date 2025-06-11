import pytest
import config
from pages.login_page import LoginPage  # sesuaikan path sesuai foldermu
from pages.admin.user_page import UserPage

@pytest.mark.user
def test_user_success(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login()

    user_page = UserPage(page)
    user_page.navigate()
    user_page.create_user()
    
    # assert page.url == f"{config.BASE_URL}/dashboard"