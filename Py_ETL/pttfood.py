import requests
from bs4 import BeautifulSoup
import os
from urllib import request

url = 'https://www.ptt.cc/bbs/Food/index.html' #給一個網址
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

ss = requests.session()
ss.cookies['over18'] = '1'

path = r'./res_Food'
if not os.path.exists(path):
    os.mkdir(path)


# res = ss.get(url, headers=headers)
#
# soup = BeautifulSoup(res.text, 'html.parser')
#
# title2 = soup.select('div[class="title"] a')
for i in range(0, 100):
    print('=== 第',(i+1),'頁 ===')
    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    title2 = soup.select('div[class="title"] a')
    #進去標題網址寫法
    for each_title in title2:
            try:
                res_good = ss.get(url, headers=headers)
                soup_good = BeautifulSoup(res_good.text, 'html.parser')
                x = soup_good.select('span[class="hl f3"]')[0].text
                y = str(x)
                #print(x)
                if y == '爆' or y >= '20':
                    article_url = 'https://www.ptt.cc/' + each_title['href']
                    res_img = ss.get(article_url, headers=headers)
                    soup_img = BeautifulSoup(res_img.text, 'html.parser')
                    print(each_title.text)
                    # 以下進去內文抓取圖片寫法
                    title_img = soup_img.select('div[id="main-content"] a')
                    for i in title_img:
                            if i['href'].split('.')[-1] == 'jpg':  # 判斷網址是否為jpg，用split('.')做分割，然後取最後一個.jpg做判斷
                                    print(i['href']) # 印出圖片網址
                                    if not os.path.exists('./res_Food/%s' % (each_title.text)):
                                        os.mkdir(r'./res_Food/%s' % (each_title.text))
                                    request.urlretrieve(i['href'], r'./res_Food/%s/%s'%(each_title.text, i['href'].split('/')[-1]))  # 存檔的語法
                else:
                    pass
            except:
                pass
    url_list = soup.select('div[class="btn-group btn-group-paging"] a[class="btn wide"]')   # 翻頁格式
    url = 'https://www.ptt.cc/' + url_list[1]['href']
