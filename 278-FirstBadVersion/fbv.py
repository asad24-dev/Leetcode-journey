def firstBadVersion(n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (right + left) // 2
            if isBadVersion(mid):
                right = mid 
            else:
                left = mid + 1
        if isBadVersion(left):
            return left
        else:
            return left + 1
