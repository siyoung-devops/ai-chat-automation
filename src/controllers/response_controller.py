import time
from states.response_state import ResponseState
from enums.ai_response import AIresponse

from utils.defines import TIMEOUT_MAX, STOPPED_MAX

class ResponseController:

    @staticmethod
    def until(condition, timeout = TIMEOUT_MAX):
        start = time.monotonic()
        while time.monotonic() - start < timeout:
            try:
                if condition():
                    return True
            except:
                pass
            time.sleep(0.3)
        return False

    @staticmethod
    def wait_for_resp(btn_stop, stop_time = STOPPED_MAX, timeout = TIMEOUT_MAX):
        state = ResponseState(
            resp_btn_stop=btn_stop,
            stop_time=stop_time,
            resp_timeout=timeout
        )

        finished = ResponseController.until(
            condition=state.check,
            timeout=timeout 
        )

        return state.result if finished else AIresponse.TIMEOUT