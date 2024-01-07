#!/usr/bin/python3
"""hbtn_header module
sends a request to the URl and displays the value of header
"""

import sys
import requests


def do_request(url):
    """do_request function
    Sends a request to the URL and displays the header
    url (str): URL
    """
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))


if __name__ == '__main__':
    url = sys.argv[1]
    do_request(url)
