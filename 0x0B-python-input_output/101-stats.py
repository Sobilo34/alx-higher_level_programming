#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""

def print_stats(size, status_codes):
    """
    Declaration of function to print the computed statistics
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}  # Changed to a set of integers
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            words = line.split()

            try:
                size += int(words[-1])
            except (IndexError, ValueError):
                pass

            try:
                if int(words[-2]) in valid_codes:  # Changed to compare integers
                    status_codes[int(words[-2])] = status_codes.get(int(words[-2]), 0) + 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
