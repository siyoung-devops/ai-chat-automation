import time
import platform
from selenium.webdriver.common.keys import Keys
from controllers.clipboard_controller import ClipboardController
from selenium.webdriver.support.ui import WebDriverWait

class ChatInputController:

    @staticmethod
    def send_text(element, text: str):
        element.click()
        element.send_keys(text)

    @staticmethod
    def paste_text(element, text: str):
        ClipboardController.copy(text)
        element.click()
        ClipboardController.paste(element)
        
    @staticmethod
    def reset_text(element):
        element.click()
        system = platform.system()
        modifier = Keys.COMMAND if system == "Darwin" else Keys.CONTROL
        element.send_keys(modifier, "a")
        element.send_keys(Keys.BACK_SPACE)

        
