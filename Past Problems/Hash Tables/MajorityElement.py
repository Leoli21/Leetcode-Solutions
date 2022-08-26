def majorityElement(nums):
    count = 0
    majority = None

    for num in nums:
        if count == 0:
            majority = num
        if num == majority:
            count += 1
        else:
            count -= 1
    return majority

nums = [1,3,4,1,5,1,1,1,1,4,4,1,4,43,3,1,1,1,1,1,1]

print(majorityElement(nums))