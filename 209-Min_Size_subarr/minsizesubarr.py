def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        l = 0 
        retval = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                retval = min(retval, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if retval == float("inf") else retval