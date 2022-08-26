import collections


def checkInclusion(s1, s2):
    s1Count = collections.Counter(s1)
    windowLen = len(s1)
    # Keeps track of how many matches we have in current window
    # If it reaches the length of the s1, there is a permutation
    matches = 0

    for i in range(len(s2)):
        # Check if current letter is in Counter
        if s2[i] in s1Count:
            # Decrease count by 0
            s1Count[s2[i]] -= 1

            # If count reaches 0, it means we have reached the exact amount of that letter
            # that we need in our window for there to be a permutation
            if s1Count[s2[i]] == 0:
                matches += 1

        # Check if the length of the window has been exceeded and whether
        # the letter located on left of window is a required letter for a permutation
        if i >= windowLen and s2[i - windowLen] in s1Count:
            # Check if it was a neccesary letter for there to be a permutation
            if s1Count[s2[i - windowLen]] == 0:
                matches -= 1

            # Reset its count as it is not in current window anymore
            s1Count[s2[i - windowLen]] += 1

        # Check if our current window has all the correct counts of letters
        # needed for a permutation. This means our window not only contains all
        # the characters for a permutation but also their respective counts.
        # This means that the input string, s1, could contain duplicates of
        # characters.
        if matches == len(s1Count):
            return True
    return False


s1 = "ab"
s2 = "eidboaoo"

print(checkInclusion(s1, s2))
