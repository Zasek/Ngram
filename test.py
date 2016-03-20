#!/usr/bin/python3
# -*- coding: utf-8 -*-
#这个文件用来随便写些脚本

import TrieNode
import codecs


class Trie:

    root = TrieNode.Node()
    treelist = dict()

    def insert(self, string):
        index, node = self.findLastNode(string)

        for char in string[index:]:
            new_node = TrieNode.Node()
            node.dic[char] = new_node
            node = new_node
        node.isWord = True
        node.count += 1

    def find(self, string):

        index, node = self.findLastNode(string)
        return index == len(string) and node.isWord

    def findLastNode(self, string):

        node = self.root
        index = 0
        while index < len(string):
            char = string[index]
            if char in node.dic:
                node = node.dic[char]
            else:
                break
            index += 1
        return index, node

    def printTree(self, node, strp):

        if len(node.dic) == 0:
            return
        word = strp
        items = node.dic.items()
        for item in items:
            word += item[0]
            if item[1].isWord:
                print('Word = %s Freq = %d' % (word, item[1].count))
                self.printTree(item[1], word)
            else:
                self.printTree(item[1], word)
            word = strp

    def getrecord(self):

        self.printTree(self.root, '')
        return self.treelist

if __name__ == '__main__':
    tree = Trie()
    STOPWORDS = "D:\\Gdesign\\sougouDic.utf8"
    input_data = codecs.open(STOPWORDS, 'r', 'utf-8')
    for line in input_data.readlines():
        line = line.replace('\n', '')
        tree.insert(line)
    tree.printTree(tree.root, '')
    if tree.find("亲自"):
        print("OK")
    else:
        print("Oh No")
    input_data.close()
