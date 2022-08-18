#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print('Body response:')
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
