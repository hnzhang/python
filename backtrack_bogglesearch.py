def is_a_solution(path, k, matrix, word):
    print("is_a_solution", k)
    if k < len(word)-1:
        return False
    row = path[k][0]
    col = path[k][1]
    return word[k] == matrix[row][col]

def is_good_path(path, k, matrix, word):
    row = path[k][0]
    col = path[k][1]
    return word[k] == matrix[row][col]

def process_solution(path, matrix):
    for cell in path:
        print("[", cell[0], ",",cell[1], "]:", matrix[cell[0]][cell[1]], end=" - ")

def build_candidates(path, k, matrix )->list:
    candidates = []
    row = path[k-1][0]
    col = path[k-1][1]
    candidate = (row+1, col)
    if candidate[0] < len(matrix) and candidate not in path:
        candidates.append(candidate)
    
    candidate = (row-1, col)
    if candidate[0] >=0 and candidate not in path:
        candidates.append(candidate)
    
    candidate = (row, col+1)
    if candidate[1] < len(matrix[0]) and candidate not in path:
        candidates.append(candidate)
    
    candidate = (row, col-1)
    if candidate[1] >=0 and candidate not in path:
        candidates.append(candidate)
    
    return candidates

def backtrack(path, k, matrix, word):
    print("backtrack", k)
    if is_a_solution(path, k, matrix, word ):
        process_solution(path, matrix)
        return True
    elif  is_good_path(path, k, matrix, word):
        k += 1
        candidates = build_candidates(path, k, matrix)
        for candidate in candidates:
            path[k] = candidate
            if backtrack(path, k, matrix, word):
                return True
        return False

def boggle_search(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == word[0]:
                path = [(row, col)]* len(word)
                if backtrack(path, 0, matrix, word):
                    return True
    return False
board = [
        'AFAJ',
        'SIVA',
        'EROC',
        'CXEK',
        'ODFS',
        'DEEE'
        ]
boggle_search(board, "PREP")
boggle_search(board, "FEES")
board = [
        'AOL',
        'DEL',
        'GHI',
    ]

boggle_search(board, "HELLO")