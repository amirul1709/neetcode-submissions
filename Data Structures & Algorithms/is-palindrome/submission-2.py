class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwardList = []

        for char in s:
            if char.isalnum():
                forwardList.append(char.lower())

        reverseList = []

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                reverseList.append(s[i].lower())

        if "".join(forwardList) == "".join(reverseList):
            return True

        return False