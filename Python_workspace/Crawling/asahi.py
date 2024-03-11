import requests
from bs4 import BeautifulSoup

#URL
url = 'https://www.asahi.com/rensai/list.html?id=61&iref=kwmbs'

#Connected
response = requests.get(url)

# HTTP
if response.status_code == 200:
    #BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #News
    article_titles = soup.select('.ItemTitle')
    for title in article_titles:
        print(title.text.strip())
else:
    print('ウェブページにアクセスできません。 ステータスコード:' , response.status_code)