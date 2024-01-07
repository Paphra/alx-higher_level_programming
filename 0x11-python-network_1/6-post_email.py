#!/usr/bin/python3
"""post_email module
Sends a POST requet to the passed URL
"""

import sys
import requests


def do_request(url, email):
    """do_request funciton
    For sending a POST request containg the email to the URL
    url (str): the URL
    email (str): the email
    """

    data = {
        'email': email
    }
    res = requests.post(url, data=data)
    print(res.content.decode('utf-8'))


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    do_request(url, email)
