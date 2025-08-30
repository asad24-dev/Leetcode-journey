def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        retlist = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            retlist[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            retlist[i] *= postfix
            postfix *= nums[i]
        return retlist

print(productExceptSelf([1,2,3,4])) # [24,12,8,6]

#prefix postfix algorithm
