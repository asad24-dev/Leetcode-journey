def numJewelsInStones(jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        s = set(jewels)
        for i in stones:
            if i in s:
                count += 1

        return count