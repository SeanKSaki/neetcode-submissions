class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        forward = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                forward += i.lower()
                reverse = i.lower() + reverse
        return True if forward == reverse else False
