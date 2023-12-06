#!/usr/bin/python3
"""Simple Status Code logger written in python"""
import re  # pattern finding
import collections  # faster dictionary creation
import operator  # for faster item retrival from dict


def parse_input(line):
    """Parses the inputs and return the status codes
    file size
    Args:
        line (str): data from the standard input
    Return:
        returns the file size and the status code inside
        the line data from stdinput
    """
    # Define a regular expression to extract relevant information
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] \
            "GET /projects/260 HTTP/1.1" (\d+) (\d+)')
    # Use the regular expression to match the pattern
    match = pattern.match(line)

    if match:
        # Extract information from the match object
        ip_address, date, status_code, file_size = match.groups()

        return file_size, status_code
    else:
        return None


def printer(sorted_status_code, total_size):
    """prints the required format to stdout
    Args:
        sorted_status_code (dict): dict having a the code and
        the number of times it appeared
        total_size (int): total value of all the first ten
        codes
    """
    print("File size: {}".format(total_size))
    for code, count in status_totals:
        print("{}: {}".format(code, count))


# Entry point
while True:
    status_codes_counter = collections.Counter()
    total_size = 0
    try:
        for _ in range(10):
            line = input()
            result = parse_input(line)
            if result is None:
                break
            total_size += int(result[0])
            status_codes_counter.update([result[1]])

        status_totals = sorted(status_codes_counter.items(),
                               key=operator.itemgetter(0))
        printer(status_totals, total_size)
    except KeyboardInterrupt:
        printer(status_totals, total_size)
