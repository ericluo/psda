# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests, bs4
from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth1

HEADERS = {
        'Host': 'www.jisilu.cn', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
        'Cache-Control': 'no-cache', 'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Origin': 'https://www.jisilu.cn', 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Referer': 'https://www.jisilu.cn/login/',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8'
    }

def login(self, response):
    url = 'https://www.jisilu.cn/account/ajax/login_process/'
    data = {
        'return_url': 'https://www.jisilu.cn/',
        'user_name': 'ericluo',
        'password': 'snow327',
        'net_auto_login': '1',
        '_post_type': 'ajax',
    }

    yield FormRequest(
        url=url,
        headers=HEADERS,
        formdata=data,
        callback=self.parse,
        dont_filter=True
    )

url = 'https://www.jisilu.cn/data/ha/#ha'
auth = HTTPDigestAuth('ericluo', 'snow327')
resp = requests.get(url, auth = auth)

print(resp.text)
# soup = bs4.BeautifulSoup(resp.text)

# table = soup.select("div#topic_ha > table")
# table.select("tr")
# rs = soup.select("tr")

# print(resp.text)

