def minimalDifference(nums, k):
    if len(nums) == 1:
        return 0
    # To ensure that the value at left end of window is
    # smallest value in the window and value at right end
    # of window is always the largest, we sort the input array.
    # This prevents an O(n^2) solution.
    nums.sort()

    # Setting the current minDiff as the difference of the first
    # possible window
    minDiff = nums[k - 1] - nums[0]

    # Starting our traversal from the second possible window b/c
    # our starting minDiff already took care of first window
    for i in range(1, len(nums) - k + 1):
        currDiff = nums[i + k - 1] - nums[i]
        minDiff = min(minDiff, currDiff)

    return minDiff
