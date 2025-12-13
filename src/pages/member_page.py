from utils.headers import *
from utils.context import LoginContext
from utils.browser_utils import BrowserUtils

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH

class MemberPage(BasePage):
    #로그인 > 메인 페이지 이동
    def go_to_main_page(self):
        self.go_to_page(TARGET_URL["MAIN_URL"])
        time.sleep(4) 

    #우측 사람 이미지 > 계정관리 순차 클릭 > 새 창 이동
    def go_to_member_page(self):
        modal_btn = self.get_element_by_css_selector(SELECTORS["MEMBER_MODAL"])
        modal_btn.click()
        time.sleep(4)
        member_btn = self.get_element_by_xpath(XPATH["BTN_MEMBER"])
        self.driver.execute_script("arguments[0].click();", member_btn)
        time.sleep(4)
        
        self.ensure_account_window()
        return True
    
    #계정 페이지 새로고침
    def refresh_member_account_page(self):
        if "accounts.elice.io/members/account" not in self.driver.current_url:
            if not self.go_to_member_page():
                return False
        self.driver.refresh()
        time.sleep(3)
        return True

    #이름 관련 테스트 케이스를 위한 메서드
    def open_name_edit_form(self, timeout=5):
        print("open_name_edit_form 시작")

        # 0) '이름' 행 스크롤 위치 맞추기
        name_row = self.get_element(
            By.XPATH,
            XPATH["NAME_ROW"],
            option="presence",
            timeout=timeout,
        )
        if not name_row:
            print(" '이름' 행을 찾지 못함 (NAME_ROW)")
            return False

        self.driver.execute_script("""
            const rect = arguments[0].getBoundingClientRect();
            const y = rect.top + window.scrollY - 120;
            window.scrollTo({top: y, behavior: 'instant'});
        """, name_row)
        time.sleep(0.3)

        # 1) '이름' 수정 버튼 찾기
        edit_btn = self.get_element(
            By.XPATH,
            XPATH["NAME_EDIT_BTN"],
            option="visibility",
            timeout=timeout,
        )
        if not edit_btn:
            print("'이름' 수정 버튼 못 찾음 (NAME_EDIT_BTN)")
            return False

        print("'이름' 수정 버튼 찾음, 클릭 시도")

        # 스크롤 + JS 클릭 (debug_find_name_edit_button과 동일 패턴)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_btn)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", edit_btn)
        time.sleep(0.5)

        # 2) fullname 입력 필드 대기
        input_name = self.get_element_by_name(NAME["INPUT_NAME"], option="visibility", timeout=timeout)
        if not input_name:
            print("이름 입력란 안 나타남 (폼 안 열림)")
            return False

        print("이름 수정 폼 열림")
        return True


    def member_name(self, name):
        input_name = self.get_element_by_name(NAME["INPUT_NAME"], option="visibility", timeout=3)
        if not input_name:
            print("이름 입력란 못 찾음")
            return False

        self.driver.execute_script("""
            const rect = arguments[0].getBoundingClientRect();
            const y = rect.top + window.scrollY - 100;
            window.scrollTo({top: y, behavior: 'instant'});
        """, input_name)
        time.sleep(0.3)

        try:
            input_name.click()
        except Exception as e:
            print(f"input 클릭 실패: {e}")
            self.driver.execute_script("arguments[0].focus();", input_name)

        self.driver.execute_script("arguments[0].value = '';", input_name)
        input_name.send_keys(name)

        time.sleep(0.5)
        print(f"테스트 내용 입력 완료: {repr(name)}")
        return True


    def submit_name(self):
        """저장 버튼 JS 클릭 + '이름' 행으로 스크롤 복귀 + enabled 상태로 성공/실패 판단."""
        xpath = XPATH["SUBMIT_NAME"] 

        submit_btn = self.get_element(By.XPATH, xpath, option="visibility", timeout=3)
        if not submit_btn:
            print(" 저장 버튼 없음 (DOM에 없음)")
            return False

        #저장 버튼 활성화 여부 먼저 확인
        if not submit_btn.is_enabled():
            print("저장 버튼 비활성화 상태 (저장 불가)")
            return False

        try:
            # 위치 맞추기
            self.driver.execute_script("""
                const rect = arguments[0].getBoundingClientRect();
                const y = rect.top + window.scrollY - 100;
                window.scrollTo({top: y, behavior: 'instant'});
            """, submit_btn)
            time.sleep(0.3)

            # JS 클릭
            self.driver.execute_script("arguments[0].click();", submit_btn)
            time.sleep(0.8)

            # 저장 후 다시 '이름' 행으로 스크롤 복귀
            name_row = self.get_element(By.XPATH, XPATH["NAME_ROW"], option="presence", timeout=3)
            if name_row:
                self.driver.execute_script("""
                    const rect = arguments[0].getBoundingClientRect();
                    const y = rect.top + window.scrollY - 120;
                    window.scrollTo({top: y, behavior: 'instant'});
                """, name_row)
            else:
                self.driver.execute_script("window.scrollTo({top: 0, behavior: 'instant'});")

            time.sleep(0.5)
            print("저장 버튼 JS 클릭 + 이름 행으로 복귀")
            return True

        except Exception as e:
            print(f" 저장 버튼 JS 클릭 실패: {e}")
            return False
    
    #메일 관련 테스트를 위한 메서드

    
    def click_to_mkt(self):
        element = self.get_element_by_name(NAME["BTN_MKT"])
        element.click()
        time.sleep(4)
    
    def choose_lang_dropbox(self):
        element = self.get_element_by_xpath(XPATH["BOX_LANG"])
        element.click()
        time.sleep(4)

