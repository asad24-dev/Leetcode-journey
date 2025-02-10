def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        while top <= bottom:
            mid = top + (bottom - top) / 2
            if target > matrix[m - 1][n - 1] or target < matrix[0][0]:
                return False
            if matrix[mid][n - 1] == target:
                return True
            elif target > matrix[mid][n - 1]:
                top = mid + 1
            else:
                bottom = mid - 1
        left = 0
        right = n - 1
        while left <= right:
            midcol = left + (right - left) / 2
            if matrix[top][midcol] == target:
                return True
            elif matrix[top][midcol] > target:
                right = midcol - 1
            elif matrix[top][midcol] < target:
                left = midcol + 1
        return False
