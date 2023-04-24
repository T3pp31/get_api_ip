import socket
from urllib.parse import urlparse


def get_API_ip(url):
    """
    Parameters:
    ----------
    url : str

    Returns:
    --------
    ip : str 調べたurlのip
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    ip = socket.gethostbyname(domain)
    return ip


if __name__ == "__main__":
    ip = get_API_ip("https://www.mlb.com/")
    print(ip)
