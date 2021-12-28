from datetime import date
LOCK_STRING = 'X'
board = [
    ["JAN","FEB","MAR","APR","MAY","JUN"],
    ["JUL","AUG","SEP","OCT","NOV","DEC"],
    ["1"  ,"2"  ,"3"  ,"4"  ,"5"  ,"6"  ],
    ["7"  ,"8"  ,"9"  ,"10" ,"11" ,"12" ],
    ["13" ,"14" ,"15" ,"16" ,"17" ,"18" ],
    ["19" ,"20" ,"21" ,"22" ,"23" ,"24" ],
    ["25" ,"26" ,"27" ,"28" ,"29" ,"30" ],
    ["31" ," "  ," "  ,"MON","TUE","WED"],
    [" "  ," "  ,"THU","FRI","SAT","SUN"]
]
bk1 = [
    [1,0,0],
    [1,1,1],
    [1,0,0],
    [1,0,0]
]
bk2 = [
    [1,0],
    [1,1],
    [1,0],
    [1,0],
    [1,0]
]
bk3 = [
    [1,1],
    [1,0],
    [1,0],
    [1,0]
]
bk4 = [
    [1,1],
    [1,0],
    [1,0],
    [1,0],
    [1,0]
]
bk5 = [
    [1,1,1],
    [1,0,0],
    [1,0,0],
    [1,0,0]
]
bk6 = [
    [1,0],
    [1,1],
    [0,1],
    [0,1]
]
bk7 = [
    [1,0,1],
    [1,1,1],
    [1,0,0]
]
bk8 = [
    [1,0,0],
    [1,1,1],
    [0,1,0],
    [0,1,0]
]
bk9 = [
    [1,0],
    [1,1],
    [1,1]
]

def rotate(bk, times= 0):
    res = bk
    if times < 0:
        res = list(map(lambda x:x[::-1],res))
        times += 1
    for _ in range(abs(times)):
        res = list(zip(*res[::-1]))
    return res

def printBk(bk):
    for i in bk:
        for j in i:
            print(j,end=" ")
        print()

def markDateBoard():
    today = date.today()
    nboard = board
    weekday = today.weekday()
    for i in range(9):
        for j in range(6):
            if i < 2 and j + i*6 == today.month - 1:
                nboard[i][j] = LOCK_STRING
            if i > 1 and i < 8 and  j + (i-2)*6 == today.day - 1:
                nboard[i][j] = LOCK_STRING
            if i == 7 and weekday < 4 and j - 3 == weekday:
                nboard[i][j] = LOCK_STRING
            if i == 8 and weekday > 3 and j + 1 == weekday:
                nboard[i][j] = LOCK_STRING
    return nboard

def plot():
    pass
def main():
    pass

# printBk(rotate(bk2,-2))