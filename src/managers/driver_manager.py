from utils.headers import *

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

        if browser.lower() == "chrome":
           
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

        # ...elif browser.lower() == "safari/edge"

        return self.driver


    # 드라이버 가져오기
    def get_driver(self):
        return self.driver

    # 드라이버 종료
    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None