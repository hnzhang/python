# Collections module has already been imported.
def matrix_max_sum_dfs_helper(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    if row >= rows or col >= cols:
        return 0
    print("Grid,", row, col, grid[row][col])
    return grid[row][col] + max(
            matrix_max_sum_dfs_helper(grid, row+1, col),
            matrix_max_sum_dfs_helper(grid, row, col+1)
        )
 

def matrix_max_sum_dfs(grid):
    if not grid or not grid[0]:
        return 0
    
    return grid[0][0] + max(matrix_max_sum_dfs_helper(grid, 0, 1), 
            matrix_max_sum_dfs_helper(grid, 1, 0))

def test():
    grid = [
            [1,2,3],
            [4,5,6]
        ]
    print(matrix_max_sum_dfs(grid))

test()