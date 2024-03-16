from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import os
current_user = os.getlogin()
print("현재 사용자 이름:", current_user)
# Chrome WebDriver 실행
service = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')  # 크롬 드라이버 경로를 지정해야 합니다.
service.start()

chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저를 표시하지 않고 실행합니다.

driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹 페이지 접속
url = 'https://digital.asahi.com/articles/DA3S15887471.html?iref=pc_rensai_long_61_article'
driver.get(url)

# 버튼 클릭
print("인쇄 버튼을 클릭합니다.")
print("인쇄 창이 열릴 때까지 잠시 기다려주세요...")

button = driver.find_element(By.CLASS_NAME, 'KFuMd')
button.click()

# WebDriver 종료
driver.quit()
