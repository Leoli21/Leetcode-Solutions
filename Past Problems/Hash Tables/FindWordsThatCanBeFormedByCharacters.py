import collections


def countCharacters(words, chars):
    total = 0
    charCount = collections.Counter(chars)

    for word in words:
        include = True
        wordCount = collections.Counter(word)
        for c in word:
            if wordCount[c] > charCount[c]:
                include = False
                break

        if include:
            total += len(word)

    return total