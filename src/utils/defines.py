import pyautogui
# define를 모으는 곳입니다.
# 각자 사용해야하는 selector나 xpath를 작성해주세요!

# 예시입니다!!
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
FULLSCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


TARGET_URL = {
    "MAIN_URL": "https://qaproject.elice.io/ai-helpy-chat",
}


SELECTORS = {
    "BTN_NEW_CHAT" : 'a[href="/ai-helpy-chat"]',
    "MEMBER_MODAL" : ".css-jgzpb4",
    "CHAT_LIST_ITEMS" : "a[data-item-index]",
    "SCROLL_TO_BOTTOM_BUTTON" : 'button[aria-label="맨 아래로 스크롤"]',
    "TEXTAREA" : "textarea[name='input']",
    "UPDATE_BTN" : "#root > div.MuiStack-root.css-1k8t7d9 > div > main > div.css-ts9wun.e9qrkv71 > div > section:nth-child(1) > div.MuiBox-root.css-0 > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > button > svg",
    

}

# By.ID
ID = {
    "CHECKBOX_HEADER" : "agreement-header",
}

# By.NAME
NAME = {
    "INPUT_ID" : "loginId",    
    "INPUT_PW" : "password",  
    "INPUT_NAME" : "fullname",
}

# By.XPATH
XPATH = {
    "BTN_LOGIN": "//button[normalize-space()='Login']",
    "BTN_CREATE_ACCOUNT" : "//a[contains(@href, 'signup')]",
    "BTN_CREATE_EMAIL" : "//button",
    "SIGNUP_AGREE" : "//input[contains(@class, 'PrivateSwitchBase')]",
    "CHECK_SIGNUP" : "//a[contains(@href, 'recover')]",
    "BTN_SIGNUP" : "//button[@type = 'submit']",
    "BTN_MEMBER" : "//a[contains(@href,'account')]",
    "SIGNUP_FAIL" : "//p",
    "SCROLL_MAIN_CHAT" : "//div[contains(@class,'css-ovflmb')]",
    "BTN_UPLOAD" : "//button[contains(@class,'MuiIconButton-root') and .//svg[contains(@data-icon,'plus')]]",
    "BTN_SEND" : "//button[@aria-label='보내기']",
    
}