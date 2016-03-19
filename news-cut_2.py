#!/usr/bin/python3
# -*- coding: utf-8 -*-
#本程序运行过一次以后就没什么用了

import codecs

INPUT_FILE = "D:\\Gdesign\\news_2.utf8"
OUTPUT_FILE = "D:\\Gdesign\\news_2.utf8"


def cut_2():

    input_data = codecs.open(INPUT_FILE, 'r', "utf-8")
    #output_data = codecs.open(OUTPUT_FILE, 'w', "utf-8")
    old_1 = "<content>"
    old_1.encode('utf-8')
    old_2 = "</content>"
    old_2.encode('utf-8')

    for line in input_data.readlines():

        line_1 = line.replace(old_1, "")
        line_2 = line_1.replace(old_2, "")
        print(line_2)
        break

    input_data.close()
    #output_data.close()

if __name__ == '__main__':
    cut_2()
