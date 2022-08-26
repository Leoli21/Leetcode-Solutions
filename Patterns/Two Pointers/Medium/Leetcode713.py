def numSubarrayProductLessThanK(nums, k):
    '''
    The key idea here is to use a sliding window of variable size. We should also keep a variable
    that stores the product of our values in the current window.

    Every time we expand our window by adding a new number on the right, we must update our
    product and then check if our window product has exceeded or is equal to 'k'.

    If it is then try to reduce the product by contracting our window (remove elements by moving
    our 'l' pointer and updating window product) until is is strictly less than 'k'.

    For each value introduced with our 'r' pointer (every expansion), our total number of subarrays
    increases by the size of our current window

    For example, if our current window is (5, 6), when we introduce a new value 6, we end up with
    3 new subarrays
         (6)
       (2,6)
     (5,2,6)
    '''
    if k <= 1:
        return 0

    left, prod, count = 0, 1, 0
    for right, val in enumerate(nums):
        prod *= val

        while prod >= k:
            prod /= nums[left]
            left += 1
        count += right - left + 1
    return count