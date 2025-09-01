class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0
        for num in numset:
            if num == 0:
                continue
            else:
                count += 1
        return count