def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    # Start our search from bottom left
    # This means we either move two ways:
    # 1. Up if curValue > target (we need to look for a smaller value)
    # 2. Right if curValue < target (we need to look for a greater value)

    curRow = ROWS - 1
    curCol = 0

    # Due to our movement conditions, we either risk reaching an
    # out of bounds row (less than 0) or an out of bounds column
    # (greater than or equal to COLS)
    while curRow >= 0 and curCol < COLS:
        curElement = matrix[curRow][curCol]
        if curElement == target:
            return True
        elif curElement < target:
            curCol += 1
        else:
            curRow -= 1
    return False

def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    # Start our search from top right
    # This means we are only moving either:
    # Down if we need a greater value
    # Left if we need a smaller value
    curRow = 0
    curCol = COLS - 1

    # This means we only either risk getting to an invalid column (less than 0)
    # or an invalid row (greater than or equal to ROWS)
    while curCol >= 0 and curRow < ROWS:
        curElement = matrix[curRow][curCol]
        if curElement == target:
            return True
        elif curElement < target:
            curRow += 1
        else:
            curCol -= 1
    return False

# Perform a Binary Search on each row
# Time: O(m * logn)
def searchMatrix(matrix, target):
    COLS = len(matrix[0])

    # 'row' reprsents a row in matrix
    for row in matrix:
        # Perform a binary search on each row
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            # Since row represents a row in the matrix, we can just directly
            # access the element by using row as our array
            curElement = row[m]
            if curElement == target:
                return True
            elif curElement < target:
                l = m + 1
            else:
                r = m - 1
    return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix(matrix, target))