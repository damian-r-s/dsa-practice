def searchRange(nums, target):
    i = 0
    j = len(nums) - 1
    m = (i + j) // 2
    r = -1
    
    while i <= j:
        m = (i + j) // 2    
        c = nums[m]
        
        if c == target:
            r = m
        
        if target < c:
            j = m - 1
        else:
            i = m + 1
    
    if r == -1:
        return (-1, -1)
    
    i = r
    j = r
    
    while i >= 0 and nums[i] == nums[r]:
        i = i - 1
    
    while j <= len(nums) - 1 and nums[j] == nums[r]:
        j = j + 1
        
    return (i + 1 , j - 1)