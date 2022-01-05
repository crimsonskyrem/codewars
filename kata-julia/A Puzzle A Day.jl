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

force_check = 0

function markDateBoard()
    date = Dates.now()
    nboard = zeros(Int8, BOARD_HEIGHT, BOARD_WIDTH)
    wdpos = [[8,4] ,[8,5],[8,6],[9,3] ,[9,4],[9,5] ,[9,6]]
    if Dates.month(date) > BOARD_WIDTH
        nboard[2,Dates.month(date) - BOARD_WIDTH] = LOCK
    else
        nboard[1,Dates.month(date)] = LOCK
    end
    if Dates.month(date) == 1
        global force_check = 1
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
        fullfill = filter(x -> x == LOCK,currBoard)
        if length(fullfill) > 21
            fillrows = fdiv(length(fullfill), 8) 
            return all(currBoard[1:fillrows,:] .== LOCK)
        else
            global force_check
            return currBoard[1,force_check] == LOCK
        end
    end
    return false
end


function placeBlock(currBoard, blk)
    for i in 0:BOARD_HEIGHT
        for j in 0:BOARD_WIDTH
            row,column = size(blk)
            if row + i < 10 && column + j < 7
                posBlk = pos(blk,i,j)
                curr = (+).(currBoard,posBlk)
                if validBoard(curr)
                    run(`clear`)
                    display(curr)
                    return true,curr,posBlk
                end
            end
        end
    end
    return false,currBoard,blk
end


function enumFill(currBoard,leftBlk,placedBlk)
    curr = currBoard
    lefts = leftBlk
    placed = placedBlk
    if isempty(lefts)
        return true,curr,lefts,placed
    end
    for i in 1:ndims(lefts)
        for j in -5:5
            chk1,curr1,pos1 = placeBlock(curr,rotate(lefts[i],j))
            if chk1
                lefts1 = copy(lefts)
                deleteat!(lefts1,i)
                placed1 = cat(placed,pos1;dims=3)
                chk2,curr2,lefts2,placed2 = enumFill(curr1,lefts1,placed1)
                if chk2
                    return true,curr2,lefts2,placed2
                end
            end
        end
    end
    return false,curr,lefts,placed
end
function main()
    blocks = [bk3,bk2,bk4,bk6,bk1,bk5,bk7,bk8,bk9]
    board = markDateBoard()
    placedBlocks = []
    chk,curr,lefts,placed = enumFill(board,blocks,placedBlocks)
    if chk
        run(`clear`)
        display(placed)
    end
end

main()
# display(rotate(bk1, -1))
# test = placeBlock(board,rotate(bk1, -1))
# display(test)