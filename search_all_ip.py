from src.get_API_ip import get_API_ip
from src.get_API_url import get_API_url
from tqdm import tqdm

f = open('search.txt','r')
read_search_urls = f.readlines()
search_urls = [search_url.replace('\n','') for search_url in read_search_urls]

#search_urls = ['https://www.mlb.com','http://portal.kyodonews.jp/']
results = {}

for search_url in tqdm(search_urls):

    result_url = get_API_url(search_url)

    result = {}
    for url in tqdm(result_url):
        ip = get_API_ip(url)
        if ip != '0.0.0.0':
            result[url] = ip

    results[search_url] = result


with open('result.txt','w') as file:
    #get results' key
    for url in results.keys():
        #
        for (key,value) in zip(results[url].keys(),results[url].values()):
            print(f'{url}|{key}|{value}')
            file.write(f'{url}|{key}|{value}\n')




