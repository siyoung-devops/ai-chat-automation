from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH, ID

class MemberPage(BasePage):
    def click_member_btn(self): #사람 이미지 > 계정관리 순차 클릭 
        self.get_element_by_css_selector(SELECTORS["MEMBER_MODAL"]).click()
        time.sleep(0.5)
        self.get_element_by_xpath(SELECTORS["BTN_MEMBER"]).click()
        time.sleep(0.5)

    
    