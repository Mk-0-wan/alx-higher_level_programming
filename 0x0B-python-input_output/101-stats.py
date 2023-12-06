#!/usr/bin/python3
"""Simple Status Code logger written in python"""


def printer(sorted_status_code, total_size):
    """prints the required format to stdout
    Args:
        sorted_status_code (dict): dict having a the code and
        the number of times it appeared
        total_size (int): total value of all the first ten
        codes
    """
    print("File size: {}".format(total_size))
    for code, count in status_totals.items():
        print("{}: {}".format(code, count))


# Entry point
if __name__ == "__main__":
    total_size = 0
    n = -1
    status_x = {}
    try:
        while (line := input()):
            try:
                try:
                    line = line.split()
                    key = line[-2]
                    total_size += int(line[-1])
                    if key not in status_x:
                        status_x[key] = 1
                    else:
                        status_x[key] += 1
                    n += 1
                except (ValueError, TypeError):
                    continue
                if (n + 1) % 10 == 0:
                    status_totals = dict(sorted(status_x.items()))
                    printer(status_totals, total_size)
            except KeyboardInterrupt:
                status_totals = dict(sorted(status_x.items()))
                printer(status_totals, total_size)
        if (n) % 10 != 0:
            status_totals = dict(sorted(status_x.items()))
            printer(status_totals, total_size)
    except EOFError:
        status_totals = dict(sorted(status_x.items()))
        printer(status_totals, total_size)
    except KeyboardInterrupt:
        status_totals = dict(sorted(status_x.items()))
        printer(status_totals, total_size)
        pass
