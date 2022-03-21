def solution(N):
    res = []
    sparses = [False] * 3
    for i in range(N // 2):
        if checkSparse(i , sparses):
            rest = N - i
            if checkSparse(rest , sparses):
                res.append(i)
                res.append(rest)
    if len(res) == 0:
        return -1
    return sorted(res)

def checkSparse(N,sparses):
    if N < len(sparses):
        return sparses[N]
    strN = bin(N)[2:]
    tmp = int(strN[0])
    for i in range(1,len(strN)):
        i_int = int(strN[i])
        if i_int & tmp == 1:
            return False
        else:
            tmp = i_int
    sparses.append(N)
    return True


# print(solution(26) == [5,8,9,10,16,17,18,21])
print(solution(1000000000))