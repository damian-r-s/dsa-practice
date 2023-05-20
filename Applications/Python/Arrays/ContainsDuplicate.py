# 217. Contains Duplicate - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(self, nums) -> bool:
    dic = set()

    for n in nums:
        if n in dic:
            return True
        dic.add(n)

    return False