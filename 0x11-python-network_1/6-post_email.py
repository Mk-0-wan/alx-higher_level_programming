#!/usr/bin/python3
"""Making a post request with requests"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    mail = {'email': argv[2]}
    response = requests.post(argv[1], data=mail)
    print(response.text)
