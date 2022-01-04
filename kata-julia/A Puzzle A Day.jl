using Dates
LOCK = 1
EMPT = 0
BOARD_HEIGHT = 9
BOARD_WIDTH = 6
FILE_NAME = "julia-logfile.txt"
bk1 = [
    LOCK EMPT EMPT
    LOCK LOCK LOCK
    LOCK EMPT EMPT
    LOCK EMPT EMPT
]
bk2 = [
    LOCK EMPT
    LOCK LOCK
    LOCK EMPT
    LOCK EMPT
    LOCK EMPT
]
bk3 = [
    LOCK LOCK
    LOCK EMPT
    LOCK EMPT
    LOCK EMPT
]
bk4 = [
    LOCK LOCK
    LOCK EMPT
    LOCK EMPT
    LOCK EMPT
    LOCK EMPT
]
bk5 = [
    LOCK LOCK LOCK
    LOCK EMPT EMPT
    LOCK EMPT EMPT
    LOCK EMPT EMPT
]
bk6 = [
    LOCK EMPT
    LOCK LOCK
    EMPT LOCK
    EMPT LOCK
]
bk7 = [
    LOCK EMPT LOCK
    LOCK LOCK LOCK
    LOCK EMPT EMPT
]
bk8 = [
    LOCK EMPT EMPT
    LOCK LOCK LOCK
    EMPT LOCK EMPT
    EMPT LOCK EMPT
]
bk9 = [
    LOCK EMPT
    LOCK LOCK
    LOCK LOCK
]

function markDateBoard()
    date = Dates.now()
    nboard = zeros(Int8, BOARD_HEIGHT, BOARD_WIDTH)
    wdpos = [[8,4] ,[8,5],[8,6],[9,3] ,[9,4],[9,5] ,[9,6]]
    if Dates.month(date) > BOARD_WIDTH
        nboard[2,Dates.month(date) - BOARD_WIDTH] = LOCK
    else
        nboard[1,Dates.month(date)] = LOCK
    end
    r, c = divrem(Dates.day(date), BOARD_WIDTH)
    nboard[r + 3,c] = LOCK
    i, j = wdpos[Dates.dayofweek(date)]
    nboard[i,j] = LOCK
    return nboard
end

function pos(bk,x,y)
    r,c = size(bk)
    if x > 0
        bk = vcat(zeros(Int8,x,c),bk)
    end
    bk = vcat(bk,zeros(Int8,BOARD_HEIGHT - r - x,c))
    r,c = size(bk)
    if y > 0
        bk = hcat(zeros(Int8,r,y),bk)
    end
    bk = hcat(bk,zeros(Int8,r,BOARD_WIDTH - c - y))
    return bk
end

function rotate(bk, times = 0)
    if times < 0
        bk = transpose(bk)
        times += 1
    end
    return rotl90(bk, times)
end

function validBoard(currBoard)
    if maximum(currBoard) == LOCK
        # fullfill = np.where(currBoard == LOCK)
        # if currBoard[fullfill].size > 21
        #     fillrows = (currBoard[fullfill].size) // 8 
        #     if currBoard[0:fillrows],ones(Int8,fillrows,6)
        #         return True
        #     end
        # else
        #     global force_check
        #     return currBoard[0][force_check] == LOCK
        # end
    end
    return False
end


function placeBlock(currBoard, blk)
    for i in 0:BOARD_HEIGHT
        for j in 0:BOARD_WIDTH
            row,column = size(blk)
            if row + i < 10 && column + j < 7
                posBlk = pos(blk,i,j)
                curr = broadcast(+,currBoard,posBlk)
                if validBoard(curr)
                    clearconsole()
                    display(curr)
                    return True,curr,posBlk
                end
            end
        end
    end
    return False,currBoard,blk
end
board = markDateBoard()
# display(board)
# display(rotate(bk1, -1))
test = placeBlock(board,rotate(bk1, -1))
display(test)