#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILE = "D:\\Gdesign\\kai_news_sub.utf8"
OUTPUT_FILE = "D:\\Gdesign\\kai_news_sub_2.utf8"

if __name__ == '__main__':

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    for line in input_data.readlines():
        new_line1 = line.replace("１", '1')
        new_line2 = new_line1.replace("２", '2')
        new_line3 = new_line2.replace("３", '3')
        new_line4 = new_line3.replace("４", '4')
        new_line5 = new_line4.replace("５", '5')
        new_line6 = new_line5.replace("６", '6')
        new_line7 = new_line6.replace("７", '7')
        new_line8 = new_line7.replace("８", '8')
        new_line9 = new_line8.replace("９", '9')
        new_line0 = new_line9.replace("０", '0')
        output_data.write(new_line0)
    input_data.close()
    output_data.close()

