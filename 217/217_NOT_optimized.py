from typing import List

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        for elem in nums:
            if nums.count(elem) > 1:
                return True
        return False