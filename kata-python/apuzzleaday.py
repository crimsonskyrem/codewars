from datetime import date
from os import system,name
import numpy as np
LOCK = 1
EMPT = 0
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
    [LOCK,EMPT,EMPT],
    [LOCK,LOCK,LOCK],
    [LOCK,EMPT,EMPT],
    [LOCK,EMPT,EMPT]
]
bk2 = [
    [LOCK,EMPT],
    [LOCK,LOCK],
    [LOCK,EMPT],
    [LOCK,EMPT],
    [LOCK,EMPT]
]
bk3 = [
    [LOCK,LOCK],
    [LOCK,EMPT],
    [LOCK,EMPT],
    [LOCK,EMPT]
]
bk4 = [
    [LOCK,LOCK],
    [LOCK,EMPT],
    [LOCK,EMPT],
    [LOCK,EMPT],
    [LOCK,EMPT]
]
bk5 = [
    [LOCK,LOCK,LOCK],
    [LOCK,EMPT,EMPT],
    [LOCK,EMPT,EMPT],
    [LOCK,EMPT,EMPT]
]
bk6 = [
    [LOCK,EMPT],
    [LOCK,LOCK],
    [EMPT,LOCK],
    [EMPT,LOCK]
]
bk7 = [
    [LOCK,EMPT,LOCK],
    [LOCK,LOCK,LOCK],
    [LOCK,EMPT,EMPT]
]
bk8 = [
    [LOCK,EMPT,EMPT],
    [LOCK,LOCK,LOCK],
    [EMPT,LOCK,EMPT],
    [EMPT,LOCK,EMPT]
]
bk9 = [
    [LOCK,EMPT],
    [LOCK,LOCK],
    [LOCK,LOCK]
]

def rotate(bk, times= 0):
    res = np.array(bk)
    if times < 0:
        res = np.fliplr(res)
        times += 1
    res = np.rot90(res,abs(times))
    return res

def position(bk,x,y):
    res = np.array(bk)
    row,column = res.shape
    res = np.pad(res,((x,9-row-x),(y,6-y-column)))
    return res

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def printBk(bk):
    for i in bk:
        for j in i:
            print(j,end=" ")
        print()

def markDateBoard():
    today = date.today()
    nboard = np.zeros((9,6),np.int8)
    wdpos = [[7,3],[7,4],[7,5],[8,2],[8,3],[8,4],[8,5]]
    nboard[(today.month - 1) // 6][(today.month - 1) % 6] = LOCK
    nboard[(today.day - 1) // 6 + 2][(today.day - 1) % 6] = LOCK
    i,j = wdpos[today.weekday()]
    nboard[i][j] = LOCK
    return nboard

def validBoard(currBoard):
    if np.array_equal(currBoard[0:2,0:2],[[0,1],[1,1]]):
        return False
    if np.array_equal(currBoard[0:2,4:6],[[1,0],[1,1]]):
        return False
    if np.array_equal(currBoard[0:2,0:3],[[0,0,1],[1,1,1]]):
        return False
    if np.array_equal(currBoard[0:2,3:6],[[1,0,0],[1,1,1]]):
        return False
    if np.array_equal(currBoard[7:9,0:2],[[1,1],[0,1]]):
        return False
    if np.array_equal(currBoard[7:9,4:6],[[1,1],[1,0]]):
        return False
    if np.array_equal(currBoard[7:9,0:3],[[1,1,1],[0,0,1]]):
        return False
    if np.array_equal(currBoard[7:9,3:6],[[1,1,1],[1,0,0]]):
        return False
 
    p = np.where(currBoard > LOCK)
    if currBoard[p].size == 0:
        return True
    return False

def isFullFill(currBoard):
    p = np.where(currBoard == LOCK)
    return currBoard[p].size == 54

def placeBlock(currBoard, blk):
    blk = np.array(blk)
    for i in range(9):
        for j in range(6):
            row,column = blk.shape
            if row + i < 9 and column + j < 6:
                posBlk = position(blk,i,j)
                curr = np.add(currBoard,posBlk)
                if validBoard(curr):
                    clear()
                    print(curr)
                    return True,curr,posBlk
    return False,currBoard,blk

def enumFill(currBoard,leftBlk,placedBlk):
    curr = currBoard
    lefts = leftBlk
    placed = placedBlk
    if lefts.size == 0:
        return True,curr,lefts,placed
    for i in range(-5,5):
        for j in range(lefts.size):
            chk1,curr1,pos1 = placeBlock(curr,rotate(lefts[j],i))
            if chk1:
                lefts1 = np.delete(lefts,j)
                placed1 = np.append(placed,pos1)
                chk2,curr2,lefts2,placed2 = enumFill(curr1,lefts1,placed1)
                if chk2:
                    return True,curr2,lefts2,placed2
    return False,curr,lefts,placed

def plot():
    pass

def main():
    blocks = np.array([bk1,bk2,bk3,bk4,bk5,bk6,bk7,bk8,bk9],dtype='object')
    board = markDateBoard()
    placedBlocks = np.array([])
    chk,curr,lefts,placed = enumFill(board,blocks,placedBlocks)
    if chk:
        clear()
        print(curr)
        print(placed)

def test():
    board = markDateBoard()
    print(board[7:9,4:6])
    # print(np.array_equal(board[0:2,4:2],[[0,0],[0,1]]))

main()
# test()