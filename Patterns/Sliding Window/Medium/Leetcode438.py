import collections

def findAnagrams(s, p):
    count = collections.Counter(p)

    out = []

    l = 0
    for r, c in enumerate(s):
        count[c] -= 1

        while count[c] < 0:
            count[s[l]] += 1
            l += 1

        if r - l + 1 == len(p):
            out.append(l)

    return out

