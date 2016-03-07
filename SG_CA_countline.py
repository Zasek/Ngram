#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILE = "D:\\Grad\\news_xml.dat"


def countline():

    input_data = codecs.open(INPUT_FILE, 'r')
    line = input_data.readline()
    line = input_data.readline()
    line = input_data.readline()
    line = input_data.readline()
    line = input_data.readline()

    line = unicode()

    print(line)

    input_data.close()

if __name__ == '__main__':
    countline()
