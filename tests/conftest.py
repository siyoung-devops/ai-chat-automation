from utils.headers import *

from managers.driver_manager import DriverManager
from managers.file_manager import FileManager

from pages.main_page import MainPage


# 모든 fixture를 관리하는 곳

@pytest.fixture(scope="session")
def driver():
    dm = DriverManager()
    driver = dm.create_driver()

    yield driver
    dm.quit_driver()
    
@pytest.fixture
def fm():
    return FileManager()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page