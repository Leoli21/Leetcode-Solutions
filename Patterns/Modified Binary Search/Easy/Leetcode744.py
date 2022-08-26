def nextGreatestLetter(letters, target):
    # Check for Edge Cases
    # 1. The target is the smallest letter in the input array 'letters'
    # 2. The target is the greatest letter in the input array 'letters'
    if target < letters[0] or target >= letters[-1]:
        return letters[0]

    '''
     Idea:
     Perform Binary Search to collapse our 'l' and 'r' pointers on the 
     next greatest letter of target. In other words, we are moving our 
     'l' and 'r' pointers until they meet at the next greatest letter.
    
     Example #1:
     ["c", "f", "j"] target = "c"

     Initial:

       l    m    r
     ["c", "f", "j"]   "f" > "c"
      Move 'r' to m because letter at 'r' could be the next greatest letter
      and all letters to the right of 'm' would be too large

       l   m,r
     ["c", "f", "j"]

      l,m   r
     ["c", "f", "j"]   "c" == "c"
     Move 'r' to m because we know our answer cannot be the actual target itself,
     but the next letter greater than it. So set 'l' to m + 1

       m    l,r
     ["c", "f", "j"]

     Loop terminates as l == r
     Return letter at 'l' or 'r': "f"
    '''

    l, r = 0, len(letters) - 1
    while l < r:
        m = (l + r) // 2
        if letters[m] <= target:
            l = m + 1

        else:
            r = m
    return letters[r]


letters = ["a", "c", "f", "h", "j", "k", "m", "p", "q", "z"]
target = "l"
print(nextGreatestLetter(letters, target))



