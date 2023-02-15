def selectionSort(lst):
    for idx in range(len(lst)):
        min = idx
        for current in range(idx + 1, len(lst)):
            if lst[min] > lst[current]:
                min = current
                
        lst[idx], lst[min] = lst[min], lst[idx]
        
    return lst
                
print(selectionSort([3, 6, 1, 2, 3, 8, 9]))