def minSubarrayLen(target, nums):
    l = currSum = 0
    minLen = len(nums) + 1
    for r, val in enumerate(nums):
        currSum += val
        # Reduce our window until our window sum is less than
        # the target
        while currSum >= target:
            minLen = min(minLen, r - l + 1)
            currSum -= nums[l]
            l += 1

    # Return the actual minLen value if it has been updated from
    # its default value (len(nums) + 1) otherwise return 0.
    return minLen if minLen != len(nums) + 1 else 0

