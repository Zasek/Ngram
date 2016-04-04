#!/usr/bin/python3
# -*- coding: utf-8 -*-


def isAdjacent(str_1, str_2):
    flag = False
    len_1 = len(str_1)
    pos = 0
    for char in str_2:
        if char == str_1[len_1-1]:
            pos += 1
            break
        else:
            pos += 1
    substr_1 = str_1[-pos:]
    substr_2 = str_2[:pos]
    if substr_1 == substr_2:
        flag = True
    print("pos = ", pos)
    return flag
