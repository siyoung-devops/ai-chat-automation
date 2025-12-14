from utils.headers import *

# main 홈화면 테스트만 진행합니다. 
# 메뉴 접기 버튼 기능
# 메뉴 열기 버튼 기능
# 메뉴 '=' 버튼 기능
# 메뉴 '=' 버튼 기능

# 사용자가 보낸 메시지 내용 편집
# 사용자가 보낸 메시지 내용 편집 중 취소

# 이름변경' 버튼 동작
# 이름 변경 '취소' 버튼 동작
# 삭제' 버튼 동작

# 모델 선택
# 선택 all 후, 메인 홈에서 모든 모델 리스트가 나온다 ? 선택 완
# 해제 all 후, 메인 홈에서 기본 모델 리스트밖에 없다 ? 해제 완

############# 진행완 ##############
# 대화 진행
# 새 대화
# 대화 진행
# 다시 보내기
# 복사 붙여넣기 
# 5초 지나면 취소 버튼 클릭 

# 스크롤 진행
# up 
# down
# 맨 아래로 스크롤


# def test_conversation_text(logged_in_main, fm):
#     page = logged_in_main
#     page.click_btn_home_menu("새 대화")
#     ai_input_lst = fm.read_json_file("ai_text_data.json")["inputs"]
    
#     for item in ai_input_lst:
#         if item["type"] != "text":
#             continue
        
#         page.input_chat(item["content"])
        
#     page.click_btn_retry()
#     page.copy_last_response()
#     page.paste_last_response()
    

# def test_scroll(logged_in_main):
#     page = logged_in_main
#     time.sleep(0.5)
  
#     page.click_on_past_chat(index = 0)
#     page.scroll_up_chat()
#     page.scroll_down_chat()
#     page.click_btn_scroll_to_bottom()
#     time.sleep(1)


def test_menu_scenario(logged_in_main):
    page = logged_in_main
    page.sync_menu_status()
    
    page.action_menu_arrow()

    page.action_menu_bar()
    page.action_menu_bar()

    page.action_menu_arrow()
    
# def test_select_model(logged_in_main):
#     page = logged_in_main
#     time.sleep(0.5)
    
    