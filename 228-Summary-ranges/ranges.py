def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        retlist = []
        start = 0
        end = 1
        step = 1
        while start < len(nums) and end < len(nums):
            if nums[end] - nums[start] == step:
                end += 1
                if end == len(nums):
                    retlist.append(str(nums[start]) + "->" + str(nums[end - 1]))
                    break
                step += 1
            else:
                if end - 1 == start:
                    retlist.append(str(nums[start]))
                    step = 1
                    start = end
                    end += 1
                    if end == len(nums):
                        retlist.append(str(nums[start]))
                else:
                    retlist.append(str(nums[start]) + "->" + str(nums[end - 1]))
                    start = end
                    end += 1
                    if end == len(nums):
                        retlist.append(str(nums[start]))
                    step = 1
        return retlist

print(summaryRanges([1,3])) # ["0->2","4->5","7"]

#start end pointers
