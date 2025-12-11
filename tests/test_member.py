from utils.headers import *

from pages.member_page import MemberPage
from pages.login_page import LoginPage

from managers.driver_manager import DriverManager

driver = DriverManager().create_driver()


def test_site_login(driver,login_page, user_data):
    login_page.go_to_login_page()
    login_page.input_user_data(user_data)

# #계정관리 접속
def test_member_in():    
    try:
        page = MemberPage(driver)
        page.click_member_btn()
        
    finally:
        driver.quit()