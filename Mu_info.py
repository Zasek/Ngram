#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import Trie_tree
import re

ORI_FILE = "D:\\Gdesign\\kaisan_news_sub_2.utf8"
OUT_FILE = "D:\\Gdesign\\Intresting_kaisan.utf8"
SOUGOUDIC = "D:\\Gdesign\\sougouDic.utf8"
TWO_TABLE = "D:\\Gdesign\\kaisan_2_gram_dic_fin.utf8"
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
                    if index < 0:
                        i += 1
                        j += 1
                        continue
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
    input_data.close()
    return pair_prob_dic


def mutual_check(char_prob, pair_prob_dic):

    input_data = codecs.open(ORI_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUT_FILE, 'w', 'utf-8')

    dic_data = codecs.open(SOUGOUDIC, 'r', 'utf-8')
    dic_tree = Trie_tree.Trie()

    for n_word in dic_data.readlines():
        n_word = n_word.replace('\n', '')
        dic_tree.insert(n_word)

    filtered_data = codecs.open(TWO_TABLE, 'r', 'utf-8')
    filtered_tree = Trie_tree.Trie()

    for twogramw in filtered_data.readlines():
        gram_word = twogramw.split(" ")
        filtered_tree.insert(gram_word[0])

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
                    if index < 0:
                        i += 1
                        j += 1
                        continue
                    first_char = words[i][index]
                    second_char = words[j][0]
                    if re.match(r'\d', first_char) or re.match(r'\d', second_char):
                        i += 1
                        j += 1
                        continue
                    else:
                        prob_cal = char_prob[first_char] * char_prob[second_char]
                        prob_index = pair_prob_dic.get(first_char+second_char)
                        if prob_index > 0 and prob_index/prob_cal > 20:
                            if (not dic_tree.find(words[i]+words[j])) and (not filtered_tree.find(words[i]+words[j])):
                                output_data.write("interesting:  " + words[i]+words[j] + '\n')
                                pair_prob_dic[first_char+second_char] = -1
                    i += 1
                    j += 1

    dic_data.close()
    filtered_data.close()
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    freq_list, char_num = preproc()
    char_prob = dict()
    print("总字数", char_num)
    for char in freq_list:
        char_prob[char] = freq_list.get(char)/char_num

    pair_prob_dic = prob_calculate()
    mutual_check(char_prob, pair_prob_dic)

