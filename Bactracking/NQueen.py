k = 1


def SolveNq(Arr):
    if (solveNqUtil(Arr, 0) == False):
        print("Solution doesn't exist")
        return
    return


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if (board[[i][j]]):
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < 4:
        if(board[i][j]):
            return False
        i += 1
        j -= 1
    return True


def printSolution(board):
    global k
    k += 1
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print("\n")
    print("\n")


def solveNqUtil(board, col):
    if (col == 4):
        printSolution(board)
        return True
    res = False
    for i in range(4):
        if(isSafe(board, i, col)):
            board[i][col] = 1

            res = solveNqUtil(board, col+1) or res
            board[i][col] = 0
    return res


R = 4
C = 4

board = [[0 for j in range(10)]
         for i in range(10)]
# print(Arr)
SolveNq(board)
