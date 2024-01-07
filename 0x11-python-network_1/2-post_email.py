#!/usr/bin/python3
"""post_email module
sends a POST request to passed URL
"""
import sys
import urllib.request
import urllib.parse


def do_request(url, email):
    """do_request function
    Sends a POST request to the passed URL with email as a parameter
    url (str): the URL
    email (str): the email data
    """
    json = {
        'email': email
    }
    data = urllib.parse.urlencode(json)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        res = response.read()
        print(res.decode('utf-8'))


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    do_request(url, email)
