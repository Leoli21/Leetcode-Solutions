def peakInMountainArray(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2

        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m
    return l

arr = [0,10,5,2]
print(peakInMountainArray(arr))