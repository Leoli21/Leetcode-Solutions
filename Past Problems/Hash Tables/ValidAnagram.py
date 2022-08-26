import collections


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    counts = collections.Counter(s)

    for c in t:
        if c in counts:
            counts[c] -= 1
        else:
            return False

    return all(val == 0 for val in counts.values())