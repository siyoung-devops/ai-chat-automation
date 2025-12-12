from utils.headers import *
from utils.context import LoginContext
from utils.browser_utils import BrowserUtils

from pages.base_page import BasePage
from utils.defines import TARGET_URL, SELECTORS, NAME, XPATH, ID

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
        
        #계정 페이지 전환을 위한 확인 작업
        self.ensure_account_window() 
        return True
    
    def update_info(self): 
        return self.get_elements_by_xpath(XPATH["BTNS_UPDATE"])

    def open_name_edit_form(self, timeout=5):
        print("🔍 open_name_edit_form 시작")

        # 0) 먼저 페이지를 항상 같은 위치로 초기화 (예: 이름 행 위쪽)
        name_row = self.get_element(By.XPATH, XPATH["NAME_ROW"], option="presence", timeout=3)
        if name_row:
            self.driver.execute_script("""
                const rect = arguments[0].getBoundingClientRect();
                const y = rect.top + window.scrollY - 120;
                window.scrollTo({top: y, behavior: 'instant'});
            """, name_row)
            time.sleep(0.3)

        # 1) '이름' 수정 버튼 찾기
        edit_btn = self.get_element(
            By.XPATH,
            XPATH["NAME_EDIT_BTN"],  # //tr[.//td[normalize-space(.)='이름']]//button[...]
            option="visibility",
            timeout=timeout,
        )
        if not edit_btn:
            print("❌ '이름' 수정 버튼 못 찾음")
            return False

        print("✅ '이름' 수정 버튼 찾음, 클릭 시도")

        try:
            edit_btn.click()
        except Exception as e:
            print(f"⚠️ 수정 버튼 기본 클릭 실패: {e}")
            self.driver.execute_script("arguments[0].click();", edit_btn)
        time.sleep(0.5)

        # 2) fullname 입력 필드 대기
        input_name = self.get_element_by_name(NAME["INPUT_NAME"], option="visibility", timeout=timeout)
        if not input_name:
            print("❌ 이름 입력란 안 나타남 (폼 안 열림)")
            return False

        print("✅ 이름 수정 폼 열림")
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
        """저장 버튼 JS 클릭 + '이름' 행으로 스크롤 복귀"""
        xpath = XPATH["SUBMIT_NAME"]  # //button[@type='submit' and normalize-space(.)='완료']

        submit_btn = self.get_element(By.XPATH, xpath, option="visibility", timeout=3)
        if not submit_btn:
            print(" 저장 버튼 없음 (DOM에 없음)")
            return False

        try:
            self.driver.execute_script("""
                const rect = arguments[0].getBoundingClientRect();
                const y = rect.top + window.scrollY - 100;
                window.scrollTo({top: y, behavior: 'instant'});
            """, submit_btn)
            time.sleep(0.3)

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
            print("✅ 저장 버튼 JS 클릭 + 이름 행으로 복귀")
            return True

        except Exception as e:
            print(f" 저장 버튼 JS 클릭 실패: {e}")
            return False

    
    def click_to_mkt(self):
        element = self.get_element_by_name(NAME["BTN_MKT"])
        element.click()
        time.sleep(4)
    
    def choose_lan_dropbox(self):
        element = self.get_element_by_xpath(XPATH["BOX_LANG"])
        element.click()
        time.sleep(4)

    def debug_submit_once(self):
        elems = self.driver.find_elements(By.XPATH, XPATH["SUBMIT_NAME"])
        print(f"🔍 현재 DOM에서 저장 버튼 개수: {len(elems)}")
    
    def debug_find_name_edit_button(self):
        # ✅ MUI 편집 버튼 + 이름 행 기준 (랜덤 클래스 제거)
        name_edit_btns = self.get_elements(By.XPATH, 
            "//tr[.//td[normalize-space(.)='이름']]//button[contains(@class,'MuiIconButton-root') or @data-testid='EditOutlinedIcon']")
        
        print(f"🔍 '이름' 행 수정 버튼 개수: {len(name_edit_btns)}")
        
        if not name_edit_btns:
            # 대안: 모든 MUI 편집 버튼에서 이름 행 근처만
            all_edit_btns = self.get_elements(By.CSS_SELECTOR, "button.MuiIconButton-root")
            print(f"🔍 모든 MUI 편집 버튼: {len(all_edit_btns)}개")
            return 0 if all_edit_btns else None
        
        # 첫 번째 이름 수정 버튼 클릭 테스트
        btn = name_edit_btns[0]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)
        
        # fullname 확인
        input_name = self.get_element_by_name("fullname", option="visibility", timeout=2)
        print(f"✅ 이름 수정 버튼 클릭 후 fullname: {input_name is not None}")
        return 0 if input_name else None
