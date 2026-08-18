# 121. Best Time to Buy and Sell Stock
# Solved
# Easy
# Topics
# premium lock iconCompanies

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        min = float('inf')

        for i in range(len(prices)):
            current = prices[i]

            if current < min:
                min = current
                continue

            if current - min > result:
                result = current - min

        return result    