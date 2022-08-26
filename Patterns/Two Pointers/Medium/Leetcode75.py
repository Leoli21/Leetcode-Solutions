def sortColors(nums):
    nextRed, nextWhite, nextBlue = 0, 0, len(nums) - 1
    # nextWhite pointer can be at the same position as nextBlue as
    # we have never checked what value lies at nextWhite.
    # If we did nextWhite < nextBlue, we end up never checking
    # the value that lies at their meeting point. This would be
    # the value at nextBlue. For example:
    #         nW
    # nums = [2, 0 , 1]
    #         nR     nB
    # Swap values at nW and nB
    # Update nB pointer, but not nW b/c the value at nB was never checked.
    # It could be a 1, which would require us to check it and swap again in next
    # iteration.
    #         nW
    # nums = [1, 0 , 2]
    #         nR nB
    # Swap values at nW and nR and update both pointers. Because at this point:
    # every value to the left of nR would be a zero and everything after nW would
    # be 0's and 1's.
    #            nW
    # nums = [1, 0 , 2]
    #         nR nB
    # Swap value at nW with value at nR and update nR and nW pointers
    #                nW
    # nums = [0, 1 , 2]
    #            nB
    #            nR
    # Terminate as nW has crossed nB. We know that every value to the left of nextRed are zeroes,
    # every value to the left of nW are 0's and 1's, and every value to the right of nextBlue are
    # 2's.
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
