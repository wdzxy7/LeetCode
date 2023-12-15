def searchMatrix(self, matrix, target):
    high = len(matrix)
    for i in range(high - 1):
        matrix[0] += matrix[1]
        del matrix[1]
    matrix = matrix[0]
    low = 0
    high = len(matrix) - 1
    while low <= high:
        mid = (low + high) // 2
        if matrix[mid] == target:
            return True
        elif matrix[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

print(searchMatrix(None, [[1]], 2))