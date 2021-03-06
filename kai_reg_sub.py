#!/usr/bin/python3
# -*- coding: utf-8 -*-
#用正则表达式将文章中的多余的空格和标点符号去掉

import re
import codecs
import Trie_tree

INPUT_FILE = "D:\\Gdesign\\news_done.utf8"
STOP_INPUT = "D:\\Gdesign\\stopwords.utf8"
VERB_INPUT = "D:\\Gdesign\\Verb_dic.utf8"
OUTPUT_FILE = "D:\\Gdesign\\kaisan_news_sub.utf8"


def sub_punc(stop_list, verb_tree):

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    for line in  input_data.readlines():

        str_list = re.split(r'[\s]+', line)
        # \。\，\（\）\！\？\；\：\《\》\“\”\…\—\、\【\】
        for word in str_list:

            if isPunc(word) or isStopword(word, stop_list) or verb_tree.find(word):
                output_data.write(";")
            else:
                output_data.write(word + "/")
        output_data.write('\n')

    input_data.close()
    output_data.close()


def isPunc(word):

    flag = False

    pun_list = ("。", "，", "（", "）", "！", "？", "；", "：", "《", "》", "“", "”", "…", "—", "、", "【", "】")

    for char in pun_list:
        if word == char:
            flag = True
            break
        else:
            continue
    return flag


def isStopword(word, stop_list):

    flag = False

    for char in stop_list:
        if word == char:
            flag = True
            break
        else:
            continue
    return flag

if __name__ == '__main__':

    stop_data = codecs.open(STOP_INPUT, 'r', 'utf-8')
    stop_list = list()

    for line in stop_data.readlines():
        line = line.replace('\n', '')
        line = line.replace('\ufeff', '')
        stop_list.append(line)

    verb_data = codecs.open(VERB_INPUT, 'r', 'utf-8')
    verb_tree = Trie_tree.Trie()
    for v_word in verb_data.readlines():
        v_word = v_word.replace('\n', '')
        verb_tree.insert(v_word)

    sub_punc(stop_list, verb_tree)
