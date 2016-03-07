#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILE = "D:\\Grad\\news_xml.dat"
OUTPUT_FILE = "D:\\Grad\\news_part.dat"


def countline():

    input_data = codecs.open(INPUT_FILE, 'rb')
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
