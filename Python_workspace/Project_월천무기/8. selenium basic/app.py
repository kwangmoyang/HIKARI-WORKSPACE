import time

from selenium import webdriver
from selenium.webdriver.common.by import By 
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()


# 3. Driver Wait
# 3-1. 3초때 로딩이 끝나서, element가 찾아짐
# 3-2. 30초까지는 기다리겠음
# 3-3. 30초 넘어가면 에러던짐

try:
    driver.get("http://www.naver.com")
    selector = "#shortcutArea > ul > li:nth-child(1)"
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(
        By.CSS_SELECTOR, selector
    ))
except : 
    print("에러 발생")   
print("element 로딩 끝")
print("다음 코드 실행")

##############################################################

# driver.get("http://www.naver.com")
# time.sleep(2)
# # 2. browser information
# # 2-1. title ~ 웹 사이트의 타이틀을 가지고옴
# 타이틀 = driver.title
# print(타이틀, "이 타이틀이다")

# # 2-2. current_url 주소창을 그대로 가지고옴
# 현재링크주소 = driver.current_url
# print(현재링크주소, "이것이 커렌트 url")

##############################################################
# 1. 네비게이션 관련 툴
# get(), back(), forward(), refresh()

# 1. 웹 드라이브 주소 컨트롤하기
# 1-1. get() 원하는 url을 가져오는 함수
# driver.get("http://www.naver.com")
# time.sleep(3)
# driver.get("http://www.google.com")

# # 1-2. back() 뒤로가기
# driver.back()
# time.sleep(2)
# # 1-3. forward() 앞으로가기
# driver.forward()
# time.sleep(2)

# # 1-4. refresh() 페이지 새로고침
# driver.refresh()
# time.sleep(2)


##############################################################
# 2-1. 요소를 찾아 copy. 
#css_selector = "#shortcutArea > ul"

# 2-2. 찾아온 요소 변수에 저장
#element = driver.find_element(By.CSS_SELECTOR, css_selector)

# 3-1. 데이터 가져오기
#print(element.text)

# 3-2. 요소를 클릭하기[액션]
#element.click()

print("동작 완료")
input()