def reverseWords(s):
    words = s.split()

    result = " ".join(word[::-1] for word in words)
    return result

    '''
    My way
    words = s.split()
        
    res = ""
    for word in words:
        res += word[::-1]
        res += " "
            
    return res[:len(res)-1] 
    '''
s = "Let's take LeetCode contest"
print(reverseWords(s))