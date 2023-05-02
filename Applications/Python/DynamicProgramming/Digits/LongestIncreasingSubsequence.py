global toalMax

def rec(arr, n):
    global totalMax

    if (n == 1):
        return 1

    maximum = 1

    for i in range(1, n):
        res = rec(arr, i)
        left = arr[i - 1]
        right = arr[n - 1]

        if(left < right and res + 1 > maximum):
            maximum = res + 1

    totalMax = max(maximum, totalMax)

    return maximum

def lis(arr):
    global totalMax
    totalMax = 1
    rec(arr, len(arr))
    
    return totalMax

arr = [1, 2, 3, 4]
print(lis(arr))