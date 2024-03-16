import requests
from bs4 import BeautifulSoup

# URL
url = 'https://digital.asahi.com/articles/DA3S15886550.html?iref=pc_rensai_long_61_article'

# 연결
response = requests.get(url)

# HTTP 상태 확인
if response.status_code == 200:
    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 내용 추출
    content = soup.find('div', class_='nfyQp').find('p').get_text(separator='\n', strip=True)

    print("내용:", content)
else:
    print('웹 페이지에 접근할 수 없습니다. 상태 코드:', response.status_code)
