def lcs(str1, str2):
    return recurrsion(str1, str2, 0, 0, len(str1), len(str2))

def recurrsion(str1, str2, idx1, idx2, len1, len2):
    if(len1 == idx1 or len2 == idx2):
        return 0

    if(str1[idx1] == str2[idx2]):
        return 1 + recurrsion(str1, str2, idx1 + 1, idx2 + 1, len1, len2)

    return max(recurrsion(str1, str2, idx1 + 1, idx2, len1, len2), recurrsion(str1, str2, idx1, idx2 + 1, len1, len2))

print(lcs("abc", "bca"))
print(lcs("bbbccc", "aaabbbcc"))
print(lcs("123456789", "12345789"))