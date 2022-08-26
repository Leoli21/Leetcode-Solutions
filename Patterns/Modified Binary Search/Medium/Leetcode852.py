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


nums = [3,9,8,6,4]
print(peakIndexMountainArray(nums))