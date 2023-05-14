# You are given a 0-indexed string num of length n consisting of digits.
# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

def digitCount(num: str) -> bool:
    for i in range(len(num)):
        counter = num.count(str(i)) # calculate number of occurences I hope this is clever method O(1)
        if counter != int(num[i]):
            return False
    return True