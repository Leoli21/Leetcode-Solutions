import collections

#Longest window we can find with 'k' replacements is:
# longest = majorityCharacter + k
def characterReplacement(s, k):
    count = collections.defaultdict(int)
    maxLength = 0
    l = 0
    maxCount = 0
    for r, c in enumerate(s):
        # Add character to the count dict
        count[c] += 1
        # Key Idea (2): Find the new maxCount. This is much like Kadane's, where we only consider
        # if the new length exceeds the maxLength overall
        # This is essentially checking whether or not after adding 1 to the current letter's count will
        # make it the max letter count. If it does, then make it our new max letter count.
        # This essentially prevents us from constantly searching for the maximum value in
        # our counts dictionary. in the following line (Line 21)
        maxCount = max(maxCount, count[c])

        # Unoptimized:
        # if (r - l + 1) - max(counts.values()) > k:
        if (r - l + 1) - maxCount > k:
            count[s[l]] -= 1
            l += 1

        maxLength = max(maxLength, r - l + 1)
    return maxLength

s= "QQQQBCHIQQD"
k = 2
print(characterReplacement(s,k))