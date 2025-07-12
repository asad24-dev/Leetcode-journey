import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        retval = None
        for i in range(len(nums) - k + 1):
            retval = heapq.heappop(nums)
        return retval