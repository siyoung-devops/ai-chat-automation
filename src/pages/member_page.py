from utils.headers import *
from utils.context import LoginContext
from utils.browser_utils import BrowserUtils

from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH, ID

from utils.headers import By

class MemberPage(BasePage):
    def go_to_member_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])
        time.sleep(1)  

    def click_member_btn(self): #사람 이미지 > 계정관리 순차 클릭 
        self.get_element_by_css_selector(SELECTORS["MEMBER_MODAL"]).click()
        time.sleep(0.5)
        self.get_element_by_xpath(XPATH["BTN_MEMBER"]).click()
        time.sleep(0.5)
        print("계정관리 페이지 이동")
    
    def click_name_update(self): #이름 수정 활성화 
        
        member_btns = self.get_element(By.CSS_SELECTOR,SELECTORS["UPDATE_BTN"])
        if not member_btns:
            print("없습니다.")
            
        time.sleep(3)
        # $x("//*[contains(@class,'css-69t54h')]/tbody/tr/td/div/div/button")
        # $x("//*[contains(@class,'css-1yccujk')]/li/button")
