def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numdict = {value: index for index, value in enumerate(nums)}
        for i in range(len(nums)):
            if target - nums[i] in numdict and numdict[target - nums[i]] != i:
                return [i, numdict[target - nums[i]]]
        return []
        