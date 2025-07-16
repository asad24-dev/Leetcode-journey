import math
import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distance_arr = []
        for point in points:
            dist = math.sqrt((point[0]**2) + (point[1]**2))
            heapq.heappush(distance_arr, (dist, point))
        result = [heapq.heappop(distance_arr)[1] for _ in range(k)]
        return result