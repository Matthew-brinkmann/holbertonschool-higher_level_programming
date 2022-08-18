#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
from requests import get

if __name__ == "__main__":
    urlToQuery = 'https://intranet.hbtn.io/status'
    urlRequest = get(urlToQuery)
    responseContent = urlRequest.text
    print('Body response:')
    print("\t- type: {}".format(type(responseContent)))
    print("\t- content: {}".format(responseContent))
