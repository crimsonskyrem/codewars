def generateParenthesis(n: int):
    if n == 1:
        return ["()"]
    else:
        start = ["((", "()"]
        res = []
        while n*2 >= len(start[0]):
            res = start
            start = []
            for i in res:
                start += [i + "(", i + ")"]
        final = []
        for j in res:
            if checkParenthesis(j):
                final.append(j)
        return final

def checkParenthesis(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(generateParenthesis(3))