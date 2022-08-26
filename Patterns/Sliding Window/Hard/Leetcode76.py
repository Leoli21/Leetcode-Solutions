import collections


def minWindow(s, t):
    tCount = collections.Counter(t)
    start, end = 0, 0
    minWindow = ""
    tLen = len(t)

    for end in range(len(s)):
        # If current character exists in 't' string and we still need
        # that character in our window
        if tCount[s[end]] > 0:
            tLen -= 1

        # Characters in 't' would be decremented starting from a count
        # greater than 0 while those not in 't' would be decremented
        # starting from 0. This means when contracting the window, they
        # will always be restored back to 0, while those in 't' should
        # be restored back to its original count if we still need it in
        # the window.
        tCount[s[end]] -= 1

        # Contraction that occurs as long as all needed characters are
        # in window.
        while tLen == 0:
            # Compute curr window length and update if it's
            # shorter than minWindow
            windowLen = end - start + 1
            if not minWindow or windowLen < len(minWindow):
                minWindow = s[start:end + 1]

            # Updating count of letter being removed from window
            tCount[s[start]] += 1

            # If any target character needs to be found again, increase
            # count of needed characters to begin process of expanding
            # window again to find all needed characters.
            if tCount[s[start]] > 0:
                tLen += 1

            start += 1

    return minWindow

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))