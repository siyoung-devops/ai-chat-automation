from utils.headers import *
from pages.signup_page import (
    SignupPage
)
from managers.driver_manager import (
    DriverManager
)

def test_signup_success() :
    driver = DriverManager().create_driver()
    
    try :
        page = SignupPage(driver)
        
        page.go_to_signup_page()
        page.signup_email("bimisi@gmail.com")
        page.signup_pw("asdf1234!")
        page.signup_name("이수진")
        elements = page.signup_checkbox()
        elements[0].click()
        page.btn_create()
        success = page.check_signup_success()
        
        assert "Forgot" in success, "PHC-TS02-TC001 : Test fail"
        
    finally :
        driver.quit()
        