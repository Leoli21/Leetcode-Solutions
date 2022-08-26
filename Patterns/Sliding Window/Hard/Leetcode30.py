import collections


def findSubstring(s, words):
    res = []
    wordsNeeded = collections.Counter(words)
    wordsMissing = len(words)  # Number of words needed to form a substring using all words in 'words' array
    wordsLength = len(words[0])
    substrLength = wordsMissing * wordsLength
    for left in range(0, len(s) - substrLength + 1):
        # Create a copy of the Counter variable storing the counts of each word we need
        # to form a valid substring
        neededWords = dict(wordsNeeded)

        # Create a copy of the counts variable that keeps track of how many words we need left to form a
        # valid substring.
        missingWords = wordsMissing
        for right in range(left, left + substrLength, wordsLength):
            currWord = s[right: right + wordsLength]
            # If the value for the currWord in the "neededWords" counter is greater than 0, that
            # means we still require an occurrence of "currWord". This means we can decrease
            # the number of words we are still missing.
            if currWord in neededWords and neededWords[currWord] > 0:
                neededWords[currWord] -= 1
                missingWords -= 1

            # Means the current word is not a valid word or we do not need that word
            # anymore to form a substring as it has already been used.

            # We break from the loop b/c the moment we reach this 'else' block, we know
            # the current substring from [l: l + substrLength] cannot be a valid substring
            # as it must only contain words from "words" and not include any duplicates.
            else:
                break

        if missingWords == 0:
            res.append(left)

    return res

s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words))