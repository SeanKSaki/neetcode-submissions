class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        if len(word1) >= len(word2):
            count = 0
            while count < len(word2):
                merged += word1[count] + word2[count]
                count += 1
            merged += word1[count::]
        else:
            count = 0
            while count < len(word1):
                merged += word1[count] + word2[count]
                count += 1 
            merged += word2[count::]
        return merged

