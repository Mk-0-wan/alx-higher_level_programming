#!/usr/bin/python3
"""Posting to a url using urllib"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    mail = {'email': argv[2]}
    data = urlencode(mail)
    data_utf8 = data.encode('utf-8')
    req = Request(url, data_utf8)

    with urlopen(req) as resp:
        print(resp.read().decode())
