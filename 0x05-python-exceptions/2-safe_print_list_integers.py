#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of integers to print.

    Returns:
        The number of integers actually printed.
    """
count = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
