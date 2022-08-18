#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""
from requests import get
import sys


if __name__ == "__main__":
    urlToQuery = sys.argv[1]
    responseContent = get(urlToQuery)
    if responseContent.ok:
        print(responseContent.text)
    else:
        print('Error code: {}'.format(responseContent.status_code))
