def findDisappearedNumbers(nums):
    res = []

    for num in nums:
        index = abs(num) - 1
        nums[index] = abs(nums[index]) * -1

    for i, num in enumerate(nums):
        if num > 0:
            res.append(i + 1)
    return res

nums = [1,1]
print(findDisappearedNumbers(nums))
