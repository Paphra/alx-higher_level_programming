#!/usr/bin/python3
"""hbtn_header module
Taks a URL, sends a request to the URL and displays the header
"""
import sys
import urllib.request


def fetch(url):
    """fetch function
    Fetches the response from url

    url (str): the URL to request from
    """

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == '__main__':
    url = sys.argv[1]
    fetch(url)
