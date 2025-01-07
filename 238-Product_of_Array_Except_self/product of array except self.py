def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        retval = 1
        j = 0
        listret = []
        for i in range(len(nums)):
            retval = 1
            while j < len(nums):
                if j == i:
                    j += 1
                else:
                    retval = retval * nums[j]
                    j += 1
            j = 0
            listret.append(retval)
        return listret

print(productExceptSelf([1,2,3,4])) # [24,12,8,6]

#prefix postfix algorithm
