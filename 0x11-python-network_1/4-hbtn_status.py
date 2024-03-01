#!/usr/bin/python3
"""Using requests module"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    data_type = type(response.content.decode())
    content = response.content.decode()
    print("Body response:")
    print(f"\t- type: {data_type}")
    print(f"\t- content: {content}")
