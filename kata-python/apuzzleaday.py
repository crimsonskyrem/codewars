from datetime import date,datetime
from os import system,name
import numpy as np
LOCK = 1
EMPT = 0
BLK_EDGE = 10
BOARD_HEIGHT = 9
BOARD_WIDTH = 6
FILE_NAME = 'logfile.txt'

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
force_check = 0
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

def markDateBoard(daystr = ''):
    today = date.today()
    if daystr:
        today = datetime.strptime(daystr, '%Y-%m-%d')
    if today.month == 1:
        global force_check
        force_check = 1
    nboard = np.zeros((BOARD_HEIGHT,BOARD_WIDTH),np.int8)
    wdpos = [[7,3],[7,4],[7,5],[8,2],[8,3],[8,4],[8,5]]
    nboard[(today.month - 1) // BOARD_WIDTH][(today.month - 1) % BOARD_WIDTH] = LOCK
    nboard[(today.day - 1) // BOARD_WIDTH + 2][(today.day - 1) % BOARD_WIDTH] = LOCK
    i,j = wdpos[today.weekday()]
    nboard[i][j] = LOCK
    return nboard

def validBoard(currBoard):
    if np.max(currBoard) == LOCK:
        fullfill = np.where(currBoard == LOCK)
        if currBoard[fullfill].size > 21:
            fillrows = (currBoard[fullfill].size) // 8 
            if np.array_equal(currBoard[0:fillrows],np.ones((fillrows,6),dtype=np.int8)):
                return True
        else:
            global force_check
            return currBoard[0][force_check] == LOCK
    return False

def placeBlock(currBoard, blk):
    blk = np.array(blk)
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            row,column = blk.shape
            if row + i < 10 and column + j < 7:
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
    if len(lefts) == 0:
        return True,curr,lefts,placed
    for i in range(len(lefts)):
        for j in range(-5,5):
            chk1,curr1,pos1 = placeBlock(curr,rotate(lefts[i],j))
            if chk1:
                lefts1 = lefts.copy()
                lefts1.pop(i)
                placed1 = placed.copy()
                placed1.append(pos1)
                chk2,curr2,lefts2,placed2 = enumFill(curr1,lefts1,placed1)
                if chk2:
                    return True,curr2,lefts2,placed2
    return False,curr,lefts,placed

def plot(ans):
    resBoard = np.zeros((BOARD_HEIGHT,BOARD_WIDTH),np.int8)
    num = 1
    for blk in ans:
        resBoard = np.add(resBoard,blk * num)
        num += 1
    log(resBoard)
    print(resBoard)


def log(arr):
    f = open(FILE_NAME, "a")
    f.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
    f.write('\n')
    if type(arr) == list:
        for i in arr:
            tmp = np.array(i)
            f.write(np.array2string(tmp))
            f.write('\n')
    else:
        f.write(np.array2string(arr))

    f.write('\n')
    f.close()

def main():
    blocks = [bk3,bk2,bk4,bk6,bk1,bk5,bk7,bk8,bk9]
    board = markDateBoard()
    log(board)
    placedBlocks = []
    chk,curr,lefts,placed = enumFill(board,blocks,placedBlocks)
    if chk:
        clear()
        plot(placed)


def test():
    pass
    # blocks = [bk3,bk2,bk4,bk6,bk1,bk5,bk7,bk8,bk9]
    # ans = []
    # board = markDateBoard('2021-12-29')
    # tmp = rotate(blocks[0],1)
    # chk1,curr1,pos1 = placeBlock(board,tmp)
    # ans.append(pos1)
    # tmp = rotate(blocks[1],3)
    # chk1,curr1,pos1 = placeBlock(curr1,tmp)
    # ans.append(pos1)
    # tmp = rotate(blocks[2],-2)
    # chk1,curr1,pos1 = placeBlock(curr1,tmp)
    # ans.append(pos1)
    # tmp = rotate(blocks[4],-1)
    # chk1,curr1,pos1 = placeBlock(curr1,tmp)
    # ans.append(pos1)
    # tmp = rotate(blocks[3],-2)
    # chk1,curr1,pos1 = placeBlock(curr1,tmp)
    # ans.append(pos1)
    # tmp = rotate(blocks[4],-1)
    # print(tmp)
    # log(ans)
    # plot(ans)

main()
# test()