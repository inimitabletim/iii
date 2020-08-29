import requests
from bs4 import BeautifulSoup
url = 'https://buzzorange.com/techorange/' #給一個網址
post = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

post_data_str = '''action: fm_ajax_load_more
nonce: 03087a1ad6
page: 4'''

post_data = {}

for i in post_data_str.split('\n'):
    post_data[i.split(': ')[0]] = i.split(': ')[1]

post_data['page'] = '0'
# print(post_data)
res = requests.get(url, headers=headers, data=post_data)
print(res)
