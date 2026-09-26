# Problem: Best Time to Buy and Sell Stock
# Topic: Arrays
# LeetCode: 121
# Idea: Track the minimum price and maximum profit
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=prices[0]
        profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            current_profit=price-min_price
            if current_profit>profit:
                profit=current_profit
        return  profit      