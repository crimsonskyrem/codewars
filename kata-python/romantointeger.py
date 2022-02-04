def romanToInt(s: str) -> int:
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    tmp = 0
    for i in s:
        num = dict[i]
        if  tmp > 0 and num > tmp:
            res = res - 2 * tmp + num
        else:
            res += num
        tmp = num
    return res

def test():
    assert romanToInt("III") == 3
    assert romanToInt("IV") == 4
    assert romanToInt("XLIII") == 43
    assert romanToInt("MCMXCIV") == 1994