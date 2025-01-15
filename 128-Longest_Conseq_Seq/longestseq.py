def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        ret = set(nums)
        for num in ret:
            if num - 1 not in ret:
                seqlen = 1
                while num + seqlen in ret:
                    seqlen += 1
                if seqlen > longest:
                    longest = seqlen
        return longest