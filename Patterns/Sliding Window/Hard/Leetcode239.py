import collections

def maxSlidingWindow(nums, k):
    q = collections.deque()
    res = []

    for i, val in enumerate(nums):
        while q and nums[q[-1]] <= val:
            # Pop last element of queue out b/c it is less than or equal to current element
            q.pop()

        # Add current element index after everything smaller than it is popped out of
        # queue
        q.append(i)

        # Remove first element if it's outside the window
        if q[0] == i - k:
            q.popleft()

        # When window length is k elements, add to results
        # This is because for the first k - 1 elements: we have less than k elements b/c
        # we start from an empty window and add 1 element for each iteration.
        if i >= k - 1:
            res.append(nums[q[0]])

    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))