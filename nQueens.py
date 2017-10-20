def mark_board(board, row, col):
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):#row loop
        if board[i][col] != 1:
            board[i][col] = 2
    for i in range(cols):
        if board[row][i] != 1:
            board[row][i] = 2
    #diagnal loop
    i = row - 1; j = col -1
    while i >= 0 and j >= 0:
        if  board[i][j] != 1:
            board[i][j] = 2
        i-=1;j-=1
    
    i = row + 1; j = col + 1
    while i < rows and j < cols:
        if  board[i][j] != 1:
            board[i][j] = 2
        i+=1;j+=1
    i = row + 1; j = col -1
    while i < rows and j >= 0:
        if  board[i][j] != 1:
            board[i][j] = 2
        i +=1;j-=1
    i = row -1; j = col+1
    while i >= 0  and j < cols:
        if  board[i][j] != 1:
            board[i][j] = 2
        i -= 1; j += 1
    
    board[row][col] = 1
def get_candidates_for_col(board, col):
    candidates = []
    for i in range(len(board)):
        if board[i][col] == 0:
            candidates.append(i)
    return candidates

def bk(board,  col, half_solution, solutions):
    if len(board) == len(half_solution):
        solutions.append(half_solution)
        return True
    candidates = get_candidates_for_col(board, col)
    if not candidates:
        return False
    for row_candidate in candidates:
        new_board = [row[0:] for row in board]
        mark_board(new_board, row_candidate, col)
        new_half_solution = half_solution[0:]
        new_half_solution.append(row_candidate+1)
        bk(new_board, col+1, new_half_solution, solutions)
        
    return False
def nQueens(n):
    if n == 1:
        return [[1]]
    board_row = [0]*n
    board = [board_row[0:]]*n#n*n board
    candidates = [x for x in range(n)]#get candidate
    solutions = []
    
    for row in candidates:
        new_board = [ row[0:] for row in board]#n*n board
        mark_board(new_board, row, 0)
        bk(new_board, 1, [row+1], solutions)
    return solutions

solutions = (nQueens(8))
print("No of solutions", len(solutions))