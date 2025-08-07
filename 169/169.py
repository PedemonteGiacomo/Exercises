# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        # mi faccio un dizionario di conteggio per contare qunte volte un valore appare nell'array
        count_ = {}
        for i in range(len(nums)):
            count_[nums[i]] = count_.get(nums[i],0) + 1
        target = len(nums) / 2
        for i in range(len(nums)):
            if count_[nums[i]] > target:
                return nums[i]
        