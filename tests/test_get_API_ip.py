import socket
from urllib.parse import urlparse

import pytest

from .src.get_API_ip import get_API_ip


def test_get_API_ip():
    url = "https://www.mlb.com/"
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    expected_ip = socket.gethostbyname(domain)
    assert get_API_ip(url) == expected_ip
