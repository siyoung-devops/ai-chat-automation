from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL

class SignupPage(BasePage):
    def go_to_signup_page(self):
        self.go_to_page(TARGET_URL["SIGNUP_URL"])
        time.sleep(1)