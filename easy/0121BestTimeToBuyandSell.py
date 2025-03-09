class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0  # Handle edge case
        profit = 0
        currentLow = float('inf')
        for price in prices:
            if currentLow > price:
                currentLow = price
            else: 
                profit = max(profit, price - currentLow)
        return profit