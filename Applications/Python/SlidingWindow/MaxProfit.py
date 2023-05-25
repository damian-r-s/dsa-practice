# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(self, prices: List[int]) -> int:
    buy = prices[0]
    sell = prices[0]
    profit = 0

    for i in range(1, len(prices)):            
        sell, current = prices[i], prices[i] 
        diff = sell - buy

        if diff > profit:
            profit = diff

        if current < buy:
            buy = current        

    return profit