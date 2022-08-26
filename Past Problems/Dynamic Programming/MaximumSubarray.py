def maxSubArray(nums):
    # Time: O(n)
    # Space: O(1)

    currSum, maxSum = nums[0]

    for i in range(1, len(nums)):
        currSum = max(currSum + nums[i], nums[i])
        maxSum = max(maxSum, currSum)
    return maxSum