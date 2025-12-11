from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, XPATH, ID

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
        
        
    def signup_email(self, email) :
        element = self.get_element_by_id(ID["SIGNUP_EMAIL"])
        element.click()
        element.clear()
        element.send_keys(email)
        time.sleep(0.5)
        
    def signup_pw(self, password) :
        element = self.get_element_by_xpath(XPATH["SIGNUP_PW"])
        element.click()
        element.clear()
        element.send_keys(password)
        time.sleep(0.5)