from utils.headers import *

from pages.base_page import BasePage
from utils.defines import NAME, XPATH,SELECTORS, TARGET_URL

class LoginPage(BasePage):
    def go_to_login_page(self):
        self.go_to_page(TARGET_URL["LOGIN_URL"])


    # 입력값 제어 메서드
    def input_id(self, username):
        element = self.get_element_by_name(NAME["INPUT_ID"])
        element.click()
        element.clear()
        element.send_keys(username)
        time.sleep(0.3)

    def input_pw(self, password):
        element = self.get_element_by_name(NAME["INPUT_PW"])
        element.click()
        element.clear()
        element.send_keys(password)
        time.sleep(0.3)

    def input_user_data(self, user_data):
        # user_data가 리스트인 경우 첫 번째 원소 사용
        if isinstance(user_data, list):
            user_data = user_data[0]
        self.input_id(user_data["username"])
        self.input_pw(user_data["password"])

    # 버튼 제어 메서드
    def click_login_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_LOGIN"])
        btn.click()
        time.sleep(0.3)
        
    # 로그인 실패/유효성 검증 메서드
    
    
    # 로그아웃 기능 메서드
    def click_account_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_ACCOUNT"]) # 아직 안됨
        btn.click()
        time.sleep(0.3)
        
    def click_logout_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_LOGOUT"]) # 아직 안됨
        btn.click()
        time.sleep(0.3)
        
    def logout(self):
        self.click_account_button
        self.click_logout_button
        time.sleep(0.3)
        
    def is_logged_out_page(self):
        url = self.driver.current_url
        return "/accounts/signin/history" in url
    
    # View Password 기능 메서드
    def click_view_password_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_VIEW_PASSWORD"]) # 아직 안됨
        btn.click()
        time.sleep(0.3)
    
    def is_password_visible(self):
        pw_input = self.get_element_by_name(NAME["INPUT_PW"])
        if pw_input is None:
            return False
        return pw_input.get_attribute("type") == "text"
    
    def is_password_masked(self):
        pw_input = self.get_element_by_name(NAME["INPUT_PW"])
        if pw_input is None:
            return False
        return pw_input.get_attribute("type") == "password"
    
    # Forgot password 기능 메서드
    def click_forgot_password_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_FORGOT_PASSWORD"]) # 아직 안됨
        btn.click()
        time.sleep(0.3)
        
    def get_current_url(self): # 현재 URL 가져오기
        return self.driver.current_url  
    
    def is_forgot_password_page(self):
        url = self.driver.current_url
        return "recover" in url or "password" in url
        
    # Sign in with a different account 기능 메서드
    def click_diff_account_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_DIFF_ACCOUNT"]) # 아직 안됨
        btn.click()
        time.sleep(0.3)
        
    
    
    # Remove history 기능 메서드
    def click_remove_history_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_REMOVE_HISTORY"]) # 아직 안됨
        btn.click()
        time.sleep(0.3)
        
    def get_id_value(self): # 
        element = self.get_element_by_name(NAME["INPUT_ID"])
        return element.get_attribute("value")

    def get_pw_value(self):
        element = self.get_element_by_name(NAME["INPUT_PW"])
        return element.get_attribute("value")
    
    def is_inputs_cleared(self):
        return self.get_id_value() == "" and self.get_pw_value() == ""