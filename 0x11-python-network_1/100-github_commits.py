#!/usr/bin/python3
"""
Python script that retrieves the 10 most recent commits of a given repository
by a specified owner using the GitHub API.
"""
import requests
import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: script.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    repo_url = "https://api.github.com/repos"
    url = f"{repo_url}/{owner_name}/{repository_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    main()
