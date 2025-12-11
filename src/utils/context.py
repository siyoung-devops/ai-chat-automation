from dataclasses import dataclass

@dataclass
class LoginContext:
    driver: object
    fm: object
    login_page: object
    main_page: object
    user_data: list
    file_name: str = "cookies.json"
    url: str = "https://qaproject.elice.io/ai-helpy-chat"