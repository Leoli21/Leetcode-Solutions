import collections

def sortedSquares(nums):
    res = collections.deque()
    l, r = 0, len(nums) - 1
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            # By appending left, we end up maintaining the greater squares to the
            # right side of the deque
            res.appendleft(nums[l] ** 2)
            l += 1
        else:
            # By appending left, we end up maintaining the greater squares to the
            # right side of the deque
            res.appendleft(nums[r] ** 2)
            r -= 1
    return list(res)