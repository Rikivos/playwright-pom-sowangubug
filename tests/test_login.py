import pytest
import config
from pages.login_page import LoginPage  # sesuaikan path sesuai foldermu

@pytest.mark.login
def test_login_success(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login()
    
    # assert page.url == f"{config.BASE_URL}/dashboard"