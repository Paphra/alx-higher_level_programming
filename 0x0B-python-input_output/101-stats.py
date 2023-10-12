#!/usr/bin/python3
"""101-stats module

A Script that reads stdin line by line and computes metrics
"""

import sys
import re


def print_stats(counts, total_size):
    """Prints the stats
    """

    print("File size:", total_size)
    for code in sorted(counts.keys()):
        if counts[code] != 0:
            print("{}: {}".format(code, counts[code]))


pattern = r'(?P<ip>[\d\.]+) - \[.*\] "GET /projects/260 HTTP/1.1" ' + \
    r'(?P<status>\d+) (?P<size>\d+)'
compiled = re.compile(pattern)

# Counters
line_counter = 0
total_size = 0
counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

for line in sys.stdin:
    match = compiled.search(line)

    if match:
        status = match.group("status")
        size = int(match.group('size'))

        total_size += size
        if status in counts:
            counts[status] += 1

        line_counter += 1
        if line_counter % 10 == 0:
            print_stats(counts, total_size)

print_stats(counts, total_size)
