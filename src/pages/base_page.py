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
        
    
    # 예시입니다!
    # id, selector, xpath, name등 함수를 하나씩 만드는게 나을지
    # 아예 함수하나만 만들어서, 외부에서 By.XPATH, By.ID 이런식으로 매개변수를 넣어서 이용할지 
    # 어떤게 좋을지 논의해보면 좋을거같아요!
    def get_element_by_id(self, id, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((By.ID, id)))
        except (TimeoutException, NoSuchElementException):
            print("element를 by.id로 찾을 수 없음.")
            return None