import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second != first:
                heapq.heappush(stones, first - second)
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0