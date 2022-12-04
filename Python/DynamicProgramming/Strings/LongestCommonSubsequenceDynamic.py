def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    results = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    path = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):

            if(str1[i - 1] == str2[j - 1]):
                results[i][j] = results[i - 1][j - 1] + 1
                path[i][j] = 0            
            elif(results[i - 1][j] > results[i][j - 1]):
                results[i][j] = results[i - 1][j]
                path[i][j] = 1
            else:
                results[i][j] = results[i][j - 1]
                path[i][j] = 2

    return (results[len1][len2], path)

def recurExtractLcs(str1, path, i, j):
    if(i == 0 or j == 0):
        return ""

    if(path[i][j] == 0):
        return recurExtractLcs(str1, path, i - 1, j - 1) + str1[i - 1]
    elif(path[i][j] == 1):
        return recurExtractLcs(str1, path, i - 1, j)
    
    return recurExtractLcs(str1, path, i, j - 1)

def printSolution(str1, str2):

    result, path = lcs(str1, str2)
    print("Result: " + str(result))    
    print("Common subsequence: " + recurExtractLcs(str1, path, len(str1), len(str2)))


printSolution("abc", "abc")
printSolution("ab", "abcd")
printSolution("eabd", "1234a2b4d")