import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #reverse string
        arr = [x for x in s.lower() if x.isalnum()]
        rev = arr[::-1]

        if arr == rev:
            return True
        return False
        