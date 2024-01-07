#!/usr/bin/python3
"""json_api module
Contains code to send a POST request to url
"""

import sys
import requests


def do_request(url, letter):
    """do_request function
    Sends a POST request with a letter as a param
    url (str): the URL
    letter (str): the letter to send
    """
    if letter is None:
        letter = ""
    data = {
        'q': letter
    }
    res = requests.post(url, data=data)
    try:
        json = res.json()
        if len(json.items) > 0:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    do_request(url, letter)
