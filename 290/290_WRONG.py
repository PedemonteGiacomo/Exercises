# https://leetcode.com/problems/word-pattern/description/

class Solution(object):
    def wordPattern(self, pattern: str, s: str):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        pattern_words = {}
        words_pattern = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern_words.get(words[i],"") == "" or words_pattern.get(pattern[i], "") == "":
                pattern_words[pattern[i]] = words[i]
                words_pattern[words[i]] = pattern[i]
            elif pattern_words[pattern[i]] != words[i] or words_pattern[words[i]] != pattern[i]:
                return False
        return True
