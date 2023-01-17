def search(nums, target):
    i = 0
    j = len(nums) - 1
    a = nums[i]
    b = nums[j]        
            
    while i <= j:
        mid = (i + j) // 2                         
        a = nums[i]
        b = nums[j]
        c = nums[mid]
        
        if target == c:
            return mid
        if target == a:
            return i
        if target == b:
            return j
                    
        if a <= b:
            if target < c:
                j = mid - 1
            else:
                i = mid + 1            
        elif a > b:
            if a < c and target > a and target < c:
                j = mid - 1
            elif c < b and target > c and target < b:
                i = mid + 1                
            elif a > c and (target > a or target < c):
                j = mid - 1                
            elif c > b and (target > c or target < b):
                i = mid + 1
            else:
                i = mid + 1
            
    return -1


print(search([4,5,6,7,0,1,2], 3))