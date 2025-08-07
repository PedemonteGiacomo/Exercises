# https://leetcode.com/problems/contains-duplicate/
from typing import List

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Se la lunghezza del set è diversa dalla lista, ci sono duplicati
        return len(nums) != len(set(nums))
