def sortColors(nums):
    nextRed, nextWhite, nextBlue = 0, 0, len(nums) - 1
    while nextWhite <= nextBlue:
        if nums[nextWhite] == 0:
            nums[nextRed], nums[nextWhite] = nums[nextWhite], nums[nextRed]
            nextRed += 1
            nextWhite += 1
        elif nums[nextWhite] == 1:
            nextWhite += 1
        else:
            nums[nextBlue], nums[nextWhite] = nums[nextWhite], nums[nextBlue]
            nextBlue -= 1

nums = [2,0,1]
sortColors(nums)
