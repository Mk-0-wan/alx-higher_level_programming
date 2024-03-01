#!/usr/bin/python3
"""Getting the body content"""
if __name__ == "__main__":
    import urllib.request as url

    with url.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()

    print(f"Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
