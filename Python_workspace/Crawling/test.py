import requests
from bs4 import BeautifulSoup

# URL 입력 받기
url = input("URL을 입력하세요: ")

# 웹 페이지 가져오기
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# span 태그 찾기
span_tags = soup.find_all('span', class_='se-fs- se-ff-')

# 추출된 문자열 출력
if span_tags:
    for span_tag in span_tags:
        # span 태그의 텍스트 가져오기
        text = span_tag.text.strip()
        print("추출된 문자열:", text)
else:
    print("해당 클래스를 가진 span 태그를 찾을 수 없습니다.")
