from src.get_API_ip import get_API_ip
from src.get_API_url import get_API_url
from tqdm import tqdm

search_urls = ['https://www.mlb.com','https://google.com']
results = {}

for search_url in tqdm(search_urls):
    result_url = get_API_url(search_url)
    result = {}
    for url in result_url:
        ip = get_API_ip(url)
        result[url] = ip
    results[search_url] = result


with open('result.txt','w') as file:
    file.write(results)

