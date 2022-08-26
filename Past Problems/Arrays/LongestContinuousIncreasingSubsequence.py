def findLengthOfLCIS(nums):
    length = anchor = 0
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] >= nums[i]:
            anchor = i
        length = max(length, i - anchor + 1)
    return length
    '''
    maxLength = 1
    currLength = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            currLength += 1
        else:
            maxLength = max(maxLength, currLength)
            currLength = 1
    return max(maxLength, currLength)
    '''

nums = [1,3,5,4,2,3,4,5]
print(findLengthOfLCIS(nums))