#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import json
from requests import post
import sys


if __name__ == "__main__":
    urlToQuery = 'http://0.0.0.0:5000/search_user'
    payload = {'q': ""}
    if len(sys.argv) > 1:
        payload['q'] = sys.argv[1]
    bodyOfResponse = post(urlToQuery, data=payload)
    if not bodyOfResponse.ok or len(bodyOfResponse.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            jsonResponse = bodyOfResponse.json()
            valueId = jsonResponse.get('id')
            valueName = jsonResponse.get('name')
        except ValueError:
            print('Not a valid JSON')
        if len(jsonResponse) == 0:
            print('No result')
            sys.exit()
        print("[{}] {}".format(valueId, valueName))
