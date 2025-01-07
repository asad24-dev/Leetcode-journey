def rotate(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = rows
        for i in range(rows):
            for j in range(cols):
                if i != j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        left = 0
        right = cols
        while right > left:
            for i in range(rows):
                temp = matrix[i][right - 1]
                matrix[i][right - 1] = matrix[i][left]
                matrix[i][left] = temp
            left += 1
            right -= 1
        return matrix        

print(rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
#print(rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])) # [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]