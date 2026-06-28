class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        max_length = 0
        seen = set()
        for i, letter in enumerate(s):
            while letter in substr:
                substr = substr[1:]
            substr += letter
            max_length = max(len(substr), max_length)
        return max_length
            