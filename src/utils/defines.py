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
    "INPUT_MOBILE" : "input[name='to'][autocomplete='tel']",

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
    "INPUT_EMAIL" : "to",
    "INPUT_PWD" :"password",
    "INPUT_NEW_PWD" : "newPassword",
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
    "BTN_COPY_RESPONSE" : '//button[@aria-label="취소"]',
    "BTN_RETRY" : '//button[@aria-label="다시 생성"]',
    "BTN_COPY" : '//button[@aria-label="복사"]',
    "BOX_LANG" : "//div[@aria-haspopup='listbox']",
    "SUBMIT_NAME" : "//button[@type='submit' and normalize-space(.)='완료']",
    "NAME_ROW": "//table[contains(@class,'css-69t54h')]//tr[td[normalize-space(.)='이름']]",
    "BTN_NAME_EDIT": "//tr[td[normalize-space(.)='이름']]//button[contains(@class,'MuiIconButton-root')]",
    "EMAIL_ROW" : "//table[contains(@class,'css-69t54h')]//tr[td[normalize-space(.)='이메일']]",
    "BTN_EMAIL_EDIT": "//tr[td[normalize-space(.)='이메일']]//button[contains(@class,'MuiIconButton-root')]",
    "BTN_CERTI_MAIL" : "//button[@type='submit' and normalize-space(.)='인증메일 발송']",
    "INVALID_MSG" : "//p[contains(@id,'helper-text')]",
    "MOBILE_ROW": "//table[contains(@class,'css-69t54h')]//tr[td[normalize-space(.)='휴대폰 번호']]",
    "BTN_MOBILE_EDIT" : "//tr[td[normalize-space(.)='휴대폰 번호']]//button[contains(@class,'MuiIconButton-root')]",
    "BTN_CERTI_MOBIL" : "//button[@type='submit' and contains(@class,'MuiLoadingButton-root')]",
    "TOAST_CONTAINER" : "//div[@role='alert'][@aria-describedby='notistack-snackbar']",
    "PWD_ROW" : "//table[contains(@class,'css-69t54h')]//tr[td[normalize-space(.)='비밀번호']]",
    "BTN_PWD_EDIT" : "//tr[td[normalize-space(.)='비밀번호']]//button[contains(@class,'MuiIconButton-root')]",
    "SUBMIT_PWD" : "//button[@type='submit' and normalize-space(.)='완료']",
    
    "BTN_COPY_QUESTION" : "//div[@data-floating='true'])[last()]",
}