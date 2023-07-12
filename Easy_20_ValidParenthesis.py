def valid_parenthesis(s):
    stack = []
    close_to_open = {')': '(', ']': '[', '}': '{'}

    for each in s:
        if each in close_to_open: # each is close parenthesis
            if stack and stack[-1] == close_to_open[each]:
                stack.pop()
            else:
                return False
        else:
            stack.append(each) # Only open parenthesis in stack
        print(stack)

    return True if not stack else False


s = "()(){[]}"
print(valid_parenthesis(s))