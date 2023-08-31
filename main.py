from src.get_API_ip import get_API_ip
from src.get_API_url import get_API_url

# 調べたいWebサイトのurlを入力
url = input("調べたいWebサイトのURLを入力(例:https://www.mlb.com/):")
want_ip = input("きになるipを入力(例:151.101.41.91)なければ空白:")

urls = get_API_url(url)

result = {}
for url in urls:
    ip = get_API_ip(url)

    if want_ip != '':
        if ip == want_ip:
            print("ip:{}  url:{}".format(ip,url))
    result[url] = ip

print('result.txtに結果を書き出しました')

# ファイル書き出し
with open("result.txt", "w") as file:
    for url, ip in result.items():
        file.write(f"{url}|{ip}\n")
