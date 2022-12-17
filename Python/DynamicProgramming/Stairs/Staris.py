def stairsRecursive(k, n):    
    if n == 0:
        return 1        
    
    sum = 0
    for i in range(1, k + 1):    
        key = k
        if(n - i < k):
            key = n - 1            
        sum += stairsRecursive(key, n - i)
        
    return sum        

print(stairsRecursive(4, 0)) #I assume level 0 requires 1 step
print(stairsRecursive(2, 3)) # 3       
print(stairsRecursive(3, 7)) # 44