#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILE = "D:\\Gdesign\\news.utf8"
OUTPUT_FILE = "D:\\Gdesign\\news_1.utf8"


def cut():

    input_data = codecs.open(INPUT_FILE, 'r', "utf-8")
    output_data = codecs.open(OUTPUT_FILE, 'w', "utf-8")

    count = 0
    blank = " "

    for line in input_data.readlines():
        count += 1
        if count == 12:
            blank = line
        if line == blank:
            continue
        else:
            output_data.write(line)

    input_data.close()
    output_data.close()

if __name__ == '__main__':
    cut()
