# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def containsNearbyDuplicate(self, nums: list[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i
        return False