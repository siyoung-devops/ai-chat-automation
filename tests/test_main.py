from utils.headers import *

from pages.model_setting_page import ModelSettingPage

# main 홈화면 테스트만 진행합니다. 

# 사용자가 보낸 메시지 내용 편집
# 사용자가 보낸 메시지 내용 편집 중 취소

# 이름변경' 버튼 동작
# 이름 변경 '취소' 버튼 동작
# 삭제' 버튼 동작


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
  
#     page.click_on_past_chat()
#     page.scroll_up_chat()
#     page.scroll_down_chat()
#     page.click_btn_scroll_to_bottom()
#     time.sleep(1)


# def test_menu_scenario(logged_in_main):
#     page = logged_in_main
#     page.sync_menu_status()
    
#     page.action_menu_arrow()

#     page.action_menu_bar()
#     page.action_menu_bar()

#     page.action_menu_arrow()
    

# def test_model_select(logged_in_main,driver):
#     logged_in_main
    
#     model_page = ModelSettingPage(driver)
#     model_page.open_model_menu()
#     model_page.select_model("GPT-5")
#     model_page.open_model_menu()
#     model_page.select_model("Helpy Pro Agent")


def test_model_setting(logged_in_main, driver):
    logged_in_main
    
    model_page = ModelSettingPage(driver)
    model_page.open_model_menu()
    model_page.go_to_model_setting()
    model_page.toggle_all_models_and_verify()
                
    # 설정창 닫기
    model_page.go_back()

    # 드롭다운 검증
    model_page.compare_active_modes()
    
    