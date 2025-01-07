def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    retlist =[]
    while top < bottom and left < right:
        for i in range(left, right):
            retlist.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            retlist.append(matrix[i][right - 1])
        right -= 1
        if not (top < bottom and left < right):
            break
        for i in range(right - 1, left - 1, -1):
            retlist.append(matrix[bottom - 1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            retlist.append(matrix[i][left])
        left += 1
    return retlist

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
#print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]