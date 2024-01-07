#!/usr/bin/python3
"""github_commits module
Contains code to fetche atleast 10 commits
"""

import sys
import requests


def do_request(base_url, owner, repo):
    """do_request function
    Fetches the commits from Github
    """

    url = '{}/{}/{}/commits'.format(
        base_url, owner, repo)
    res = requests.get(url)
    data = res.json()
    count = 0
    for commit in data:
        if count < 10:
            print('{}: {}'.format(
                commit.get('sha'),
                commit.get('commit').get('author').get('name')))
        else:
            break
        count += 1


if __name__ == '__main__':
    url = 'https://api.github.com/repos'
    repo = sys.argv[1]
    owner = sys.argv[2]

    do_request(url, owner, owner)
