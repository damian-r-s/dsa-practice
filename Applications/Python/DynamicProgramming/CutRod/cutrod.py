def rodcut(n, prices, memoization):
    if(n in memoization):
        return memoization[n]

    if n == 0:
        return 0

    result = -1    
    for i in range(n):                
        result = max(result, prices[i] + rodcut(n - i - 1, prices, memoization))        
        
    if (n not in memoization or (n in memoization and memoization[n] < result)):
        memoization[n] = result            

    return result


def rodCutBootmUp(n, prices):
    r = [0 for i in range(n + 1)]
    r[0] = 0
    
    for j in range(1, n + 1):
        maximum = -1

        for i in range(1, j + 1):
            idx = j - i
            rr = r[idx]
            p = prices[i - 1] 
            maximum = max(maximum, p + rr)
        r[j] = maximum

    return r[n]

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print(rodCutBootmUp(6, prices))