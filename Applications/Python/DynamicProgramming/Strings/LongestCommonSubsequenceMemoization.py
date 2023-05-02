def lcs(str1, str2):
    memo = {}
    return recurrsion(str1, str2, 0, 0, len(str1), len(str2), memo)

def recurrsion(str1, str2, idx1, idx2, len1, len2, memo):
    if(len1 == idx1 or len2 == idx2):
        return 0

    index = (idx1, idx2)
    if(index in memo):
        return memo[index]
        
    if(str1[idx1] == str2[idx2]):
        memo[index] = 1 + recurrsion(str1, str2, idx1 + 1, idx2 + 1, len1, len2, memo)
        return memo[index]

    memo[index] =  max(recurrsion(str1, str2, idx1 + 1, idx2, len1, len2, memo), recurrsion(str1, str2, idx1, idx2 + 1, len1, len2, memo))
    return memo[index]

print(lcs("123456789", "12345789"))