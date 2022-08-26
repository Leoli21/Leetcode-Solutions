def numOfSubarrays(arr, k, threshold):
    target = threshold * k
    total = 0
    currSum = sum(arr[:k])
    if currSum >= target:
        total = 1

    for r in range(k, len(arr)):
        currSum += arr[r] - arr[r - k]
        if currSum >= target:
            total += 1

    return total

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold =4
print(numOfSubarrays(arr, k, threshold))