def isMatch(s,p):
    dp = [[True] + [False] * len(s)]
    for i, pc in enumerate(p):
        row = [pc == '*' and dp[-2][0]]
        for j, sc in enumerate(s):
            if pc == '.':
                row.append(dp[-1][j])
            elif pc == '*':
                row.append(dp[-2][j + 1] or ((p[i - 1] == '.' or p[i - 1] == sc) and row[j]))
            else:
                row.append(dp[-1][j] and pc == sc)
        dp.append(row)
    return dp[-1][-1]

# print(isMatch("a",".*..a*") == False)
print(isMatch("bbbba",".*a*a") == True)
# print(isMatch("abcdede","ab.*de") == True)
# print(isMatch("ab",".*..c*") == True)
# print(isMatch("a","ab*") == True)
# print(isMatch("ab",".*c") == False)
# print(isMatch("aab","c*a*b") == True)
# print(isMatch("aaa","a*a") == True)
# print(isMatch("aaaa","aaa") == False)
# print(isMatch("aaa","aaaa") == False)
# print(isMatch("aa","a*") == True)
# print(isMatch("aaa","ab*ac*a") == True)
# print(isMatch("aaa","ab*a*c*a") == True)
# print(isMatch("a","ab*a") == False)
# print(isMatch("mississippi","mis*is*ip*.") == True)
# print(isMatch("mississippi","mis*is*p*.") == False)