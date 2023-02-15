def bubleSort(lst):
    swapped = True
    while swapped:
        swapped = False        
        for idx in range(len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                swapped = True
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                
    return lst
                
print(bubleSort([4, 5, 1, 3, 5, 10, 1, 2]))