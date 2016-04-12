#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def isStop(word):
    flag = False
    if re.match(r'的', word):
        flag = True
        return flag
    if re.match(r'了', word):
        flag = True
        return flag
    if re.match(r'是', word):
        flag = True
        return flag
    if re.match(r'和', word):
        flag = True
        return flag
    if re.match(r'我', word):
        flag = True
        return flag
    if re.match(r'已', word):
        flag = True
        return flag
    if re.match(r'在', word):
        flag = True
        return flag
    if re.match(r'也', word):
        flag = True
        return flag
    if re.match(r'得', word):
        flag = True
        return flag
    if re.match(r'地', word):
        flag = True
        return flag
    if re.match(r'与', word):
        flag = True
        return flag
    if re.match(r'于', word):
        flag = True
        return flag
    if re.match(r'有', word):
        flag = True
        return flag
    if re.match(r'被', word):
        flag = True
        return flag
    if re.match(r'而', word):
        flag = True
        return flag
    if re.match(r'对', word):
        flag = True
        return flag
    if re.match(r'为', word):
        flag = True
        return flag
    if re.match(r'就', word):
        flag = True
        return flag
    if re.match(r'中', word):
        flag = True
        return flag
    if re.match(r'上', word):
        flag = True
        return flag
    if re.match(r'说', word):
        flag = True
        return flag
    if re.match(r'声明', word):
        flag = True
        return flag
    if re.match(r'表示', word):
        flag = True
        return flag
    if re.match(r'将', word):
        flag = True
        return flag
    if re.match(r'或', word):
        flag = True
        return flag
    if re.match(r'把', word):
        flag = True
        return flag
    if re.match(r'因为', word):
        flag = True
        return flag
    if re.match(r'之', word):
        flag = True
        return flag
    if re.match(r'您', word):
        flag = True
        return flag
    if re.match(r'会', word):
        flag = True
        return flag
    if re.match(r'到', word):
        flag = True
        return flag
    if re.match(r'对', word):
        flag = True
        return flag
    if re.match(r'－', word):
        flag = True
        return flag
    if re.match(r'网', word):
        flag = True
        return flag
    if re.match(r'／', word):
        flag = True
        return flag
    if re.match(r'从', word):
        flag = True
        return flag
    if re.match(r'报道', word):
        flag = True
        return flag
    if re.match(r'如果', word):
        flag = True
        return flag
    return flag
