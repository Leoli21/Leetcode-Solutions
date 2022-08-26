def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    # Reverse entire array
    reverse(nums, 0, len(nums) - 1)

    # Reverse first k -1  elements
    reverse(nums, 0, k - 1)

    # Reverse remaining elements
    reverse(nums, k, len(nums) - 1)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)

print(nums)
