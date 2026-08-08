class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointerD = {}
        left = 0

        numSubstring = 0

        for right in range(len(s)):
            if s[right] in pointerD:
                left = max(pointerD[s[right]] + 1, left)

            pointerD[s[right]] = right
            numSubstring = max(numSubstring, right - left + 1)

        return numSubstring