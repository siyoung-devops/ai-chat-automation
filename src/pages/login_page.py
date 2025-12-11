from utils.headers import *

from pages.base_page import BasePage
from utils.defines import NAME, XPATH,SELECTORS, TARGET_URL

class LoginPage(BasePage):
    def go_to_login_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"]) # url 아직업어용

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

    def click_login_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_LOGIN"])
        btn.click()
        time.sleep(0.3)
        
    def login_remove_history(self): #아이디 저장 내용 초기화용
        btn = self.get_element_by_css_selector(SELECTORS["REMOVE_HISROTY"])
        btn.click()
        time.sleep(0.5)