import codecs
import re
import Trie_tree

INPUT_FILE = "D:\\Gdesign\\1_gram_freq.utf8"
STOPWORDS = "D:\\Gdesign\\stopwords.utf8"
SOUGOUDIC = "D:\\Gdesign\\sougouDic.utf8"
OUTPUT_FILE = "D:\\Gdesign\\1_gram_dic_filtered.utf8"


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

    if dic_tree.find("志坚行苦"):
        print("OOOOHHH")
    else:
        print("FUCK")

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    for line in input_data.readlines():
        words = line.split(' ')
        word = words[0]
        if stop_tree.find(word):
            continue
        if dic_tree.find(word):
            continue
        if re.match(r'\d.', word):
            continue
        if re.match(r'.*\d', word):
            continue
        output_data.write(line)

    output_data.close()
    stop_data.close()
    dic_data.close()
