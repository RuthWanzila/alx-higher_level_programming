#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list from which the elements will be printed from.
        x (int): The number of elements to be printed from my list.

    Returns:
        number of elements printed.
    """
    count = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
