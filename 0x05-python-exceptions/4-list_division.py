#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element from two lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the resulting list.

    Returns:
        A new list of length list_length with the division results.
    """
result_list = []
    for b in range(0, list_length):
        try:
            div = my_list_1[b] / my_list_2[b]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result_list.append(div)
    return (result_list)
