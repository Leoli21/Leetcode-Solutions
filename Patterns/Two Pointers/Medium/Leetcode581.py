def findUnsortedSubarray(nums):
    endPointer = 0
    maxSeen = nums[0]

    # Traversing array from left to right (ascending order)
    # In the increasing loop, keeps track of previous maximum value, all numbers
    # followed that is less than that value is out of place -> find the last out of place index
    for i in range(1, len(nums)):
        if nums[i] < maxSeen:
            endPointer = i
        else:
            maxSeen = nums[i]
    startPointer = len(nums) - 1
    minSeen = nums[startPointer]

    # Traversing array from right to left (descending order)
    # in the decreasing loop, keeps track of previous minimum value, all numbers followed
    # that is bigger than that value is out of place -> find the earliest out of place index
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > minSeen:
            startPointer = i
        else:
            minSeen = nums[i]

    if endPointer != 0:
        return endPointer - startPointer + 1

    # This would mean that the endPointer remained  at 0 and that the array is
    # already in ascending order.
    else:
        return 0

nums = [2,6,4,8,10,9,15]
print(findUnsortedSubarray(nums))