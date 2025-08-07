class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary_ = {}
        left = 0
        right = 0
        max_length = 0
        while right < len(s):
            dictionary_[s[right]] = dictionary_.get(s[right], 0) + 1
            while dictionary_[s[right]] > 1:
                dictionary_[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length