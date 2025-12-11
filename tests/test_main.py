from utils.headers import *


def test_main_chat(logged_in_main):
    page = logged_in_main
    time.sleep(5)
  
    # 1. 기존 대화 선택 = PHC-TS03-TC001
    page.click_on_past_chat(0)
    
    # 2. 스크롤 이동 테스트 
    page.scroll_up_chat()
    
    # 3. 스크롤 이동 테스트 
    page.scroll_down_chat()
    
    # 4.  최근 메시지로 스크롤 정상 이동 = PHC-TS03-TC026 
    page.click_btn_scroll_to_bottom()
    
    # 5. 새 대화 = PHC-TS03-TC014
    page.click_new_chat_button()
    time.sleep(2)

# def test_conversation(main_page):
#     #main_page.go_to_main_page()
#     pass
    
    
    
    