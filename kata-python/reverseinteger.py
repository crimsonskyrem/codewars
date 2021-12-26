def reverse(x: int):
    res = str(x)[::-1]
    if res.find('-') > 0:
        res = '-' + res[:-1]
        if len(res) == 11 and int(res[1:10]) >= 214748365:
            return 0
    elif len(res) == 10 and int(res[:9])>= 214748365:
        return 0
    return int(res)


# print(reverse(2**31 -1))
# print(reverse(-123))
# print(reverse(-2147483647))
# print(reverse(-1563847412))
print(reverse(1463847412))