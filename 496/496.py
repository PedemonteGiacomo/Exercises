from typing import List
# https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1: List[int], nums2: List[int])->List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        ans = List[int]
        found = False
        for i in range(n): 
            for j in range(m):
                if nums1[i] == nums2[j]:
                    found = False
                    for w in range(j,m):
                        if nums2[w] > nums2[j]:
                            found=True
                            ans.append(nums2[w])
                            break
                    if not found:
                        ans.append(-1)
        return ans