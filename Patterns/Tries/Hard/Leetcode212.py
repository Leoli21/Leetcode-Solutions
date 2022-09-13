class TrieNode:
    def __init__(self):
        # Key is the Character and Values are TrieNodes
        self.children = {}
        self.isWord = False

        # Quantifies the amount of times this node is used to construct
        # a word
        self.refs = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self.root
        # Removes a reference from the starting character of the word
        # (one of root's children)
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                # Remove the reference from the character used to form the word
                cur.refs -= 1


class Solution:
    def findWords(self, board, words):
        trie = Trie()

        for w in words:
            trie.addWord(w)

        res = set()
        visit = set()

        def dfs(r, c, node, word):
            # If the direction we are going for DFS is out of bounds
            if r < 0 or c < 0 or r == len(board) or c == len(board[0]):
                return

            # If the letter at (r,c) does not exist (meaning there is no prefix in the trie when this character
            # is added) or if there is no reference for this character left, or if this character at this position
            # has been visited already
            if board[r][c] not in node.children or node.children[board[r][c]].refs < 1 or (r, c) in visit:
                return

            visit.add((r, c))
            # Move our current node position to this character
            node = node.children[board[r][c]]

            # Add the current character at (r,c) to our word
            word += board[r][c]

            if node.isWord:
                node.isWord = False
                res.add(word)
                trie.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Remove the character at position (r,c) after checking all possible prefixes using this character
            visit.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, trie.root, "")

        return res