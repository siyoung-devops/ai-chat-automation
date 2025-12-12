from utils.headers import *

# PHC-TS01-TC09: Logout 테스트
def test_logout(login_page):
    login_page.go_to_login_page()
    login_page.input_user_data() #테스트 데이터 입력
    login_page.click_login_button()
    login_page.click_account_button()
    login_page.click_logout_button()
    assert login_page.is_logged_out_page(), "로그아웃이 실행되지 않음"

# PHC-TS01-TC010: View Password 테스트
def test_view_password(login_page):
    login_page.go_to_login_page()
    login_page.input_pw() # 테스트 데이터 입력
    assert login_page.is_password_masked(), "비밀번호 마스킹 실패"

    login_page.click_view_password_button()
    assert login_page.is_password_visible(), "비밀번호가 표시 상태(text)로 변경되지 않음"
    
# PHC-TS01-TC011: Forgot password 테스트
def test_forgot_password(login_page):
    login_page.go_to_login_page()
    login_page.click_forgot_password_button()
    assert login_page.is_forgot_password_page(), "비밀번호 찾기 탭으로 이동 실패"
    
# PHC-TS01-TC012: Sign up with different account 테스트
def test_diff_account(login_page):
    login_page.go_to_login_page()


# PHC-TS01-TC013: Remove History 테스트
def test_remove_history(login_page):
    login_page.go_to_login_page()
    login_page.input_id() # 테스트 데이터 입력
    login_page.input_password() # 테스트 데이터 입력
    login_page.logout()
    login_page.click_remove_history_button()
    assert login_page.is_inputs_cleared(), "Remove history 클릭 후 입력값이 초기화되지 않음"