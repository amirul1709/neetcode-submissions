class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        left, right = 0, len(heights) - 1

        while left < right:
            area = min(heights[left], heights[right]) * abs(left - right)
            result = max(area, result)
            if heights[left] < heights[right]: #maximize the area (h * w)
                left += 1
            else:
                right -= 1

        return result