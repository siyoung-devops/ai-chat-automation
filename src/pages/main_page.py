from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME

class MainPage(BasePage):
    def go_to_main_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])
        time.sleep(0.5)

    def click_new_chat_button(self):
        btn = self.get_element_by_css_selector(SELECTORS["BTN_LOGIN"])
        btn.click()
        time.sleep(0.3)