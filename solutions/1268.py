"""
trie树模板
"""

from typing import List
from typing import Optional
import math

def charToInt(ch):
    return ord(ch) - ord('a')

def intToChar(i):
    return chr(ord('a')+i)

class Node:
    def __init__(self, char) -> None:
        self.nodes = [None for _ in range(26)]
        self.char = char
        self.hasWord = False

class Trie:
    def __init__(self) -> None:
        self.root = Node("#")

    def addWord(self, word):
        cur = self.root
        for ch in word:
            if cur.nodes[charToInt(ch)] is None:
                cur.nodes[charToInt(ch)] = Node(ch)
            cur = cur.nodes[charToInt(ch)]
        cur.hasWord = True

    def isWord(self, word):
        cur = self.root
        for ch in word:
            if cur.nodes[charToInt(ch)] is None:
                return False
            cur = cur.nodes[charToInt(ch)]
        return cur.hasWord

    def findFirstThreeWord(self, cur, word, words):
        if cur is None and len(words) >= 3:
            return
        if cur.hasWord:
            words.append(word)
        if len(words) >= 3:
            return
        for i in range(26):
            if cur.nodes[i]:
                self.findFirstThreeWord(cur.nodes[i], word+intToChar(i), words)
                if len(words) == 3:
                    return
    
    def searchPrompt(self, prompt):
        cur = self.root
        for ch in prompt:
            if cur.nodes[charToInt(ch)]:
                cur = cur.nodes[charToInt(ch)]
            else:
                return []
        words = []
        self.findFirstThreeWord(cur, "", words)
        return [prompt+word for word in words]

    def continuousSearchPrompt(self, prompt):
        ans = []
        cur = self.root
        noMore = False
        for i, ch in enumerate(prompt):
            if noMore:
                ans.append([])
                continue
            if cur.nodes[charToInt(ch)]:
                words = []
                self.findFirstThreeWord(cur.nodes[charToInt(ch)], prompt[:i+1], words)
                ans.append(words)
                cur = cur.nodes[charToInt(ch)]
            else:
                ans.append([])
                noMore = True
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.addWord(word)
        ans = trie.continuousSearchPrompt(searchWord)
        return ans

s = Solution()
sol = s.suggestedProducts(["havana"], "tatiana")
print(sol)