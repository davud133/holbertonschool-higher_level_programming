#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except TypeError as err:
        print(err)
        return False
    except ValueError as err:
        print(err)
        return False
    return True
