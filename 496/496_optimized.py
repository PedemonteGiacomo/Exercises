# https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1: list[int], nums2: list[int])->list[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        ans = []
        for i in range(n):
            start = nums2.index(nums1[i])
            to_find = nums2[start]
            found = False
            while start < m:
                if nums2[start] > to_find:
                    ans.append(nums2[start])
                    found=True
                    break
                start += 1
            if not found:
                ans.append(-1)
        return ans
