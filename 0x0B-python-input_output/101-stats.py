#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""


import sys

metrics = {
    'total_size': 0,
    'status_codes': {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0},
    'line_count': 0
}

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 7:
            try:
                status_code, file_size = int(parts[-2]), int(parts[-1])
                metrics['total_size'] += file_size
                metrics['status_codes'][status_code] += 1
                metrics['line_count'] += 1

                if metrics['line_count'] % 10 == 0:
                    print(f"File size: {metrics['total_size']}")
                    for code in sorted(metrics['status_codes']):
                        if metrics['status_codes'][code] > 0:
                            print(f"{code}: {metrics['status_codes'][code]}")

            except ValueError:
                continue

except KeyboardInterrupt:
    pass

print(f"File size: {metrics['total_size']}")
for code in sorted(metrics['status_codes']):
    if metrics['status_codes'][code] > 0:
        print(f"{code}: {metrics['status_codes'][code]}")

