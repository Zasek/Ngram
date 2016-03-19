#!/usr/bin/python3
# -*- coding: utf-8 -*-
#这个文件用来随便写些脚本

import codecs

INPUT_FILE = "D:\\Gdesign\\sougouDic.utf8"


def readpassage():

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    line = input_data.readline()
    line = line.replace('\n', '')
    print(line)
    line = input_data.readline()
    line = line.replace('\n', '')
    print(line)
    line = input_data.readline()
    line = line.replace('\n', '')
    print(line)

if __name__ == '__main__':
    readpassage()