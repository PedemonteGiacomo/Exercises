from typing import List
# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums: List[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sub_len = 1 # starting point
        count = 0
        n = len(nums)
        while sub_len <= n:
            sum_ = sum(nums[:sub_len])
            if sum_ == k:
                count += 1
            for i in range(1, n - sub_len + 1):
                # Update sum incrementally instead of recalculating
                sum_ = sum_ - nums[i - 1] + nums[i + sub_len - 1]
                if sum_ == k:
                    count += 1
            sub_len += 1
        return count
        