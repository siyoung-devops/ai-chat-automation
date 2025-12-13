import pyperclip
import platform

from selenium.webdriver.common.keys import Keys

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
        btn_send = self.get_element_by_xpath(XPATH["BTN_SEND"])
        if btn_send.is_enabled():
            btn_send.click()
            time.sleep(0.5)
            print("채팅 보내기 성공")


    # 취소, 다시보내기-hidden 설정되어있음..
    def click_btn_stop(self):
        btn_stop = self.get_element_by_xpath(XPATH["BTN_STOP"], option="visibility")
        if btn_stop.is_displayed():
            btn_stop.click()
            time.sleep(0.5)
            print("채팅 stop 성공")

    def click_btn_retry(self):
        btns_retry = self.get_elements_by_xpath(XPATH["BTN_RETRY"])
        if not btns_retry:
            print("다시 생성하기 버튼 없음")
            return

        btns_retry[-1].click()
        print("다시 생성하기 버튼 클릭됨")

        # 응답 기다리기
        if self.wait_for_response(timeout=15, stop_time=7):
            print("다시 생성 완료")
        else:
            print("응답 시간 초과")
        time.sleep(0.5)

    # 1.    복사
    def click_btn_copy(self):
        btns_copy = self.get_elements_by_xpath(XPATH["BTN_COPY_RESPONSE"])
        if not btns_copy:
            print("복사하기 버튼 없음")
            return
        
        btns_copy[-1].click()
        print("복사 버튼 클릭됨")
        time.sleep(0.5)
    
    # 2.    복사된 클립보드 읽기
    def get_clipboard_text(self):
        try:
            text = pyperclip.paste()
            return text.strip()
        except:
            print("클립보드 읽기 실패")
            return ""
    
    # 3.    붙여넣기로 테스트 
    def copy_and_past(self):
        self.click_btn_copy()
        
        content = self.get_clipboard_text()
        print(content)
        
        textarea = self.get_element_by_css_selector(SELECTORS["TEXTAREA"])
        textarea.click()
        time.sleep(0.1)

        # mac 용
        textarea.send_keys(Keys.COMMAND, "V")
        time.sleep(0.3)
        
        self.click_btn_send()
        time.sleep(0.3)
        
          # 응답 기다리기
        if self.wait_for_response(timeout=15, stop_time=7):
            print("다시 생성 완료")
        else:
            print("응답 시간 초과")
        time.sleep(0.5)
        
    
    # ====== 어떻게하면 좋을까 ================================        
    def time_passed(self, start_time, seconds):
        return time.time() - start_time >= seconds
    
    def wait_for_response(self, timeout=15, stop_time=7):
        start_time = time.time()
        stop_clicked = False

        while True:
            if self.time_passed(start_time, timeout):
                print(f"응답 시간 초과 : ({timeout}초)")
                return False
            try:
                btn_stop = self.get_element_by_xpath(XPATH["BTN_STOP"], option="visibility")

                # stop 버튼이 보이면
                if btn_stop and btn_stop.is_displayed():

                    # stop_time 초 지나면 stop 클릭
                    if self.time_passed(start_time, stop_time) and not stop_clicked:
                        btn_stop.click()
                        stop_clicked = True
                        print(f"{stop_time}초 경과 , stop 클릭")
                        return True
                else:
                    # stop 버튼이 사라짐 ? 응답 종료된 것으로 판단
                    print("응답 완료")
                    return True

            except Exception:
                pass
            time.sleep(0.3)
            
    def input_chat_data(self, data, timeout=15, stop_time=7):
        textarea = self.get_element_by_css_selector(SELECTORS["TEXTAREA"])
        textarea.click()
        textarea.send_keys(data)
        time.sleep(1)
        
        self.click_btn_send()
        time.sleep(0.3)

        self.wait_for_response(timeout, stop_time)
    # ===================================================        