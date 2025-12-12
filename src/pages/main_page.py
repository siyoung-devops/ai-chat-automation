from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH

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
    

    def scroll_up_chat(self, step=200):
        scroll_area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        if scroll_area is None:
            print("스크롤 영역을 찾을 수 없습니다.")
            return

        scroll_to_top = None
        while True:
            current_scroll_top = self.driver.execute_script("return arguments[0].scrollTop;", scroll_area)
            
            if current_scroll_top == 0 or current_scroll_top == scroll_to_top:
                print("맨 위 도착!")
                break
            
            # 테스트 용 ===================================
            print(f"[up] current_scroll_top :{current_scroll_top} == scroll_to_top :{scroll_to_top} ?")
            #  ==========================================
            
            self.driver.execute_script(f"arguments[0].scrollBy(0, {-step});", scroll_area)
            time.sleep(0.3)
            
            scroll_to_top = current_scroll_top
    
    def scroll_down_chat(self, step=200):
        scroll_area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        if scroll_area is None:
            print("스크롤 영역을 찾을 수 없습니다.")
            return

        scroll_to_btm = None
        while True:
            current_scroll_top = self.driver.execute_script("return arguments[0].scrollTop;", scroll_area)  
            scroll_height = self.driver.execute_script("return arguments[0].scrollHeight;", scroll_area)    

            if current_scroll_top + scroll_area.size['height'] >= scroll_height:
                print("화면 맨 아래 도착!")
                break
            
            if current_scroll_top == scroll_to_btm:
                print("화면 맨 아래 도착!")
                break
            
            # 테스트 용 ====================================
            print(f"[down] current_scroll_top :{current_scroll_top} + scroll_area.size['height']: {scroll_area.size['height']} >= scroll_height :{scroll_height} ?")
            #  ==========================================
            
            self.driver.execute_script(f"arguments[0].scrollBy(0, {step});", scroll_area)
            time.sleep(0.3)

            scroll_to_btm = current_scroll_top
       
    def click_btn_scroll_to_bottom(self):
        self.scroll_up_chat()
        
        btn_scroll = self.get_element_by_css_selector(SELECTORS["SCROLL_TO_BOTTOM_BUTTON"])
        
        if btn_scroll.is_enabled():
            btn_scroll.click()
            print("맨 아래로 스크롤 버튼 클릭")
            time.sleep(1)

    
    def click_btn_send(self):
        btn_scroll = self.get_element_by_xpath(XPATH["BTN_SEND"])
        
        if btn_scroll.is_enabled():
            btn_scroll.click()
            print("채팅 보내기 성공")
            time.sleep(1)
    
    
    def click_btn_stop(self):
        # 취소 버튼은 hidden 으로 되어있음
        try:
            btn_stop = self.get_element_by_xpath(XPATH["BTN_STOP"], option="visibility")
            if btn_stop.is_displayed():
                btn_stop.click()
                time.sleep(1)
                return True
            return False
        except:
            return False
            
            
    def is_visible_btn_stop(self):
        try:
            btn_stop = self.get_element_by_xpath(XPATH["BTN_STOP"], option="visibility")
            if btn_stop.is_displayed():
                return False  # 채팅 진행 중
            return True       # 채팅 완료
        except:
            # stop 버튼이 아예 없으면 완료로 판단
            return True
    
            
        # 응답이 완료되었는지 확인
    def check_is_chat_complete(self):
        while True:
            if not self.is_visible_btn_stop():
                print("AI응답 완료, 채팅 종료")
                time.sleep(0.5)
                return
            
    def input_chat_data(self, data):
        input_chat = self.get_element_by_css_selector(SELECTORS["TEXTAREA"])
        input_chat.click()
        input_chat.clear()
        time.sleep(1)
        
        # 데이터 입력
        input_chat.send_keys(data)
        self.click_btn_send()

        
        
    