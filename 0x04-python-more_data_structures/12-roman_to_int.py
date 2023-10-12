#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    length = len(roman_string)

    for i in range(length):
        c = roman_string[i]

        if c not in roman_numerals:
            return 0

        value = roman_numerals[c]

        if i < length - 1:
            nc = roman_string[i + 1]
            if nc in roman_numerals and roman_numerals[nc] > value:
                result -= value
                continue

        result += value

    return result
