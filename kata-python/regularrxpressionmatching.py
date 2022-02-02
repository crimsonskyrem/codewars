# def isMatch(self, s: str, p: str) -> bool:
#     if len(p) == 0:
#         return False
#     if len(s) < 2 and len(p) < 5:
#         if len(p) == 1:
#             return s == p or p == '.'
#         elif len(s) == 0 and len(p) == 2 and p[1] == '*':
#             return True
#         elif len(p) > 1 and p[-1] == '*':
#             return s == p[0] or p[0] == '.'
#         elif len(p) > 1 and p[1] == '*':
#             return s == p[2] or p[2] == '.'
#         else:
#             return False
#     for _ in range(len(s)):
#         if p[-1] == "." or p[-1] == s[-1]:
#             return self.isMatch(s[:-1], p[:-1])
#         else:
#             break
#     for i in range(len(s)):
#         if p[i] == "." or p[i] == s[i]:
#             if len(p) > i+1 and p[i+1] == "*":
#                 j = i
#                 while (j < len(s)) and (p[i] == s[j] or p[i] == "."):
#                     j += 1
#                 if len(p) == 2:
#                     return True
#                 return self.isMatch(s[j:], p[i+2:]) or self.isMatch(s[i:], p[i+2:]) 
#             else:
#                 return self.isMatch(s[i+1:], p[i+1:])
#         else:
#             if len(p) > i+1 and p[i+1] == "*":
#                 return self.isMatch(s[i:], p[i+2:])
#             else:
#                 return False

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