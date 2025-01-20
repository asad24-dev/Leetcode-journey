def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    retarray = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        start = i + 1
        end = len(nums) - 1
        while start < end:
            threesum = nums[i] + nums[start] + nums[end]
            if threesum == 0:
                retarray.append([nums[i], nums[start], nums[end]])
                end -= 1
                start += 1
                while nums[start] == nums[start - 1] and start < end:
                    start += 1
            elif threesum > 0:
                end -= 1
            elif threesum < 0:
                start += 1
    return retarray

