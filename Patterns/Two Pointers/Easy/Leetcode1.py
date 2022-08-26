def twoSum(nums, target):
    seen = {}
    for i, val in enumerate(nums):
        comp = target - val
        if comp in seen:
            return [i, seen[comp]]
        seen[val] = i