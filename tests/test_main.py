from utils.headers import *


def test_new_chat(logged_in_main):
    page = logged_in_main
    time.sleep(3)
    print("바로 메인페이지로 레츠기릿")
    
    page.click_new_chat_button()
    

    
    