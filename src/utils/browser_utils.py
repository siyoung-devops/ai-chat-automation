from utils.headers import *

from utils.context import LoginContext
from utils.defines import TARGET_URL

#fm = FileManager()

class BrowserUtils:
    def save_cookies(self, driver, fm, file_name = "cookies.json"):
        cookies = driver.get_cookies()
        fm.save_json_file(file_name, cookies)

    def load_cookies(self, driver, fm, url, file_name = "cookies.json"):
        cookies = fm.read_json_file(file_name)
        if not cookies:
            print(f"쿠키 파일 없음")
            return False

        # 여기 부분 driver manager로 뺄수도.
        driver.get(url)
        time.sleep(0.5)
        for cookie in cookies:
            cookie.pop("domain", None)
            driver.add_cookie(cookie)

        return True

    def login_with_cookies(self, ctx: LoginContext):
        loaded_cookies = self.load_cookies(ctx.driver, ctx.fm, ctx.url)

        # 로그인 정보 없으면 user_data이용
        if not loaded_cookies:
            ctx.main_page.go_to_main_page()
            user = ctx.user_data[-1]
            ctx.login_page.input_user_data(user)
            ctx.login_page.click_login_button()

            # 로그인 후 쿠키 저장!
            self.save_cookies(ctx.driver, ctx.fm, ctx.file_name)

        return ctx.main_page