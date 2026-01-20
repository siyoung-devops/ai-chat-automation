import time
from selenium.webdriver.common.by import By
from utils.defines import STEP

class ScrollController:

    @staticmethod
    def scroll_up(driver, scroll_area, step=STEP, delay = 0.5):
        if not scroll_area:
            return

        while True:
            current_top = driver.execute_script("return arguments[0].scrollTop;", scroll_area)
            if current_top <= 0:
                break  
            
            driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", scroll_area, -step)
            time.sleep(delay)

    @staticmethod
    def scroll_down(driver, scroll_area, step=STEP, delay=0.5):
        if not scroll_area:
            return

        scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_area)
        client_height = driver.execute_script("return arguments[0].clientHeight;", scroll_area)

        while True:
            current_top = driver.execute_script("return arguments[0].scrollTop;", scroll_area)
            if current_top + client_height >= scroll_height:
                break  
            
            driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", scroll_area, step)
            time.sleep(delay)

    @staticmethod
    def scroll_to_element(driver, scroll_area, target_xpath, step=STEP):
        if not scroll_area:
            return

        scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_area)
        client_height = driver.execute_script("return arguments[0].clientHeight;", scroll_area)

        while True:
            # 타겟 요소가 화면에 보이는지 확인
            try:
                elements = driver.find_elements(By.XPATH, target_xpath)
                for element in elements:
                    if element.is_displayed():
                        return
            except:
                pass

            current_top = driver.execute_script("return arguments[0].scrollTop;", scroll_area)
            if current_top + client_height >= scroll_height:
                break  
            
            driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", scroll_area, step)
            # UI 렌더링을 위한 최소한의 대기 (명시적 대기 대체)
            time.sleep(0.1)
