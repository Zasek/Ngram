#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILE = "D:\\Grad\\news_xml.dat"
OUTPUT_FILE = "D:\\Gdesign\\gb2312.dat"


def countline():

    input_data = open(INPUT_FILE, 'rb')
    output_data = codecs.open(OUTPUT_FILE, 'wb')

    count = 0

    for line in input_data.readlines():

        if (count % 6 == 4) and (count <= 800004):
            output_data.write(line)
            count += 1
        else:
            count += 1
            continue

    input_data.close()
    output_data.close()

if __name__ == '__main__':
    countline()
