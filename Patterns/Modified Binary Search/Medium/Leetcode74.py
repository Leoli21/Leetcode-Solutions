def searchMatrix(matrix, target):
    r = len(matrix)
    c = len(matrix[0])

    # First binary search to identify which row to search in
    # for our second binary search

    startRow, endRow = 0, r - 1
    searchRow = 0
    while startRow <= endRow:
        currRow = (startRow + endRow) // 2
        # Target is within this row if it
        if matrix[currRow][0] <= target <= matrix[currRow][-1]:
            searchRow = currRow
            break

        # Since target is greater than the largest element in the current
        # row, we know that it cannot lie within this row. Thus, adjust the
        # search space to the rows after currRow
        elif target > matrix[currRow][-1]:
            startRow = currRow + 1

        # This means our target lies within a row that contains elements smaller
        # than the smallest element in our current row. Adjust search space to
        # the rows from the start to the row before the currRow (inclusive)
        else:
            endRow = currRow - 1

    # Second binary search to check if the target value exists in our matrix
    # At this point, we have already identified the row to search in as it
    # has a range that contains the target value
    l, r = 0, c - 1
    while l <= r:
        m = (l + r) // 2
        currNum = matrix[searchRow][m]
        if target == currNum:
            return True
        elif target < currNum:
            r = m - 1
        else:
            l = m + 1

    return False

def searchMatrix(matrix, target):
    r = len(matrix)
    c = len(matrix[0])
    l, r = 0, r * c - 1
    while l <= r:
        m = (l + r) // 2
        # Since each row can only contain 'c' elements, then for every multiple of
        # 'c', we will be at a new row.

        # The remainder of the currIndex and the number of columns will equal the current
        # column our element is located at.
        currVal = matrix[m // c][m % c]
        if currVal == target:
            return True

        elif currVal < target:
            l = m + 1
        else:
            r = m - 1

    return False