class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashing = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in hashing:
                return [hashing[comp], i]
            hashing[n] = i