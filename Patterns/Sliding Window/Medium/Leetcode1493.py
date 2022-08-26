def longestSubarray(nums):
    longest = sum = l = 0

    for r, val in enumerate(nums):
        sum += val
        if sum < r -l: # r - l to account for the deletion of at least an element. Even after deletion
                       # of one element, if the sum is still less than the window, it means there exists
                       # more than one zero.
            sum -= nums[l]
            l += 1

        longest = max(longest, r - l)
    return longest

nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))
