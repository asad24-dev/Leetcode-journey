def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        sum = 0
        for i in range(k):
            sum += nums[i]
        max_avg = float(sum) / k
        for i in range(k, n):
            sum += nums[i]
            sum -= nums[i - k]
            avg = float(sum) / k
            max_avg = max(max_avg, avg)
        return max_avg