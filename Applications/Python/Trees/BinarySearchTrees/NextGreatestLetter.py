def nextGreatestLetter(letters, target):                
    n = len(letters)
    i = 0
    j = n
    
    while i < j:
        m = (i + j) // 2
        
        item = letters[m]
                    
        if item > target:
            j = m
        else:
            i = m + 1
    
                            
    return letters[i % n]


print(nextGreatestLetter(['c', 'd', 'm', 'n'], 'a'))
print(nextGreatestLetter(['c', 'd', 'm', 'n'], 'n'))
print(nextGreatestLetter(['c', 'd', 'm', 'n'], 'd'))