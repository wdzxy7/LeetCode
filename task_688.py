def knightProbability(self, n, k, row, column):
    count = 0
    from functools import cache
    # @cache
    def search(row_index, col_index, step):
        nonlocal count
        if step < 0:
            count += 1
            return 0
        if row_index < 0 or row_index > n:
            count += 1
            return 1
        elif col_index < 0 or col_index > n:
            count += 1
            return 1
        elif step == 0:
            count += 1
            return 0
        else:
            step -= 1
            return ((search(row_index - 2, col_index + 1, step) + search(row_index - 2, col_index - 1, step) +
                    search(row_index - 1, col_index + 2, step)) + search(row_index - 1, col_index - 2, step) +
                    search(row_index + 2, col_index + 1, step) + search(row_index + 2, col_index - 1, step) +
                    search(row_index + 1, col_index + 2, step) + search(row_index + 1, col_index - 2, step))

    out = ((search(row - 2, column + 1, k - 1) + search(row - 2, column - 1, k - 1) +
            search(row - 1, column + 2, k - 1)) + search(row - 1, column - 2, k - 1) +
            search(row + 2, column + 1, k - 1) + search(row + 2, column - 1, k - 1) +
            search(row + 1, column + 2, k - 1) + search(row + 1, column - 2, k - 1))
    return 1 - out / count

print(knightProbability(None, 3, 2, 0, 0))