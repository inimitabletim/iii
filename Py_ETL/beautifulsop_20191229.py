from urllib import request #加入一個請求模組
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html' #給一個網址
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req).read().decode('utf8')

soup = BeautifulSoup(res, 'html.parser')
#print(soup)

logo = soup.findAll('a', {'id':'logo'})
# print(logo)
# print(logo[0])
# print(logo[0].text) # 取出括號裡的字串
# print(logo[0].string) # 取出括號裡的字串
print(logo[0]['href']) # 取出網址
