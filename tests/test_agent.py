from utils.headers import *
from enums.ui_status import AIresponse

# PHC-TS06-TC001
# def test_search_agent_list(logged_in_agent):
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.search_input("project")
#     result = agent_page.search_result()
    
#     assert "project" in result.text.strip(), "PHC-TS06-TC001 : Test Fail"
#     print("PHC-TS06-TC001 : Test Success")
    
# # PHC-TS06-TC002
# def test_search_agent_fail(logged_in_agent) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.search_input("마라탕")
#     result = agent_page.search_no_result()
    
#     assert result, "PHC-TS06-TC002 : Test Fail"
#     print("PHC-TS06-TC002 : Test Success")
   
# # PHC-TS06-TC003
# def test_agent_talk_card(logged_in_agent) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.talk_with_agent_screen()
#     element_text = agent_page.agent_talk_card_text().text.strip()
#     agent_page.agent_talk_card_click()
#     agent_page.scroll_up_chat()
#     my_text = agent_page.check_my_talk_input().text.strip()
    
#     assert element_text == my_text, "PHC-TS06-TC003 : Test Fail"
#     print("PHC-TS06-TC003 : Test Success")
    
# # PHC-TS06-TC004

# # PHC-TS06-TC005   
# def test_agent_talk_response_stop(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.talk_with_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     question = data["inputs"][0]["content"]
#     result = agent_page.input_chat(question)
    
#     assert result == AIresponse.STOPPED, "PHC-TS06-TC005 : Test Fail"
#     print("PHC-TS06-TC005 : Test Success")
    
# PHC-TS06-TC028
# def test_agent_setting_for_me(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     name = data["setting_inputs"][0]["content"]
#     intro = data["setting_inputs"][1]["content"]
#     rule = data["setting_inputs"][2]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input(name)
#     agent_page.setting_intro_input(intro)
#     agent_page.setting_rule_input(rule)
#     agent_page.setting_card_input(card)
#     check = agent_page.make_agent_for_me().text.strip()
    
#     assert "나만보기" or "Private" in check, "PHC-TS06-TC028 : Test Fail"
#     print("PHC-TS06-TC028 : Test Success")
    
# # PHC-TS06-TC029
# def test_agent_setting_for_agency(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     name = data["setting_inputs"][0]["content"]
#     intro = data["setting_inputs"][1]["content"]
#     rule = data["setting_inputs"][2]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input(name)
#     agent_page.setting_intro_input(intro)
#     agent_page.setting_rule_input(rule)
#     agent_page.setting_card_input(card)
#     check = agent_page.make_agent_for_agency().text.strip()
    
#     assert "기관 공개" or "Organization" in check, "PHC-TS06-TC029 : Test Fail"
#     print("PHC-TS06-TC029 : Test Success")

# PHC-TS06-TC030  
# def test_agent_setting_no_name(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     intro = data["setting_inputs"][1]["content"]
#     rule = data["setting_inputs"][2]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input("")
#     agent_page.setting_intro_input(intro)
#     agent_page.setting_rule_input(rule)
#     agent_page.setting_card_input(card)
#     btn = agent_page.check_btn_disabled()
#     error = agent_page.error_message().text.strip()
    
#     assert btn.get_attribute("disabled") is not None, "PHC-TS06-TC030 : Test Fail"
#     assert "이름" or "Name" in error, "PHC-TS06-TC030 : Test Fail"
#     print("PHC-TS06-TC030 : Test Success")

# PHC-TS06-TC031 
# def test_agent_setting_long_name(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     name = data["over_inputs"][0]["content"]
#     intro = data["setting_inputs"][1]["content"]
#     rule = data["setting_inputs"][2]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input(name)
#     agent_page.setting_intro_input(intro)
#     agent_page.setting_rule_input(rule)
#     agent_page.setting_card_input(card)
#     btn = agent_page.check_btn_disabled()
#     error = agent_page.error_message().text.strip()
    
#     assert btn.get_attribute("disabled") is not None, "PHC-TS06-TC031 : Test Fail"
#     assert "이름" or "Name" in error, "PHC-TS06-TC031 : Test Fail"
#     print("PHC-TS06-TC031 : Test Success")
    
# PHC-TS06-TC032 
# def test_agent_setting_no_intro(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     name = data["setting_inputs"][0]["content"]
#     rule = data["setting_inputs"][2]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input(name)
#     agent_page.setting_intro_input("")
#     agent_page.setting_rule_input(rule)
#     agent_page.setting_card_input(card)
#     time.sleep(3)
#     btn = agent_page.check_btn_disabled()
    
#     assert btn.get_attribute("disabled") is None, "PHC-TS06-TC032 : Test Fail"
#     print("PHC-TS06-TC032 : Test Success")
    
# PHC-TS06-TC033
# def test_agent_setting_long_intro(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     name = data["setting_inputs"][0]["content"]
#     intro = data["over_inputs"][1]["content"]
#     rule = data["setting_inputs"][2]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input(name)
#     agent_page.setting_intro_input(intro)
#     agent_page.setting_rule_input(rule)
#     agent_page.setting_card_input(card)
#     btn = agent_page.check_btn_disabled()
#     error = agent_page.error_message().text.strip()
    
#     assert btn.get_attribute("disabled") is not None, "PHC-TS06-TC033 : Test Fail"
#     assert "한줄" or "Description" in error, "PHC-TS06-TC033 : Test Fail"
#     print("PHC-TS06-TC033 : Test Success")
    
# PHC-TS06-TC034  
# def test_agent_setting_no_rule(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     name = data["setting_inputs"][0]["content"]
#     intro = data["setting_inputs"][1]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input(name)
#     agent_page.setting_intro_input(intro)
#     agent_page.setting_rule_input("")
#     agent_page.setting_card_input(card)
#     btn = agent_page.check_btn_disabled()
#     error = agent_page.error_message().text.strip()
    
#     assert btn.get_attribute("disabled") is not None, "PHC-TS06-TC034 : Test Fail"
#     assert "규칙" or "prompt" in error, "PHC-TS06-TC034 : Test Fail"
#     print("PHC-TS06-TC034 : Test Success")
    
# PHC-TS06-TC035  
# def test_agent_setting_long_rule(logged_in_agent, fm) :
#     agent_page = logged_in_agent
#     agent_page.go_to_agent_page()
#     agent_page.make_agent_screen()
    
#     data = fm.read_json_file("agent_text_data.json")
#     name = data["setting_inputs"][0]["content"]
#     intro = data["setting_inputs"][1]["content"]
#     rule = data["over_inputs"][2]["content"]
#     card = data["setting_inputs"][3]["content"]
#     agent_page.setting_name_input(name)
#     agent_page.setting_intro_input(intro)
#     agent_page.setting_rule_input(rule)
#     agent_page.setting_card_input(card)
#     time.sleep(3)
#     btn = agent_page.check_btn_disabled()
    
#     assert btn.get_attribute("disabled") is not None, "PHC-TS06-TC035 : Test Fail"
#     print("PHC-TS06-TC035 : Test Success")