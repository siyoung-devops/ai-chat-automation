from utils.headers import *


def test_main_chat(logged_in_main):
    page = logged_in_main
    time.sleep(5)
  
    # 메뉴 탭 열기 접기 추가 
  
    # 1. 기존 대화 선택 = PHC-TS03-TC001
    page.click_on_past_chat(0)
    
    # 2. 스크롤 이동 테스트 
    page.scroll_up_chat()
    
    # 3. 스크롤 이동 테스트 
    page.scroll_down_chat()
    
    # 4.  최근 메시지로 스크롤 정상 이동 = PHC-TS03-TC026 
    page.click_btn_scroll_to_bottom()
    time.sleep(0.5)


# 대화 테스트 
def test_conversation(logged_in_main, fm):
    page = logged_in_main
    
    # 5. 새 대화 = PHC-TS03-TC014
    page.click_new_chat_button()
    
    # 6. AI 응답 테스트 PHC-TS03-TC004
    ai_dict = fm.read_json_file("ai_text_data.json")
    ai_input_lst = ai_dict["inputs"]
    
    for idx, item in enumerate(ai_input_lst):
        if item["type"] == "text":
            page.input_chat_data(item["content"])
            time.sleep(1.5)
            
            # 추후 5초 이상 응답완료 안됐을때로 변경예정
            if idx == 2 and not page.check_is_chat_complete():
                # 7. AI 응답 취소 - PHC-TS03-TC005, 
                page.click_btn_stop()
                time.sleep(1)

    
    # 8. AI 응답 재생성 - PHC-TS03-TC006
    
    
    # 9. 