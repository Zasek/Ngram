#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import Trie_tree
import re

ORI_FILE = "D:\\Gdesign\\kai_news_sub_2.utf8"
SUM_WORDS = 22252581


def preproc():

    charlist = dict()
    count = 0

    ori_data = codecs.open(ORI_FILE, 'r', "utf-8")
    for line in ori_data.readlines():
        for char in line:
            if char == '/' or char == ';':
                continue
            else:
                if char in charlist:
                    charlist[char] += 1
                else:
                    charlist[char] = 1
                count += 1
    print("count every char finished.")
    ori_data.close()
    return charlist, count


def prob_calculate():

    input_data = codecs.open(ORI_FILE, 'r', "utf-8")

    pair_tree = Trie_tree.Trie()
    pair_freq_dic = dict()
    pair_prob_dic = dict()

    for line in input_data.readlines():
        sentences = line.split(';')
        for sent in sentences:
            words = sent.split('/')
            wlenth = len(words) - 1
            if wlenth == 1:
                continue
            else:
                i = 0
                j = 1
                while j < wlenth-1:
                    index = len(words[i]) - 1
                    first_char = words[i][index]
                    second_char = words[j][0]
                    if re.match(r'\d', first_char) or re.match(r'\d', second_char):
                        i += 1
                        j += 1
                        continue
                    pair = first_char+second_char
                    pair_tree.insert(pair)
                    i += 1
                    j += 1
        # break
    pair_freq_dic = pair_tree.getrecord()
    for worpair in pair_freq_dic:
        pair_prob_dic[worpair] = pair_freq_dic.get(worpair) / SUM_WORDS
    return pair_prob_dic


if __name__ == '__main__':
    # freq_list, sub_num = preproc()
    # char_prob = dict()
    # print("总字数", sub_num)
    # for char in freq_list:
    #     char_prob[char] = freq_list.get(char)/sub_num
    prob_calculate()
