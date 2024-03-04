#!/usr/bin/python3
"""Using the GitHub API to get my personal ID"""

if __name__ == "__main__":
    import requests
    from sys import argv, exit

    custom_header = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {argv[2]}',
            'X-GitHub-Api-Version': '2022-11-28',
            }
    response = requests.get(f'https://api.github.com/users/{argv[1]}', headers=custom_header)
    if (response.status_code != 200):
        print("None")
        exit()
    response_json = response.json()
    print(f"{response_json['id']}")
