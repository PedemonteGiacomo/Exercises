from typing import List
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = float('inf')
        n = len(nums)
        i = 0
        while i < n:
            current = nums[i]
            if prev == current:
                nums.pop(i)
                n = len(nums)
            else: 
                prev = current
                i+=1
        return len(nums)
        