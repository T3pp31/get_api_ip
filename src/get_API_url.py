import requests
from bs4 import BeautifulSoup


def get_API_url(url="google.com"):
    """
    Parameters
    ----------
    url : str 調べたいurl default:google.com

    Returns:
    -------
    urls : list href等の後にあるリンク
    """
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    urls = []

    for link in soup.find_all("a"):
        urls.append(link.get("href"))

    for link in soup.find_all("script"):
        urls.append(link.get("src"))

    for link in soup.find_all("link"):
        urls.append(link.get("href"))

    return urls


if __name__ == "__main__":
    urls = get_API_url("https://www.mlb.com/")
