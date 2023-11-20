#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    if fct is not None:
        try:
            x = fct(*args)
            return (x)
        except (ZeroDivisionError) as err:
            sys.stderr.write("Exception: {}\n".format(err))
            return None
        except (IndexError) as err2:
            sys.stderr.write("Exception: {}\n".format(err2))
            return None
