#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import Trie_tree

INPUT_FILE = "D:\\Gdesign\\kai_news_sub_2.utf8"
OUTPUT_FILE = "D:\\Gdesign\\kai_2_gram_freq.utf8"


def two_gram_process():

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    news_tree = Trie_tree.Trie()
    for line in input_data.readlines():

        sents = line.split(';')
        for sent in sents:
            words = sent.split('/')
            length = len(words)
            i = 1
            while i < length-3:
                two_gram = words[i:i+2]
                news_tree.insert(two_gram)
                i += 1
    freq_list = news_tree.getrecord()
    item_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)
    for item in item_list:
        if len(item[0]) != 1:
            output_data.write(item[0]+"     "+str(item[1])+"\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    two_gram_process()