from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL
from utils.defines import NAME

class MainPage(BasePage):
    def go_to_main_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])
        time.sleep(0.5)

