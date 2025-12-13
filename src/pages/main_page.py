import time
from pages.base_page import BasePage
from utils.defines import SELECTORS, XPATH, TARGET_URL

from controllers.chat_input_controller import ChatInputController
from controllers.clipboard_controller import ClipboardController
from controllers.response_controller import ResponseController
from controllers.scroll_controller import ScrollController

from states.response_state import ResponseState

class MainPage(BasePage):
    def go_to_main_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])

    def click_new_chat(self):
        self.get_element_by_css_selector(SELECTORS["BTN_NEW_CHAT"]).click()
        time.sleep(0.5)

    def click_on_past_chat(self, index):
        items = self.get_elements_by_css_selector(SELECTORS["CHAT_LIST_ITEMS"])
        if not items:
            raise Exception("대화 내역이 없습니다.")
        items[index].click()
        time.sleep(1)

    # Scroll
    def scroll_up_chat(self):
        area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        ScrollController.scroll_up(self.driver, area)

    def scroll_down_chat(self):
        area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        ScrollController.scroll_down(self.driver, area)

    def click_btn_scroll_to_bottom(self, timeout=5):
        start = time.time()

        while time.time() - start < timeout:
            btn = self.get_element_by_css_selector(SELECTORS["SCROLL_TO_BOTTOM_BUTTON"])

            if btn and btn.is_displayed():
                try:
                    btn.click()
                    print("맨 밑으로 이동")
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
        
        # 람다.. 라는게 있었지 = lambda: 표현식, 
        # 아래 형식과 같은 것, 표현하고자 하는 함수를 한줄로 쓰고 싶을때 사용
        # def wait_condition():
        #   return self.get_element_by_xpath(...)
        # wait_for_resp를 즉시 실행하지 않고 함수를 인자로 넘겨서 조건을 만족할때 까지 계속 호출함. 
        result = ResponseController.wait_for_resp(
            lambda: self.get_element_by_xpath(
                XPATH["BTN_STOP"], option="visibility"
            )
        )
        if result == ResponseState.TIMEOUT:
            raise TimeoutError("AI 응답 시간 초과")
    
    def click_btn_retry(self):
        btns = self.get_elements_by_xpath(XPATH["BTN_RETRY"])
        if not btns:
            raise Exception("다시 생성하기 버튼이 없음.")
        btns[-1].click()

        ResponseController.wait_for_resp(
            lambda: self.get_element_by_xpath(
                XPATH["BTN_STOP"], option="visibility"
            )
        )

    # Clipboard
    def copy_last_response(self):
        btns = self.get_elements_by_xpath(XPATH["BTN_COPY_RESPONSE"])
        if not btns:
            raise Exception("복사 버튼이 없음.")

        btns[-1].click()
        time.sleep(0.3)
        return ClipboardController.read()
    
    def paste_last_response(self):
        textarea = self.get_element_by_css_selector(SELECTORS["TEXTAREA"])
        ChatInputController.paste_text(textarea)
        time.sleep(0.3)