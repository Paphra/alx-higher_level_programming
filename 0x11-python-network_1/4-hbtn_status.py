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
    content = res.content.decode('utf-8')
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))


if __name__ == '__main__':
    fetch()
