from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, XPATH, ID, NAME

class SignupPage(BasePage):
    def go_to_signup_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])
        time.sleep(1)
        create_button = self.get_element_by_xpath(XPATH["BTN_CREATE_ACCOUNT"])
        create_button.click()
        time.sleep(1)
        create_withemail = self.get_element_by_xpath(XPATH["BTN_CREATE_EMAIL"])
        create_withemail.click()
        time.sleep(1)
        print("회원 가입 페이지로 이동")
        
    def signup_email(self, email) :
        element = self.get_element_by_name(NAME["INPUT_ID"])
        element.click()
        element.clear()
        element.send_keys(email)
        time.sleep(0.5)
        print("이메일 입력 완료")
        
    def signup_pw(self, password) :
        element = self.get_element_by_name(NAME["INPUT_PW"])
        element.click()
        element.clear()
        element.send_keys(password)
        time.sleep(0.5)
        print("비밀번호 입력 완료")
        
    def signup_name(self, name) :
        element = self.get_element_by_name(NAME["INPUT_NAME"])
        element.click()
        element.clear()
        element.send_keys(name)
        time.sleep(0.5)
        print("이름 입력 완료")
        
    def checkbox_spread(self) :
        header = self.get_element_by_id(ID["CHECKBOX_HEADER"])
        header.click()
        time.sleep(0.5)
        
    def signup_checkbox(self) :
        elements = self.get_elements_by_xpath(XPATH["SIGNUP_AGREE"])
        return elements
    
    def btn_create(self) :
        btn = self.get_element_by_xpath(XPATH["BTN_SIGNUP"])
        btn.click()
        print("회원가입 완료")
        
    def check_signup_success(self) :
        success = self.get_element_by_xpath(XPATH["CHECK_SIGNUP"])
        return success.text.strip()