def romanToInteger(s):
    conversions = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0

    for i in range(len(s) - 1):
        if conversions[s[i]] < conversions[s[i + 1]]:
            ans -= conversions[s[i]]
        else:
            ans += conversions[s[i]]

    ans += conversions[s[-1]]
    return ans