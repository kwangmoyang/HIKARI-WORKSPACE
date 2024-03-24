import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime

#today_url = input("오늘의 URL을 입력하세요.")

#today_response = requests.get(today_url)
#today_html_content = today_response.text

#today_soup = BeautifulSoup(today_html_content, 'html.parser')
#today_location = today_soup.select('#SE-3eaa6e7f-ebdf-4c44-b468-e67504d6015a')
#print(today_location)


#################################################################################################
#원하는 지역, 업종을 입력
location = input("검색할 지역을 입력하세요 ex) 구로, 강서, 까치산 : ")
type = input("추출할 업종을 입력하세요 ex) 네일,속눈썹,카페 : ")

# 웹 페이지 가져오기
url = f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={location}+{type}"
response = requests.get(url)
html_content = response.text
print(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# 날짜 가져오기
today = datetime.now().strftime("%Y-%m-%d")
# 저장 디렉토리 생성
directory = "C:/study/"
# 파일 이름 설정
filename = f"user_info_{today}.txt"

# user_info 클래스를 가진 요소를 찾고, 그 안에서 cru 속성값을 가져오기
user_info_divs = soup.select('.user_info')

user_count = 0

file_path = os.path.join(directory, filename)
with open(filename, 'w', encoding='utf-8') as file :
    for user_info in user_info_divs:
        a_tag = user_info.find('a')
        if a_tag:
            href_value = a_tag.get('href')
            match = re.search(r'\/([\w-]+)$', href_value)
            if match :
                user_id = match.group(1)
                print(user_id)
                file.write(user_id)
                user_count += 1

                # user_id가 10의 배수일 때마다 줄바꿈 추가
                if user_count % 10 == 0:
                    file.write('\n')
                elif user_count < len(user_info_divs) :
                    file.write(',')

print("총", user_count, "번 출력되었습니다.")
print("유저 정보가", {filename} ,"파일에 저장되었습니다.")