class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = 1
        max_profit = profit = 0
        while right < n:
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            right += 1
        return max_profit
# Time Complexity - O(n)
