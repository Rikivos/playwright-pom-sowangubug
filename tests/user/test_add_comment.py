import pytest
import config
# from pages.login_page import LoginPage  
from pages.user.add_comment_page import AddCommentPage

@pytest.mark.add_comment
def test_add_comment_success(page):
    add_comment_page = AddCommentPage(page)
    add_comment_page.navigate()
    add_comment_page.add_comment()


    
    # assert page.url == f"{config.BASE_URL}/dashboard"