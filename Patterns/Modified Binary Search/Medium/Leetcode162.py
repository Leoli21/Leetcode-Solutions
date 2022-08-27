def findPeakElement(nums):
    if len(nums) == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1
    l, r = 1, len(nums) - 2
    while l <= r:
        m = (l + r) // 2

        # Value at mid is our peak element (it is both greater than its left and right neighbors)
        if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
            return m

        # A peak lies to the left of our array, so decrease our search space to [1, m - 1]
        elif nums[m] < nums[m - 1]:
            r = m - 1

        # A peak must lie in the right portion of our array, so decrease our search space to:
        # [m + 1, len(nums) - 2]
        elif nums[m] < nums[m + 1]:
            l = m + 1

    return -1

# Collapse 'l' and 'r' pointers onto the peak element
def findPeakElement(nums):
    if len(nums) == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    n = len(nums)
    if nums[n - 1] > nums[n - 2]:
        return n - 1

    l, r = 1, n - 2
    while l < r:
        m = (l + r) // 2
        if nums[m] <= nums[m + 1]:
            l = m + 1

        else:
            r = m
    return l
