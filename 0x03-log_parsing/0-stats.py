#!/usr/bin/python3
"""Log parsing script that reads stdin line by line and computes metrics"""

import sys
import signal
import re


def print_stats():
    """Prints total file size and status code counts"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    log_pattern = re.compile(
        r'^(\d{1,3}\.){3}\d{1,3} - \[[^\]]+\] '
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = log_pattern.match(line)
            if not match:
                continue

            status_code = match.group(2)
            file_size_str = match.group(3)

            try:
                file_size = int(file_size_str)
                total_size += file_size

                if status_code in valid_codes:
                    status_counts[status_code] = status_counts.get(
                        status_code, 0) + 1
            except (ValueError, IndexError):
                continue

            line_count += 1
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        pass
