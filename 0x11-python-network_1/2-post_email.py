#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    urlToQuery = sys.argv[1]
    plainData = {'email': sys.argv[2]}
    dataToSend = parse.urlencode(plainData).encode('utf-8')
    with request.urlopen(urlToQuery, dataToSend) as response:
        bodyOfResponse = response.read().decode('utf-8')
        print(bodyOfResponse)
