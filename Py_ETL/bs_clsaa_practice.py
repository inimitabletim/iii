from urllib import request #加入一個請求模組
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html' #給一個網址
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req).read().decode('utf8')
soup = BeautifulSoup(res, 'html.parser')

title = soup.findAll('div', class_='title')
print(title)

#print(title[0])
#each_title = title[0].finaALL('a')
#print(each_title[0].text)

# for title_html in title:
#     try:
#         print(title_html.findAll('a')[0].text)
#     except IndexError as e:
#         print(e.args)
#     print('=======')