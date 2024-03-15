import requests
from bs4 import BeautifulSoup
import re

#원하는 지역, 업종을 입력
location = input("검색할 지역을 입력하세요 ex) 구로, 강서, 까치산")
type = input("추출할 업종을 입력하세요 ex) 네일,속눈썹,카페")

# 웹 페이지 가져오기
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={location}+{type}"
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# user_info 클래스를 가진 요소를 찾고, 그 안에서 cru 속성값을 가져옵니다.
user_info_divs = soup.select('.user_info')

user_count = 0

for user_info in user_info_divs:
    a_tag = user_info.find('a')
    if a_tag:
        href_value = a_tag.get('href')
        match = re.search(r'\/([\w-]+)$', href_value)
        if match :
            user_id = match.group(1)
            print(user_id)
            user_count += 1

print("총", user_count, "번 출력되었습니다.")