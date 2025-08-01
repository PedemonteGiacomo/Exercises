from typing import List
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = nums[0]
        n = len(nums)
        write = 1
        read = 1
        while read < n:
            current = nums[read]
            if prev == current: # se sono uguali continuo finche non trovo un valore nuovo
                read += 1
            else:
                nums[write] = current
                write += 1
                prev = current
        return len(nums[:write])
