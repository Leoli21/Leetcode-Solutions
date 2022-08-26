def longestOnes(nums, k):
    l = 0
    for r, val in enumerate(nums):
        if val == 0:
            k -= 1

        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1

    return r - l + 1

nums = [1,1,1,0,0,1,0,1,0,0,0,0,0]
k = 3

print(longestOnes(nums, k))