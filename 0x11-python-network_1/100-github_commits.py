#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API, here is the
documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == '__main__':
    repoName = sys.argv[1]
    repoOwner = sys.argv[2]
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(repoOwner, repoName))
    try:
        responseDict = response.json()
    except ValueError:
        sys.exit()
    for item in responseDict[:10]:
        print(item.get('sha'), end=": ")
        print(item.get('commit').get('author').get('name'))
