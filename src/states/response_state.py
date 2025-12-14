import time
from enums.ai_response import AIresponse

from utils.defines import TIMEOUT_MAX, STOPPED_MAX

class ResponseState:
    def __init__(self, resp_btn_stop, stop_time=STOPPED_MAX, resp_timeout=TIMEOUT_MAX):
        self.resp_btn_stop = resp_btn_stop  # 함수형, lambda: WebElement
        self.stop_time = stop_time          # STOP 클릭 시점
        self.timeout = resp_timeout         # 최대 대기 시간

        self.start = time.monotonic()
        self.stop_clicked = False
        self.result = None

    def check(self):
        passed = time.monotonic() - self.start

        if passed >= self.timeout:
            self.result = AIresponse.TIMEOUT
            print("타임 아웃")
            return True

        if passed >= self.stop_time and not self.stop_clicked:
            try:
                btn = self.resp_btn_stop()
                if btn and btn.is_displayed():
                    btn.click()
                    self.stop_clicked = True
                    self.result = AIresponse.STOPPED
                    print("취소 버튼 클릭")
                    return True
            except:
                pass

        return False