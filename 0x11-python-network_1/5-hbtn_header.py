#!/usr/bin/python3
"""Getting specific headers from the response using requests"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    if response:
        print(response.headers['X-Request-Id'])
