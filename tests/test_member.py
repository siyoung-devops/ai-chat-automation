from utils.headers import *
from utils.browser_utils import BrowserUtils
from pages.member_page import MemberPage


def test_go_to_main(logged_in_main):
    page = logged_in_main

def test_go_to_member(member_page): #계정관리 접속
    page = member_page
    page.click_member_btn()

    page.click_name_update()
    