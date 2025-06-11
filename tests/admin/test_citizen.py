import pytest
import config
from pages.login_page import LoginPage  
from pages.admin.citizen_page import CitizenPage

@pytest.mark.citizen
def test_category_success(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login()

    citizen_page = CitizenPage(page)
    citizen_page.navigate()
    citizen_page.create_citizen()
    
    # assert page.url == f"{config.BASE_URL}/dashboard"