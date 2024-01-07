#!/usr/bin/python3
"""my_github module
Contains code to connect to Github API and display user id
"""

import sys
import requests


def do_request(url, username, password):
    """do_request funciton
    Connects to Github and fetches the user id
    url (str): the github API url
    username (str): the Github username
    password (str): the Github pernal access token
    """

    auth = (username, password)
    res = requests.get(url, auth=auth)
    print(res.json().get('id'))


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    do_request(url, username, password)
