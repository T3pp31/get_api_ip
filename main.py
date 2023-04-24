from get_API_ip import get_API_ip
from get_API_url import get_API_url

# 調べたいWebサイトのurlを入力
url = input("調べたいWebサイトのURLを入力(例:https://www.mlb.com/):")

urls = get_API_url(url)

result = {}
for url in urls:
    ip = get_API_ip(url)
    result[url] = ip

print(result)

# ファイル書き出し
with open("result.txt", "w") as file:
    for url, ip in result.items():
        file.write(f"{url}:{ip}\n")
