def BoggleSearch(board, word):
    if not board or not board[0]:
        return False
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == word[0]:
                history = set()
                print("Boggle Search:", i, j)
                print("init history:", history)
                if BoggleSearchHelper(board, word, history, 0, i, j):
                    print("success")
                    return True
    print("Cannot find")
    return False

def BoggleSearchHelper(board, word, history, index, row, col):
    print("index", index, "row", row, "col", col)
    if row < 0 or row >= len(board):
        #print("row out of scope", row)
        return False
    if col < 0 or col >= len(board[0]):
        #print("col out of scope", col)
        return False
    #visited node
    if (row, col) in  history:
        print("visited, go back")
        return False 
    print("history:", history)
    #reject
    if word[index] != board[row][col]:
        return False
    #accept, base case
    if word[index] == board[row][col] and index == len(word) -1:
        history.add((row, col))
        print("success:", board[row][col])
        return True

    history.add((row, col))
    print("success:", board[row][col])

    if BoggleSearchHelper(board, word, history,  index+1, row-1, col) or
        BoggleSearchHelper(board, word,history,  index+1, row+1, col) or
        BoggleSearchHelper(board, word,history,  index+1, row, col-1) or
        BoggleSearchHelper(board, word, history,  index+1,row, col+1):
        return True
     
def test():
    board = [
        'AFAJ',
        'SIVA',
        'EROC',
        'CXEK',
        'ODFS',
        'DEEE'
        ]
    BoggleSearch(board, "PREP")
    board = [
        'AOL',
        'DEL',
        'GHI',
    ]

    BoggleSearch(board, "HELLO")
test()