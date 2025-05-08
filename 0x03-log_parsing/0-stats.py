#!/usr/bin/python3
"""Log parsing script that reads stdin line by line and computes metrics"""

import sys
import signal
import re


def print_stats(status_log):
    """Prints total file size and status code counts"""
    print("File size: {}".format(status_log['file_size']))
    for code in sorted(status_log['code_list']):
        print("{}: {}".format(code, status_log['code_list'][code]))


def init_log():
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_log = {
        "file_size": 0,
        "code_list": {str(code): 0 for code in valid_codes}}
    return status_log


def read_line(line, log_pattern, status_log):
    match = log_pattern.match(line)
    if match:
        status_code = match.group(2)
        file_size = match.group(3)

        status_log["file_size"] += int(file_size)

        if status_code.isdecimal():
            status_log["code_list"][status_code] += 1
    return status_log


def main():
    log_pattern = re.compile(
        r'^(\d{1,3}\.){3}\d{1,3} - \[[^\]]+\] '
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )

    status_log = init_log()
    line_count = 0

    for line in sys.stdin:
        line = line.strip()

        line_count = line_count + 1

        logs = read_line(line, log_pattern, status_log)

        if line_count % 10 == 0:
            print_stats(logs)


if __name__ == "__main__":
    main()
