import math
def evalRPN(tokens):
    stack = []
    for each in tokens:
        if each == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif each == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif each == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif each == '/':
            b = stack.pop()
            a = stack.pop()
            res = math.trunc(a/b)
            stack.append(res)
        else:
            stack.append(int(each))
    return stack.pop()

# tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(evalRPN(tokens))