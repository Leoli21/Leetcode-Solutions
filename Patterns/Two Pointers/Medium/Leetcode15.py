def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        # If current position has a previous element and its previous
        # element is a duplicate with previous element, skip it because
        # it can result in duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Relates to key idea:
        # a + b + c = 0 ==> -a = b + c after rearrangement
        target = -1 * nums[i]
        start, end = i + 1, len(nums) - 1

        # Finding two numbers that add up to the target (-1 * nums[i])
        while start < end:
            if nums[start] + nums[end] == target:
                res.append([nums[i], nums[start], nums[end]])
                # Adjust either the start or end pointer
                # We must adjust one of the pointers here b/c there can only be one answer for:
                # [nums[i], nums[start]]
                # Thus, we have already found that answer in our input array and we have to find
                # another answer.
                start += 1

                # Update start pointer again if the value that current start pointer points to
                # is the same as the previous value
                while start < end and nums[start] == nums[start - 1]:
                    start += 1

            # Sum of two numbers is less than target, adjust start b/c
            # we need a greater sum. Adjusting the left pointer gives us
            # a greater sum.
            elif nums[start] + nums[end] < target:
                start += 1

            # Sum of two numbers is greater than target, adjust end b/c
            # we need a lesser sum. Adjusting the right pointer gives us
            # a smaller sum.
            else:
                end -= 1
    return res