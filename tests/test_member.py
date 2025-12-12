from utils.headers import *

from pages.member_page import MemberPage

#메인페이지 접속
def test_go_to_main(logged_in_main):
    page = logged_in_main

#계정관리 접속(새창)
def test_go_to_member(member_page): 
    member_page.go_to_member_page()

#이름, 이메일, 휴대폰 번호, 비밀번호 수정 버튼
# def click_first_update_btn(member_page):
#     btns = member_page.update_info()  # 항상 새로 찾음
#     assert btns, "수정 버튼 없음"
#     btns[0].click()
def test_debug_name_button(member_page):
    assert member_page.go_to_member_page()
    idx = member_page.debug_find_name_edit_button()
    assert idx is not None

# @pytest.mark.parametrize("value, should_save", [
#     ("   ", False),  # 1: 탭/여러 공백 → 저장 안 돼야 한다
#     (" ", False),    # 2: 스페이스 1개
#     ("\n \r\n", False),  # 3: 개행 포함
#     ("<html><head></head><body>&nbsp;</body></html>", True),  # 4: 코드 형태 (예: 허용)
#     ("ㅤ", True),    # 5: 특수 공백
# ])
# def test_update_name_cases(member_page, value, should_save):
#     # 1) 항상 폼 새로 열기
#     assert member_page.open_name_edit_form()

#     # 2) 값 입력
#     assert member_page.member_name(value)

#     # 3) 저장 시도
#     result = member_page.submit_name()

#     # 4) 기대 결과 검증
#     if should_save:
#         assert result, f"'{value}' 는 저장되어야 하는 값인데 실패함"
#     else:
#         assert not result, f"'{value}' 는 저장되면 안 되는 값인데 저장됨"

# def test_btn_mkt(member_page):
#     member_page.click_to_mkt()
    
# def test_update_lang(member_page):
#     member_page.choose_lan_dropbox()