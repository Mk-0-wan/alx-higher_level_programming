#!/usr/bin/python3
"""Capture Http errors"""

if __name__ == "__main__":
    from sys import argv
    import requests


    url = argv[1]
    try:
        response = requests.get(url)
        if (response.status_code >= 400):
            response.raise_for_status()
        else:
            print(response.text)
    except requests.exceptions.HTTPError as e:  # something is happening here (inheritance)
        print(f"Erro code: {e.response.status_code}")

