#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
from requests import post
import sys


if __name__ == "__main__":
    urlToQuery = sys.argv[1]
    payload = {'email': sys.argv[2]}
    bodyOfResponse = post(urlToQuery, data=payload)
    print(bodyOfResponse.text)
