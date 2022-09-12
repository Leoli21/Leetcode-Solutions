class TrieNode:
    def __init__(self):
        # HashSet that stores a given node's children
        self.children = {}

        # Marker that checks if the current node is the last character
        # of a word
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            # Check if the current letter in 'word' is a
            # child of the current node. Create a new TrieNode
            # if not for the current node
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move pointer to the next letter
            cur = cur.children[c]

        # 'cur' is at the last letter of word, so set the 'word'
        # attribute for this node to True
        cur.word = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # We have traversed all letters of 'word' and need to check
        # if the node that we are currently at is an end of a word
        return cur.word

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True