def findMedianSortedArrays(nums1, nums2):
    # Perform Binary Search on the Smaller Array so that we decrease
    # the number of searhces
    if len(nums1) > len(nums2):
        return self.findMedianSortedArrays(nums2, nums1)

    x, y = len(nums1), len(nums2)

    low, high = 0, x

    while low <= high:
        # Get number of elements we are partitioning for both arrays
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # Calculate the 4 Boundary Number of each partition that will be used for
        # comparison
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]

        # We dont need to subtract from partitionX b/c partitionX represents the length
        # of our first half of X partition. Thus, the index at partitionX, would be the
        # first element of our second half of the partition.
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        # Correct Partition Found
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Even Total Length
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

            # Odd Total Length
            else:
                return max(maxLeftX, maxLeftY)

        # Too far on the right for partition of X array. This means we need to
        # include more values of Y by reducing the number of values in our X
        # partition. We need smaller elements for X left partition and larger
        # elements in Y right partition.
        elif maxLeftX > minRightY:
            high = partitionX - 1

        # Too far on the left for partition of X array. This means we need to include
        # more values of X by increasing the number of values in our X partition and
        # thereby reducing the number of elements in our Y partition. This leads us to
        # having a greater maxLeftX and smaller minRightY.
        else: # maxLeftY > minRightX
            low = partitionX + 1
