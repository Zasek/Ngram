#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILES = "D:\\Gdesign\\kai_2_gram_freq_test_filtered.utf8"
OUTPUT_FILES = "D:\\Gdesign\\kai_2_gram_freq_test_fin.utf8"


def del_1_freq():

    input_data = codecs.open(INPUT_FILES, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILES, 'w', 'utf-8')

    for line in input_data.readlines():

        line = line.split()
        if int(line[1]) > 1:
            output_data.write(line[0]+"    "+line[1])
            output_data.write('\n')
        else:
            continue

    input_data.close()
    output_data.close()

if __name__ == '__main__':
    del_1_freq()