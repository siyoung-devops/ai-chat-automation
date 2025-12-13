from utils.headers import *

from pages.member_page import MemberPage

#메인페이지 접속
def test_go_to_main(logged_in_main):
    page = logged_in_main

#계정관리 접속(새창)
def test_go_to_member(member_page): 
    member_page.go_to_member_page()

#이름, 이메일, 휴대폰 번호, 비밀번호 수정 버튼
def click_first_update_btn(member_page):
    btns = member_page.update_info()  # 항상 새로 찾음
    assert btns, "수정 버튼 없음"
    btns[0].click()

# @pytest.mark.parametrize("value, should_save", [
#     ("   ", False),  # 1: 탭/여러 공백 → 저장 안 돼야 한다
#     (" ", False),    # 2: 스페이스 1개
#     ("\n \r\n", False),  # 3: 개행 포함
#     ("<html><head></head><body>&nbsp;</body></html>", True),  # 4: 코드 형태 (예: 허용)
#     ("ㅤ", True),    # 5: 특수 공백
# ])
def test_update_name_normal(member_page):
    assert member_page.open_name_edit_form()
    assert member_page.member_name("정상이름")
    assert member_page.submit_name()
    
    

# def test_btn_mkt(member_page):
#     member_page.click_to_mkt()
    
# def test_update_lang(member_page):
#     member_page.choose_lan_dropbox()