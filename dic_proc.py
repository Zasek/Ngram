#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILES = "D:\\Grad\\SougouW\\SogouLabDic_8.dic"
OUTPUT_FILES = "D:\\Gdesign\\sougouDic.utf8"


def dictionary_p():

    input_data = codecs.open(INPUT_FILES, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILES, 'w', 'utf-8')

    for line in input_data.readlines():
        wline = line.split()
        word = wline[0]
        output_data.write(word+"\n")

if __name__ == '__main__':
    dictionary_p()
