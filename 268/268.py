# https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i = 0
        aux = []
        while i <= n:
            aux.append(i)
            i+=1
        # ora scorro partendo da 0 fino a n-1 (per stare dentro all'array nums)
        for i in range(len(nums)):
            if aux[i] != nums[i]:
                return aux[i]
        return aux[-1]

        
        

        