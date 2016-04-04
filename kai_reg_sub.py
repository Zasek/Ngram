#!/usr/bin/python3
# -*- coding: utf-8 -*-
#用正则表达式将文章中的多余的空格和标点符号去掉

import re
import codecs

INPUT_FILE = "D:\\Gdesign\\news_done.utf8"
OUTPUT_FILE = "D:\\Gdesign\\kai_news_sub.utf8"


def sub_punc():

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    for line in  input_data.readlines():

        str_list = re.split(r'[\s]+', line)
        # \。\，\（\）\！\？\；\：\《\》\“\”\…\—\、\【\】
        for word in str_list:

            if isPunc(word):
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

if __name__ == '__main__':
    sub_punc()
