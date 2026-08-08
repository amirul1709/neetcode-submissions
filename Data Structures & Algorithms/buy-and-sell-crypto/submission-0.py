class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                currProfit = prices[right] - prices[left]
                profit = max(profit, currProfit)
                right += 1
            else:
                left = right # Want to skip to the low price
                right += 1

        return profit

