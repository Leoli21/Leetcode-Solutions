def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:

        # Skip the current value at 'l' if it's neighbor is the same
        # b/c there is no point in searching values we have already checked.
        # Decrease our search space by excluding those duplicates.
        # Must first check that 'l' is less than 'r' b/c if 'l' is equal to
        # 'r', we end up including a value outside of our search space (either
        # a value that has already been eliminated from our binary search or an
        # index lying outside our bounds)
        while l < r and nums[l] == nums[l + 1]:
            l += 1

        while r > l and nums[r] == nums[r - 1]:
            r -= 1

        mid = (l + r) // 2
        if nums[mid] == target:
            return True

        if nums[mid] >= nums[l]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1

            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return False

nums = [5,1,3]
target = 2
print(search(nums, target))