from utils.headers import *
from utils.context import LoginContext
from utils.browser_utils import BrowserUtils
from utils.browser_setup import create_driver
from utils.context import LoginContext

from managers.file_manager import FileManager
from pages.signup_page import SignupPage
 
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.member_page import MemberPage

# 모든 fixture를 관리하는 곳
# session = 하나의 드라이버 공유
@pytest.fixture(scope="session")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

# 수진 - 회원가입 용 driver를 따로 만들었어요
# function = 테스트마다 새 드라이버 생성
@pytest.fixture(scope="function")
def signup_driver() :
    driver = create_driver()
    yield driver
    driver.quit()

    
@pytest.fixture
def fm():
    return FileManager()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture
def signup_page(signup_driver) :
    return SignupPage(signup_driver)

@pytest.fixture
def member_page(driver):
    page = MemberPage(driver)
    return page



####### 메안화면 확인용 #######
@pytest.fixture
def user_data(fm):
    return fm.read_json_file("user_data.json")

@pytest.fixture
def logged_in_main(driver, fm, user_data, main_page, login_page,member_page):
    ctx = LoginContext(
        driver=driver,
        fm=fm,
        login_page=login_page,
        main_page=main_page,
        member_page=member_page,
        user_data=user_data
    )
    
    browser_utils = BrowserUtils()
    return browser_utils.auto_login(ctx)