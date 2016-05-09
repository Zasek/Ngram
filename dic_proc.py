#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILES = "D:\\Grad\\SougouW\\SogouLabDic_8.dic"
OUTPUT_FILES = "D:\\Gdesign\\Verb_dic.utf8"


def dictionary_p():

    input_data = codecs.open(INPUT_FILES, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILES, 'w', 'utf-8')

    for line in input_data.readlines():
        wline = line.split()
        if len(wline) == 3:
            attr = wline[2].split(',')
            if len(attr) == 2 and attr[0] == 'V':
                output_data.write(wline[0]+'\n')

    input_data.close()
    output_data.close()


if __name__ == '__main__':
    dictionary_p()
