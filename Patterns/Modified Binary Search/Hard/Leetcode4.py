def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return self.findMedianSortedArrays(nums2, nums1)

    x, y = len(nums1), len(nums2)

    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

            else:
                return max(maxLeftX, maxLeftY)

        # Too far on the right for partition of X array. This means we need to
        # include more values of Y by reducing the number of values in our X
        # partition.
        elif maxLeftX > minRightY:
            high = partitionX - 1

        # Too far on the left for partition of X array. This means we need to include
        # more values of X by increasing the number of values in our X partition and
        # thereby reducing the number of elements in our Y partition.
        else:
            low = partitionX + 1
