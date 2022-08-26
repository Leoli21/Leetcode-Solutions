# Solution 1: Max Left, Max Right So Far!
def trap(height):
    n = len(height)
    maxLeft, maxRight = [0] * n, [0] * n

    for i in range(1, n):
        maxLeft[i] = max(height[i-1], maxLeft[i-1])
    for i in range(n - 2, -1, -1):
        maxRight[i] = max(height[i + 1], maxRight[i+1])

    ans = 0
    for i in range(n):
        waterLevel = min(maxLeft[i], maxRight[i])
        if waterLevel >= height[i]:
            ans += waterLevel - height[i]
    return ans

# Solution 2: Two Pointers (Optimal O(1) space)
def trap2(height):
    if not height: return 0

    l, r = 0, len(height) - 1
    totalWater = 0
    leftMax, rightMax = height[l], height[r]
    while l < r:
        if leftMax < rightMax:
            if height[l] > leftMax:
                leftMax = height[l]
            else:
                totalWater += leftMax - height[l]
            l += 1
        else:
            if height[r] > rightMax:
                rightMax = height[r]
            else:
                totalWater += rightMax - height[r]
            r -= 1
    return totalWater