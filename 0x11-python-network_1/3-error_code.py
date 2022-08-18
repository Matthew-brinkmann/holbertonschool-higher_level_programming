#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    urlToQuery = sys.argv[1]
    try:
        with request.urlopen(urlToQuery) as response:
            bodyOfResponse = response.read().decode('utf-8')
            print(bodyOfResponse)
    except error.HTTPError as responseError:
        print("Error code: {}".format(responseError.code))
