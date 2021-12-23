def longestPalindrome(s: str) -> str:
        l = len(s)
        if l == 1:
            return s
        res = ''
        tmp = ''
        s_l = len(s)
        tail = 0
        repeat = False
        reverse = s[::-1]
        for i in range(s_l):
            if reverse[i] == s[0]:
                tail = s_l - i
                repeat = True
                break
        if not repeat:
            return ''
        tmp = s[:tail]
        tmp_l = len(tmp)
        mid = tmp_l // 2 
        single = tmp_l % 2
        if tmp[mid:][::-1] == tmp[:mid + single]:
            res = tmp
        else:
            tmp2 = longestPalindrome(s[1:])
            if len(res) < len(tmp2):
                res = tmp2
        return res

print(longestPalindrome('cbbdbb'))
# print(longestPalindrome("abbcccbbbcaaccbababcbcabca"))
