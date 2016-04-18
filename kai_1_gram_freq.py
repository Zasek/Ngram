#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import Trie_tree
#
# INPUT_FILE = "D:\\Gdesign\\kai_news_sub_2.utf8"
# OUTPUT_FILE = "D:\\Gdesign\\kai_1_gram_freq.utf8"


def one_gram_process(INPUT_FILE, OUTPUT_FILE):

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    news_tree = Trie_tree.Trie()
    for line in input_data.readlines():

        sents = line.split(';')
        for sent in sents:
            words = sent.split('/')
            length = len(words)
            valid_words = words[1:length-2]
            for word in valid_words:
                news_tree.insert(word)
    freq_list = news_tree.getrecord()
    item_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)
    for item in item_list:
        if len(item[0]) != 1:
            output_data.write(item[0]+"     "+str(item[1])+"\n")

    input_data.close()
    output_data.close()


# def filter_one_char(freq_list):
#
#     prc_list = dict()
#     for item in freq_list:
#         if len(item[0]) == 1:
#             continue
#         else:
#             prc_list[item[0]] = item[1]
#     return prc_list
