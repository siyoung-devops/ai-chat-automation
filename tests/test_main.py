from utils.headers import *


def test_conversation_text(logged_in_main, fm):
    page = logged_in_main

    # 5. 새 대화 = PHC-TS03-TC014
    page.click_new_chat()

    # 6. AI 응답 테스트 = PHC-TS03-TC004
    ai_input_lst = fm.read_json_file("ai_text_data.json")["inputs"]

    for item in ai_input_lst:
        if item["type"] != "text":
            continue
        
        page.input_chat(item["content"])

    # 9. AI 응답 재생성 = PHC-TS03-TC006
    page.click_btn_retry()

    # 10. 복사 + 붙여넣기 검증
    copied_text = page.copy_last_response()
    assert copied_text != ""
    
    page.paste_last_response()
    

def test_scroll(logged_in_main):
    page = logged_in_main
    time.sleep(5)
  
    # 1. 기존 대화 선택 = PHC-TS03-TC001
    page.click_on_past_chat(index = 2)
    
    # 2. 스크롤 이동 테스트 
    page.scroll_up_chat()
    page.scroll_down_chat()
    
    # 3.  최근 메시지로 스크롤 정상 이동 = PHC-TS03-TC026 
    page.click_btn_scroll_to_bottom()


