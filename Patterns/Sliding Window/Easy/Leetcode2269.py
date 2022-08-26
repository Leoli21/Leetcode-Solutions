def divisorSubstrings(num, k):
    count = 0
    numStr= str(num)

    for i in range(len(numStr) - k + 1):
        currNum = int(numStr[i:i+k])
        if currNum != 0 and num % currNum == 0:
            count += 1

    return count

num = 430043
k = 2
print(divisorSubstrings(num, k))

print(int("00000004"))