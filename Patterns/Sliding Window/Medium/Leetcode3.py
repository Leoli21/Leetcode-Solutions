def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    maxLength = 0

    for r, c in enumerate(s):

        # Encounter already seen character and the previous seen character is
        # in the range of the sliding window.
        if c in seen and seen[c] >= l:
            # Updating the left part of window to exclude the repeated character
            l = seen[c] + 1

        # No repeating character encountered. Just update the length of the longest
        # substring w/o any repeating characters
        else:
            # r - l + 1 to include current character in the length
            maxLength = max(maxLength, r - l + 1)

        # Add the encountered character to dict or update the new position of an
        # already seen character
        seen[c] = r

    return maxLength