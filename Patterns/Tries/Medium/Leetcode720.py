import collections


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        cur.word = word

    def bfs(self):
        q = collections.deque([self.root])
        res = ''
        while q:
            cur = q.popleft()
            for n in cur.children.values():
                if n.isEnd:
                    q.append(n)
                    if len(n.word) > len(res) or n.word < res:
                        res = n.word
        return res


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)

        return trie.bfs()
words = ["w", "wo", "wor", "worl", "world"]
words2 = ["a","banana","app","appl","ap","apply","apple"]

print(longestWord(words))