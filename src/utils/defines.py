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
    "MEMBER_MODAL" : "button.MuiAvatar-root.MuiAvatar-circular",
    "CHAT_LIST_ITEMS" : "a[data-item-index]",
    "SCROLL_TO_BOTTOM_BUTTON" : 'button[aria-label="맨 아래로 스크롤"]',
    "TEXTAREA" : "textarea[name='input']",
    "CHECK_CHAT_COMPLETE" : 'div[data-status="complete"]',
    "EDIT_BUTTONS" : 'button.MuiIconButton-root',

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
    "BTN_MKT" : "marketing",
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
    "PASS_ELEMENT" : "//p[contains(text(), '통신사')]",
    "PASS_IFRAME" : "//iframe[contains(@src, 'certificates')]",
    "SIGNUP_VIEW_PW" : "//button[contains(@aria-controls, 'Password')]",
    "BTN_STOP" : '//button[@aria-label="취소"]',
    "BTN_RETRY" : '//button[@aria-label="다시 생성"]',
    "BTN_COPY" : '//button[@aria-label="복사"]',
    "BOX_LANG" : "//div[@aria-haspopup='listbox']",
    "BTNS_UPDATE" : "//*[contains(@class,'css-69t54h')]/tbody/tr/td/div/div/button",
    "SUBMIT_NAME" : "//button[@type='submit' and normalize-space(.)='완료']",
    "NAME_ROW": "//table[contains(@class,'css-69t54h')]//tr[td[normalize-space(.)='이름']]",
    "NAME_EDIT_BTN": "//button[contains(@class,'MuiIconButton-root')]",
    
}