#!/usr/bin/python3
"""Capture Http errors"""

if __name__ == "__main__":
    from sys import argv
    import requests


    url = argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Erro code: {e.response.status_code}")

