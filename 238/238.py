from typing import List
# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = List[int]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                mul *= nums[j]
            answer.append(mul)
        return answer

        