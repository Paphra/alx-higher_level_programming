#!/usr/bin/python3
"""error_code module
Sends a request to the passed URL
"""

import sys
import requests


def do_request(url):
    """do_request funciton
    Sends a request to the url
    url (str): the URL
    """

    res = requests.get(url)
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.content.decode('utf-8'))


if __name__ == '__main__':
    url = sys.argv[1]
    do_request(url)
