def isHappy(self, n):
    if n== 1: return True

    seen = set()

    while n not in seen:
        seen.add(n)
        n = sqSum(n)

        if n == 1:
            return True

def sqSum(self, n):
    total = 0
    while n != 0:
        digit = n % 10
        total += (digit ** 2)
        n //= 10
    return total