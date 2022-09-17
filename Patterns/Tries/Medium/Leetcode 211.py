class LetterNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = LetterNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = LetterNode()
            cur = cur.children[c]

        cur.isWord = True


    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return node.isWord

            if word[i] == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True

            else:
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                return dfs(i + 1, node)
        return dfs(0, self.root)
