import pytest

from src.get_API_url import get_API_url


def test_valid_url():
    # Verify that valid URLs return a list of links
    url = "https://www.mlb.com/"
    urls = get_API_url(url)
    assert isinstance(urls, list)
    assert len(urls) > 0


def test_invalid_url():
    # Verify that invalid URLs raise an exception
    url = "invalid-url"
    with pytest.raises(Exception):
        get_API_url(url)
