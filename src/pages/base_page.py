from utils.headers import *



# base_page 에서 공통 기능을 관리하는것이 어떨까요?? 
# base_page > login_page, chat_page, main_page 등 상속받아서 사용하거나
# 아니면 page_manager로 만들어서 관리하는게 나을지 한번 논의해보면 좋을것같아요!



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def go_to_page(self, url):
        self.driver.get(url)
        time.sleep(1)
        
    
    def get_element(self, by, value, option="presence", timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            if option == "presence":
                return wait.until(EC.presence_of_element_located((by, value)))
            
            elif option == "visibility":
                return wait.until(EC.visibility_of_element_located((by, value)))
        except (TimeoutException, NoSuchElementException):
            print(f"element를 {by} = {value} 로 찾을 수 없음.")
            return None

    def get_element_by_id(self, id, option="presence", timeout = 5):
        return self.get_element(By.ID, id, option, timeout)

    def get_element_by_name(self, name, option="presence", timeout = 5):
        return self.get_element(By.NAME, name, option, timeout)

    def get_element_by_xpath(self, xp, option="presence", timeout = 5):
        return self.get_element(By.XPATH, xp, option, timeout)
    
    def get_element_by_tag(self, tag, option="presence", timeout = 5):
        return self.get_element(By.TAG_NAME, tag, option, timeout)

    def get_element_by_css_selector(self, cs, option="presence", timeout = 5):
        return self.get_element(By.CSS_SELECTOR, cs, option, timeout)
    
    
    # 수진 - 여러 요소 받는 함수도 만들었습니다
    def get_elements(self, by, value, timeout=5) :
        try :
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_all_elements_located((by, value)))
            return self.driver.find_elements(by, value)
        except (TimeoutException, NoSuchElementException):
            print(f"elements를 {by} = {value} 로 찾을 수 없음.")
            return []
        
    def get_elements_by_xpath(self, xp) :
        return self.get_elements(By.XPATH, xp)
    
    def get_elements_by_css_selector(self, cs) :
        return self.get_elements(By.CSS_SELECTOR, cs)
    
    def debug_current_window_safe(self):
        """안전한 창 디버깅 (제목 없이 핸들만)"""
        current_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        
        print(f"🔍 현재 활성: {current_handle[:8]}...")
        print(f"📋 창 목록 ({len(all_handles)}개):")
        
        for i, handle in enumerate(all_handles):
            is_active = "✅" if handle == current_handle else "  "
            print(f"  {i}: {is_active} {handle[:8]}...")
        
        return current_handle, all_handles
    def ensure_account_window(self, timeout=10):
        """계정 창 확인/전환 (이미 있으면 전환만)"""
        handles = self.driver.window_handles
        
        # 계정 페이지 URL 패턴
        account_patterns = ["accounts.elice.io", "member", "account"]
        
        for handle in handles:
            self.driver.switch_to.window(handle)
            current_url = self.driver.current_url
            
            # 계정 페이지면 전환 완료
            for pattern in account_patterns:
                if pattern in current_url:
                    print(f"계정 창 발견: {current_url[:50]}")
                    self.debug_current_window_safe()
                    return True
            
            time.sleep(0.5)
        
        print("계정 창 없음")
        return False
