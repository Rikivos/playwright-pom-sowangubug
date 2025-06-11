import pytest
import config
from pages.login_page import LoginPage  # sesuaikan path sesuai foldermu
from pages.admin.post_page import PostPage

@pytest.mark.post
def test_post_success(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login()

    post_page = PostPage(page)
    post_page.navigate()
    post_page.create_post()
    
    # assert page.url == f"{config.BASE_URL}/dashboard"