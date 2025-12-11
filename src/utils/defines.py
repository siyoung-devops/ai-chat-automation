import pyautogui
# define를 모으는 곳입니다.
# 각자 사용해야하는 selector나 xpath를 작성해주세요!

# 예시입니다!!
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
FULLSCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


TARGET_URL = {
    "MAIN_URL": "https://qaproject.elice.io/ai-helpy-chat",
    "SIGNUP_URL" : "https://accounts.elice.io/accounts/signup/method?continue_to=https%3A%2F%2Fqaproject.elice.io%2Fai-helpy-chat&lang=en-US&org=qaproject"
}


SELECTORS = {

  
}

# By.NAME
NAME = {
    "INPUT_ID" : "loginId",    
    "INPUT_PW" : "password",    
}

XPATH = {
    "BTN_LOGIN": "//button[normalize-space()='Login']",
}