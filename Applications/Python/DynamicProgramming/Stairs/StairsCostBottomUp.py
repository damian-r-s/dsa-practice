def stairsWithCostBottomUp(k, n, costs):
    if n <= 1:
        return costs[0]
    
    result = [99999 for x in range(n)]
    result[0] = 0 # I assume that stair numer 0 requires 1 step
    result[1] = costs[1]
    
    for stairs in range(2, n):
        for step in range(1, k + 1):
            result[stairs] = min(result[stairs - step] + costs[stairs], result[stairs])
    
    return result[n - 1]

print(stairsWithCostBottomUp(2, 4, [0, 3, 5, 2])) #5
print(stairsWithCostBottomUp(4, 4, [0, 3, 5, 2])) #2
print(stairsWithCostBottomUp(1, 0, [0, 3, 5, 2, 10])) #0
print(stairsWithCostBottomUp(4, 5, [0, 3, 5, 2, 10])) #10
print(stairsWithCostBottomUp(4, 5, [0, 3, 5, 2, 10])) #10
print(stairsWithCostBottomUp(3, 5, [0, 3, 5, 2, 10])) #12