from utils.headers import *
from pages.base_page import BasePage
from utils.defines import SELECTORS, XPATH, TARGET_URL
from utils.defines import TIMEOUT_MAX

from enums.ui_status import MenuStatus

from controllers.chat_input_controller import ChatInputController
from controllers.clipboard_controller import ClipboardController
from controllers.response_controller import ResponseController
from controllers.scroll_controller import ScrollController



class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  
        self.menu_status = MenuStatus.OPENED
        
    def go_to_main_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])

    # 이거 나중에 위로 빼야 겠다. 
    def click_btn_home_menu(self, button_text: str):
        try:
            buttons = self.get_elements_by_css_selector(SELECTORS["BTNS_HOME_MENU"])

            for btn in buttons:
                if btn.text.strip() == button_text:
                    btn.click()
                    return True  
                
            print(f"[WARN] 버튼 '{button_text}'를 찾지 못함")
            return False
        
        except NoSuchElementException:
            print(f"[ERROR] 버튼 '{button_text}' 요소 자체를 찾을 수 없음")
            return False
        

    def click_on_past_chat(self):
        items = self.get_elements_by_css_selector(SELECTORS["CHAT_LIST_ITEMS"])
        if not items:
            raise Exception("대화 내역이 없습니다.")

        # 인덱스 접근방식 대신, data-item들중 가장 큰 index를 선택하도록. (즉, 가장 밑 대화 클릭)
        latest = max(items, key=lambda x: int(x.get_attribute("data-item-index")))
        latest.click()
        time.sleep(1)

    # Scroll
    def scroll_up_chat(self):
        area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        ScrollController.scroll_up(self.driver, area)

    def scroll_down_chat(self):
        area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        ScrollController.scroll_down(self.driver, area)

    def click_btn_scroll_to_bottom(self, timeout = TIMEOUT_MAX):
        start = time.time()

        while time.time() - start < timeout:
            btn = self.get_element_by_css_selector(SELECTORS["BTN_SCROLL_TO_BOTTOM"])

            if btn and btn.is_enabled():
                try:
                    btn.click()
                    print("맨 밑으로 이동스크롤 클릭")
                    return True
                except Exception:
                    pass

            self.scroll_up_chat()
            time.sleep(0.3)

        raise TimeoutError("스크롤 버튼 안보임")

    # Chat
    def click_send(self):
        btn = self.get_element_by_xpath(XPATH["BTN_SEND"])
        if btn.is_enabled():
            btn.click()

    def input_chat(self, text: str):
        textarea = self.get_element_by_css_selector(SELECTORS["TEXTAREA"])
        ChatInputController.send_text(textarea, text)
        self.click_send()
    
        result = ResponseController.wait_for_resp(
            btn_stop=lambda: self.get_element_by_xpath(XPATH["BTN_STOP"])
        )
        time.sleep(1)
    
    def click_btn_retry(self):
        btns = self.get_elements_by_xpath(XPATH["BTN_RETRY"])
        if not btns:
            raise Exception("다시 생성하기 버튼이 없음.")
        btns[-1].click()

        result = ResponseController.wait_for_resp(
            btn_stop=lambda: self.get_element_by_xpath(XPATH["BTN_STOP"])
        )
        time.sleep(1)

    # Clipboard
    def copy_last_response(self):
        btns = self.get_elements_by_xpath(XPATH["BTN_COPY_RESPONE"])
        if not btns:
            raise Exception("복사 버튼이 없음.")

        btns[-1].click()
        time.sleep(0.5)
        print("복사 완성")
        return ClipboardController.read()
    
    def paste_last_response(self):
        textarea = self.get_element_by_css_selector(SELECTORS["TEXTAREA"])
        ChatInputController.paste_text(textarea, self.copy_last_response())
        time.sleep(0.5)
    
    def reset_chat(self):
        textarea = self.get_element_by_css_selector(SELECTORS["TEXTAREA"])
        ChatInputController.reset_text(textarea)
        time.sleep(0.5)
    
    # 메뉴 
    def sync_menu_status(self):
        try:
            # 메뉴 열기 버튼이 보이면 CLOSED 상태
            btn_open = self.get_element_by_xpath(XPATH["BTN_MENU_OPEN"])
            if btn_open and btn_open.is_displayed():
                self.menu_status = MenuStatus.CLOSED
                return
        except NoSuchElementException:
            pass

        try:
            # 메뉴 닫기 버튼이 보이면 OPENED 상태
            btn_close = self.get_element_by_xpath(XPATH["BTN_MENU_CLOSE"])
            if btn_close and btn_close.is_displayed():
                self.menu_status = MenuStatus.OPENED   
        except NoSuchElementException:
            pass

    # 메뉴
    def toggle_menu(self, btn_element):
        if not btn_element:
            print("버튼 찾기 실패")
            return

        if btn_element.is_enabled():
            btn_element.click()
            time.sleep(0.5)
            
            if self.menu_status == MenuStatus.CLOSED:
                self.menu_status = MenuStatus.OPENED  
            else:
                self.menu_status = MenuStatus.CLOSED
            print(self.menu_status)

    def action_menu_arrow(self):
        if self.menu_status == MenuStatus.CLOSED: 
            btn_arrow = self.get_element_by_xpath(XPATH["BTN_MENU_OPEN"])
        else: 
            btn_arrow = self.get_element_by_xpath(XPATH["BTN_MENU_CLOSE"])
        self.toggle_menu(btn_arrow)

    def action_menu_bar(self):
        btn_bar = self.get_element_by_css_selector(SELECTORS["BTN_MENU_BAR"])
        self.toggle_menu(btn_bar)
    
    