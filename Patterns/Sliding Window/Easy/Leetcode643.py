def findMaxAverage(nums, k):
    # Sliding Window
    # Time: O(n)
    # Space: O(k) where k is the size of the subarrays

    if len(nums) == 1:
        return float(nums[0])

    currSum = maxSum = sum(nums[:k])
    for r in range(k, len(nums)):
        currSum += nums[r]
        currSum -= nums[r - k]
        maxSum = max(maxSum, currSum)

    return float(maxSum) / k