from utils.headers import *


def test_new_chat(logged_in_main):
    page = logged_in_main
    time.sleep(2)
  
    page.click_on_past_chat(0)
    
    
    #page.click_new_chat_button()
    time.sleep(2)

   