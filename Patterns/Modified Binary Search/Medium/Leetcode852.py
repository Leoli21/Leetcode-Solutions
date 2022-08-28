def peakIndexMountainArray(arr):
    # Edge Case:
    #   If 'arr' contains 3 total elements (index range 0-2),
    #   the peak index must be located at index 1 due to constraints.
    if len(arr) == 3:
        return 1

    # Otherwise, conduct regular binary search
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        # If current element is the peak, both left and right
        # neighboring elements will be less than current element
        if arr[m] > arr[m - 1] and arr[m] > arr[m + 1]:
            return m

        # As long as the current element's index is not 0, we can
        # check to see if the current element's value is less than
        # its previous element.
        # If it is, that means the peak element must be located somewhere
        # to the left of the current element.
        # Adjust search space of indices to: [0, m - 1]
        if m > 0 and arr[m] < arr[m - 1]:
            r = m - 1

        # If current element is 0, then the peak index must be at
        # index 1. Otherwise, if the current element is greater than
        # the previous element, then the peak must be located to the
        # left of current element.
        # Adjust search space of indices to: [m + 1, len(arr) - 1]
        else:
            l = m + 1

# O(n) Solution (Not Optimized but good starting)
def findClosestElements(arr, k, x):
    # Intuition: Use 2 pointers to rule out the furthest element in the current
    # array for each iteration.
    # The reason this works is because it will always be 'True' that either the
    # leftmost or rightmost element in the subarray (eliminated some elements from
    # ends) are the furthest from 'x'.
    # When the size of the window [l, r] becomes k, then we have found the solution
    # If n is the total number of elements, we just need to elminate 'n - k' elements.
    l, r = 0, len(arr) - 1

    # Keep on elminating elements as long as our range [l, r] still contains
    # more than 'k' elements.
    while r - l >= k:
        # If our current leftmost element is the furthest away from 'x', eliminate
        # it from our answer, by increasing our left pointer.
        if x - arr[l] > arr[r] - x:
            l += 1

        # If our rightmost element is the furthest away from 'x', eliminate it from
        # our answer OR if the distances are the same, eliminate element at 'r'.
        # EDGE CASE:
        # If our target, 'x', is smaller than our smallest element in 'arr', eliminate
        # our rightmost element.
        else:
            r -= 1

    # Return our window as an array.
    return arr[l:r + 1]
nums = [3,9,8,6,4]
print(peakIndexMountainArray(nums))