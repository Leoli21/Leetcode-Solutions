def isIsomorphic(s,t):
    sToT = {}
    tToS = {}

    for i in range(len(s)):
        # If character in strings are not mapped yet
        if s[i] not in sToT and t[i] not in tToS:
            sToT[s[i]] = t[i]
            tToS[t[i]] = s[i]

        # If one of the characters in the one of the two strings have already been mapped
        # but mapped to a different character than the current letter in other string.
        if sToT.get(s[i]) != t[i] or tToS.get(t[i]) != s[i]:
            return False
    return True

s = "badc"
t = "baba"

print(isIsomorphic(s,t))