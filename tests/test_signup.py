from utils.headers import *
from pages.signup_page import (
    SignupPage
)
from utils.browser_utils import random_string

generated_email = None # 전역 변수, TC 1번째의 이메일을 받아 2번째 중복 테스트에 사용하려고

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
    print("PHC-TS02-TC001 : Test success")

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
    print("PHC-TS02-TC002 : Test success")
    
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
    print("PHC-TS02-TC003 : Test success")
    
# PHC-TS02-TC004
def test_signup_fail_no_address(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    email_input = signup_page.signup_email(f"{email}@")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    # 브라우저 기본 유효성 검사 툴팁
    msg = signup_page.driver.execute_script(
        "return arguments[0].validationMessage;", email_input
    )
    
    assert "@" in msg, "PHC-TS02-TC004 : Test fail" 
    print("PHC-TS02-TC004 : Test success")

# PHC-TS02-TC005
def test_signup_fail_notcomplete_address(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    fail = signup_page.check_signup_fail()
    
    assert "incorrect" in fail, "PHC-TS02-TC005 : Test fail" 
    print("PHC-TS02-TC005 : Test success")  
    
# PHC-TS02-TC006
def test_signup_fail_empty_email(signup_page) : 
    signup_page.go_to_signup_page()
    email_input = signup_page.signup_email("")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    # 브라우저 기본 유효성 검사 툴팁
    msg = signup_page.driver.execute_script(
        "return arguments[0].validationMessage;", email_input
    )
    
    assert "입력란" in msg, "PHC-TS02-TC006 : Test fail" 
    print("PHC-TS02-TC006 : Test success")
    
# PHC-TS02-TC007
def test_signup_fail_pw_less(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdf")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    fail = signup_page.check_signup_fail()
    
    assert "password stronger!" in fail, "PHC-TS02-TC007 : Test fail" 
    print("PHC-TS02-TC007 : Test success")
        