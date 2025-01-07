class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        intervals.sort(key = lambda i : i[0]) #remember that when there is a list of lists we can specify which element we want to sort with
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i + 1][1], intervals[i][1])]
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals
                
        