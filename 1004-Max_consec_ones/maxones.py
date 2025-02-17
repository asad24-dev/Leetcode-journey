
def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    max_l = 0
    num_zeros = 0
    l = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            num_zeros += 1
        while num_zeros > k:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1
        length = (i - l) + 1
        max_l = max(max_l, length)
    return max_l