#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
from requests import get
import sys


if __name__ == "__main__":
    urlToQuery = sys.argv[1]
    responseContent = get(urlToQuery)
    print(responseContent.headers.get('X-Request-Id'))
