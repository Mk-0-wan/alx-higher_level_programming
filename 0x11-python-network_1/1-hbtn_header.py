#!/usr/bin/python3
"""Getting the specific header content"""
if __name__ == "__main__":
    import urllib.request as url
    import sys

    with url.urlopen(sys.argv[1]) as res:
        print(res.getheader('X-Request-Id'))
