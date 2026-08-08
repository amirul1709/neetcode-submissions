class Solution:
    def isPalindrome(self, s: str) -> bool:
        charArr = []
        
        for c in s:
            if c.isalnum():
                charArr.append(c.lower())

        right = len(charArr) - 1

        reverseArr = []

        while (right >= 0):
            reverseArr.append(charArr[right])

            right -= 1

        if ''.join(charArr) == ''.join(reverseArr):
            return True

        return False