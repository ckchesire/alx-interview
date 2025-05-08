#!/usr/bin/python3
"""Log parsing script that reads stdin line by line and computes metrics"""
import sys
import signal
import re

total_size = 0
status_cnts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

log_pattern = re.compile(
    r'^(\d{1,3}\.){3}\d{1,3} - \[[^\]]+\] '
    r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_cnts.keys()):
        print("{}: {}".format(code, status_cnts[code]))


def signal_handler(sig, frame):
    """Handles CTRL+C interruption"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

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
                status_cnts[status_code] = status_cnts.get(status_code, 0)+1

        except ValueError:
            continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
