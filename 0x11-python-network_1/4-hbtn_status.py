#!/usr/bin/python3
"""htbn_status module
Fetches the request
"""

import requests


def fetch():
    """fetch function
    fetches the status of https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(res.content)))
    print('\t- content: {}'.format(res.content.decode('utf-8')))


if __name__ == '__main__':
    fetch()
