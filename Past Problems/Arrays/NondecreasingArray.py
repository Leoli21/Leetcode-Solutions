def checkPossibility(nums):
    changes = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            if changes == 1:
                return False
            changes += 1
            if i >= 2 and nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
            else:
                nums[i-1] = nums[i]
nums = [3,4,2,3]
print(checkPossibility(nums))