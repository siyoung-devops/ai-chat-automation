import pyperclip
import platform
from selenium.webdriver.common.keys import Keys


class ClipboardController:

    @staticmethod
    def copy(text: str):
        pyperclip.copy(text)

    @staticmethod
    def paste(element):
        system = platform.system()
        if system == "Darwin": # 맥용!
            element.send_keys(Keys.COMMAND, "V")
        else:   # 윈도우 용!
            element.send_keys(Keys.CONTROL, "V")

    @staticmethod
    def read():
        try:
            return pyperclip.paste().strip()
        except Exception:
            return ""