def maxArea(height):
    l, r = 0, len(height) - 1
    maxArea = 0
    while l < r:
        maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
        # Shift pointer that contains the limiting height (height that is less)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxArea