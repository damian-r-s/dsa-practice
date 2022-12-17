#Bottom up approach
def stairsDynamic(k, n):
    if(n <= 1):
        return 1
    
    result = [0 for _ in range(n + 1)]
    result[0] = 1 # I assume that stair numer 0 requires 1 step
    result[1] = 1
    
    for stairs in range(2, n + 1):        
        for step in range(1, k + 1):            
            result[stairs] += result[stairs - step]
           
    return result[n]

print(stairsDynamic(4, 0)) #I assume level 0 requires 1 step
print(stairsDynamic(2, 3)) # 3
print(stairsDynamic(4, 4)) # 8
print(stairsDynamic(3, 7)) # 44