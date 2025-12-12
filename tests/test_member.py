from utils.headers import *

from pages.member_page import MemberPage
from pages.login_page import LoginPage

from managers.driver_manager import DriverManager

driver = DriverManager().create_driver()
page = MemberPage(driver)

#로그인 -> 가져와서 쓸만한 로그인 함수 없나..? 일단 로그인 시켜두고 이후에 수정하자ㅠ
def test_site_login(driver,login_page, user_data):
    login_page.go_to_login_page()
    login_page.login_remove_history()
    login_page.input_user_data(user_data)
    login_page.click_login_button()
        


def test_member_in():    
    try:
        page.click_member_btn() #계정관리 접속
        time.sleep(7)
    finally:
        driver.quit()