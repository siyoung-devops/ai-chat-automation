from utils.headers import *
from utils.defines import FULLSCREEN_SIZE

"""
드라이버 매니저 
1. 드라이버가 여러개일 경우 - name으로 분류해서 관리
2. 여러개를 생성할 필요가 없으면 하나로 사용하면 되니까 같이 정하면 좋을것같아요
"""


class DriverManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = None
        return cls._instance

    def create_driver(self, browser="chrome"):
        if self.driver:
            return self.driver

        browser = browser.lower()
        if browser == "chrome":
           
            chrome_options = Options()
            chrome_options.add_experimental_option(
                "detach", False
            )  
            
            # 드라이버 옵션 설정
            chrome_options.add_argument("--start-maximized")  
            chrome_options.add_argument("--disable-autofill")
            chrome_options.add_argument("--disable-save-password-bubble")
            chrome_options.add_argument("--disable-password-manager-reauthentication")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--user-data-dir=/tmp/selenium_temp_profile")

            # 드라이버 자동 설치 및 서비스 설정
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

        elif browser == "safari":
            # safari는 옵션이 필요없으나 환경설정 -> 개발자 메뉴 -> 원격 자동화 옵션 허용이 필요하다고합니다!
            try:
                self.driver = webdriver.Safari()
                self.driver.set_window_size(*FULLSCREEN_SIZE) # maximized 옵션 없음
            except Exception as e:
                print("Safari webdriver 실패 원격자동화 옵션을 확인해주세요.") 
                raise e
        else:
            raise ValueError(f"지원하지 않는 브라우저입니다 = {browser}")

        return self.driver


    # 드라이버 가져오기
    def get_driver(self):
        return self.driver

    # 드라이버 종료
    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None