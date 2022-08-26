def fourSum(nums, target):
    def kSum(l, r, target, k, currRes, result):
        # Early termination cases:
        # 1. If the current subarray being evaluated does not contain enough elements to form
        #    a valid quad
        # 2. If the kSum is less than a 2Sum problem
        # 3. If every element in the array is equal to the first element (minimum possible sum)
        #    and it is greater than target, then it is impossible to reach target as sums will
        #    always be greater than target.
        # 4. If every element in the array is equal to the last element (maximum possible sum)
        #    and it is still less than target, then it is impossible to reach target.
        if r - l + 1 < k or k < 2 or target < nums[l] * k or target > nums[r] * k:
            return

        if k == 2:
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum == target:
                    result.append(currRes + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif currSum < target:
                    l += 1
                else:
                    r -= 1

        else:
            for i in range(l, r + 1):
                if i == l or (i > l and nums[i - 1] != nums[i]):
                    kSum(i + 1, r, target - nums[i], k - 1, currRes + [nums[i]], result)

    nums.sort()
    result = []
    kSum(0, len(nums) - 1, target, 4, [], result)
    return result

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))