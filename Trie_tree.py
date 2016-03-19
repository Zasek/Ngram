#!/usr/bin/python3
# -*- coding: utf-8 -*-

import TrieNode


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
                self.treelist[word] = item[1].count
                self.printTree(item[1], word)
            else:
                self.printTree(item[1], word)
            word = strp

    def getrecord(self):

        self.printTree(self.root, '')
        return self.treelist

# if __name__ == '__main__':
#     tree = Trie()
#     tree.insert("苹果")
#     tree.insert("苹果")
#     tree.insert("苹果")
#     tree.insert("苹果")
#     tree.insert("苹果派")
#     tree.insert("申请")
#     tree.printTree(tree.root, '')
#     if tree.find("苹果派"):
#         print("OK")
#     else:
#         print("Oh No")
