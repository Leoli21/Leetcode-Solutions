def backspaceCompare(s, t):
    sPos = len(s) - 1
    tPos = len(t) - 1

    sSkips, tSkips = 0, 0

    while sPos >= 0 or tPos >= 0:

        # Find next valid character to compare after processing
        # backspace characters
        while sPos >= 0:
            if s[sPos] == '#':
                sSkips += 1
                sPos -= 1
            elif sSkips > 0:
                sSkips -= 1
                sPos -= 1

            # Pointer points to character that is neither a backspace
            # character and all backspaces have been processed
            else:
                break
        # Find next valid character to compare after processing
        # backspace characters
        while tPos >= 0:
            if t[tPos] == '#':
                tPos -= 1
                tSkips += 1
            elif tSkips > 0:
                tPos -= 1
                tSkips -= 1

            # Pointer points to character that is neither a backspace
            # character and all backspaces have been processed
            else:
                break

        # Condition to check that we are not comparing a character with
        # an empty character from empty string
        if (tPos < 0 and sPos >= 0) or (tPos >= 0 and sPos < 0):
            return False

        # Compare the characters as long as both are at a valid position
        # Check that both are at valid positions to avoid Edge Case where
        # both pointers, sPos and tPos are negative (empty strings). If this
        # is the case, it means we are comparing empty strings. We have to include
        # this check b/c if both are at negative positions, we end up checking letters
        # starting from the end of each string. s[-1] and t[-1], which may not be equal,
        # resuting in an untrue return of False.
        if sPos >= 0 and tPos >= 0 and s[sPos] != t[tPos]:
            return False

        # Update pointers after processing the two characters
        # Getting to here means the two characters at two pointers
        # were equal to each other
        sPos -= 1
        tPos -= 1
    return True

s="a##cab##"
t="a##c"
print(backspaceCompare(s,t))