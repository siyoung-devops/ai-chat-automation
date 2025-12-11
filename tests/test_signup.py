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
        page.signup_email("hihello@gmail.com")
        page.signup_pw("asdf1234!")
        
    finally :
        driver.quit()
        