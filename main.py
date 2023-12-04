import requests
from bs4 import BeautifulSoup

# スクレイピング対象のURL
url = 'https://www.softbankhawks.co.jp/game/stats/team/batter/'

# ウェブページの取得
response = requests.get(url)

# 取得したコンテンツをBeautiful Soupで解析
soup = BeautifulSoup(response.text, 'html.parser')

# 例: タイトルの取得

# 例: 特定の要素の取得

with open('output.txt','w',encoding='utf_8')as file:
    file.write(soup.prettify())
    # file.write(str(sample_element))

# peach_Tech代表のゆうせいさんとfirst commitしました。