def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        maxleft = [0]
        for i in range(1, len(height)):
            if height[i - 1] > max:
                max = height[i - 1]
            maxleft.append(max)
        max = 0
        maxright = [0]
        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > max:
                max = height[i + 1]
            maxright.append(max)
        maxright = maxright[::-1]
        water = 0
        for i in range(0, len(height)):
            waterb = min(maxleft[i], maxright[i]) - height[i]
            if waterb < 0:
                water += 0
            else:
                water += waterb
        return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
