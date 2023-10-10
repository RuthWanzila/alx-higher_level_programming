#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    tuple_x = ()
    if size == 0:
        tuple_x = 0, "None"
    else:
        tuple_x = size, sentence[0]
    return tuple_x
