# 1876. Substrings of Size Three with Distinct Characters

def countGoodSubstrings(s):
    count = 0
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) == 3:
            count += 1
    return count

s = "aababcabc"
print(countGoodSubstrings(s))