from utils.headers import *


def test_conversation_text(logged_in_main, fm):
    page = logged_in_main
    page.click_new_chat()
    ai_input_lst = fm.read_json_file("ai_text_data.json")["inputs"]
    
    for item in ai_input_lst:
        if item["type"] != "text":
            continue
        page.input_chat(item["content"])
        
    page.click_btn_retry()
    page.copy_last_response()
    page.paste_last_response()
    

def test_scroll(logged_in_main):
    page = logged_in_main
    time.sleep(1)
  
    page.click_on_past_chat(index = 0)
    page.scroll_up_chat()
    page.scroll_down_chat()
    page.click_btn_scroll_to_bottom()
    time.sleep(1)

