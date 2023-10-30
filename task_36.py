def isValidSudoku(self, board):
    for i in range(9):
        nums = [1 for i in range(10)]
        for j in range(9):
            index = board[i][j]
            if index == '.':
                continue
            else:
                nums[int(index)] -= 1
                if nums[int(index)] == -1:
                    return False
    for i in range(9):
        nums = [1 for i in range(10)]
        for j in range(9):
            index = board[j][i]
            if index == '.':
                continue
            else:
                nums[int(index)] -= 1
                if nums[int(index)] == -1:
                    return False
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            nums = [1 for i in range(10)]
            for ii in range(3):
                for jj in range(3):
                    index = board[i + ii][j + jj]
                    if index == '.':
                        continue
                    else:
                        nums[int(index)] -= 1
                        if nums[int(index)] == -1:
                            return False
    return True

print(isValidSudoku(None, [["8","3",".",".","7",".",".",".","."]
                                     ,["6",".",".","1","9","5",".",".","."]
                                     ,[".","9","8",".",".",".",".","6","."]
                                     ,["8",".",".",".","6",".",".",".","3"]
                                     ,["4",".",".","8",".","3",".",".","1"]
                                     ,["7",".",".",".","2",".",".",".","6"]
                                     ,[".","6",".",".",".",".","2","8","."]
                                     ,[".",".",".","4","1","9",".",".","5"]
                                     ,[".",".",".",".","8",".",".","7","9"]]))