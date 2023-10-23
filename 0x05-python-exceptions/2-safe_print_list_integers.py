#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The from which the elements will be printed from.
        x (int): number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
