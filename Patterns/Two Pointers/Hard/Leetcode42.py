# Solution 1: Max Left, Max Right So Far!
def trap(height):
    n = len(height)
    maxLeft, maxRight = [0] * n, [0] * n

    # No need to calculate the maxLeft at i = 0 because we end up going out of
    # bounds. Thus, we keep the default value of 0 for i = 0 and start at i = 1.
    for i in range(1, n):
        # The max value to our left at 'i' is either the previous (i - 1) max left value
        # or the previous height.
        maxLeft[i] = max(height[i-1], maxLeft[i-1])

    # No need to calculate the maxRight at i = n - 1 because we end up going out of bounds.
    # We know that the max value for our last element is just 0, our default value.
    for i in range(n - 2, -1, -1):
        # The max value to our right at i is either the previous (i + 1) max right value
        # or the height we just visited at i + 1.
        maxRight[i] = max(height[i + 1], maxRight[i+1])

    ans = 0
    # For each index, we calculate our water level (the height that is limiting the amount of
    # water we can trap; essentially our bottleneck). Then we check if that is greater than
    # our current height. If it is, it means we end up with a negative amount of water to trap.
    # Thus, we only update our total water trapped if the waterLevel is greater than our current
    # height at index 'i'.
    for i in range(n):
        waterLevel = min(maxLeft[i], maxRight[i])
        if waterLevel >= height[i]:
            ans += waterLevel - height[i]
    return ans

# Solution 2: Two Pointers (Optimal O(1) space)
def trap2(height):
    # Edge Case: all heights are 0, thus we cannot trap any water
    if not height: return 0

    total = 0
    l, r = 0, len(height) - 1

    # Our leftMax represents the highest bar from left
    leftMax = height[l]

    # Our rightMax represents the highest bar from the right
    rightMax = height[r]

    # Use two pointers to scan the entire array until they meet and cross each other
    # Key Points: any bars in the middle of leftMax bar and rightMax bar will not affect
    # how much water the current position can trap
    while l <= r:

        # How much water a current position depends on the shorter bar. This is because the
        # taller bar may cause water to leak water from the lower side.
        if leftMax < rightMax:
            # Check if our base(land) is lower than the wall.

            # The base (height[l]) is greater than or equal to the wall, thus no water can be held
            # here. Update our wall height.
            if leftMax <= height[l]:
                leftMax = height[l]

            # The land is lower than the wall, thus this position can trap some water.
            else:
                total += leftMax - height[l]
            l += 1

        else:
            # Check if our base(land) is lower than the wall.

            # The base (height[r]) is greater than or equal to the wall, thus no water can be held
            # here. Update our wall height.
            if rightMax <= height[r]:
                rightMax = height[r]

            # The land is lower than the wall, thus this position can trap some water.
            else:
                total += rightMax - height[r]
            r -= 1
    return total