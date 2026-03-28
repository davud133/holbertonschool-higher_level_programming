#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except TypeError as err:
        print("Exception: " + str(err), file=sys.stderr)
        return False
    except ValueError as err:
        print("Exception: " + str(err), file=sys.stderr)
        return False
    return True
