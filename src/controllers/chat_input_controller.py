import time
from selenium.webdriver.common.keys import Keys
from controllers.clipboard_controller import ClipboardController


class ChatInputController:

    @staticmethod
    def send_text(element, text: str):
        element.click()
        element.clear()
        element.send_keys(text)

    @staticmethod
    def paste_text(element, text: str):
        ClipboardController.copy(text)
        element.click()
        time.sleep(0.1)
        ClipboardController.paste(element)
        time.sleep(0.1)

