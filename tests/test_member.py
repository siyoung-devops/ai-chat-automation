from utils.headers import *

from pages.member_page import MemberPage
#메인페이지 접속
def test_go_to_main(logged_in_main):
    page = logged_in_main
#계정관리 접속(새창)
def test_go_to_member(member_page): 
    member_page.go_to_member_page()
#PHC-TS05-TC001
# def test_update_name_normal(member_page,test_cases):
#     data = test_cases["normal"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# def test_update_name_tab_blank(member_page,test_cases):
#     data = test_cases["spacebar_blank"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert not member_page.submit_name()

# def test_update_name_spacebar_blank(member_page,test_cases):
#     data = test_cases["tab_blank"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert not member_page.submit_name()

# def test_update_name_newline(member_page,test_cases):
#     data = test_cases["newline"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert not member_page.submit_name()

# def test_update_name_code_html(member_page,test_cases):
#     data = test_cases["code_html"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# def test_update_name_character_blank(member_page,test_cases):
#     data = test_cases["character_blank"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()
    
# #PHC-TS05-TC002
# def test_update_name_maximum(member_page,test_cases):
#     data = test_cases["maximum_name"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# #PHC-TS05-TC003
# def test_update_name_lang_thai_true(member_page,test_cases):
#     data = test_cases["thai_name_t"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# def test_update_name_lang_thai_false(member_page,test_cases):
#     data = test_cases["thai_name_f"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# def test_update_name_lang_jpn_true(member_page,test_cases):
#     data = test_cases["jpn_name_t"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# def test_update_name_lang_jpn_false(member_page,test_cases):
#     data = test_cases["jpn_name_f"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# def test_update_name_lang_eng_true(member_page,test_cases):
#     data = test_cases["eng_name_t"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# def test_update_name_lang_eng_false(member_page,test_cases):
#     data = test_cases["eng_name_f"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_name_edit_form()
#     assert member_page.member_name(data["value"])
#     assert member_page.submit_name()

# #PHC-TS05-TC004
# def test_update_email_blank(member_page,test_cases):
#     data = test_cases["email_blank_tab"] 
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_email_edit_form()
#     assert member_page.member_email(data["value"])
#     assert not member_page.certification_email()

# def test_update_email_duplication(member_page,test_cases):
#     data = test_cases["email_duplication"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_email_edit_form()
#     assert member_page.member_email(data["value"])
#     assert not member_page.certification_email()

# def test_update_email_character(member_page,test_cases):
#     data = test_cases["email_character"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_email_edit_form()
#     assert member_page.member_email(data["value"])
#     assert not member_page.certification_email()

# #PHC-TS05-TC006
# def test_update_mobile(member_page,test_cases):
#     data = test_cases["mobile"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_mobile_edit_form()
#     assert member_page.member_mobile(data["value"])
#     assert member_page.certification_mobile()

# #PHC-TS05-TC008
# def test_update_fail_pwd(member_page,test_cases):
#     data = test_cases["valid_pwd"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_pwd_edit_form()
#     assert member_page.member_fail_pwd(data["value"])
#     assert not member_page.change_fail_pwd()
# #PHC-TS05-TC009
# def test_update_fail_pwd(member_page,test_cases):
#     data = test_cases["exist_pwd"]
#     data_new = test_cases["valid_pwd"]
#     assert member_page.refresh_member_account_page()
#     assert member_page.open_pwd_edit_form()
#     assert member_page.member_success_pwd(data["value"],data_new["value"])
#     assert member_page.change_success_pwd()
#PHC-TS05-TC010
def test_update_lang_(member_page, test_cases):
    assert member_page.refresh