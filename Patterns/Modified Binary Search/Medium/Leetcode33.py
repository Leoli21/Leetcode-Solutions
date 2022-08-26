def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        # Check if value at mid is equal to the target. Return if it is.
        if nums[mid] == target:
            return mid

        # Check if the left partition is strictly increasing. '=' to factor in
        # the case where there are only two elements left in the search space.
        # In this case, 'l' and 'mid' might be pointing at the same element.
        # The reason our 'l' and 'mid' might be pointing at same element when there are
        # only two elements left is because of the calculation in line 4:
        # mid = (l + r) // 2.
        # This calculation always rounds our answer down to the index at 'l' rather than
        # the index at 'r'.
        if nums[mid] >= nums[l]:
            # At this point, we know that the left partition is strictly increasing.
            # Check if the target value lies within this increasing portion of the
            # input array.
            # Adjusting our remaining search space to be:
            # [l, mid - 1]
            if nums[l] <= target < nums[mid]:
                r = mid - 1

            # The target does not lie within the partition range and thus it must either
            # lie in the right partition (not strictly increasing subarray) or simply does
            # not exist in the left partition (This means that the number is not in our 'nums'
            # array.
            # Adjust our search space to be:
            # [mid + 1, r]
            else:
                l = mid + 1

        # Our right partition (elements to the right of the calculated mid element) is
        # strictly increasing.
        else:
            # At this point, we know that the right partition is strictly increasing.
            # Now we check if the target lies within the range (mid, right]. If it does,
            # we update our remaining search space for target to be [mid + 1, r]
            if nums[mid] < target <= nums[r]:
                l = mid + 1

            # The target does not lie withing the current partition range and thus it
            # might either lie i the left partition (not strictly increasing subarray
            # portion) or it simply does not exist in our right partition (this would
            # mean that the target is not even in our input array in the first place)
            # Thus, our search space gets adjusted to: [l, mid - 1]
            else:
                r = mid - 1
    return -1