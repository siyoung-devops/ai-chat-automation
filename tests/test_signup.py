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
    
# PHC-TS02-TC008
def test_signup_success_pw_criteria(signup_page) :  
    email = random_string()
       
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdf123!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    success = signup_page.check_signup_success()
    
    assert "Forgot" in success, "PHC-TS02-TC008 : Test fail"
    print("PHC-TS02-TC008 : Test success")
    
# PHC-TS02-TC009
def test_signup_fail_pw_no_english(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("12341234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    fail = signup_page.check_signup_fail()
    
    assert "password stronger!" in fail, "PHC-TS02-TC009 : Test fail" 
    print("PHC-TS02-TC009 : Test success")
    
# PHC-TS02-TC010
def test_signup_fail_pw_no_number(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdfasdf!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    fail = signup_page.check_signup_fail()
    
    assert "password stronger!" in fail, "PHC-TS02-TC010 : Test fail" 
    print("PHC-TS02-TC010 : Test success")
    
# PHC-TS02-TC011
def test_signup_fail_pw_no_character(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdfg12345")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    fail = signup_page.check_signup_fail()
    
    assert "password stronger!" in fail, "PHC-TS02-TC011 : Test fail" 
    print("PHC-TS02-TC011 : Test success")
    
# PHC-TS02-TC012
def test_signup_fail_empty_pw(signup_page) : 
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    password_input = signup_page.signup_pw("")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    # 브라우저 기본 유효성 검사 툴팁
    msg = signup_page.driver.execute_script(
        "return arguments[0].validationMessage;", password_input
    )
    
    assert "입력란" in msg, "PHC-TS02-TC012 : Test fail" 
    print("PHC-TS02-TC012 : Test success")
    
# PHC-TS02-TC013
def test_signup_fail_empty_name(signup_page) : 
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdf1234!")
    name_input = signup_page.signup_name("")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    signup_page.btn_create()
    # 브라우저 기본 유효성 검사 툴팁
    msg = signup_page.driver.execute_script(
        "return arguments[0].validationMessage;", name_input
    )
    
    assert "입력란" in msg, "PHC-TS02-TC013 : Test fail" 
    print("PHC-TS02-TC013 : Test success")
    
# PHC-TS02-TC014
def test_signup_fail_no_agree(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    btn = signup_page.btn_element()
    
    assert btn.get_attribute("disabled") is not None, "PHC-TS02-TC014 : Test fail" 
    print("PHC-TS02-TC014 : Test success")
    
# PHC-TS02-TC015
def test_signup_success_no_optional(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    time.sleep(0.5)
    signup_page.checkbox_spread()
    elements[4].click()
    signup_page.btn_create()
    success = signup_page.check_signup_success()
    
    assert "Forgot" in success, "PHC-TS02-TC015 : Test fail"
    print("PHC-TS02-TC015 : Test success")
    
# PHC-TS02-TC016
def test_signup_fail_no_required(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    time.sleep(0.5)
    signup_page.checkbox_spread()
    elements[3].click()
    btn = signup_page.btn_element()
    
    assert btn.get_attribute("disabled") is not None, "PHC-TS02-TC016 : Test fail"
    print("PHC-TS02-TC016 : Test success")
    
# PHC-TS02-TC017
def test_signup_14_age_verify(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    elements = signup_page.signup_checkbox()
    elements[0].click()
    time.sleep(0.5)
    signup_page.checkbox_spread()
    elements[1].click()
    btn = signup_page.btn_element()
    
    if "Verify" in btn.text.strip() :
        btn.click()
        # pass 인증화면 iframe으로 되어있음
        iframe = signup_page.iframe_element()
        signup_page.driver.switch_to.frame(iframe) # iframe 화면으로 이동
        # pass 인증화면 요소 찾기
        pass_element = signup_page.iframe_pass_element()
        
        assert "통신사" in pass_element.text.strip(), "PHC-TS02-TC017 : Test fail"
        print("PHC-TS02-TC017 : Test success")
        
    else :
        try :
            signup_page.iframe_element()
        except TimeoutException :
            print("PHC-TS02-TC017 : Test fail")
            
# PHC-TS02-TC021
def test_signup_view_password(signup_page) :
    email = random_string()
    
    signup_page.go_to_signup_page()
    signup_page.signup_email(f"{email}@gmail.com")
    element = signup_page.signup_pw("asdf1234!")
    signup_page.signup_name("이수진")
    signup_page.view_password()
    assert element.get_attribute("type") == "text", "PHC-TS02-TC021 : Test fail"
    print("PHC-TS02-TC021 : Test success")
    
    signup_page.view_password()
    assert element.get_attribute("type") == "password", "PHC-TS02-TC021 : Test fail"
    print("PHC-TS02-TC021 : Test success")