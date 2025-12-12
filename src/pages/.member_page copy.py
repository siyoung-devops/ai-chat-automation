from utils.headers import *
from utils.context import LoginContext
from utils.browser_utils import BrowserUtils

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH, ID

class MemberPage(BasePage):
    def go_to_main_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])
        time.sleep(4) 

    def go_to_member_page(self): #사람 이미지 > 계정관리 순차 클릭 

        modal_btn = self.get_element_by_css_selector(SELECTORS["MEMBER_MODAL"])
        modal_btn.click()
        time.sleep(4)
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(20)
        self.get_element_by_xpath(XPATH["BTN_MEMBER"]).click()
        time.sleep(4)

    def click_to_mkt(self):
        element = self.get_element_by_name(NAME["MKT_BTN"])
        element.click()
        time.sleep(4)
        
    def choose_lan_dropbox(self):
        element = self.get_element_by_xpath(XPATH["LANG_BOX"])
        element.click()
        time.sleep(4)
        
        
    def click_name_update(self,idx): #이름 수정 활성화 
        btns = self.get_elements_by_css_selector(SELECTORS["BTNS_UPDATE"])
        print(f"🔍 수정 버튼 {len(btns)}개 찾음 (요청: {idx})")
        
        if not btns:
            print("❌ 수정버튼 없음.")
            return False
        
        if idx >= len(btns):
            print(f"❌ 인덱스 {idx} 초과 (최대 {len(btns)-1})")
            print(f"   사용 가능한 버튼: {len(btns)}개")
            return False
        
        target_btn = btns[idx]
        if not target_btn.is_displayed():
            print(f"❌ {idx}번째 버튼 숨김")
            return False
        
        # React 호환 JS 클릭
        self.driver.execute_script("""
            arguments[0].scrollIntoView({block: 'center'});
            arguments[0].click();
        """, target_btn)
        
        print(f"✅ {idx}번째 버튼 클릭 완료")
        time.sleep(1)
        return True
        time.sleep(1)
        # $x("//*[contains(@class,'css-69t54h')]/tbody/tr/td/div/div/button")
        # $x("//*[contains(@class,'css-1yccujk')]/li/button")
        ##root > div.MuiStack-root.css-1k8t7d9 > div > main > div.css-ts9wun.e9qrkv71 > div > section:nth-child(1) > div.MuiBox-root.css-0 > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > button > svg

       
 #self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", input_name)