#!/usr/bin/python3
"""Capture Http errors"""

if __name__ == "__main__":
    from sys import argv
    import requests


    url = argv[1]
    response = requests.get(url)
    if (response.status_code == 200):
        print(response.text)
    else:
        print(f"Erro code: {response.status_code}")
