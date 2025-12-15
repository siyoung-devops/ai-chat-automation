from utils.headers import *

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH

class AgentPage(BasePage) :
        
    def go_to_agent_page(self):
        menu_btn = self.get_element_by_xpath(XPATH["AGENT_MENU_BTN"])
        menu_btn.click()
        self.get_element_by_xpath(XPATH["MY_AGENT_BTN"])
        
    def search_input(self, agents) :
        search = self.get_element_by_xpath(XPATH["AGENT_SEARCH"])
        search.click()
        search.clear()
        search.send_keys(agents)
        
    def search_result(self) :
        result = self.get_element_by_xpath(XPATH["AGENT_SEARCH_RESULT"])
        return result