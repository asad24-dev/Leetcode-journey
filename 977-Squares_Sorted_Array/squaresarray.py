def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftp = 0
        rightp = len(nums) - 1
        retlist = []
        while leftp <= rightp:
            if nums[leftp] * nums[leftp] > nums[rightp] * nums[rightp]:
                retlist.append(nums[leftp] * nums[leftp])
                leftp += 1
            else:
                retlist.append(nums[rightp] * nums[rightp])
                rightp -= 1
        retlist.reverse()
        return retlist

'''
The two-pointer technique leverages the fact that the input array 
is sorted, with the largest absolute values either at the beginning 
(left) or the end (right). By comparing the squares of the numbers at 
these two pointers, the larger square is appended to the result list, 
and the corresponding pointer is moved inward. This works because the 
largest square at each step will always be at one of the two ends, 
ensuring an efficient O(n) solution without needing to sort.
'''