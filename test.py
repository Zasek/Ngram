#!/usr/bin/python3
# -*- coding: utf-8 -*-
#这个文件用来随便写些脚本

import TrieNode
import codecs

if __name__ == '__main__':
    TWO_TABLE = "D:\\Gdesign\\kai_2_gram_dic_filtered.utf8"
    input_data = codecs.open(TWO_TABLE, 'r', 'utf-8')
    line = input_data.readline()
    line = input_data.readline()
    line = line.split(" ")
    print(line[0])
