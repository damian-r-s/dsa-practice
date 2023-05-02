def insertionSort(lst):
    n = len(lst)
    
    for pointerA in range(1, n):
        for pointerB in range(pointerA, 0, -1):
            if lst[pointerB] > lst[pointerB - 1]:
                break
            
            lst[pointerB], lst[pointerB - 1] = lst[pointerB - 1], lst[pointerB]
                        
    return lst

print(insertionSort([10, 1, 2, 3, 4, 4, 2, 1, 0]))
                
                