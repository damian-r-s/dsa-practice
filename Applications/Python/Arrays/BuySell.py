def buyAndSellStockOnce(prices):  
  result = 0
  minp = float('inf')

  for i in range(1, len(prices)):
    c = prices[i]

    minp = min(c, minp)

    compare = c - minp
    if compare > result:
        result = compare

  return result


print(buyAndSellStockOnce([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))