from utils.headers import *

from pages.base_page import BasePage
from utils.defines import NAME, XPATH, TARGET_URL

class LoginPage(BasePage):
    def go_to_login_page(self):
        self.go_to_page(TARGET_URL["LOGIN_URL"]) # url 아직업어용

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
        self.input_id(user_data["username"])
        self.input_pw(user_data["password"])

    def click_login_button(self):
        btn = self.get_element_by_xpath(XPATH["BTN_LOGIN"])
        btn.click()
        time.sleep(0.3)