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
        
    
    def get_element(self, by, value, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, value)))
        except (TimeoutException, NoSuchElementException):
            print(f"element를 {by} = {value} 로 찾을 수 없음.")
            return None

    def get_element_by_id(self, id):
        return self.get_element(By.ID, id)

    def get_element_by_name(self, name):
        return self.get_element(By.NAME, name)

    def get_element_by_xpath(self, xp):
        return self.get_element(By.XPATH, xp)
    
    def get_element_by_tag(self, tag):
        return self.get_element(By.TAG_NAME, tag)

    def get_element_by_css_selector(self, cs):
        return self.get_element(By.CSS_SELECTOR, cs)
    
    
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