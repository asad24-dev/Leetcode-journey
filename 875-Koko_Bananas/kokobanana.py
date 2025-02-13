
def minEatingSpeed(self, piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    left = 1
    right = max(piles)
    retval = right
    while left <= right:
        mid = (left + right) // 2
        time = 0
        for i in piles:
            time += math.ceil(float(i)/mid)
        if  time <= h:
            retval = mid
            right = mid - 1
        else:
            left = mid + 1
    return retval
