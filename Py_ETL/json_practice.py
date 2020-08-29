import requests
import json
from urllib import request
import os

if not os.path.exists('./dcard_img'):
    os.mkdir(r'./dcard_img')

url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232804114' #給一個網址
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
res = requests.get(url, headers=headers)
print(res)
print(type(res.text))
print(res.text)

tmp_json = json.loads(res.text)
print(type(tmp_json))
print(tmp_json)

# for each_title in tmp_json:
#     article_title = each_title['title'].replace('/','')
#     if not os.path.exists('./dcard_img/%s'%(article_title)):
#         os.mkdir(r'./dcard_img/%s'%(article_title))
#     print(article_title)
#     print('https://www.dcard.tw/f/photography/p/'+str(each_title['id']))
#     for img_url_dict in each_title['mediaMeta']:
#         img_url = img_url_dict['url']
#         try:
#             request.urlretrieve(img_url, r'./dcard_img/%s/%s'%(article_title, img_url.split('/')[-1]))
#         except:
#             pass
#         #print('\t%s'%(img_url))