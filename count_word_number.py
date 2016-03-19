#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILES = "D:\\Gdesign\\news_sub.utf8"

def count_number():

    input_data = codecs.open(INPUT_FILES, 'r', 'utf-8')
    num = 0

    for line in input_data.readlines():

        wordlist = line.split('/')
#       print(wordlist)
        per_num = len(wordlist)-3
        num += per_num

    print(num)

    #总词数是22252581个

if __name__ == '__main__':
    count_number()
