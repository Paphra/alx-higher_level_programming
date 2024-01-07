#!/usr/bin/python3
"""error_code module
Sends a request to the URL and displays response
"""
import sys
import urllib.request
import urllib.error


def do_request(url):
    """do_request function
    Sends a request to the passed url
    url (str): the URL
    """

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    url = sys.argv[1]
    do_request(url)
