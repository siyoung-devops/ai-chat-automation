from utils.headers import *
from pages.member_page import MemberPage
from managers.driver_manager import DriverManager

def test_main_in(logged_in_main):
    page = logged_in_main

def test_member_in():    
    driver = DriverManager().create_driver()
    try:
        page = MemberPage(driver)
        
    finally:
        driver.quit()