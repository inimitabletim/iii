from urllib import request  # 加入一個請求模組

from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = 8660

for i in range(0,10):
        url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page) #給一個網址
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req).read().decode('utf8')

        soup = BeautifulSoup(res, 'html.parser')


        title = soup.select('div[class="title"] a')


        for each_title in title:
                print(each_title.text)
                print('https://www.ptt.cc/' + each_title['href'])
                #print()

        page -= 1