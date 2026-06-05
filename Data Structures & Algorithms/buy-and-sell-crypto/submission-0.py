class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        profit = 0
        for price in prices:
            min_price = min(price, min_price)
            if price > min_price:
                profit = max(profit, price - min_price)
            else:
                min_price = price
        return profit