def isValid(str):
    d = {'(': ')',
         '{': '}',
         '[': ']'}

    # Stores opening types of brackets
    stack = []

    for c in s:
        # Character is an opening type of bracket
        if c in d:
            stack.append(c)
        # Character is a closing type of bracket
        else:
            # Check that stack is not empty and that top element of stack
            # corresponds to the current closing brackets' opening bracket
            if len(stack) != 0 and d[stack[-1]] == c:
                stack.pop()
            else:
                return False

    return len(stack) == 0

s = "()"
print(isValid(s))