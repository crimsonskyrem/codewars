def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    if numRows == 2:
        return s[::2] + s[1::2]
    arr = []
    row = 0
    column = 0
    pos = numRows - 2
    sl = list(s)
    q = column % (numRows -1)  
    while sl:
        if q == 0:
            if row >= len(arr):
                arr.append([sl.pop(0)])
            else:
                arr[row].append(sl.pop(0))
        else:
            if row == pos:
                arr[row].append(sl.pop(0))
                if pos-1 > 0:
                    pos -= 1
            else:
                arr[row].append('')
        row += 1
        if row == numRows:
            row = 0
            column += 1
            q = column % (numRows -1)  
            if q == 0:
                pos = numRows - 2
    res = ''
    for sub in arr:
        res += ''.join(sub)
    return res

def convert2(s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        split = numRows + (numRows - 2)
        end = numRows - 1
        first = s[::split]
        last = s[end::split]
        for i in range(1,end):
            tmp1 = list(s[i::split])
            tmp2 = list(s[split - i::split])
            while tmp1 or tmp2:
                if tmp1:
                    first += tmp1.pop(0)
                if tmp2:
                    first += tmp2.pop(0)
        return first + last

T = convert2("PAYPALISHIRING", 3)
print(T)

# for r in T:
#    for c in r:
#       print(c,end = " ")
#    print()