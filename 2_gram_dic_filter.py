import codecs
import re
import Trie_tree

INPUT_FILE = "D:\\Gdesign\\kai_2_gram_freq_test.utf8"
STOPWORDS = "D:\\Gdesign\\stopwords.utf8"
SOUGOUDIC = "D:\\Gdesign\\sougouDic.utf8"
OUTPUT_FILE = "D:\\Gdesign\\kai_2_gram_freq_test_filtered.utf8"


def isStop(word):
    flag = False
    if re.match(r'.*的.*', word):
        flag = True
        return flag
    if re.match(r'.*了.*', word):
        flag = True
        return flag
    if re.match(r'.*是.*', word):
        flag = True
        return flag
    if re.match(r'.*和', word):
        flag = True
        return flag
    if re.match(r'.*我.*', word):
        flag = True
        return flag
    if re.match(r'.*已.*', word):
        flag = True
        return flag
    if re.match(r'.*在.*', word):
        flag = True
        return flag
    if re.match(r'.*也.*', word):
        flag = True
        return flag
    if re.match(r'.*得.*', word):
        flag = True
        return flag
    if re.match(r'.*地.*', word):
        flag = True
        return flag
    if re.match(r'.*与.*', word):
        flag = True
        return flag
    if re.match(r'.*于.*', word):
        flag = True
        return flag
    if re.match(r'.*有.*', word):
        flag = True
        return flag
    if re.match(r'.*被.*', word):
        flag = True
        return flag
    if re.match(r'.*一', word):
        flag = True
        return flag
    if re.match(r'.*而', word):
        flag = True
        return flag
    if re.match(r'对.*', word):
        flag = True
        return flag
    if re.match(r'为.*', word):
        flag = True
        return flag
    if re.match(r'.*就', word):
        flag = True
        return flag
    if re.match(r'.*中', word):
        flag = True
        return flag
    if re.match(r'.*上', word):
        flag = True
        return flag
    if re.match(r'.*说.*', word):
        flag = True
        return flag
    if re.match(r'.*声明.*', word):
        flag = True
        return flag
    if re.match(r'.*表示.*', word):
        flag = True
        return flag
    if re.match(r'将.*', word):
        flag = True
        return flag
    if re.match(r'.*或.*', word):
        flag = True
        return flag
    if re.match(r'把.*', word):
        flag = True
        return flag
    if re.match(r'.*因为.*', word):
        flag = True
        return flag
    if re.match(r'之.*', word):
        flag = True
        return flag
    if re.match(r'.*您.*', word):
        flag = True
        return flag
    if re.match(r'会.*', word):
        flag = True
        return flag
    if re.match(r'到.*', word):
        flag = True
        return flag
    if re.match(r'.*对', word):
        flag = True
        return flag
    if re.match(r'.*－.*', word):
        flag = True
        return flag
    if re.match(r'.*网.*', word):
        flag = True
        return flag
    if re.match(r'.*／.*', word):
        flag = True
        return flag
    return flag


if __name__ == '__main__':
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    stop_data = codecs.open(STOPWORDS, 'r', 'utf-8')
    stop_tree = Trie_tree.Trie()

    for stop_word in stop_data.readlines():
        stop_word = stop_word.replace('\n', '')
        stop_tree.insert(stop_word)

    dic_data = codecs.open(SOUGOUDIC, 'r', 'utf-8')
    dic_tree = Trie_tree.Trie()

    for n_word in dic_data.readlines():
        n_word = n_word.replace('\n', '')
        dic_tree.insert(n_word)

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    for line in input_data.readlines():
        words = line.split(' ')
        # word = words[2]
        # word = word.replace('\n', '')
        word = words[0]
        if stop_tree.find(word):
            continue
        if dic_tree.find(word):
            continue
        if re.match(r'\d.', word):
            continue
        if re.match(r'.*\d', word):
            continue
        if isStop(word):
            continue
        output_data.write(line)

    output_data.close()
    stop_data.close()
    dic_data.close()
