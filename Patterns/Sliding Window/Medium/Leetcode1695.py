def maximumUniqueSubarray(nums):
    l, r = 0, 0
    seen = set()
    currScore = 0
    maxScore = 0

    while r < len(nums):
        if nums[r] not in seen:
            currScore += nums[r]
            maxScore = max(maxScore, currScore)
            seen.add(nums[r])
            r += 1
        else:
            currScore -= nums[l]
            seen.remove(nums[l])
            l += 1
    return maxScore

nums = [5,2,1,2,5,2,1,2,5]
print(maximumUniqueSubarray(nums))