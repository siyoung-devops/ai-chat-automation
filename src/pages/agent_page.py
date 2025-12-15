from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH
from utils.defines import TIMEOUT_MAX

from enums.ui_status import MenuStatus

from controllers.chat_input_controller import ChatInputController
from controllers.clipboard_controller import ClipboardController
from controllers.response_controller import ResponseController
from controllers.scroll_controller import ScrollController

class AgentPage(BasePage) :
        
    def go_to_agent_page(self):
        menu_btn = self.get_element_by_xpath(XPATH["AGENT_MENU_BTN"])
        menu_btn.click()
        self.get_element_by_xpath(
            XPATH["MY_AGENT_BTN"],
            option="clickable",
            timeout=10
        )
        
    def search_input(self, agents) :
        search = self.get_element_by_xpath(
            XPATH["AGENT_SEARCH"],
            option="visibility",
            timeout=10
        )
        search.click()
        search.clear()
        search.send_keys(agents)
        
    def search_result(self) :
        result = self.get_element_by_xpath(XPATH["AGENT_SEARCH_RESULT"])
        return result
    
    def search_no_result(self) :
        result = self.get_element_by_xpath(XPATH["AGENT_SEARCH_NO_RESULT"])
        return result
    
    def talk_with_agent_screen(self) :
        element = self.get_element_by_xpath(XPATH["AGENT_TALK"])
        element.click()
        
    def agent_talk_card_text(self):
        element_text = self.get_element_by_xpath(XPATH["AGENT_TALK_CARD_TEXT"])
        return element_text
        
    def agent_talk_card_click(self) :
        element = self.get_element_by_xpath(XPATH["AGENT_TALK_CARD"])
        element.click()
        
    def make_agent_screen(self) :
        element = self.get_element_by_xpath(XPATH["GO_MAKE_AGENT"])
        element.click()
        
    def setting_name_input(self, text: str) :
        namearea = self.get_element_by_xpath(XPATH["NAME_SETT"])
        ChatInputController.send_text(namearea, text)
        
    def setting_intro_input(self, text: str) :
        introarea = self.get_element_by_xpath(XPATH["INTRO_SETT"])
        ChatInputController.send_text(introarea, text)
        
    def setting_rule_input(self, text: str) :
        rulearea = self.get_element_by_xpath(XPATH["RULE_SETT"])
        ChatInputController.send_text(rulearea, text)
        
    def setting_card_input(self, text: str) :
        cardarea = self.get_element_by_xpath(XPATH["CARD_SETT"])
        ChatInputController.send_text(cardarea, text)
        
    def go_to_make_agent(self) :
        element = self.get_element_by_xpath(XPATH["BTN_AGENT_MAKE"])
        element.click()
        
    def make_agent_for_me(self) :
        element = self.get_element_by_xpath(XPATH["BTN_AGENT_MAKE"])
        element.click()
        me = self.get_element_by_xpath(XPATH["BTN_FOR_ME"])
        me.click()
        btn = self.get_element_by_xpath(XPATH["BTN_AGENT_PUBLISH"])
        btn.click()
        time.sleep(3)
        check = self.get_element_by_xpath(XPATH["CHECK_MAKE"])
        return check
        
    def make_agent_for_agency(self) :
        element = self.get_element_by_xpath(XPATH["BTN_AGENT_MAKE"])
        element.click()
        agency = self.get_element_by_xpath(XPATH["BTN_FOR_AGENCY"])
        agency.click()
        btn = self.get_element_by_xpath(XPATH["BTN_AGENT_PUBLISH"])
        btn.click()
        check = self.get_element_by_xpath(XPATH["CHECK_MAKE"])
        return check
        
    def check_btn_disabled(self) :
        element = self.get_element_by_xpath(XPATH["BTN_AGENT_MAKE"])
        return element
    
    def error_message(self) :
        element = self.get_element_by_xpath(XPATH["ERROR_MSG"])
        return element
        
    # Agent Talk Scroll
    def scroll_up_chat(self):
        area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        ScrollController.scroll_up(self.driver, area)

    def scroll_down_chat(self):
        area = self.get_element_by_xpath(XPATH["SCROLL_MAIN_CHAT"])
        ScrollController.scroll_down(self.driver, area)
        
    def click_btn_scroll_to_bottom(self, timeout = TIMEOUT_MAX, wait_time=3):
        start = time.time()

        while time.time() - start < timeout:
            btn = self.get_element_by_css_selector(SELECTORS["SCROLL_TO_BOTTOM_BUTTON"])

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
    
    def check_my_talk_input(self) :
        text = self.get_element_by_xpath(XPATH["AGENT_INPUT_TEXT"])
        return text
    
    # Agent Chat
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
        return result
        
    