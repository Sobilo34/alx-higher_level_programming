#!/bin/bash
# This is to sends a DELETE request to URL passed as the first argument & displays the body of the response
curl -s -X DELETE "$1"
