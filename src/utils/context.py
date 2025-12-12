from dataclasses import dataclass
from utils.defines import TARGET_URL

@dataclass
class LoginContext:
    driver: object
    fm: object
    login_page: object
    main_page: object
    member_page: object
    user_data: list
    file_name: str = "cookies.json"
    url: str = TARGET_URL["MAIN_URL"]