from typing import List
# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums.count(0) < 1:
            return nums
        pointer_zero = nums.index(0)
        pointer_non_zero = pointer_zero + 1
        n = len(nums)
        while pointer_non_zero < n:
            if nums[pointer_non_zero] != 0:
                nums[pointer_zero] = nums[pointer_non_zero]
                nums[pointer_non_zero] = 0
                pointer_zero +=1
            else:
                pointer_non_zero += 1
        return nums