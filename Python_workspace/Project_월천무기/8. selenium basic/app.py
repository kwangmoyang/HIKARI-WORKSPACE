import time

from selenium import webdriver
from selenium.webdriver.common.by import By 
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 1. 웹 드라이브 주소 컨트롤하기
driver.get("http://www.naver.com")
time.sleep(3)

# 2-1. 요소를 찾아 copy. 
css_selector = "#newsstand > div.ContentHeaderView-module__content_header___nSgPg > div > ul"

# 2-2. 찾아온 요소 변수에 저장
element = driver.find_element(By.CSS_SELECTOR, css_selector)

print(element.text)
input()