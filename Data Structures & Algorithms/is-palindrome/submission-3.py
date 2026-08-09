class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for character in s:
            if character.isalnum():
                new_s += character.lower()

        return new_s == new_s[::-1]