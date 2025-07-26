# https://leetcode.com/problems/sum-of-two-integers/description/

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Using bitwise operations to calculate the sum
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # Mask to get last 32 bits
        MASK = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        # if a is negative, get its 32-bit signed value
        return a if a <= MAX else ~(a ^ MASK)
    
# Time complexity: O(1) - The operations are constant time bitwise operations.
# Space complexity: O(1) - No additional space is used.

# This solution uses bitwise operations to calculate the sum of two integers without using the '+' operator.
# It handles both positive and negative integers correctly by using a mask to limit the result to 32 bits.
# The carry is calculated using bitwise AND, and the sum is calculated using bitwise XOR.
# The loop continues until there are no more carries to add, ensuring that the final result is the correct sum.
# This approach is efficient and works for both positive and negative integers, adhering to the constraints of 32-bit signed integers.
# The solution is efficient and works within the constraints of 32-bit signed integers.
# The time complexity is O(1) because the operations are constant time bitwise operations, and the space complexity is O(1) as no additional space is used.
# This solution is optimal for the problem and handles all edge cases, including overflow and negative numbers
# correctly by using the mask to limit the result to 32 bits.

    
