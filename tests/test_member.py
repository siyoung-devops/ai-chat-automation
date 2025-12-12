from utils.headers import *
from utils.browser_utils import BrowserUtils
from pages.member_page import MemberPage


def test_member_page(logged_in_member):
    page = logged_in_member

    page.click_member_btn() #계정관리 접속