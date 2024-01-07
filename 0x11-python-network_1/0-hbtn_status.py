#!/usr/bin/python3
"""hbtn_status module
Fetches the status the hbtn intranet
"""

import urllib.request


def fetch():
    """fetch function
    Fetches the https://alx-intranet.hbtn.io/status
    """

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
        print('\t- utf8 content: {}'.format(data.decode('utf-8')))


if __name__ == '__main__':
    fetch()
