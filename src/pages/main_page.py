from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME

class MainPage(BasePage):
    def go_to_main_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])
        time.sleep(0.5)

    def click_new_chat_button(self):
        btn = self.get_element_by_css_selector(SELECTORS["BTN_NEW_CHAT"])
        btn.click()
        time.sleep(0.5)
    
    def click_on_past_chat(self, idx):
        list_items = self.get_elements_by_css_selector(SELECTORS["CHAT_LIST_ITEMS"])
        if not list_items:
            print("대화 내역이 없습니다.")
        
        list_items[idx].click()
        time.sleep(1)
    
    def scroll_up(self):
        #driver.execute_script("window.scrollBy(0, -200);")  # 200px씩 위로
        time.sleep(0.3)  # 잠시 대기 후 다시 체크

    
       
    def click_btn_scroll_to_bottom(self):
        btn_scroll = self.get_element_by_css_selector(SELECTORS["SCROLL_TO_BOTTOM_BUTTON"])
        if btn_scroll.is_enabled():
            btn_scroll.click()
        else:
            print("버튼이 비활성화되어 있음.")
        time.sleep(0.5)