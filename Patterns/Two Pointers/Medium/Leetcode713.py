def numSubarrayProductLessThanK(nums, k):
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