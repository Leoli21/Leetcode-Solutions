def findMin(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        # We know that the subarray [m + 1: len(nums) - 1] is unsorted
        # The pivot occurs in this region
        # We exclude value at 'm' because we know that there exists a smaller
        # value to the left of 'm' in the unsorted portion.
        if nums[m] > nums[r]:
            l = m + 1

        # We know that the subarray[0: m] is unsorted.
        # The pivot occurs in this region.
        # We do not exclude value at 'm' because this value could
        # be the minimum in the rotated sorted array
        else:  # nums[m] <= nums[r]
            r = m

    # Return value at 'l' or 'r' because the binary search
    # algo above collapses on a value (where 'l' and 'r' meet)
    return nums[r]

nums = [3,4,5,1,2]
print(findMin(nums))