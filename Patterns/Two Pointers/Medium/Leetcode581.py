def findUnsortedSubarray(nums):
    endPointer = 0
    maxSeen = nums[0]

    # Traversing array from left to right (ascending order)
    # This means elements should be increasing as we move to right
    for i in range(1, len(nums)):
        # maxSeen = max(maxSeen, nums[i])
        if nums[i] < maxSeen:
            endPointer = i
        else:
            maxSeen = nums[i]
    startPointer = len(nums) - 1
    minSeen = nums[startPointer]

    # Traversing array from right to left (descending order)
    # This means elements should be decreasing as we move to the left
    for i in range(len(nums) - 2, -1, -1):
        # minSeen = min(minSeen, nums[i])
        if nums[i] > minSeen:
            startPointer = i
        else:
            minSeen = nums[i]

    if endPointer > 0:
        return endPointer - startPointer + 1

    else:
        return 0

nums = [2,6,4,8,10,9,15]
print(findUnsortedSubarray(nums))