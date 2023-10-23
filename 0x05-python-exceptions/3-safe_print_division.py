#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide two integers and print the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        The result of the division, or None if an exception occurs.
    """
try:
        div_res = a / b
    except (TypeError, ZeroDivisionError):
        div_res = None
    finally:
        print("Inside result: {}".format(div))
    return (div_res)
