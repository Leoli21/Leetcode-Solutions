def findAllConcatenatedWordsInADict(self, words):
    words_dict = set(words)
    res = []

    for word in words:
        # Remove the current word from dictionary
        words_dict.remove(word)

        # Check if the current word is a 'concatenated word' (a word that is comprised of
        # two or more shorter words in word dictionary)
        if self.check(word, words_dict):
            res.append(word)

        # Add the current word back for next check
        words_dict.add(word)

    return res

def check(self, word, d):
    # Check if the word (a substring of the original input (word)) exists in the dictionary of words
    if word in d:
        return True

    # Starting from the last index of 'word', start building substrings of the word and check if
    # it exists in the word dictionary. We have to consider breaking the second half of the subtring
    # b/c the second half might contain a word that is in the given array when broken in half.
    for i in range(len(word), 0, -1):
        if word[:i] in d and self.check(word[i:], d):
            return True

    return False