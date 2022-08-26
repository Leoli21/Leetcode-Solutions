def trailingZeroes(n):
    count = 0
    k = 5
    while k <= n:
        numFives = n // k
        count += numFives
        k *= 5
    return count