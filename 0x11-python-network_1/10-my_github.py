#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
password in this case would be a personal access token
"""
import requests
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
            "https://api.github.com/user", auth=(username, password))

    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)


if __name__ == "__main__":
    main()
