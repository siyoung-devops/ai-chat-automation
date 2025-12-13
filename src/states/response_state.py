import time
from enums.ai_response import AIresponse


class ResponseState:
    def __init__(self, get_stop_btn, stop_time):
        self.get_stop_btn = get_stop_btn
        self.stop_time = stop_time
        self.start = time.time()
        self.stop_clicked = False
        self.result = None

    def check(self):
        btn = self.get_stop_btn()

        # 일단은 stop 버튼이 사라지면 완료로 판단. 
        if not btn or not btn.is_displayed():
            self.result = AIresponse.COMPLETED
            return True

        # stop_time을 경과하면 취소 버튼을 클릭하게 함. 
        if time.time() - self.start > self.stop_time and not self.stop_clicked:
            btn.click()
            self.stop_clicked = True
            self.result = AIresponse.STOPPED
            return True

        return False