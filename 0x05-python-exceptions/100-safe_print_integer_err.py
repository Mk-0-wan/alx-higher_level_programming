#!/usr/bin/python3
def safe_print_integer_err(value):
    if value is not None:
        try:
            print("{:d}".format(value))
            return True
        except (TypeError, ValueError) as err:
            import sys
            sys.stderr.write("Exception:{}\n".format(err))
            return False
    else:
        return None
