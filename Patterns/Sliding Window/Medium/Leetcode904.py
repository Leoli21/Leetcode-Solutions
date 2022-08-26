def totalFruit(fruits):
    if len(fruits) <= 2:
        return len(fruits)

    types = {}
    maxFruit = float('-inf')
    l = 0
    for r, val in enumerate(fruits):
        if val not in types and len(types) == 2:
            l = min(types.values()) + 1
            del types[fruits[l - 1]]

        types[val] = r
        maxFruit = max(maxFruit, r - l + 1)

    return maxFruit

fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruit(fruits))