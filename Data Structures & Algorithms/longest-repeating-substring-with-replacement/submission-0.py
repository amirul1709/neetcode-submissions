class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0 
        count = {}

        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            if (right - left + 1) - max(count.values()) <= k:
                result = max(result, right - left + 1) #increase window size
            else:
                count[s[left]] -= 1 #decrease window size
                left += 1
            
            result = max(result, right - left + 1)

        return result