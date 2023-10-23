#!/usr/bin/python3
def safe_print_integer_err(value):
    """Print an integer and handle errors.

    Args:
        value(int): The value to print.

    Returns:
        True if the value is an integer and printed correctly,
        False otherwise.
    """
try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
