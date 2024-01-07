#!/usr/bin/python3
"""hbtn_status module
Fetches the status the hbtn intranet
"""

import urllib.request


def fetch():
    """fetch function
    Fetches the https://alx-intranet.hbtn.io/status
    """

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        print('    - type: {}'.format(type(data)))
        print('    - content: {}'.format(data))
        print('    - utf8 content: {}'.format(data.decode()))


if __name__ == '__main__':
    fetch()
