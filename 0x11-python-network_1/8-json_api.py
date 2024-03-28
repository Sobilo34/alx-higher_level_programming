#!/usr/bin/python3

"""
Python script that takes a query string and sends a POST request to
http://0.0.0.0:5000/search_user with the query string as a parameter.
"""

import sys
import requests


def main():
    if len(sys.argv) == 1:
        query = ""
    else:
        query = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {"query": query}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
