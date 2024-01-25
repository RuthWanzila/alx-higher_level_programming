#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(lst):
    """Finds a peak in lst"""

    if lst is None or lst == []:
        return None
    low = 0
    high = len(lst)
    middle = ((high - low) // 2) + low
    middle = int(middle)
    if high == 1:
        return lst[0]
    if high == 2:
        return max(lst)
    if lst[middle] >= lst[middle - 1] and lst[middle] >= lst[middle + 1]:
        return lst[middle]
    if middle > 0 and lst[middle] < lst[middle + 1]:
        return find_peak(lst[middle:])
    if middle > 0 and lst[middle] < lst[middle - 1]:
        return find_peak(lst[:middle])
