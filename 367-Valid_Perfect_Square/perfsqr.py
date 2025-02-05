def isPerfectSquare(num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        right = num // 2
        left = 0
        while left <= right:
            mid = left + (right -  left) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False