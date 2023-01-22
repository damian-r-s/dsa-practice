def findMin(nums):
    i = 0
    j = len(nums) - 1
    
    while i < j:
        a = nums[i]
        b = nums[j]                
        
        if a < b:
            return a
        
        m = (i + j) // 2
        c = nums[m]
        if c > b:
            i = m + 1
        else:
            j = m           

    return nums[i]

print(findMin([2, 3, 1]))
print(findMin([2]))