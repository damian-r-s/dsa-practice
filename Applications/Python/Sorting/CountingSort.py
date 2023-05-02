def countingSort(lst):
    k = max(lst)
    counts = [0] * (k + 1)
    for element in lst: #count elements
        counts[element] += 1
        
    index = 0
    for i, count in enumerate(counts):
        counts[i] = index
        index += count
        
    result = [0] * len(lst)
    for element in lst:
        idx = counts[element]
        result[idx] = element
        counts[element] += 1
        
    return result

