from utils.headers import *
from pages.signup_page import (
    SignupPage
)
from managers.driver_manager import (
    DriverManager
)
from utils.browser_utils import random_string

generated_email = None # 전역 변수

# PHC-TS02-TC001
def test_signup_success(signup_page) :  
    global generated_email
    generated_email = random_string()
       
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{generated_email}@gmail.com")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    success = signup_page.check_signup_success()
    
    assert "Forgot" in success, "PHC-TS02-TC001 : Test fail"

# PHC-TS02-TC002
def test_signup_fail_duplicate(signup_page) :
    global generated_email
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{generated_email}@gmail.com")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    fail = signup_page.check_signup_fail()
    
    assert "already" in fail, "PHC-TS02-TC002 : Test fail" 
    
# PHC-TS02-TC003
def test_signup_fail_no_a(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}gmail.com")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    fail = signup_page.check_signup_fail()
    
    assert "incorrect" in fail, "PHC-TS02-TC003 : Test fail" 
    
# PHC-TS02-TC004
def test_signup_fail_no_address(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    # 브라우저 기본 유효성 검사 툴팁
    
    assert "incorrect" in fail, "PHC-TS02-TC004 : Test fail" 
         
        