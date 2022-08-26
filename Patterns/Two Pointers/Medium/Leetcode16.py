def threeSumClosest(nums, target):
    nums.sort()
    closest = sum(nums[:3])
    for left in range(len(nums) - 2):
        mid, right = left + 1, len(nums) - 1

        # Perform 2Sum problem
        while mid < right:
            currSum = nums[left] + nums[mid] + nums[right]

            # If found target, no sum can be closer than the actual target, so just
            # return the target or current sum
            if currSum == target:
                return currSum

            # Update Check:
            # Checking whether the currSum is closer to the target than the previously
            # found closest sum.
            # If so, update teh closest sum to the currSum
            # Otherise, begin updating pointers accordingly.
            if abs(currSum - target) < abs(closest - target):
                closest = currSum
            # If the current sum is smaller than the target, we need larger numbers,
            # so update our left pointer (which is causing our sum to be smaller)
            if currSum < target:
                mid += 1

            # The current sum is greater than the target, so we need smaller numbers.
            # Update our right pointer (which is causing our sum to be greater)
            else:
                right -= 1
    return closest