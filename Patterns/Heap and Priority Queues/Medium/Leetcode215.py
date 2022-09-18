import heapq

# Min Heap
def findKthLargest2(nums, k):
    # Maintains the largest elements in the heap
    minHeap = []
    for num in nums:
        heapq.heappush(minHeap, num)
        # Pop the smallest elements currently in heap from the minHeap
        # Thus, the heap ends up maintaining the kth greatest elements in nums
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    # The value at index 0 of the heap is the smallest out of the other heap elements.
    return minHeap[0]


# Max Heap
def findKthLargest(nums, k):
    nums = [-num for num in nums]
    heapq.heapify(nums)
    for i in range(k - 1):
        heapq.heappop(nums)
    return -nums[0]

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest2(nums, k))

