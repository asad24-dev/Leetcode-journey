def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = set(nums)
        if len(nums) != len(a):
            return True
        else:
            return False

'''in a set each element appears only once even if their is repition so if the length of
the set is not equal to the length of the list then there is a duplicate'''
            