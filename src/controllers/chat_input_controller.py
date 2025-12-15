import time
import platform
from selenium.webdriver.common.keys import Keys
from controllers.clipboard_controller import ClipboardController
from selenium.webdriver.common.keys import Keys

class ChatInputController:

    @staticmethod
    def send_text(element, text: str):
        element.click()
        time.sleep(0.3)
        element.send_keys(text)

    @staticmethod
    def paste_text(element, text: str):
        ClipboardController.copy(text)
        element.click()
        time.sleep(0.3)
        ClipboardController.paste(element)
        time.sleep(0.3)
        
    @staticmethod
    def reset_text(element):
        system = platform.system()
        if system == "Darwin": # 맥용!
            element.send_keys(Keys.COMMAND, "A")
        else:   # 윈도우 용!
            element.send_keys(Keys.CONTROL, "A")
        element.send_keys(Keys.BACK_SPACE)