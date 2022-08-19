#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(username, password))
    print(response.json().get('id'))
