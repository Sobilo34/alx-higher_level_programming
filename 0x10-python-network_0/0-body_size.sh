#!/usr/bin/env bash
# A script that takes in a URL, sends a request to that URL
# It displays the size of the body of the response


curl -s "$1" | wc -c
