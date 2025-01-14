def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = defaultdict(int)
        for i in nums:
            ret[str(i)] += 1
        for key, value in ret.items():
            if value > len(nums) / 2:
                return int(key)