class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
    
# This solution uses the XOR operation to find the single number in O(n) time and O(1) space.

# This approach works because:
    # - XORing a number with itself results in 0 (a ^ a = 0).
    # - XORing a number with 0 results in the number itself (a ^ 0 = a).
# Therefore, all numbers that appear twice will cancel each other out, leaving only the number that appears once.