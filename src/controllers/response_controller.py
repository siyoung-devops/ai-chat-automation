import time

from states.response_state import ResponseState
from enums.ai_response import AIresponse

class ResponseController:
    
    @staticmethod
    def until(condition, timeout=15):
        start = time.time()

        # 특정 상황이 아니라면 15초까지 기다림.
        while time.time() - start < timeout:
            try:
                if condition():
                    return True
            except:
                pass

            time.sleep(0.3)
        return False


    @staticmethod
    def wait_for_resp(get_stop_btn, timeout=15, stop_time=7):
        state = ResponseState(get_stop_btn, stop_time)

        finished = ResponseController.until(
            condition=state.check,  # 위에 until 함수의 컨디션 == state의 check자체를 넘김
            timeout=timeout         # timeout(15초) 동안 함수 계속 호출, state.check()가 true되면 바로 멈춤. 
        )

        if not finished:
            return AIresponse.TIMEOUT

        return state.result
    
    
    # def wait_for_resp(get_stop_btn, timeout=15, stop_time=7):
    #     start = time.time()
    #     stop_clicked = False

    #     while time.time() - start < timeout:
    #         btn = get_stop_btn()

    #         if not btn or not btn.is_displayed():
    #             return AIresponse.COMPLETED

    #         if not stop_clicked and time.time() - start >= stop_time:
    #             btn.click()
    #             stop_clicked = True
    #             return AIresponse.CANCELED

    #         time.sleep(0.3)

    #     return AIresponse.TIMEOUT