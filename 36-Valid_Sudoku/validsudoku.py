def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[(i // 3, j // 3)]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                square[(i // 3, j // 3)].add(board[i][j])
        return True

'''
This function uses `collections.defaultdict(set)` to store sets of 
numbers already seen in rows (`row`), columns (`col`), and 
3x3 sub-grids (`square`) of a Sudoku board. The `square` dictionary uses 
keys as `(i // 3, j // 3)` to map each cell to its respective sub-grid,
where `i // 3` gives the row group and `j // 3` gives the column group of 
the grid.
'''