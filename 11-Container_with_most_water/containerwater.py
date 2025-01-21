def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max = 0
        while start < end:
            if (end - start) * min(height[start], height[end]) > max:
                max = (end - start) * min(height[start], height[end])
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max