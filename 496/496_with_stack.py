# https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
            else:
                stack.insert(0,nums2[i])
            for j in range(i, len(nums2)):
                if nums2[j] > stack[0]:
                    num_ = stack.pop(0)
                    next_greater[num_] = next_greater.get(nums2[j],0) + nums2[j]
                    break
        for i in range(len(stack)):
            next_greater[stack[i]] = next_greater.get(stack[i],0) - 1
        ans = []
        for i in range(len(nums1)):
            ans.append(next_greater[nums1[i]])
        return ans
                
            