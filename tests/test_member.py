from utils.headers import *
from pages.member_page import MemberPage
from managers.driver_manager import DriverManager

driver = DriverManager().create_driver()

#사이트 접속
def test_main_in(logged_in_main):
    page = logged_in_main

#계정관리 접속
def test_member_in():    
    try:
        page = MemberPage(driver)
        page.click_member_btn()
        
    finally:
        driver.quit()