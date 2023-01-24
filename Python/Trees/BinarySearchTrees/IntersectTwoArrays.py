def intersect(nums1, nums2):
        return merger(nums1, nums2)
        
def merger(nums1, nums2):        
    a = nums1
    a.sort()        
    b = nums2
    b.sort()
    
    i = 0
    j = 0
    result = []        
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])                
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
            
    return result


print(intersect([2, 2, 4], [1, 2, 2, 3, 4, 5]))