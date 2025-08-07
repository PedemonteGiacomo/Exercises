# https://leetcode.com/problems/contains-duplicate/
from typing import List

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_ = {}
        for i in range(len(nums)):
            dict_[nums[i]] = dict_.get(nums[i],0) + 1
            if dict_[nums[i]] > 1:
                return True
        return False
    
        