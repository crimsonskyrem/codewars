def longestPalindrome(s: str) -> str:
    l = len(s)
    if l == 1:
        return s
    res = s[0]
    tmp = ''
    middle = True
    p = 1
    left = 0
    right = 0
    while p < l:
        left = p - 1
        if middle :
            right = p
        elif p+1 < l:
            right = p + 1
        if s[left] == s[right]:
            tmp = s[left:right + 1]
            for _ in range(1,l - p):
                left -=1
                right += 1
                if left>=0 and right<l and s[left] == s[right]:
                    tmp = s[left:right + 1]
                else:
                    break
            if len(tmp) > len(res):
                res =tmp
        if not middle:
            p += 1
        middle = not middle
    return res

print(longestPalindrome('bb'))
# print(longestPalindrome('cbbdbb'))
# print(longestPalindrome("abbcccbbbcaaccbababcbcabca"))
