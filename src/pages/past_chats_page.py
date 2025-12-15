from utils.headers import *
from utils.defines import XPATH, ID, DEFAULT_MODEL

from enums.ui_status import MenuStatus

from pages.base_page import BasePage

class PastChatsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.past_chats = []
        
    
    def get_all_past_chats(self):
        pass    
    