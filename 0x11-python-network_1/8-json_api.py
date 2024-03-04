#!/usr/bin/python3
"""Search API"""
if __name__ == "__main__":
    import requests
    from sys import argv, exit

    url = 'http://0.0.0.0:5000/search_user'
    query = argv[1] if len(argv) >= 2 else ""
    data = {'q': query}
    response = requests.post(url, data=data)
    if (response.status_code != 200 or response.status_code == 204):
        print("No result")
        exit()
    try:
        r_json = response.json()
        if (not r_json):
            print("No result")
            exit()
        print(f"[{r_json['id']}] {r_json['name']}")
    except ValueError:
        print("Not a valid JSON")
