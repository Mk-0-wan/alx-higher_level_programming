#!/usr/bin/python3
"""Making a commit request"""

if __name__ == "__main__":
    from sys import argv, exit
    from requests import get

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    git_headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            }
    git_params = {
            'page': 1,
            'per_page': 10,
            }

    response = get(url, git_params, headers=git_headers)
    if (response.status_code != 200):
        print('None')
        exit()

    commits = response.json()
    for commit in commits:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
